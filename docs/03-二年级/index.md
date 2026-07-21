---
standalone_title: "二年级古诗 - 古诗诵读"
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
  <p class="poems-kicker">GRADE 2</p>
  <h1>二年级古诗</h1>
  <p>共 13 篇 · 支持筛选</p>
</section>

<section class="poems-section">
  <div class="poems-section-heading">
    <h2>篇目列表</h2>
    <p>在下方表格中筛选题目、作者、朝代、类型、主题等。</p>
  </div>

  <div id="poems-table-wrapper" data-grade="03-二年级">
    
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
    "title": "敕勒歌",
    "poet": "北朝民歌",
    "dynasty": "北朝",
    "type": "乐府诗",
    "theme": "草原",
    "grade": "03-二年级",
    "grade_label": "二年级",
    "semester": "上",
    "path": "03-二年级/敕勒歌/",
    "tags": [
      "草原",
      "民歌"
    ]
  },
  {
    "title": "登鹳雀楼",
    "poet": "王之涣",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "哲理",
    "grade": "03-二年级",
    "grade_label": "二年级",
    "semester": "上",
    "path": "03-二年级/登鹳雀楼/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "望庐山瀑布",
    "poet": "李白",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "山水",
    "grade": "03-二年级",
    "grade_label": "二年级",
    "semester": "上",
    "path": "03-二年级/望庐山瀑布/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "江雪",
    "poet": "柳宗元",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "山水",
    "grade": "03-二年级",
    "grade_label": "二年级",
    "semester": "上",
    "path": "03-二年级/江雪/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "梅花",
    "poet": "王安石",
    "dynasty": "宋",
    "type": "五言绝句",
    "theme": "咏物",
    "grade": "03-二年级",
    "grade_label": "二年级",
    "semester": "上",
    "path": "03-二年级/梅花/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "夜宿山寺",
    "poet": "李白",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "写景",
    "grade": "03-二年级",
    "grade_label": "二年级",
    "semester": "上",
    "path": "03-二年级/夜宿山寺/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "小儿垂钓",
    "poet": "胡令能",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "童趣",
    "grade": "03-二年级",
    "grade_label": "二年级",
    "semester": "上",
    "path": "03-二年级/小儿垂钓/",
    "tags": [
      "童趣"
    ]
  },
  {
    "title": "咏柳",
    "poet": "贺知章",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏物",
    "grade": "03-二年级",
    "grade_label": "二年级",
    "semester": "下",
    "path": "03-二年级/咏柳/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "晓出净慈寺送林子方",
    "poet": "杨万里",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "写景",
    "grade": "03-二年级",
    "grade_label": "二年级",
    "semester": "下",
    "path": "03-二年级/晓出净慈寺送林子方/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "赋得古原草送别",
    "poet": "白居易",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "送别",
    "grade": "03-二年级",
    "grade_label": "二年级",
    "semester": "下",
    "path": "03-二年级/赋得古原草送别/",
    "tags": [
      "送别"
    ]
  },
  {
    "title": "绝句",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "春天",
    "grade": "03-二年级",
    "grade_label": "二年级",
    "semester": "下",
    "path": "03-二年级/绝句/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "村居",
    "poet": "高鼎",
    "dynasty": "清",
    "type": "七言绝句",
    "theme": "春天",
    "grade": "03-二年级",
    "grade_label": "二年级",
    "semester": "下",
    "path": "03-二年级/村居/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "舟夜书所见",
    "poet": "查慎行",
    "dynasty": "清",
    "type": "五言绝句",
    "theme": "夜景",
    "grade": "03-二年级",
    "grade_label": "二年级",
    "semester": "下",
    "path": "03-二年级/舟夜书所见/",
    "tags": [
      "夜景"
    ]
  }
];
</script>
<script src="../../assets/scripts/poems-filter.js"></script>
