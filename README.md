# 古诗诵读

从幼儿园到高中的古诗文诵读知识库。**一首一页 · 数据驱动 · 移动端优先**。

在线访问：https://chenzhengduan.github.io/study/

## 架构

纯静态 SPA（单页应用），无构建步骤，GitHub Pages 直接托管。

```
index.html          应用外壳（顶栏 / 搜索 / 底部 Tab）
assets/
  app.js            路由 + 视图渲染 + 搜索 + 拼音/竖排/字号/深色
  styles.css        设计系统（浅色/深色，移动端优先）
data/
  index.json        总目录（各年级篇数统计）
  <年级>.json       各年级诗数据（正文 + 拼音 + 译文/注释/赏析/作者）
docs/               内容源（每篇一个 .md，人工维护）
tools/
  export_data.py    解析 docs/*.md → 生成 data/*.json
```

## 功能

- **首页**：收录统计、各年级篇数条形图、年级卡片导航
- **年级页**：朝代分布条 + 朝代/类型/主题多维筛选 + 关键词过滤
- **诗页**：拼音显隐、**竖排诵读**、字号调节、译文/注释/赏析/作者折叠卡、上一首/下一首
- **查找**：全库跨年级搜索（诗名/诗人/朝代/类型/主题）
- **体验**：深色模式、随机一首、移动端底部 Tab、状态本地持久化

## 本地预览

```bash
python -m http.server 8000
# 打开 http://localhost:8000/
```

## 内容维护

1. 在 `docs/<年级>/` 下编辑对应 `.md`（含 YAML 元数据 + ruby 拼音正文 + 译文/注释/赏析/作者小节）。
2. 重新生成数据：

```bash
pip install -r requirements.txt
python tools/export_data.py
```

3. 提交 `docs/` 与生成的 `data/` 即可。
