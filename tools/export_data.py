#!/usr/bin/env python3
"""Export docs/**/*.md poem content into per-grade JSON shards for the SPA.

Each poem becomes:
  title, poet, dynasty, type, theme, tags : from YAML front matter
  grade      : grade directory name (e.g. "08-初中")
  grade_label: "初中" ...
  lines      : list[str]  plain text of each poem line (punctuation kept)
  ruby       : list[list[[ch, py]]]  per line per char -> pinyin (punct -> "")
  sections   : {"译文","注释","赏析","作者"} raw text, "" when absent
Poems whose body is "（待补充全文）" get empty lines/ruby and show a placeholder.
"""
from __future__ import annotations

import io
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
DATA = ROOT / "data"

GRADES = [
    ("01-幼儿园", "幼儿园"), ("02-一年级", "一年级"), ("03-二年级", "二年级"),
    ("04-三年级", "三年级"), ("05-四年级", "四年级"), ("06-五年级", "五年级"),
    ("07-六年级", "六年级"), ("08-初中", "初中"), ("09-高中", "高中"),
]
SECTION_NAMES = ["译文", "注释", "赏析", "作者"]

RUBY_RE = re.compile(r"<ruby>(.*?)<rt>(.*?)</rt></ruby>")
LINE_RE = re.compile(r'<p class="poem-line">(.*?)</p>', re.S)
TAG_RE = re.compile(r"<[^>]+>")


def parse_ruby_line(inner: str):
    """Return (plain_text, ruby_pairs) for one <p class=poem-line> inner HTML."""
    pairs = []
    pos = 0
    for m in RUBY_RE.finditer(inner):
        # any non-ruby text in between (rare) -> keep as plain chars
        for ch in TAG_RE.sub("", inner[pos:m.start()]):
            pairs.append([ch, ""])
        ch, py = m.group(1), m.group(2)
        is_cjk = any("一-鿿" <= c <= "鿿" for c in ch)
        pairs.append([ch, py if is_cjk else ""])
        pos = m.end()
    for ch in TAG_RE.sub("", inner[pos:]):
        pairs.append([ch, ""])
    text = "".join(p[0] for p in pairs).strip()
    return text, pairs


def split_sections(body: str):
    """Split the trailing markdown after the poem card into named sections."""
    out = {name: "" for name in SECTION_NAMES}
    # find headings like "## 译文"
    heads = list(re.finditer(r"^##\s*(.+?)\s*$", body, re.M))
    for i, h in enumerate(heads):
        name = h.group(1).strip()
        start = h.end()
        end = heads[i + 1].start() if i + 1 < len(heads) else len(body)
        text = body[start:end].strip()
        text = re.sub(r"</?div[^>]*>", "", text).strip()
        if name in out:
            out[name] = text
    return out


def parse_poem(path: Path, grade: str, label: str):
    raw = io.open(path, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S)
    meta, body = ({}, raw)
    if m:
        meta = yaml.safe_load(m.group(1)) or {}
        body = m.group(2)

    title = re.search(r"^#\s*(.+?)\s*$", body, re.M)
    title = title.group(1).strip() if title else path.stem

    # poem body region between data-pinyin block and its closing </div>
    body_m = re.search(r'data-pinyin="1">(.*?)</div>', body, re.S)
    region = body_m.group(1) if body_m else ""

    lines, ruby = [], []
    for lm in LINE_RE.finditer(region):
        inner = lm.group(1)
        if "待补充全文" in inner:
            continue
        if "<ruby>" in inner:
            text, pairs = parse_ruby_line(inner)
        else:
            text = TAG_RE.sub("", inner).strip()
            pairs = [[c, ""] for c in text]
        if text:
            lines.append(text)
            ruby.append(pairs)

    sections = split_sections(body)
    return {
        "title": title,
        "poet": meta.get("poet", ""),
        "dynasty": meta.get("dynasty", ""),
        "type": meta.get("type", ""),
        "theme": meta.get("theme", ""),
        "tags": meta.get("tags", []) or [],
        "grade": grade,
        "grade_label": label,
        "lines": lines,
        "ruby": ruby,
        "sections": sections,
    }


def main():
    DATA.mkdir(exist_ok=True)
    index = {"total": 0, "grades": []}
    for grade, label in GRADES:
        gdir = DOCS / grade
        if not gdir.exists():
            continue
        poems = []
        for f in sorted(gdir.glob("*.md")):
            if f.name == "index.md":
                continue
            poems.append(parse_poem(f, grade, label))
        shard = {"grade": grade, "label": label, "count": len(poems), "poems": poems}
        (DATA / f"{grade}.json").write_text(
            json.dumps(shard, ensure_ascii=False), encoding="utf-8")
        with_body = sum(1 for p in poems if p["lines"])
        index["grades"].append({"grade": grade, "label": label,
                                "count": len(poems), "with_body": with_body})
        index["total"] += len(poems)
        print(f"  {grade} {label}: {len(poems)} 篇 (有正文 {with_body})")
    (DATA / "index.json").write_text(
        json.dumps(index, ensure_ascii=False), encoding="utf-8")
    print(f"导出完成 → data/ 共 {index['total']} 篇")


if __name__ == "__main__":
    main()
