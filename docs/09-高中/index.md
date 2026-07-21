---
standalone_title: "高中古诗 - 古诗诵读"
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
  <p class="poems-kicker">GRADE 8</p>
  <h1>高中古诗</h1>
  <p>共 52 篇 · 支持筛选</p>
</section>

<section class="poems-section">
  <div class="poems-section-heading">
    <h2>篇目列表</h2>
    <p>在下方表格中筛选题目、作者、朝代、类型、主题等。</p>
  </div>

  <div id="poems-table-wrapper" data-grade="09-高中">
    
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
    "title": "沁园春·长沙",
    "poet": "毛泽东",
    "dynasty": "近现代",
    "type": "词",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/沁园春·长沙/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "短歌行",
    "poet": "曹操",
    "dynasty": "汉",
    "type": "乐府诗",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/短歌行/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "归园田居（其一）",
    "poet": "陶渊明",
    "dynasty": "晋",
    "type": "五言古诗",
    "theme": "隐逸",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/归园田居(其一)/",
    "tags": [
      "隐逸"
    ]
  },
  {
    "title": "梦游天姥吟留别",
    "poet": "李白",
    "dynasty": "唐",
    "type": "七言古诗",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/梦游天姥吟留别/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "登高",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "七言律诗",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/登高/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "琵琶行",
    "poet": "白居易",
    "dynasty": "唐",
    "type": "七言古诗",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/琵琶行/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "念奴娇·赤壁怀古",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "词",
    "theme": "咏史",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/念奴娇·赤壁怀古/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "永遇乐·京口北固亭怀古",
    "poet": "辛弃疾",
    "dynasty": "宋",
    "type": "词",
    "theme": "咏史",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/永遇乐·京口北固亭怀古/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "声声慢",
    "poet": "李清照",
    "dynasty": "宋",
    "type": "词",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/声声慢/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "静女",
    "poet": "诗经",
    "dynasty": "先秦",
    "type": "四言古诗",
    "theme": "爱情",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/静女/",
    "tags": [
      "爱情"
    ]
  },
  {
    "title": "涉江采芙蓉",
    "poet": "古诗十九首",
    "dynasty": "汉",
    "type": "五言古诗",
    "theme": "思念",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/涉江采芙蓉/",
    "tags": [
      "思念"
    ]
  },
  {
    "title": "虞美人",
    "poet": "李煜",
    "dynasty": "五代",
    "type": "词",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/虞美人/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "鹊桥仙",
    "poet": "秦观",
    "dynasty": "宋",
    "type": "词",
    "theme": "爱情",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/鹊桥仙/",
    "tags": [
      "爱情"
    ]
  },
  {
    "title": "苏幕遮·燎沉香",
    "poet": "周邦彦",
    "dynasty": "宋",
    "type": "词",
    "theme": "写景",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/苏幕遮·燎沉香/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "蜀道难",
    "poet": "李白",
    "dynasty": "唐",
    "type": "乐府诗",
    "theme": "山水",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/蜀道难/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "蜀相",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "七言律诗",
    "theme": "咏史",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/蜀相/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "望海潮",
    "poet": "柳永",
    "dynasty": "宋",
    "type": "词",
    "theme": "写景",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/望海潮/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "扬州慢",
    "poet": "姜夔",
    "dynasty": "宋",
    "type": "词",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/扬州慢/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "锦瑟",
    "poet": "李商隐",
    "dynasty": "唐",
    "type": "七言律诗",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/锦瑟/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "书愤",
    "poet": "陆游",
    "dynasty": "宋",
    "type": "七言律诗",
    "theme": "爱国",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/书愤/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "将进酒",
    "poet": "李白",
    "dynasty": "唐",
    "type": "乐府诗",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/将进酒/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "江城子·乙卯正月二十日夜记梦",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "词",
    "theme": "爱情",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/江城子·乙卯正月二十日夜记梦/",
    "tags": [
      "爱情"
    ]
  },
  {
    "title": "桂枝香·金陵怀古",
    "poet": "王安石",
    "dynasty": "宋",
    "type": "词",
    "theme": "咏史",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/桂枝香·金陵怀古/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "念奴娇·过洞庭",
    "poet": "张孝祥",
    "dynasty": "宋",
    "type": "词",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/念奴娇·过洞庭/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "菩萨蛮·书江西造口壁",
    "poet": "辛弃疾",
    "dynasty": "宋",
    "type": "词",
    "theme": "爱国",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/菩萨蛮·书江西造口壁/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "青玉案·元夕",
    "poet": "辛弃疾",
    "dynasty": "宋",
    "type": "词",
    "theme": "爱情",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/青玉案·元夕/",
    "tags": [
      "爱情"
    ]
  },
  {
    "title": "贺新郎·国脉微如缕",
    "poet": "刘克庄",
    "dynasty": "宋",
    "type": "词",
    "theme": "爱国",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/贺新郎·国脉微如缕/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "长亭送别",
    "poet": "王实甫",
    "dynasty": "元",
    "type": "杂剧",
    "theme": "爱情",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/长亭送别/",
    "tags": [
      "爱情"
    ]
  },
  {
    "title": "燕歌行",
    "poet": "高适",
    "dynasty": "唐",
    "type": "乐府诗",
    "theme": "边塞",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/燕歌行/",
    "tags": [
      "边塞"
    ]
  },
  {
    "title": "李凭箜篌引",
    "poet": "李贺",
    "dynasty": "唐",
    "type": "乐府诗",
    "theme": "音乐",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/李凭箜篌引/",
    "tags": [
      "音乐"
    ]
  },
  {
    "title": "客至",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "七言律诗",
    "theme": "田园",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/客至/",
    "tags": [
      "田园"
    ]
  },
  {
    "title": "登快阁",
    "poet": "黄庭坚",
    "dynasty": "宋",
    "type": "七言律诗",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/登快阁/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "临安春雨初霁",
    "poet": "陆游",
    "dynasty": "宋",
    "type": "七言律诗",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/临安春雨初霁/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "登岳阳楼",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/登岳阳楼/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "拟行路难·其四",
    "poet": "鲍照",
    "dynasty": "南朝",
    "type": "乐府诗",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/拟行路难·其四/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "菩萨蛮·小山重叠金明灭",
    "poet": "温庭筠",
    "dynasty": "唐",
    "type": "词",
    "theme": "闺怨",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/菩萨蛮·小山重叠金明灭/",
    "tags": [
      "闺怨"
    ]
  },
  {
    "title": "氓",
    "poet": "诗经",
    "dynasty": "先秦",
    "type": "四言古诗",
    "theme": "爱情",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/氓/",
    "tags": [
      "爱情"
    ]
  },
  {
    "title": "离骚（节选）",
    "poet": "屈原",
    "dynasty": "先秦",
    "type": "楚辞",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/离骚(节选)/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "劝学（节选）",
    "poet": "荀子",
    "dynasty": "先秦",
    "type": "文言文",
    "theme": "学习",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/劝学(节选)/",
    "tags": [
      "学习"
    ]
  },
  {
    "title": "师说（节选）",
    "poet": "韩愈",
    "dynasty": "唐",
    "type": "文言文",
    "theme": "学习",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/师说(节选)/",
    "tags": [
      "学习"
    ]
  },
  {
    "title": "赤壁赋（节选）",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "文言文",
    "theme": "哲理",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/赤壁赋(节选)/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "阿房宫赋（节选）",
    "poet": "杜牧",
    "dynasty": "唐",
    "type": "文言文",
    "theme": "咏史",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/阿房宫赋(节选)/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "兵车行",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "乐府诗",
    "theme": "战争",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/兵车行/",
    "tags": [
      "战争"
    ]
  },
  {
    "title": "石头城",
    "poet": "刘禹锡",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏史",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/石头城/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "过华清宫",
    "poet": "杜牧",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏史",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/过华清宫/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "雨霖铃",
    "poet": "柳永",
    "dynasty": "宋",
    "type": "词",
    "theme": "爱情",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/雨霖铃/",
    "tags": [
      "爱情"
    ]
  },
  {
    "title": "逍遥游（节选）",
    "poet": "庄子",
    "dynasty": "战国",
    "type": "文言文",
    "theme": "哲理",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/逍遥游(节选)/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "屈原列传（节选）",
    "poet": "司马迁",
    "dynasty": "汉",
    "type": "文言文",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/屈原列传(节选)/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "陈情表",
    "poet": "李密",
    "dynasty": "晋",
    "type": "文言文",
    "theme": "孝道",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/陈情表/",
    "tags": [
      "孝道"
    ]
  },
  {
    "title": "滕王阁序（节选）",
    "poet": "王勃",
    "dynasty": "唐",
    "type": "文言文",
    "theme": "咏怀",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/滕王阁序(节选)/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "六国论",
    "poet": "苏洵",
    "dynasty": "宋",
    "type": "文言文",
    "theme": "咏史",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/六国论/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "游褒禅山记",
    "poet": "王安石",
    "dynasty": "宋",
    "type": "文言文",
    "theme": "哲理",
    "grade": "09-高中",
    "grade_label": "高中",
    "semester": "",
    "path": "09-高中/游褒禅山记/",
    "tags": [
      "哲理"
    ]
  }
];
</script>
<script src="../../assets/scripts/poems-filter.js"></script>
