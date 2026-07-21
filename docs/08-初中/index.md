---
standalone_title: "初中古诗 - 古诗诵读"
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
  <p class="poems-kicker">GRADE 7</p>
  <h1>初中古诗</h1>
  <p>共 118 篇 · 支持筛选</p>
</section>

<section class="poems-section">
  <div class="poems-section-heading">
    <h2>篇目列表</h2>
    <p>在下方表格中筛选题目、作者、朝代、类型、主题等。</p>
  </div>

  <div id="poems-table-wrapper" data-grade="08-初中">
    
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
    "title": "观沧海",
    "poet": "曹操",
    "dynasty": "汉",
    "type": "乐府诗",
    "theme": "咏怀",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/观沧海/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "次北固山下",
    "poet": "王湾",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "思乡",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/次北固山下/",
    "tags": [
      "思乡"
    ]
  },
  {
    "title": "天净沙·秋思",
    "poet": "马致远",
    "dynasty": "元",
    "type": "散曲",
    "theme": "思乡",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/天净沙·秋思/",
    "tags": [
      "思乡"
    ]
  },
  {
    "title": "行军九日思长安故园",
    "poet": "岑参",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "战争",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/行军九日思长安故园/",
    "tags": [
      "战争"
    ]
  },
  {
    "title": "夜上受降城闻笛",
    "poet": "李益",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "思乡",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/夜上受降城闻笛/",
    "tags": [
      "思乡"
    ]
  },
  {
    "title": "秋词",
    "poet": "刘禹锡",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "秋天",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/秋词/",
    "tags": [
      "秋天"
    ]
  },
  {
    "title": "夜雨寄北",
    "poet": "李商隐",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "思念",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/夜雨寄北/",
    "tags": [
      "思念"
    ]
  },
  {
    "title": "十一月四日风雨大作",
    "poet": "陆游",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "爱国",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/十一月四日风雨大作/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "潼关",
    "poet": "谭嗣同",
    "dynasty": "清",
    "type": "七言绝句",
    "theme": "山河",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/潼关/",
    "tags": [
      "山河"
    ]
  },
  {
    "title": "《论语》十二章",
    "poet": "孔子",
    "dynasty": "春秋",
    "type": "文言文",
    "theme": "学习",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/论语十二章/",
    "tags": [
      "学习"
    ]
  },
  {
    "title": "诫子书",
    "poet": "诸葛亮",
    "dynasty": "三国",
    "type": "文言文",
    "theme": "修身",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/诫子书/",
    "tags": [
      "修身"
    ]
  },
  {
    "title": "木兰诗",
    "poet": "北朝民歌",
    "dynasty": "北朝",
    "type": "乐府诗",
    "theme": "巾帼",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/木兰诗/",
    "tags": [
      "巾帼"
    ]
  },
  {
    "title": "竹里馆",
    "poet": "王维",
    "dynasty": "唐",
    "type": "五言绝句",
    "theme": "隐逸",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/竹里馆/",
    "tags": [
      "隐逸"
    ]
  },
  {
    "title": "春夜洛城闻笛",
    "poet": "李白",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "思乡",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/春夜洛城闻笛/",
    "tags": [
      "思乡"
    ]
  },
  {
    "title": "逢入京使",
    "poet": "岑参",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "思乡",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/逢入京使/",
    "tags": [
      "思乡"
    ]
  },
  {
    "title": "晚春",
    "poet": "韩愈",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "春天",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/晚春/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "登幽州台歌",
    "poet": "陈子昂",
    "dynasty": "唐",
    "type": "五言古诗",
    "theme": "咏怀",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/登幽州台歌/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "望岳",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "山水",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/望岳/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "登飞来峰",
    "poet": "王安石",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "哲理",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/登飞来峰/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "游山西村",
    "poet": "陆游",
    "dynasty": "宋",
    "type": "七言律诗",
    "theme": "田园",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/游山西村/",
    "tags": [
      "田园"
    ]
  },
  {
    "title": "己亥杂诗（浩荡离愁白日斜）",
    "poet": "龚自珍",
    "dynasty": "清",
    "type": "七言绝句",
    "theme": "爱国",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/己亥杂诗(浩荡离愁白日斜)/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "泊秦淮",
    "poet": "杜牧",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏史",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/泊秦淮/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "贾生",
    "poet": "李商隐",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏史",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/贾生/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "过松源晨炊漆公店",
    "poet": "杨万里",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "哲理",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/过松源晨炊漆公店/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "约客",
    "poet": "赵师秀",
    "dynasty": "宋",
    "type": "七言绝句",
    "theme": "闲适",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/约客/",
    "tags": [
      "闲适"
    ]
  },
  {
    "title": "陋室铭",
    "poet": "刘禹锡",
    "dynasty": "唐",
    "type": "文言文",
    "theme": "隐逸",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/陋室铭/",
    "tags": [
      "隐逸"
    ]
  },
  {
    "title": "爱莲说",
    "poet": "周敦颐",
    "dynasty": "宋",
    "type": "文言文",
    "theme": "咏物",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/爱莲说/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "河中石兽",
    "poet": "纪昀",
    "dynasty": "清",
    "type": "文言文",
    "theme": "哲理",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/河中石兽/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "野望",
    "poet": "王绩",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "田园",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/野望/",
    "tags": [
      "田园"
    ]
  },
  {
    "title": "黄鹤楼",
    "poet": "崔颢",
    "dynasty": "唐",
    "type": "七言律诗",
    "theme": "思乡",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/黄鹤楼/",
    "tags": [
      "思乡"
    ]
  },
  {
    "title": "使至塞上",
    "poet": "王维",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "边塞",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/使至塞上/",
    "tags": [
      "边塞"
    ]
  },
  {
    "title": "渡荆门送别",
    "poet": "李白",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "送别",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/渡荆门送别/",
    "tags": [
      "送别"
    ]
  },
  {
    "title": "钱塘湖春行",
    "poet": "白居易",
    "dynasty": "唐",
    "type": "七言律诗",
    "theme": "春天",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/钱塘湖春行/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "庭中有奇树",
    "poet": "古诗十九首",
    "dynasty": "汉",
    "type": "五言古诗",
    "theme": "思念",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/庭中有奇树/",
    "tags": [
      "思念"
    ]
  },
  {
    "title": "龟虽寿",
    "poet": "曹操",
    "dynasty": "汉",
    "type": "乐府诗",
    "theme": "哲理",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/龟虽寿/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "赠从弟",
    "poet": "刘桢",
    "dynasty": "汉",
    "type": "五言古诗",
    "theme": "咏物",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/赠从弟/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "梁甫行",
    "poet": "曹植",
    "dynasty": "三国",
    "type": "乐府诗",
    "theme": "民生",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/梁甫行/",
    "tags": [
      "民生"
    ]
  },
  {
    "title": "饮酒（其五）",
    "poet": "陶渊明",
    "dynasty": "晋",
    "type": "五言古诗",
    "theme": "隐逸",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/饮酒(其五)/",
    "tags": [
      "隐逸"
    ]
  },
  {
    "title": "春望",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "爱国",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/春望/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "雁门太守行",
    "poet": "李贺",
    "dynasty": "唐",
    "type": "乐府诗",
    "theme": "边塞",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/雁门太守行/",
    "tags": [
      "边塞"
    ]
  },
  {
    "title": "赤壁",
    "poet": "杜牧",
    "dynasty": "唐",
    "type": "七言绝句",
    "theme": "咏史",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/赤壁/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "渔家傲（天接云涛连晓雾）",
    "poet": "李清照",
    "dynasty": "宋",
    "type": "词",
    "theme": "咏怀",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/渔家傲(天接云涛连晓雾)/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "浣溪沙（一曲新词酒一杯）",
    "poet": "晏殊",
    "dynasty": "宋",
    "type": "词",
    "theme": "惜时",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/浣溪沙(一曲新词酒一杯)/",
    "tags": [
      "惜时"
    ]
  },
  {
    "title": "采桑子（轻舟短棹西湖好）",
    "poet": "欧阳修",
    "dynasty": "宋",
    "type": "词",
    "theme": "山水",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/采桑子(轻舟短棹西湖好)/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "相见欢（金陵城上西楼）",
    "poet": "朱敦儒",
    "dynasty": "宋",
    "type": "词",
    "theme": "爱国",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/相见欢(金陵城上西楼)/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "如梦令（常记溪亭日暮）",
    "poet": "李清照",
    "dynasty": "宋",
    "type": "词",
    "theme": "写景",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/如梦令(常记溪亭日暮)/",
    "tags": [
      "写景"
    ]
  },
  {
    "title": "三峡",
    "poet": "郦道元",
    "dynasty": "北魏",
    "type": "文言文",
    "theme": "山水",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/三峡/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "答谢中书书",
    "poet": "陶弘景",
    "dynasty": "南朝",
    "type": "文言文",
    "theme": "山水",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/答谢中书书/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "记承天寺夜游",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "文言文",
    "theme": "旷达",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/记承天寺夜游/",
    "tags": [
      "旷达"
    ]
  },
  {
    "title": "与朱元思书",
    "poet": "吴均",
    "dynasty": "南朝",
    "type": "文言文",
    "theme": "山水",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/与朱元思书/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "富贵不能淫",
    "poet": "孟子",
    "dynasty": "战国",
    "type": "文言文",
    "theme": "修身",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/富贵不能淫/",
    "tags": [
      "修身"
    ]
  },
  {
    "title": "生于忧患 死于安乐",
    "poet": "孟子",
    "dynasty": "战国",
    "type": "文言文",
    "theme": "修身",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/生于忧患 死于安乐/",
    "tags": [
      "修身"
    ]
  },
  {
    "title": "关雎",
    "poet": "诗经",
    "dynasty": "先秦",
    "type": "四言古诗",
    "theme": "爱情",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/关雎/",
    "tags": [
      "爱情"
    ]
  },
  {
    "title": "蒹葭",
    "poet": "诗经",
    "dynasty": "先秦",
    "type": "四言古诗",
    "theme": "爱情",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/蒹葭/",
    "tags": [
      "爱情"
    ]
  },
  {
    "title": "式微",
    "poet": "诗经",
    "dynasty": "先秦",
    "type": "四言古诗",
    "theme": "民生",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/式微/",
    "tags": [
      "民生"
    ]
  },
  {
    "title": "子衿",
    "poet": "诗经",
    "dynasty": "先秦",
    "type": "四言古诗",
    "theme": "爱情",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/子衿/",
    "tags": [
      "爱情"
    ]
  },
  {
    "title": "送杜少府之任蜀州",
    "poet": "王勃",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "送别",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/送杜少府之任蜀州/",
    "tags": [
      "送别"
    ]
  },
  {
    "title": "望洞庭湖赠张丞相",
    "poet": "孟浩然",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "山水",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/望洞庭湖赠张丞相/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "茅屋为秋风所破歌",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "七言古诗",
    "theme": "民生",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/茅屋为秋风所破歌/",
    "tags": [
      "民生"
    ]
  },
  {
    "title": "卖炭翁",
    "poet": "白居易",
    "dynasty": "唐",
    "type": "乐府诗",
    "theme": "民生",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/卖炭翁/",
    "tags": [
      "民生"
    ]
  },
  {
    "title": "题破山寺后禅院",
    "poet": "常建",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "山水",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/题破山寺后禅院/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "送友人",
    "poet": "李白",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "送别",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/送友人/",
    "tags": [
      "送别"
    ]
  },
  {
    "title": "卜算子·黄州定慧院寓居作",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "词",
    "theme": "咏怀",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/卜算子·黄州定慧院寓居作/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "卜算子·咏梅（陆游）",
    "poet": "陆游",
    "dynasty": "宋",
    "type": "词",
    "theme": "咏物",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/卜算子·咏梅(陆游)/",
    "tags": [
      "咏物"
    ]
  },
  {
    "title": "桃花源记",
    "poet": "陶渊明",
    "dynasty": "晋",
    "type": "文言文",
    "theme": "理想",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/桃花源记/",
    "tags": [
      "理想"
    ]
  },
  {
    "title": "小石潭记",
    "poet": "柳宗元",
    "dynasty": "唐",
    "type": "文言文",
    "theme": "山水",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/小石潭记/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "北冥有鱼",
    "poet": "庄子",
    "dynasty": "战国",
    "type": "文言文",
    "theme": "哲理",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/北冥有鱼/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "虽有嘉肴",
    "poet": "《礼记》",
    "dynasty": "西汉",
    "type": "文言文",
    "theme": "学习",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/虽有嘉肴/",
    "tags": [
      "学习"
    ]
  },
  {
    "title": "大道之行也",
    "poet": "《礼记》",
    "dynasty": "西汉",
    "type": "文言文",
    "theme": "理想",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/大道之行也/",
    "tags": [
      "理想"
    ]
  },
  {
    "title": "马说",
    "poet": "韩愈",
    "dynasty": "唐",
    "type": "文言文",
    "theme": "哲理",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/马说/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "行路难（其一）",
    "poet": "李白",
    "dynasty": "唐",
    "type": "七言古诗",
    "theme": "咏怀",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/行路难(其一)/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "酬乐天扬州初逢席上见赠",
    "poet": "刘禹锡",
    "dynasty": "唐",
    "type": "七言律诗",
    "theme": "咏怀",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/酬乐天扬州初逢席上见赠/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "水调歌头（明月几时有）",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "词",
    "theme": "哲理",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/水调歌头(明月几时有)/",
    "tags": [
      "哲理"
    ]
  },
  {
    "title": "月夜忆舍弟",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "思乡",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/月夜忆舍弟/",
    "tags": [
      "思乡"
    ]
  },
  {
    "title": "长沙过贾谊宅",
    "poet": "刘长卿",
    "dynasty": "唐",
    "type": "七言律诗",
    "theme": "咏史",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/长沙过贾谊宅/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "左迁至蓝关示侄孙湘",
    "poet": "韩愈",
    "dynasty": "唐",
    "type": "七言律诗",
    "theme": "咏怀",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/左迁至蓝关示侄孙湘/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "商山早行",
    "poet": "温庭筠",
    "dynasty": "唐",
    "type": "五言律诗",
    "theme": "羁旅",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/商山早行/",
    "tags": [
      "羁旅"
    ]
  },
  {
    "title": "咸阳城东楼",
    "poet": "许浑",
    "dynasty": "唐",
    "type": "七言律诗",
    "theme": "咏史",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/咸阳城东楼/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "无题",
    "poet": "李商隐",
    "dynasty": "唐",
    "type": "七言律诗",
    "theme": "爱情",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/无题/",
    "tags": [
      "爱情"
    ]
  },
  {
    "title": "行香子（树绕村庄）",
    "poet": "秦观",
    "dynasty": "宋",
    "type": "词",
    "theme": "春天",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/行香子(树绕村庄)/",
    "tags": [
      "春天"
    ]
  },
  {
    "title": "丑奴儿·书博山道中壁",
    "poet": "辛弃疾",
    "dynasty": "宋",
    "type": "词",
    "theme": "咏怀",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/丑奴儿·书博山道中壁/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "岳阳楼记",
    "poet": "范仲淹",
    "dynasty": "宋",
    "type": "文言文",
    "theme": "咏怀",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/岳阳楼记/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "醉翁亭记",
    "poet": "欧阳修",
    "dynasty": "宋",
    "type": "文言文",
    "theme": "山水",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/醉翁亭记/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "湖心亭看雪",
    "poet": "张岱",
    "dynasty": "明",
    "type": "文言文",
    "theme": "山水",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/湖心亭看雪/",
    "tags": [
      "山水"
    ]
  },
  {
    "title": "渔家傲·秋思",
    "poet": "范仲淹",
    "dynasty": "宋",
    "type": "词",
    "theme": "边塞",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/渔家傲·秋思/",
    "tags": [
      "边塞"
    ]
  },
  {
    "title": "江城子·密州出猎",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "词",
    "theme": "豪迈",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/江城子·密州出猎/",
    "tags": [
      "豪迈"
    ]
  },
  {
    "title": "破阵子·为陈同甫赋壮词以寄之",
    "poet": "辛弃疾",
    "dynasty": "宋",
    "type": "词",
    "theme": "爱国",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/破阵子·为陈同甫赋壮词以寄之/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "定风波（莫听穿林打叶声）",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "词",
    "theme": "旷达",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/定风波(莫听穿林打叶声)/",
    "tags": [
      "旷达"
    ]
  },
  {
    "title": "临江仙·夜登小阁",
    "poet": "陈与义",
    "dynasty": "宋",
    "type": "词",
    "theme": "咏怀",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/临江仙·夜登小阁/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "太常引·建康中秋夜为吕叔潜赋",
    "poet": "辛弃疾",
    "dynasty": "宋",
    "type": "词",
    "theme": "咏怀",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/太常引·建康中秋夜为吕叔潜赋/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "浣溪沙（身向云山那畔行）",
    "poet": "纳兰性德",
    "dynasty": "清",
    "type": "词",
    "theme": "羁旅",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/浣溪沙(身向云山那畔行)/",
    "tags": [
      "羁旅"
    ]
  },
  {
    "title": "十五从军征",
    "poet": "乐府诗集",
    "dynasty": "汉",
    "type": "乐府诗",
    "theme": "战争",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/十五从军征/",
    "tags": [
      "战争"
    ]
  },
  {
    "title": "白雪歌送武判官归京",
    "poet": "岑参",
    "dynasty": "唐",
    "type": "七言古诗",
    "theme": "边塞",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/白雪歌送武判官归京/",
    "tags": [
      "边塞"
    ]
  },
  {
    "title": "南乡子·登京口北固亭有怀",
    "poet": "辛弃疾",
    "dynasty": "宋",
    "type": "词",
    "theme": "咏史",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/南乡子·登京口北固亭有怀/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "过零丁洋",
    "poet": "文天祥",
    "dynasty": "宋",
    "type": "七言律诗",
    "theme": "爱国",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/过零丁洋/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "山坡羊·潼关怀古",
    "poet": "张养浩",
    "dynasty": "元",
    "type": "散曲",
    "theme": "咏史",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/山坡羊·潼关怀古/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "南安军",
    "poet": "文天祥",
    "dynasty": "宋",
    "type": "五言律诗",
    "theme": "爱国",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/南安军/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "别云间",
    "poet": "夏完淳",
    "dynasty": "明",
    "type": "五言律诗",
    "theme": "爱国",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/别云间/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "山坡羊·骊山怀古",
    "poet": "张养浩",
    "dynasty": "元",
    "type": "散曲",
    "theme": "咏史",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/山坡羊·骊山怀古/",
    "tags": [
      "咏史"
    ]
  },
  {
    "title": "朝天子·咏喇叭",
    "poet": "王磐",
    "dynasty": "明",
    "type": "散曲",
    "theme": "讽刺",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/朝天子·咏喇叭/",
    "tags": [
      "讽刺"
    ]
  },
  {
    "title": "鱼我所欲也",
    "poet": "孟子",
    "dynasty": "战国",
    "type": "文言文",
    "theme": "修身",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/鱼我所欲也/",
    "tags": [
      "修身"
    ]
  },
  {
    "title": "曹刿论战",
    "poet": "《左传》",
    "dynasty": "春秋",
    "type": "文言文",
    "theme": "战争",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/曹刿论战/",
    "tags": [
      "战争"
    ]
  },
  {
    "title": "送东阳马生序（节选）",
    "poet": "宋濂",
    "dynasty": "明",
    "type": "文言文",
    "theme": "学习",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/送东阳马生序(节选)/",
    "tags": [
      "学习"
    ]
  },
  {
    "title": "出师表",
    "poet": "诸葛亮",
    "dynasty": "三国",
    "type": "文言文",
    "theme": "爱国",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/出师表/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "满江红（小住京华）",
    "poet": "秋瑾",
    "dynasty": "近现代",
    "type": "词",
    "theme": "爱国",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/满江红(小住京华)/",
    "tags": [
      "爱国"
    ]
  },
  {
    "title": "浣溪沙（簌簌衣巾落枣花）",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "词",
    "theme": "田园",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/浣溪沙(簌簌衣巾落枣花)/",
    "tags": [
      "田园"
    ]
  },
  {
    "title": "临江仙·夜归临皋",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "词",
    "theme": "旷达",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/临江仙·夜归临皋/",
    "tags": [
      "旷达"
    ]
  },
  {
    "title": "沁园春·雪",
    "poet": "毛泽东",
    "dynasty": "近现代",
    "type": "词",
    "theme": "咏怀",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/沁园春·雪/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "观刈麦",
    "poet": "白居易",
    "dynasty": "唐",
    "type": "乐府诗",
    "theme": "民生",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/观刈麦/",
    "tags": [
      "民生"
    ]
  },
  {
    "title": "相见欢（无言独上西楼）",
    "poet": "李煜",
    "dynasty": "五代",
    "type": "词",
    "theme": "咏怀",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/相见欢(无言独上西楼)/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "归园田居（其三）",
    "poet": "陶渊明",
    "dynasty": "晋",
    "type": "五言古诗",
    "theme": "隐逸",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/归园田居(其三)/",
    "tags": [
      "隐逸"
    ]
  },
  {
    "title": "宣州谢朓楼饯别校书叔云",
    "poet": "李白",
    "dynasty": "唐",
    "type": "七言古诗",
    "theme": "咏怀",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/宣州谢朓楼饯别校书叔云/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "登楼",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "七言律诗",
    "theme": "咏怀",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/登楼/",
    "tags": [
      "咏怀"
    ]
  },
  {
    "title": "石壕吏",
    "poet": "杜甫",
    "dynasty": "唐",
    "type": "五言古诗",
    "theme": "民生",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/石壕吏/",
    "tags": [
      "民生"
    ]
  },
  {
    "title": "忆江南（梳洗罢）",
    "poet": "温庭筠",
    "dynasty": "唐",
    "type": "词",
    "theme": "思念",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/忆江南(梳洗罢)/",
    "tags": [
      "思念"
    ]
  },
  {
    "title": "浣溪沙（山下兰芽短浸溪）",
    "poet": "苏轼",
    "dynasty": "宋",
    "type": "词",
    "theme": "旷达",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/浣溪沙(山下兰芽短浸溪)/",
    "tags": [
      "旷达"
    ]
  },
  {
    "title": "醉花阴",
    "poet": "李清照",
    "dynasty": "宋",
    "type": "词",
    "theme": "思念",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/醉花阴/",
    "tags": [
      "思念"
    ]
  },
  {
    "title": "邹忌讽齐王纳谏",
    "poet": "《战国策》",
    "dynasty": "西汉",
    "type": "文言文",
    "theme": "治国",
    "grade": "08-初中",
    "grade_label": "初中",
    "semester": "",
    "path": "08-初中/邹忌讽齐王纳谏/",
    "tags": [
      "治国"
    ]
  }
];
</script>
<script src="../../assets/scripts/poems-filter.js"></script>
