# -*- coding: utf-8 -*-
"""批量补全"待补充全文"篇目：保留原 front matter，用 pypinyin 生成 ruby 正文，补译文/注释/赏析/作者。

数据来自 tools/poem_data/ 下各模块的 POEMS 字典：
    key = 相对仓库根的 md 路径 (如 docs/08-初中/望岳.md)
    value = {
        "lines": [句1, 句2, ...],          # 正文，每句含标点，脚本自动加 ruby
        "trans": "译文",                    # 可空
        "notes": "注释（支持 markdown）",   # 可空
        "appre": "赏析",                    # 可空
        "author": "作者简介",               # 可空
        "fix": {"字": "pīnyīn"}             # 可选，该篇多音字强制读音
    }
"""
import io, re, sys, importlib, pkgutil
from pathlib import Path
from pypinyin import lazy_pinyin, Style

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
sys.path.insert(0, str(ROOT / "tools"))

import poem_data
POEMS = {}
for m in pkgutil.iter_modules(poem_data.__path__):
    mod = importlib.import_module(f"poem_data.{m.name}")
    if hasattr(mod, "POEMS"):
        POEMS.update(mod.POEMS)

# 全局多音字倾向（古诗常见读音）；篇级 fix 优先级更高
TONE_FIX = {
    "行": "xíng", "重": "chóng", "朝": "cháo", "长": "cháng", "间": "jiān",
    "胜": "shèng", "论": "lùn", "为": "wéi", "曾": "céng", "冠": "guān",
    "相": "xiāng", "见": "jiàn", "度": "dù", "乐": "lè", "塞": "sài",
    "骑": "qí", "调": "diào", "看": "kàn", "教": "jiào", "遗": "yí",
    "王": "wáng", "阿": "ē", "殷": "yīn", "龟": "guī", "藏": "cáng",
    "当": "dāng", "创": "chuàng", "从": "cóng", "处": "chù", "传": "chuán",
    "华": "huá", "好": "hǎo", "还": "huán", "会": "huì", "降": "jiàng",
    "将": "jiāng", "觉": "jué", "卷": "juǎn", "宁": "níng", "强": "qiáng",
    "少": "shào", "省": "shěng", "思": "sī", "汤": "tāng", "挑": "tiāo",
    "咽": "yè", "要": "yào", "应": "yīng", "与": "yǔ", "载": "zǎi",
    "中": "zhōng", "重": "chóng", "便": "biàn", "分": "fēn", "令": "lìng",
    "空": "kōng", "鲜": "xiān", "解": "jiě", "舍": "shě", "汗": "hán",
    "可": "kě", "恶": "è", "泊": "bó", "扁": "piān", "刹": "chà",
    "禅": "chán", "场": "cháng", "创": "chuàng",
}


def ruby_line(line, fix=None):
    fix = fix or {}
    pys = lazy_pinyin(line, style=Style.TONE, errors="default")
    out = []
    for i, ch in enumerate(line):
        py = pys[i] if i < len(pys) else ch
        if ch in fix:
            py = fix[ch]
        elif ch in TONE_FIX:
            py = TONE_FIX[ch]
        out.append(f'<ruby>{ch}<rt>{py}</rt></ruby>')
    return "".join(out)


def build_body(meta, title, data):
    poet = meta.get("poet", "")
    dynasty = meta.get("dynasty", "")
    typ = meta.get("type", "")
    theme = meta.get("theme", "")
    fix = data.get("fix")
    lines = data.get("lines", [])
    ruby_html = "\n".join(
        f'    <p class="poem-line">{ruby_line(ln, fix)}</p>' for ln in lines
    )
    parts = [
        f"# {title}",
        "",
        f'<div class="poem-page" markdown="1" data-poet="{poet}" data-dynasty="{dynasty}" data-type="{typ}" data-theme="{theme}">',
        "",
        '<nav class="poems-topbar">',
        '  <span class="poems-topbar__title"><a href="../../">古诗诵读</a></span>',
        f'  <a href="../">{meta.get("grade","")}</a>',
        '  <span class="poems-topbar__search">🔍 搜索</span>',
        "</nav>",
        "",
        '<div class="poem-card">',
        '  <p class="poem-meta">',
        f'    <span class="poem-tag poem-tag--dynasty">{dynasty}</span>',
        f'    <span class="poem-tag poem-tag--poet">{poet}</span>',
        f'    <span class="poem-tag poem-tag--type">{typ}</span>',
        f'    <span class="poem-tag poem-tag--theme">{theme}</span>',
        "  </p>",
        '  <div class="poem-body" data-pinyin="1">',
        '<button class="poem-pinyin-toggle" type="button" aria-pressed="false"><span class="poem-pinyin-toggle__icon"> 拼</span>显示拼音</button>',
        ruby_html,
        "  </div>",
        "</div>",
        "",
    ]
    if data.get("trans"):
        parts += ["## 译文", "", data["trans"], ""]
    if data.get("notes"):
        parts += ["## 注释", "", data["notes"], ""]
    if data.get("appre"):
        parts += ["## 赏析", "", data["appre"], ""]
    if data.get("author"):
        parts += ["## 作者", "", data["author"], ""]
    parts += ["</div>", ""]
    return "\n".join(parts)


def main():
    done, missing = [], []
    for rel, data in POEMS.items():
        p = ROOT / rel
        if not p.exists():
            missing.append(rel)
            continue
        raw = io.open(p, encoding="utf-8-sig").read().replace("\r\n", "\n")
        m = re.match(r"^---[ \t]*\n(.*?)\n---[ \t]*\n(.*)$", raw, re.S)
        if not m:
            missing.append(rel + " (front matter 解析失败)")
            continue
        fm = "---\n" + m.group(1) + "\n---\n\n"
        meta = yaml.safe_load(m.group(1)) or {}
        title = meta.get("standalone_title", "").split(" - ")[0] or p.stem
        body = build_body(meta, title, data)
        io.open(p, "w", encoding="utf-8", newline="\n").write(fm + body)
        done.append(rel)
    print(f"已补全 {len(done)} 篇")
    if missing:
        print("未处理：")
        for r in missing:
            print("  " + r)


if __name__ == "__main__":
    import yaml
    main()
