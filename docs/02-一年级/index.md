---
standalone_title: "一年级古诗 - 古诗诵读"
hide:
  - navigation
  - toc
---

<div class="poems-hub poems-grade-hub">

<nav class="poems-topbar">
  <span class="poems-topbar__title"><a href="../">古诗诵读</a></span>
  <a href="../">全部年级</a>
  <span class="poems-topbar__search">🔍 搜索</span>
</nav>

<section class="poems-hero poems-hero--grade">
  <p class="poems-kicker">GRADE 1</p>
  <h1>一年级古诗</h1>
  <p>共 12 篇 · 支持筛选</p>
</section>

<section class="poems-section">
  <div class="poems-section-heading">
    <h2>篇目列表</h2>
    <p>在下方表格中筛选题目、作者、朝代、类型、主题等。</p>
  </div>

  <div id="poems-table-wrapper" data-grade="02-一年级">
    
    <div class="poems-filters">
      <input type="text" class="poem-filter" data-col="0" placeholder="搜题目…">
      <input type="text" class="poem-filter" data-col="1" placeholder="搜作者…">
      <input type="text" class="poem-filter" data-col="2" placeholder="朝代">
      <input type="text" class="poem-filter" data-col="3" placeholder="类型">
      <input type="text" class="poem-filter" data-col="4" placeholder="主题">
      <select class="poem-filter" data-col="5">
        <option value="">全部学期</option>
        <option value="上">上册</option>
        <option value="下">下册</option>
      </select>

    </div>
    <div class="poems-table-scroll">
      <table class="poems-table" id="poems-table">
        <thead>
          <tr>
            <th>题目</th>
            <th>作者</th>
            <th>朝代</th>
            <th>类型</th>
            <th>主题</th>
            <th>学期</th>
          </tr>
        </thead>
        <tbody id="poems-tbody"></tbody>
      </table>
    </div>
  </div>

  <div class="poems-empty" id="poems-empty" style="display:none">
    <p>没有匹配的篇目，试试调整筛选条件。</p>
  </div>
</section>

</div>

<script>
const POEMS_DATA = [
  {
    "title": "登鹤雀楼",
    "poet": "王之涣",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "哲理",
    "grade": "02-一年级",
    "grade_label": "一年级",
    "semester": "",
    "path": "02-一年级/登鹤雀楼/",
    "tags": [
      "哲理",
      "登高"
    ]
  },
  {
    "title": "咏鹅",
    "poet": "骆宾王",
    "dynasty": "唐",
    "type": "五言古诗",
    "theme": "咏物",
    "grade": "02-一年级",
    "grade_label": "一年级",
    "semester": "上",
    "path": "02-一年级/咏鹅/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "江南",
    "poet": "汉乐府",
    "dynasty": "汉",
    "type": "乐府诗",
    "theme": "写景",
    "grade": "02-一年级",
    "grade_label": "一年级",
    "semester": "上",
    "path": "02-一年级/江南/",
    "tags": [
      "写景",
      "江南"
    ]
  },
  {
    "title": "悯农",
    "poet": "李绅",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "惜农",
    "grade": "02-一年级",
    "grade_label": "一年级",
    "semester": "上",
    "path": "02-一年级/悯农/",
    "tags": [
      "劳动"
    ]
  },
  {
    "title": "古朗月行（节选）",
    "poet": "李白",
    "dynasty": "唐",
    "type": "五言古诗",
    "theme": "咏物",
    "grade": "02-一年级",
    "grade_label": "一年级",
    "semester": "上",
    "path": "02-一年级/古朗月行(节选)/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "风",
    "poet": "李峤",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "咏物",
    "grade": "02-一年级",
    "grade_label": "一年级",
    "semester": "上",
    "path": "02-一年级/风/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "春晓",
    "poet": "孟浩然",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "春天",
    "grade": "02-一年级",
    "grade_label": "一年级",
    "semester": "下",
    "path": "02-一年级/春晓/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "赠汪伦",
    "poet": "李白",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "送别",
    "grade": "02-一年级",
    "grade_label": "一年级",
    "semester": "下",
    "path": "02-一年级/赠汪伦/",
    "tags": [
      "送别"
    ]
  },
  {
    "title": "静夜思",
    "poet": "李白",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "思乡",
    "grade": "02-一年级",
    "grade_label": "一年级",
    "semester": "下",
    "path": "02-一年级/静夜思/",
    "tags": [
      "思乡"
    ]
  },
  {
    "title": "池上",
    "poet": "白居易",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "童趣",
    "grade": "02-一年级",
    "grade_label": "一年级",
    "semester": "下",
    "path": "02-一年级/池上/",
    "tags": [
      "童趣"
    ]
  },
  {
    "title": "小池",
    "poet": "杨万里",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "写景",
    "grade": "02-一年级",
    "grade_label": "一年级",
    "semester": "下",
    "path": "02-一年级/小池/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "寻隐者不遇",
    "poet": "贾岛",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "隐逸",
    "grade": "02-一年级",
    "grade_label": "一年级",
    "semester": "下",
    "path": "02-一年级/寻隐者不遇/",
    "tags": [
      "隐逸"
    ]
  }
];
</script>
<script src="../../assets/scripts/poems-filter.js"></script>
