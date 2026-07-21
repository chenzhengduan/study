---
standalone_title: "六年级古诗 - 古诗诵读"
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
  <p class="poems-kicker">GRADE 6</p>
  <h1>六年级古诗</h1>
  <p>共 28 篇 · 支持筛选</p>
</section>

<section class="poems-section">
  <div class="poems-section-heading">
    <h2>篇目列表</h2>
    <p>在下方表格中筛选题目、作者、朝代、类型、主题等。</p>
  </div>

  <div id="poems-table-wrapper" data-grade="07-六年级">
    
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
    "title": "六月二十七日望湖楼醉书",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "西湖",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "上",
    "path": "07-六年级/六月二十七日望湖楼醉书/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "春日",
    "poet": "朱熹",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "春天",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "上",
    "path": "07-六年级/春日/",
    "tags": [
      "春天",
      "哲理"
    ]
  },
  {
    "title": "书湖阴先生壁",
    "poet": "王安石",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "田园",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "上",
    "path": "07-六年级/书湖阴先生壁/",
    "tags": [
      "田园"
    ]
  },
  {
    "title": "江南春",
    "poet": "杜牧",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "江南",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "上",
    "path": "07-六年级/江南春/",
    "tags": [
      "江南"
    ]
  },
  {
    "title": "回乡偶书",
    "poet": "贺知章",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "思乡",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "上",
    "path": "07-六年级/回乡偶书/",
    "tags": [
      "思乡"
    ]
  },
  {
    "title": "宿建德江",
    "poet": "孟浩然",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "思乡",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "上",
    "path": "07-六年级/宿建德江/",
    "tags": [
      "思乡"
    ]
  },
  {
    "title": "过故人庄",
    "poet": "孟浩然",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "田园",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "上",
    "path": "07-六年级/过故人庄/",
    "tags": [
      "田园"
    ]
  },
  {
    "title": "西江月·夜行黄沙道中",
    "poet": "辛弃疾",
    "dynasty": "宋",
    "type": "词",
    "theme": "田园",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "上",
    "path": "07-六年级/西江月·夜行黄沙道中/",
    "tags": [
      "田园"
    ]
  },
  {
    "title": "伯牙鼓琴",
    "poet": "《吕氏春秋》",
    "dynasty": "战国",
    "type": "文言文",
    "theme": "知音",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "上",
    "path": "07-六年级/伯牙鼓琴/",
    "tags": [
      "知音"
    ]
  },
  {
    "title": "江上渔者",
    "poet": "范仲淹",
    "dynasty": "宋",
    "type": "五言绝句",
    "theme": "民生",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/江上渔者/",
    "tags": [
      "民生"
    ]
  },
  {
    "title": "石灰吟",
    "poet": "于谦",
    "dynasty": "明",
    "type": "七言绝句",
    "theme": "咏物",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/石灰吟/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "游园不值",
    "poet": "叶绍翁",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "春天",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/游园不值/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "竹石",
    "poet": "郑燮",
    "dynasty": "清",
    "type": "七言绝句",
    "theme": "咏物",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/竹石/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "泊船瓜洲",
    "poet": "王安石",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "思乡",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/泊船瓜洲/",
    "tags": [
      "思乡"
    ]
  },
  {
    "title": "春夜喜雨",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "春天",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/春夜喜雨/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "长歌行",
    "poet": "汉乐府",
    "dynasty": "汉",
    "type": "乐府诗",
    "theme": "惜时",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/长歌行/",
    "tags": [
      "惜时"
    ]
  },
  {
    "title": "闻官军收河南河北",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "七言律诗",
    "theme": "爱国",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/闻官军收河南河北/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "寒食",
    "poet": "韩翃",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "寒食",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/寒食/",
    "tags": [
      "寒食"
    ]
  },
  {
    "title": "迢迢牵牛星",
    "poet": "古诗十九首",
    "dynasty": "汉",
    "type": "五言古诗",
    "theme": "七夕",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/迢迢牵牛星/",
    "tags": [
      "七夕"
    ]
  },
  {
    "title": "十五夜望月",
    "poet": "王建",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "中秋",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/十五夜望月/",
    "tags": [
      "中秋"
    ]
  },
  {
    "title": "马诗",
    "poet": "李贺",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "咏物",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/马诗/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "采薇（节选）",
    "poet": "诗经",
    "dynasty": "先秦",
    "type": "四言古诗",
    "theme": "边塞",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/采薇(节选)/",
    "tags": [
      "边塞"
    ]
  },
  {
    "title": "卜算子·送鲍浩然之浙东",
    "poet": "王观",
    "dynasty": "宋",
    "type": "词",
    "theme": "送别",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/卜算子·送鲍浩然之浙东/",
    "tags": [
      "送别"
    ]
  },
  {
    "title": "清平乐·春归何处",
    "poet": "黄庭坚",
    "dynasty": "宋",
    "type": "词",
    "theme": "惜春",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/清平乐·春归何处/",
    "tags": [
      "惜春"
    ]
  },
  {
    "title": "早春呈水部张十八员外",
    "poet": "韩愈",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "春天",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/早春呈水部张十八员外/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "浣溪沙·游蕲水清泉寺",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "词",
    "theme": "旷达",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/浣溪沙·游蕲水清泉寺/",
    "tags": [
      "旷达"
    ]
  },
  {
    "title": "学弈",
    "poet": "孟子",
    "dynasty": "战国",
    "type": "文言文",
    "theme": "学习",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/学弈/",
    "tags": [
      "学习"
    ]
  },
  {
    "title": "两小儿辩日",
    "poet": "列子",
    "dynasty": "战国",
    "type": "文言文",
    "theme": "智慧",
    "grade": "07-六年级",
    "grade_label": "六年级",
    "semester": "下",
    "path": "07-六年级/两小儿辩日/",
    "tags": [
      "智慧"
    ]
  }
];
</script>
<script src="../../assets/scripts/poems-filter.js"></script>
