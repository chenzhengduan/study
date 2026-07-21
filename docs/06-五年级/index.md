---
standalone_title: "五年级古诗 - 古诗诵读"
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
  <p class="poems-kicker">GRADE 5</p>
  <h1>五年级古诗</h1>
  <p>共 23 篇 · 支持筛选</p>
</section>

<section class="poems-section">
  <div class="poems-section-heading">
    <h2>篇目列表</h2>
    <p>在下方表格中筛选题目、作者、朝代、类型、主题等。</p>
  </div>

  <div id="poems-table-wrapper" data-grade="06-五年级">
    
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
    "title": "黄鹤楼送孟浩然之广陵",
    "poet": "李白",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "送别",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "上",
    "path": "06-五年级/黄鹤楼送孟浩然之广陵/",
    "tags": [
      "送别"
    ]
  },
  {
    "title": "渔歌子",
    "poet": "张志和",
    "dynasty": "唐",
    "type": "词",
    "theme": "山水",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "上",
    "path": "06-五年级/渔歌子/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "枫桥夜泊",
    "poet": "张继",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "思乡",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "上",
    "path": "06-五年级/枫桥夜泊/",
    "tags": [
      "思乡"
    ]
  },
  {
    "title": "题临安邸",
    "poet": "林升",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "爱国",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "上",
    "path": "06-五年级/题临安邸/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "示儿",
    "poet": "陆游",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "爱国",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "上",
    "path": "06-五年级/示儿/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "己亥杂诗",
    "poet": "龚自珍",
    "dynasty": "清",
    "type": "七言绝句",
    "theme": "爱国",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "上",
    "path": "06-五年级/己亥杂诗/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "观书有感二首（其一）",
    "poet": "朱熹",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "哲理",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "上",
    "path": "06-五年级/观书有感二首(其一)/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "观书有感二首（其二）",
    "poet": "朱熹",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "哲理",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "上",
    "path": "06-五年级/观书有感二首(其二)/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "乞巧",
    "poet": "林杰",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "七夕",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "上",
    "path": "06-五年级/乞巧/",
    "tags": [
      "七夕"
    ]
  },
  {
    "title": "长相思",
    "poet": "纳兰性德",
    "dynasty": "清",
    "type": "词",
    "theme": "思乡",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "上",
    "path": "06-五年级/长相思/",
    "tags": [
      "思乡"
    ]
  },
  {
    "title": "山居秋暝",
    "poet": "王维",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "山水",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "上",
    "path": "06-五年级/山居秋暝/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "游子吟",
    "poet": "孟郊",
    "dynasty": "唐",
    "type": "乐府诗",
    "theme": "母爱",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "下",
    "path": "06-五年级/游子吟/",
    "tags": [
      "母爱"
    ]
  },
  {
    "title": "四时田园杂兴（其三十一）",
    "poet": "范成大",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "田园",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "下",
    "path": "06-五年级/四时田园杂兴(其三十一)/",
    "tags": [
      "田园"
    ]
  },
  {
    "title": "送元二使安西",
    "poet": "王维",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "送别",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "下",
    "path": "06-五年级/送元二使安西/",
    "tags": [
      "送别"
    ]
  },
  {
    "title": "乡村四月",
    "poet": "翁卷",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "田园",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "下",
    "path": "06-五年级/乡村四月/",
    "tags": [
      "田园"
    ]
  },
  {
    "title": "凉州词（黄河远上）",
    "poet": "王之涣",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "边塞",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "下",
    "path": "06-五年级/凉州词(黄河远上)/",
    "tags": [
      "边塞"
    ]
  },
  {
    "title": "秋夜将晓出篱门迎凉有感",
    "poet": "陆游",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "爱国",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "下",
    "path": "06-五年级/秋夜将晓出篱门迎凉有感/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "从军行",
    "poet": "王昌龄",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "边塞",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "下",
    "path": "06-五年级/从军行/",
    "tags": [
      "边塞"
    ]
  },
  {
    "title": "村晚",
    "poet": "雷震",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "田园",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "下",
    "path": "06-五年级/村晚/",
    "tags": [
      "田园"
    ]
  },
  {
    "title": "稚子弄冰",
    "poet": "杨万里",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "童趣",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "下",
    "path": "06-五年级/稚子弄冰/",
    "tags": [
      "童趣"
    ]
  },
  {
    "title": "鸟鸣涧",
    "poet": "王维",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "山水",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "下",
    "path": "06-五年级/鸟鸣涧/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "自相矛盾",
    "poet": "韩非子",
    "dynasty": "战国",
    "type": "文言文",
    "theme": "寓言",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "下",
    "path": "06-五年级/自相矛盾/",
    "tags": [
      "寓言"
    ]
  },
  {
    "title": "杨氏之子",
    "poet": "刘义庆",
    "dynasty": "南朝",
    "type": "文言文",
    "theme": "智慧",
    "grade": "06-五年级",
    "grade_label": "五年级",
    "semester": "下",
    "path": "06-五年级/杨氏之子/",
    "tags": [
      "智慧"
    ]
  }
];
</script>
<script src="../../assets/scripts/poems-filter.js"></script>
