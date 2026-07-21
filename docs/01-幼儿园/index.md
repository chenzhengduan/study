---
standalone_title: "幼儿园古诗 - 古诗诵读"
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
  <p class="poems-kicker">GRADE 0</p>
  <h1>幼儿园古诗</h1>
  <p>共 76 篇 · 支持筛选</p>
</section>

<section class="poems-section">
  <div class="poems-section-heading">
    <h2>篇目列表</h2>
    <p>在下方表格中筛选题目、作者、朝代、类型、主题等。</p>
  </div>

  <div id="poems-table-wrapper" data-grade="01-幼儿园">
    
    <div class="poems-filters">
      <input type="text" class="poem-filter" data-col="0" placeholder="搜题目…">
      <input type="text" class="poem-filter" data-col="1" placeholder="搜作者…">
      <input type="text" class="poem-filter" data-col="2" placeholder="朝代">
      <input type="text" class="poem-filter" data-col="3" placeholder="类型">
      <input type="text" class="poem-filter" data-col="4" placeholder="主题">

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
    "title": "一去二三里",
    "poet": "邵雍",
    "dynasty": "宋",
    "type": "五言绝句",
    "theme": "写景",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/一去二三里/",
    "tags": [
      "启蒙",
      "写景"
    ]
  },
  {
    "title": "古朗月行（节选）",
    "poet": "李白",
    "dynasty": "唐",
    "type": "五言古诗",
    "theme": "咏物",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/古朗月行(节选)/",
    "tags": [
      "咏物",
      "月亮"
    ]
  },
  {
    "title": "咏鹅",
    "poet": "骆宾王",
    "dynasty": "唐",
    "type": "五言古诗",
    "theme": "咏物",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/咏鹅/",
    "tags": [
      "咏物",
      "启蒙"
    ]
  },
  {
    "title": "悯农（其二）",
    "poet": "李绅",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "惜农",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/悯农(其二)/",
    "tags": [
      "劳动",
      "民生"
    ]
  },
  {
    "title": "画",
    "poet": "王维",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "咏物",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/画/",
    "tags": [
      "咏物",
      "写景"
    ]
  },
  {
    "title": "静夜思",
    "poet": "李白",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "思乡",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/静夜思/",
    "tags": [
      "思乡",
      "月亮"
    ]
  },
  {
    "title": "江畔独步寻花（其五）",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "春天",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/江畔独步寻花(其五)/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "乐游原",
    "poet": "李商隐",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "咏怀",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/乐游原/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "大风歌",
    "poet": "刘邦",
    "dynasty": "汉",
    "type": "乐府诗",
    "theme": "咏怀",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/大风歌/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "垓下歌",
    "poet": "项羽",
    "dynasty": "秦",
    "type": "乐府诗",
    "theme": "咏怀",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/垓下歌/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "七步诗",
    "poet": "曹植",
    "dynasty": "三国",
    "type": "五言绝句",
    "theme": "咏怀",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/七步诗/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "赠范晔",
    "poet": "陆凯",
    "dynasty": "南北朝",
    "type": "五言绝句",
    "theme": "友情",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/赠范晔/",
    "tags": [
      "友情"
    ]
  },
  {
    "title": "赐萧瑀",
    "poet": "李世民",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "哲理",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/赐萧瑀/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "渡汉江",
    "poet": "宋之问",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "思乡",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/渡汉江/",
    "tags": [
      "思乡"
    ]
  },
  {
    "title": "逢雪宿芙蓉山主人",
    "poet": "刘长卿",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "山水",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/逢雪宿芙蓉山主人/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "江畔独步寻花",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "春天",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/江畔独步寻花/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "赠花卿",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "音乐",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/赠花卿/",
    "tags": [
      "音乐"
    ]
  },
  {
    "title": "绝句漫兴九首（其五）",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "春天",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/绝句漫兴九首(其五)/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "望月怀远（节选）",
    "poet": "张九龄",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "思念",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/望月怀远(节选)/",
    "tags": [
      "思念"
    ]
  },
  {
    "title": "少年行（其一）",
    "poet": "王维",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "豪迈",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/少年行(其一)/",
    "tags": [
      "豪迈"
    ]
  },
  {
    "title": "相思",
    "poet": "王维",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "爱情",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/相思/",
    "tags": [
      "爱情"
    ]
  },
  {
    "title": "秋浦歌",
    "poet": "李白",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "咏怀",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/秋浦歌/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "劝学",
    "poet": "颜真卿",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "学习",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/劝学/",
    "tags": [
      "学习"
    ]
  },
  {
    "title": "采莲曲",
    "poet": "刘方平",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "田园",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/采莲曲/",
    "tags": [
      "田园"
    ]
  },
  {
    "title": "江村即事",
    "poet": "司空曙",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "田园",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/江村即事/",
    "tags": [
      "田园"
    ]
  },
  {
    "title": "登科后",
    "poet": "孟郊",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏怀",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/登科后/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "题都城南庄",
    "poet": "崔护",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "爱情",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/题都城南庄/",
    "tags": [
      "爱情"
    ]
  },
  {
    "title": "秋思",
    "poet": "张籍",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "思乡",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/秋思/",
    "tags": [
      "思乡"
    ]
  },
  {
    "title": "乌衣巷",
    "poet": "刘禹锡",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏史",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/乌衣巷/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "竹枝词",
    "poet": "刘禹锡",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "爱情",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/竹枝词/",
    "tags": [
      "爱情"
    ]
  },
  {
    "title": "遗爱寺",
    "poet": "白居易",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "山水",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/遗爱寺/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "菊花",
    "poet": "元稹",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏物",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/菊花/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "剑客",
    "poet": "贾岛",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "咏怀",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/剑客/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "题李凝幽居（节选）",
    "poet": "贾岛",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "隐逸",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/题李凝幽居(节选)/",
    "tags": [
      "隐逸"
    ]
  },
  {
    "title": "赋新月",
    "poet": "缪氏子",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏物",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/赋新月/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "南园十三首（其五）",
    "poet": "李贺",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏怀",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/南园十三首(其五)/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "题乌江亭",
    "poet": "杜牧",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏史",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/题乌江亭/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "秋夕",
    "poet": "杜牧",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "七夕",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/秋夕/",
    "tags": [
      "七夕"
    ]
  },
  {
    "title": "金缕衣",
    "poet": "杜秋娘",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "惜时",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/金缕衣/",
    "tags": [
      "惜时"
    ]
  },
  {
    "title": "韩冬郎即席为诗相送",
    "poet": "李商隐",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "送别",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/韩冬郎即席为诗相送/",
    "tags": [
      "送别"
    ]
  },
  {
    "title": "江楼感旧",
    "poet": "赵嘏",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏怀",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/江楼感旧/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "秋日湖上",
    "poet": "薛莹",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "咏怀",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/秋日湖上/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "农家",
    "poet": "颜仁郁",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "民生",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/农家/",
    "tags": [
      "民生"
    ]
  },
  {
    "title": "己亥岁",
    "poet": "曹松",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "战争",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/己亥岁/",
    "tags": [
      "战争"
    ]
  },
  {
    "title": "小松",
    "poet": "杜荀鹤",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏物",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/小松/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "自菩提步月归广化寺",
    "poet": "欧阳修",
    "dynasty": "宋",
    "type": "五言绝句",
    "theme": "写景",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/自菩提步月归广化寺/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "题花山寺壁",
    "poet": "苏舜钦",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "哲理",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/题花山寺壁/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "蚕妇",
    "poet": "张俞",
    "dynasty": "宋",
    "type": "五言绝句",
    "theme": "民生",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/蚕妇/",
    "tags": [
      "民生"
    ]
  },
  {
    "title": "咏柳",
    "poet": "曾巩",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "咏物",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/咏柳/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "客中初夏",
    "poet": "司马光",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "写景",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/客中初夏/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "江上",
    "poet": "王安石",
    "dynasty": "宋",
    "type": "五言绝句",
    "theme": "写景",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/江上/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "春日偶成",
    "poet": "程颢",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "春天",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/春日偶成/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "送春",
    "poet": "王令",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "惜时",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/送春/",
    "tags": [
      "惜时"
    ]
  },
  {
    "title": "鄂州南楼书事四首（其一）",
    "poet": "黄庭坚",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "写景",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/鄂州南楼书事四首(其一)/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "绝句四首（其四）",
    "poet": "陈师道",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "写景",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/绝句四首(其四)/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "题青泥市壁",
    "poet": "岳飞",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "爱国",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/题青泥市壁/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "冬夜读书示子聿",
    "poet": "陆游",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "学习",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/冬夜读书示子聿/",
    "tags": [
      "学习"
    ]
  },
  {
    "title": "同儿辈赋未开海棠（其一）",
    "poet": "元好问",
    "dynasty": "金",
    "type": "七言绝句",
    "theme": "哲理",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/同儿辈赋未开海棠(其一)/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "寒夜",
    "poet": "杜耒",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "友情",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/寒夜/",
    "tags": [
      "友情"
    ]
  },
  {
    "title": "北风行",
    "poet": "刘基",
    "dynasty": "明",
    "type": "乐府诗",
    "theme": "战争",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/北风行/",
    "tags": [
      "战争"
    ]
  },
  {
    "title": "首夏山中行吟",
    "poet": "祝允明",
    "dynasty": "明",
    "type": "七言绝句",
    "theme": "写景",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/首夏山中行吟/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "绝句",
    "poet": "文征明",
    "dynasty": "明",
    "type": "五言绝句",
    "theme": "写景",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/绝句/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "就义诗",
    "poet": "杨继盛",
    "dynasty": "明",
    "type": "五言绝句",
    "theme": "爱国",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/就义诗/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "明日歌",
    "poet": "钱福",
    "dynasty": "明",
    "type": "乐府诗",
    "theme": "惜时",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/明日歌/",
    "tags": [
      "惜时"
    ]
  },
  {
    "title": "马上作",
    "poet": "戚继光",
    "dynasty": "明",
    "type": "七言绝句",
    "theme": "爱国",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/马上作/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "出师讨满夷自瓜州至金陵",
    "poet": "郑成功",
    "dynasty": "明",
    "type": "七言绝句",
    "theme": "爱国",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/出师讨满夷自瓜州至金陵/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "山雨",
    "poet": "偰逊",
    "dynasty": "明",
    "type": "五言绝句",
    "theme": "写景",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/山雨/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "论诗五绝（其二）",
    "poet": "赵翼",
    "dynasty": "清",
    "type": "七言绝句",
    "theme": "哲理",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/论诗五绝(其二)/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "锦云川",
    "poet": "毕沅",
    "dynasty": "清",
    "type": "五言绝句",
    "theme": "写景",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/锦云川/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "塞外杂咏",
    "poet": "林则徐",
    "dynasty": "清",
    "type": "七言绝句",
    "theme": "咏怀",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/塞外杂咏/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "狱中题壁",
    "poet": "谭嗣同",
    "dynasty": "清",
    "type": "七言绝句",
    "theme": "爱国",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/狱中题壁/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "对酒",
    "poet": "秋瑾",
    "dynasty": "近现代",
    "type": "七言绝句",
    "theme": "爱国",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/对酒/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "闻王昌龄左迁龙标遥有此寄",
    "poet": "李白",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "送别",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/闻王昌龄左迁龙标遥有此寄/",
    "tags": [
      "送别"
    ]
  },
  {
    "title": "峨眉山月歌",
    "poet": "李白",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "山水",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/峨眉山月歌/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "江南逢李龟年",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏怀",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/江南逢李龟年/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "房兵曹胡马",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "咏物",
    "grade": "01-幼儿园",
    "grade_label": "幼儿园",
    "semester": "",
    "path": "01-幼儿园/房兵曹胡马/",
    "tags": [
      "咏物"
    ]
  }
];
</script>
<script src="../../assets/scripts/poems-filter.js"></script>
