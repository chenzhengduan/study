---
standalone_title: "四年级古诗 - 古诗诵读"
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
  <p class="poems-kicker">GRADE 4</p>
  <h1>四年级古诗</h1>
  <p>共 21 篇 · 支持筛选</p>
</section>

<section class="poems-section">
  <div class="poems-section-heading">
    <h2>篇目列表</h2>
    <p>在下方表格中筛选题目、作者、朝代、类型、主题等。</p>
  </div>

  <div id="poems-table-wrapper" data-grade="05-四年级">
    
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
    "title": "鹿柴",
    "poet": "王维",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "山水",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "上",
    "path": "05-四年级/鹿柴/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "凉州词",
    "poet": "王翰",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "边塞",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "上",
    "path": "05-四年级/凉州词/",
    "tags": [
      "边塞"
    ]
  },
  {
    "title": "别董大",
    "poet": "高适",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "送别",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "上",
    "path": "05-四年级/别董大/",
    "tags": [
      "送别"
    ]
  },
  {
    "title": "出塞",
    "poet": "王昌龄",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "边塞",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "上",
    "path": "05-四年级/出塞/",
    "tags": [
      "边塞"
    ]
  },
  {
    "title": "题西林壁",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "哲理",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "上",
    "path": "05-四年级/题西林壁/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "浪淘沙",
    "poet": "刘禹锡",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "黄河",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "上",
    "path": "05-四年级/浪淘沙/",
    "tags": [
      "黄河"
    ]
  },
  {
    "title": "夏日绝句",
    "poet": "李清照",
    "dynasty": "宋",
    "type": "五言绝句",
    "theme": "爱国",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "上",
    "path": "05-四年级/夏日绝句/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "暮江吟",
    "poet": "白居易",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "写景",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "上",
    "path": "05-四年级/暮江吟/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "嫦娥",
    "poet": "李商隐",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏物",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "上",
    "path": "05-四年级/嫦娥/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "雪梅",
    "poet": "卢钺",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "哲理",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "上",
    "path": "05-四年级/雪梅/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "精卫填海",
    "poet": "《山海经》",
    "dynasty": "先秦",
    "type": "文言文",
    "theme": "神话",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "上",
    "path": "05-四年级/精卫填海/",
    "tags": [
      "神话"
    ]
  },
  {
    "title": "王戎不取道旁李",
    "poet": "《世说新语》",
    "dynasty": "南朝",
    "type": "文言文",
    "theme": "智慧",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "上",
    "path": "05-四年级/王戎不取道旁李/",
    "tags": [
      "智慧"
    ]
  },
  {
    "title": "宿新市徐公店",
    "poet": "杨万里",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "春天",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "下",
    "path": "05-四年级/宿新市徐公店/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "四时田园杂兴（其二）",
    "poet": "范成大",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "田园",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "下",
    "path": "05-四年级/四时田园杂兴(其二)/",
    "tags": [
      "田园"
    ]
  },
  {
    "title": "清平乐·村居",
    "poet": "辛弃疾",
    "dynasty": "宋",
    "type": "词",
    "theme": "田园",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "下",
    "path": "05-四年级/清平乐·村居/",
    "tags": [
      "田园"
    ]
  },
  {
    "title": "塞下曲",
    "poet": "卢纶",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "边塞",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "下",
    "path": "05-四年级/塞下曲/",
    "tags": [
      "边塞"
    ]
  },
  {
    "title": "墨梅",
    "poet": "王冕",
    "dynasty": "元",
    "type": "七言绝句",
    "theme": "咏物",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "下",
    "path": "05-四年级/墨梅/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "蜂",
    "poet": "罗隐",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏物",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "下",
    "path": "05-四年级/蜂/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "芙蓉楼送辛渐",
    "poet": "王昌龄",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "送别",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "下",
    "path": "05-四年级/芙蓉楼送辛渐/",
    "tags": [
      "送别"
    ]
  },
  {
    "title": "独坐敬亭山",
    "poet": "李白",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "山水",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "下",
    "path": "05-四年级/独坐敬亭山/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "卜算子·咏梅",
    "poet": "毛泽东",
    "dynasty": "近现代",
    "type": "词",
    "theme": "咏物",
    "grade": "05-四年级",
    "grade_label": "四年级",
    "semester": "下",
    "path": "05-四年级/卜算子·咏梅/",
    "tags": [
      "咏物"
    ]
  }
];
</script>
<script src="../../assets/scripts/poems-filter.js"></script>
