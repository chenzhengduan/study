---
standalone_title: "三年级古诗 - 古诗诵读"
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
  <p class="poems-kicker">GRADE 3</p>
  <h1>三年级古诗</h1>
  <p>共 20 篇 · 支持筛选</p>
</section>

<section class="poems-section">
  <div class="poems-section-heading">
    <h2>篇目列表</h2>
    <p>在下方表格中筛选题目、作者、朝代、类型、主题等。</p>
  </div>

  <div id="poems-table-wrapper" data-grade="04-三年级">
    
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
    "title": "早发白帝城",
    "poet": "李白",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "山水",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "上",
    "path": "04-三年级/早发白帝城/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "望天门山",
    "poet": "李白",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "山水",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "上",
    "path": "04-三年级/望天门山/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "山行",
    "poet": "杜牧",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "秋天",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "上",
    "path": "04-三年级/山行/",
    "tags": [
      "秋天"
    ]
  },
  {
    "title": "望洞庭",
    "poet": "刘禹锡",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "山水",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "上",
    "path": "04-三年级/望洞庭/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "所见",
    "poet": "袁枚",
    "dynasty": "清",
    "type": "五言绝句",
    "theme": "童趣",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "上",
    "path": "04-三年级/所见/",
    "tags": [
      "童趣"
    ]
  },
  {
    "title": "饮湖上初晴后雨",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "写景",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "上",
    "path": "04-三年级/饮湖上初晴后雨/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "赠刘景文",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "勉励",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "上",
    "path": "04-三年级/赠刘景文/",
    "tags": [
      "勉励"
    ]
  },
  {
    "title": "夜书所见",
    "poet": "叶绍翁",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "思乡",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "上",
    "path": "04-三年级/夜书所见/",
    "tags": [
      "思乡"
    ]
  },
  {
    "title": "采莲曲",
    "poet": "王昌龄",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "田园",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "上",
    "path": "04-三年级/采莲曲/",
    "tags": [
      "田园"
    ]
  },
  {
    "title": "司马光",
    "poet": "佚名",
    "dynasty": "宋",
    "type": "文言文",
    "theme": "智慧",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "上",
    "path": "04-三年级/司马光/",
    "tags": [
      "智慧"
    ]
  },
  {
    "title": "忆江南",
    "poet": "白居易",
    "dynasty": "唐",
    "type": "词",
    "theme": "江南",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "下",
    "path": "04-三年级/忆江南/",
    "tags": [
      "江南"
    ]
  },
  {
    "title": "元日",
    "poet": "王安石",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "春节",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "下",
    "path": "04-三年级/元日/",
    "tags": [
      "春节"
    ]
  },
  {
    "title": "绝句（迟日江山丽）",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "春天",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "下",
    "path": "04-三年级/绝句(迟日江山丽)/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "九月九日忆山东兄弟",
    "poet": "王维",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "重阳",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "下",
    "path": "04-三年级/九月九日忆山东兄弟/",
    "tags": [
      "重阳"
    ]
  },
  {
    "title": "惠崇春江晚景",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "春天",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "下",
    "path": "04-三年级/惠崇春江晚景/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "清明",
    "poet": "杜牧",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "清明",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "下",
    "path": "04-三年级/清明/",
    "tags": [
      "清明"
    ]
  },
  {
    "title": "滁州西涧",
    "poet": "韦应物",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "山水",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "下",
    "path": "04-三年级/滁州西涧/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "三衢道中",
    "poet": "曾几",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "山水",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "下",
    "path": "04-三年级/三衢道中/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "大林寺桃花",
    "poet": "白居易",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "春天",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "下",
    "path": "04-三年级/大林寺桃花/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "守株待兔",
    "poet": "韩非子",
    "dynasty": "战国",
    "type": "文言文",
    "theme": "寓言",
    "grade": "04-三年级",
    "grade_label": "三年级",
    "semester": "下",
    "path": "04-三年级/守株待兔/",
    "tags": [
      "寓言"
    ]
  }
];
</script>
<script src="../../assets/scripts/poems-filter.js"></script>
