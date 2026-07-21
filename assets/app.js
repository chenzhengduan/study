/* ===== 古诗诵读 SPA ===== */
(function () {
  "use strict";

  var DATA_BASE = "data/";
  var GRADE_ORDER = [
    ["01-幼儿园", "幼儿园", "K", "启蒙咏物 · 童趣朗朗"],
    ["02-一年级", "一年级", "1", "短诗入门 · 五言绝句"],
    ["03-二年级", "二年级", "2", "思乡写景 · 名篇起步"],
    ["04-三年级", "三年级", "3", "意境加深 · 七言起步"],
    ["05-四年级", "四年级", "4", "律诗初识 · 情景交融"],
    ["06-五年级", "五年级", "5", "长诗与词 · 主题更广"],
    ["07-六年级", "六年级", "6", "综合复习 · 小学汇总"],
    ["08-初中", "初中", "7-9", "课标必背 · 中考篇目"],
    ["09-高中", "高中", "10-12", "高考必背 · 名篇荟萃"]
  ];
  var GRADE_META = {}; GRADE_ORDER.forEach(function (g) { GRADE_META[g[0]] = { label: g[1], num: g[2], desc: g[3] }; });

  var view = document.getElementById("view");
  var cache = {};
  var searchIndex = null;
  var store = {
    get: function (k, d) { try { var v = localStorage.getItem(k); return v === null ? d : v; } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };
  var state = {
    pinyin: store.get("pinyin", "1") === "1",
    vertical: store.get("vertical", "0") === "1",
    fontSize: parseInt(store.get("fontSize", "21"), 10) || 21
  };

  /* ---------- 工具 ---------- */
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function enc(s) { return encodeURIComponent(s); }
  function dec(s) { try { return decodeURIComponent(s); } catch (e) { return s; } }
  function getJSON(url) { return fetch(url).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }); }

  function loadGrade(grade) {
    if (cache[grade]) return Promise.resolve(cache[grade]);
    return getJSON(DATA_BASE + grade + ".json").then(function (d) { cache[grade] = d; return d; });
  }
  function loadIndex() { return getJSON(DATA_BASE + "index.json"); }

  function buildSearchIndex() {
    if (searchIndex) return Promise.resolve(searchIndex);
    return Promise.all(GRADE_ORDER.map(function (g) { return loadGrade(g[0]).catch(function () { return null; }); }))
      .then(function (shards) {
        var list = [];
        shards.forEach(function (s) {
          if (!s) return;
          s.poems.forEach(function (p) {
            list.push({ t: p.title, p: p.poet, d: p.dynasty, ty: p.type, th: p.theme, g: p.grade, gl: p.grade_label, has: p.lines.length > 0 });
          });
        });
        searchIndex = list; return list;
      });
  }

  /* ---------- 迷你 Markdown ---------- */
  function md(src) {
    if (!src) return "";
    var lines = String(src).split(/\r?\n/), html = "", inList = false;
    function inline(t) {
      return esc(t)
        .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
        .replace(/\*(.+?)\*/g, "<em>$1</em>")
        .replace(/`(.+?)`/g, "<code>$1</code>");
    }
    lines.forEach(function (ln) {
      var li = /^\s*[-*]\s+(.*)$/.exec(ln);
      if (li) { if (!inList) { html += "<ul>"; inList = true; } html += "<li>" + inline(li[1]) + "</li>"; }
      else {
        if (inList) { html += "</ul>"; inList = false; }
        if (ln.trim()) html += "<p>" + inline(ln) + "</p>";
      }
    });
    if (inList) html += "</ul>";
    return html;
  }

  function rubyLine(pairs) {
    return pairs.map(function (pr) {
      var ch = pr[0], py = pr[1];
      if (!py) return esc(ch);
      return "<ruby>" + esc(ch) + "<rt>" + esc(py) + "</rt></ruby>";
    }).join("");
  }

  /* ---------- 主题 ---------- */
  function applyTheme(t) {
    document.documentElement.setAttribute("data-theme", t);
    store.set("theme", t);
    var m = document.querySelector('meta[name="theme-color"]'); if (m) m.setAttribute("content", t === "dark" ? "#141519" : "#ffb300");
  }
  (function initTheme() {
    var t = store.get("theme", null);
    if (!t) t = (window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches) ? "dark" : "light";
    applyTheme(t);
  })();
  document.getElementById("theme-toggle").addEventListener("click", function () {
    applyTheme(document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark");
  });

  /* ---------- 渲染框架 ---------- */
  function setActiveTab(name) {
    document.querySelectorAll(".tab-bar__item").forEach(function (el) {
      el.classList.toggle("is-active", el.getAttribute("data-tab") === name);
    });
  }
  function show(html, tab) { view.innerHTML = html; setActiveTab(tab); window.scrollTo(0, 0); }
  function loading() { view.innerHTML = '<div class="loading"><span class="spinner"></span>加载中…</div>'; }
  function errView(msg) { show('<div class="empty"><span class="empty__icon">⚠</span>' + esc(msg) + "</div>"); }

  /* ---------- 统计 ---------- */
  function countDynasty(allShards) {
    var set = {};
    allShards.forEach(function (s) { if (s) s.poems.forEach(function (p) { if (p.dynasty) set[p.dynasty] = 1; }); });
    return Object.keys(set).length;
  }
  function countPoets(allShards) {
    var set = {};
    allShards.forEach(function (s) { if (s) s.poems.forEach(function (p) { if (p.poet) set[p.poet] = 1; }); });
    return Object.keys(set).length;
  }

  /* ===== 首页 ===== */
  function renderHome() {
    loading();
    Promise.all([loadIndex()].concat(GRADE_ORDER.map(function (g) { return loadGrade(g[0]).catch(function () { return null; }); })))
      .then(function (res) {
        var idx = res[0], shards = res.slice(1);
        var counts = {}; idx.grades.forEach(function (g) { counts[g.grade] = g; });
        var maxCount = Math.max.apply(null, idx.grades.map(function (g) { return g.count; }).concat([1]));

        // 学段分组：启蒙 / 小学 / 初中 / 高中
        var STAGES = [
          { name: "启蒙", range: [0, 1], icon: "🌱" },
          { name: "小学", range: [1, 7], icon: "📖" },
          { name: "初中", range: [7, 8], icon: "🎓" },
          { name: "高中", range: [8, 9], icon: "🏆" }
        ];
        function gradeCard(g) {
          var c = counts[g[0]] || { count: 0, with_body: 0 };
          var readPct = c.count ? Math.round((c.with_body || 0) / c.count * 100) : 0;
          return '<a class="grade-card" href="#/g/' + enc(g[0]) + '">' +
            '<span class="grade-card__badge">' + esc(g[2]) + "</span>" +
            '<span class="grade-card__body">' +
            "<strong>" + esc(g[1]) + "</strong>" +
            "<small>" + esc(g[3]) + "</small>" +
            '<span class="grade-card__meta"><b>' + c.count + '</b> 篇<span class="grade-card__full"> · 全文 ' + (c.with_body || 0) + "</span></span>" +
            '<span class="grade-card__bar"><i style="width:' + readPct + '%"></i></span>' +
            "</span></a>";
        }
        var cards = STAGES.map(function (st) {
          var items = GRADE_ORDER.slice(st.range[0], st.range[1]).map(gradeCard).join("");
          if (!items) return "";
          return '<div class="stage">' +
            '<div class="stage__head"><span class="stage__icon">' + st.icon + "</span><h3>" + st.name + "</h3></div>" +
            '<div class="grade-grid">' + items + "</div></div>";
        }).join("");

        var bars = GRADE_ORDER.map(function (g) {
          var c = counts[g[0]] || { count: 0 };
          var pct = Math.round(c.count / maxCount * 100);
          return '<a class="bar-row" href="#/g/' + enc(g[0]) + '">' +
            '<span class="bar-row__label">' + esc(g[1]) + "</span>" +
            '<span class="bar-row__track"><span class="bar-row__fill" style="width:' + pct + '%"></span></span>' +
            '<span class="bar-row__val">' + c.count + "</span></a>";
        }).join("");

        var totalBody = idx.grades.reduce(function (n, g) { return n + (g.with_body || 0); }, 0);
        var stats =
          stat(idx.total, "收录篇目") + stat(totalBody, "含全文诵读") +
          stat(countPoets(shards), "诗人作者") + stat(countDynasty(shards), "跨越朝代");
        function stat(n, l) { return '<div class="stat"><b>' + n + "</b><span>" + l + "</span></div>"; }

        show(
          '<section class="hero"><p class="hero__kicker">CLASSICAL POEMS</p><h1>古诗诵读</h1>' +
          '<p class="hero__desc">从幼儿园到高中，一首一页。按年级、诗人、朝代、类型、主题查找，支持拼音标注、竖排诵读、译文、注释与赏析，专为手机诵读而生。</p>' +
          '<div class="hero__badges"><span>一首一页</span><span>拼音标注</span><span>竖排诵读</span><span>多维度筛选</span><span>移动端优先</span></div></section>' +

          '<section class="stat-grid">' + stats + "</section>" +

          '<section class="sec"><div class="sec__head"><div><p class="sec__eyebrow">BY GRADE</p><h2>按年级学习</h2></div><p>循序渐进 · 每级有对应篇目</p></div>' +
          '<div class="grade-grid">' + cards + "</div></section>" +

          '<section class="sec"><div class="sec__head"><div><p class="sec__eyebrow">OVERVIEW</p><h2>各年级篇数</h2></div><p>点击进入对应年级</p></div>' +
          '<div class="bar-chart">' + bars + "</div></section>",
          "home"
        );
      }).catch(function () { errView("目录加载失败，请检查 data/index.json"); });
  }

  /* 筛选分组：小标题 + 全选 chip + 各值 chip */
  function fgroup(label, f, obj) {
    var keys = Object.keys(obj).filter(function (k) { return k && k.trim(); }).sort();
    if (!keys.length) return "";
    var chips = '<button class="chip chip--all" data-f="' + f + '" data-v="">全部</button>' +
      keys.map(function (v) { return '<button class="chip" data-f="' + f + '" data-v="' + esc(v) + '">' + esc(v) + "</button>"; }).join("");
    return '<div class="fgroup"><span class="fgroup__label">' + label + '</span><div class="fgroup__chips">' + chips + "</div></div>";
  }

  /* ===== 年级页 ===== */
  function renderGrade(grade, q) {
    loading();
    loadGrade(grade).then(function (shard) {
      var label = shard.label, poems = shard.poems;
      var dyn = {}, typ = {}, thm = {};
      poems.forEach(function (p) { dyn[p.dynasty] = (dyn[p.dynasty] || 0) + 1; typ[p.type] = 1; thm[p.theme] = 1; });

      // 朝代分布迷你条（带色点图例）
      var dynTotal = poems.length || 1;
      var dynKeys = Object.keys(dyn).sort(function (a, b) { return dyn[b] - dyn[a]; });
      var dynSeg = dynKeys.map(function (k, i) {
        var pct = (dyn[k] / dynTotal * 100);
        return '<span class="dynbar__seg c' + (i % 6) + '" style="width:' + pct + '%" title="' + esc(k) + " " + dyn[k] + '篇"></span>';
      }).join("");
      var dynLegend = dynKeys.map(function (k, i) {
        return '<span class="dynbar__key"><i class="dynbar__dot c' + (i % 6) + '"></i>' + esc(k) + " " + dyn[k] + "</span>";
      }).join("");

      var html =
        '<div class="crumbs"><a href="#/">首页</a><i>›</i><span>' + esc(label) + "</span></div>" +
        '<section class="hero hero--grade"><p class="hero__kicker">' + esc(GRADE_META[grade].num) + '</p><h1>' + esc(label) + '古诗</h1>' +
        '<p class="hero__desc">共 ' + shard.count + " 篇 · 点选条件筛选，或搜索题目、作者、主题。</p></section>" +

        '<div class="dynbar"><div class="dynbar__track">' + dynSeg + '</div><div class="dynbar__legend">' + dynLegend + "</div></div>" +

        '<div class="filter-panel">' +
        '<button class="filter-head" id="fhead"><span class="filter-head__title">筛选</span>' +
        '<span class="filter-head__summary" id="fsummary">全部</span>' +
        '<span class="filter-head__chev">▾</span></button>' +
        '<div class="filter-body" id="fbody"><div class="filter-row">' +
        '<input class="filter-input" id="fq" placeholder="搜题目 / 作者…" value="' + esc(q.q || "") + '"></div>' +
        fgroup("朝代", "dynasty", dyn) +
        fgroup("类型", "type", typ) +
        fgroup("主题", "theme", thm) +
        "</div></div>" +
        '<p class="result-meta" id="rmeta"></p><div class="poem-list" id="rlist"></div>';

      show(html, "search");

      // 折叠（移动端默认收起）
      var fhead = document.getElementById("fhead"), fbody = document.getElementById("fbody");
      var isMobile = window.matchMedia("(max-width: 759px)").matches;
      var panel = fhead.parentElement;
      panel.classList.toggle("is-open", !isMobile);
      fhead.addEventListener("click", function () { panel.classList.toggle("is-open"); });

      var F = { q: (q.q || ""), dynasty: q.dynasty || "", type: q.type || "", theme: q.theme || "" };
      function updateSummary() {
        var on = [];
        if (F.dynasty) on.push(F.dynasty); if (F.type) on.push(F.type); if (F.theme) on.push(F.theme);
        document.getElementById("fsummary").textContent = on.length ? on.join(" · ") : "全部";
      }
      function match(p) {
        if (F.q) { var s = (p.title + " " + p.poet + " " + (p.tags || []).join(" ")).toLowerCase(); if (s.indexOf(F.q.toLowerCase()) < 0) return false; }
        if (F.dynasty && p.dynasty !== F.dynasty) return false;
        if (F.type && p.type !== F.type) return false;
        if (F.theme && p.theme !== F.theme) return false;
        return true;
      }
      function draw() {
        var list = poems.filter(match);
        document.getElementById("rmeta").textContent = "共 " + list.length + " 篇";
        document.getElementById("rlist").innerHTML = list.length ? list.map(function (p) {
          var sub = [p.dynasty, p.poet].filter(function (s) { return s && s.trim(); }).join(" · ");
          return '<a class="poem-row" href="#/p/' + enc(grade) + "/" + enc(p.title) + '">' +
            '<span class="poem-row__main"><span class="poem-row__title">' + esc(p.title) + '</span>' +
            (sub ? '<span class="poem-row__sub">' + esc(sub) + "</span>" : "") + "</span>" +
            '<span class="poem-row__right">' +
            (p.type ? '<span class="tag tag--type">' + esc(p.type) + "</span>" : "") +
            (p.theme ? '<span class="tag tag--theme">' + esc(p.theme) + "</span>" : "") + "</span></a>";
        }).join("") : '<div class="empty"><span class="empty__icon">⌕</span>没有匹配的篇目，换个条件试试。</div>';
        document.querySelectorAll(".chip").forEach(function (c) { c.classList.toggle("is-on", F[c.getAttribute("data-f")] === c.getAttribute("data-v")); });
        updateSummary();
      }
      view.querySelectorAll(".chip").forEach(function (c) {
        c.addEventListener("click", function () { var f = c.getAttribute("data-f"), v = c.getAttribute("data-v"); F[f] = (F[f] === v) ? "" : v; draw(); });
      });
      document.getElementById("fq").addEventListener("input", function () { F.q = this.value.trim(); draw(); });
      draw();
    }).catch(function () { errView("年级数据加载失败"); });
  }

  /* ===== 诗页 ===== */
  function renderPoem(grade, title) {
    loading();
    loadGrade(grade).then(function (shard) {
      var poems = shard.poems, i = -1;
      for (var k = 0; k < poems.length; k++) if (poems[k].title === title) { i = k; break; }
      if (i < 0) { errView("未找到《" + title + "》"); return; }
      var p = poems[i], prev = poems[i - 1], next = poems[i + 1];

      var bodyHtml = p.lines.length
        ? p.ruby.map(function (pairs) { return '<p class="poem-line">' + rubyLine(pairs) + "</p>"; }).join("")
        : '<div class="poem-placeholder">本篇内容整理中，敬请期待。</div>';

      var secs = "";
      ["译文", "注释", "赏析", "作者"].forEach(function (name, idx) {
        var t = p.sections && p.sections[name];
        if (!t) return;
        secs += '<section class="sec-block' + (idx === 0 ? " is-open" : "") + '">' +
          '<div class="sec-block__head"><span class="sec-block__bar"></span><h3>' + name + '</h3><span class="sec-block__chev">▶</span></div>' +
          '<div class="sec-block__body">' + md(t) + "</div></section>";
      });

      var pager =
        '<div class="pager">' +
        (prev ? '<a class="pager__btn" href="#/p/' + enc(grade) + "/" + enc(prev.title) + '"><span class="pager__label">‹ 上一首</span><span class="pager__name">' + esc(prev.title) + "</span></a>" : "<span></span>") +
        '<a class="pager__home" href="#/g/' + enc(grade) + '">' + esc(shard.label) + "目录</a>" +
        (next ? '<a class="pager__btn pager__next" href="#/p/' + enc(grade) + "/" + enc(next.title) + '"><span class="pager__label">下一首 ›</span><span class="pager__name">' + esc(next.title) + "</span></a>" : "<span></span>") +
        "</div>";

      var tools = p.lines.length ?
        '<div class="poem-tools">' +
        toolBtn("py-toggle", "拼音", state.pinyin) +
        toolBtn("vert-toggle", "竖排", state.vertical) +
        '<div class="font-ctl" title="调整正文字号"><span class="font-ctl__label">字号</span><button id="font-dec" aria-label="减小字号">−</button><span id="font-val">' + state.fontSize + '</span><button id="font-inc" aria-label="增大字号">+</button></div>' +
        "</div>" : "";
      function toolBtn(id, label, on) { return '<button class="toggle' + (on ? " is-on" : "") + '" id="' + id + '"><span class="dot"></span>' + label + "</button>"; }

      show(
        '<article class="poem-hero">' +
        '<div class="crumbs"><a href="#/">首页</a><i>›</i><a href="#/g/' + enc(grade) + '">' + esc(shard.label) + "</a><i>›</i><span>" + esc(p.title) + "</span></div>" +
        '<h1 class="poem-title">' + esc(p.title) + "</h1>" +
        '<p class="poem-poet"><b>' + esc(p.dynasty) + "</b> · " + esc(p.poet) + "</p>" +
        '<div class="poem-tags">' +
        (p.dynasty ? '<span class="tag tag--dynasty">' + esc(p.dynasty) + "</span>" : "") +
        (p.type ? '<span class="tag tag--type">' + esc(p.type) + "</span>" : "") +
        (p.theme ? '<span class="tag tag--theme">' + esc(p.theme) + "</span>" : "") +
        (p.tags || []).filter(function (t) { return t && t.trim(); }).map(function (t) { return '<span class="tag">' + esc(t) + "</span>"; }).join("") +
        "</div>" + tools +
        '<div class="poem-body' + (state.pinyin ? " show-pinyin" : "") + (state.vertical ? " vertical" : "") + '" id="poem-body" style="font-size:' + state.fontSize + 'px">' + bodyHtml + "</div>" +
        "</article>" + secs + pager,
        ""
      );
      document.title = p.title + " - " + p.poet + " - 古诗诵读";

      var body = document.getElementById("poem-body");
      function bindToggle(id, key, cls) {
        var el = document.getElementById(id); if (!el) return;
        el.addEventListener("click", function () {
          state[key] = !state[key]; store.set(key, state[key] ? "1" : "0");
          this.classList.toggle("is-on", state[key]); body.classList.toggle(cls, state[key]);
        });
      }
      bindToggle("py-toggle", "pinyin", "show-pinyin");
      bindToggle("vert-toggle", "vertical", "vertical");

      function setFont(n) {
        state.fontSize = Math.min(34, Math.max(15, n)); store.set("fontSize", String(state.fontSize));
        body.style.fontSize = state.fontSize + "px";
        var v = document.getElementById("font-val"); if (v) v.textContent = state.fontSize;
      }
      var fi = document.getElementById("font-inc"), fd = document.getElementById("font-dec");
      if (fi) fi.addEventListener("click", function () { setFont(state.fontSize + 1); });
      if (fd) fd.addEventListener("click", function () { setFont(state.fontSize - 1); });

      view.querySelectorAll(".sec-block__head").forEach(function (h) {
        h.addEventListener("click", function () { h.parentElement.classList.toggle("is-open"); });
      });
    }).catch(function () { errView("诗文加载失败"); });
  }

  /* ===== 查找页 ===== */
  function renderSearch(q) {
    loading();
    buildSearchIndex().then(function (list) {
      var dyn = {}, typ = {}, thm = {}, grd = {};
      list.forEach(function (p) { dyn[p.d] = 1; typ[p.ty] = 1; thm[p.th] = 1; });
      GRADE_ORDER.forEach(function (g) { grd[g[0]] = g[1]; });
      var gradeGroup = '<div class="fgroup"><span class="fgroup__label">年级</span><div class="fgroup__chips">' +
        '<button class="chip chip--all" data-f="g" data-v="">全部</button>' +
        GRADE_ORDER.map(function (g) { return '<button class="chip" data-f="g" data-v="' + esc(g[0]) + '">' + esc(g[1]) + "</button>"; }).join("") +
        "</div></div>";
      show(
        '<section class="sec" style="margin-top:0"><div class="sec__head"><div><p class="sec__eyebrow">QUICK FIND</p><h2>查找一首</h2></div><p>全库 ' + list.length + " 篇</p></div>" +
        '<div class="filter-panel">' +
        '<button class="filter-head" id="fhead"><span class="filter-head__title">筛选</span>' +
        '<span class="filter-head__summary" id="fsummary">全部</span>' +
        '<span class="filter-head__chev">▾</span></button>' +
        '<div class="filter-body" id="fbody"><div class="filter-row"><input class="filter-input" id="sq" placeholder="诗名 / 诗人 / 关键字…" value="' + esc(q.q || "") + '"></div>' +
        gradeGroup +
        fgroup("朝代", "d", dyn) +
        fgroup("类型", "ty", typ) +
        fgroup("主题", "th", thm) +
        "</div></div>" +
        '<p class="result-meta" id="smeta"></p><div class="poem-list" id="slist"></div></section>',
        "search"
      );
      var fhead = document.getElementById("fhead");
      var panel = fhead.parentElement;
      panel.classList.toggle("is-open", !window.matchMedia("(max-width: 759px)").matches);
      fhead.addEventListener("click", function () { panel.classList.toggle("is-open"); });

      var F = { q: q.q || "", g: q.g || "", d: q.d || "", ty: q.ty || "", th: q.th || "" };
      function updateSummary() {
        var on = [];
        if (F.g) on.push(GRADE_META[F.g].label); if (F.d) on.push(F.d); if (F.ty) on.push(F.ty); if (F.th) on.push(F.th);
        document.getElementById("fsummary").textContent = on.length ? on.join(" · ") : "全部";
      }
      function draw() {
        var res = list.filter(function (p) {
          if (F.q) { var s = (p.t + " " + p.p + " " + p.d + " " + p.ty + " " + p.th + " " + p.gl).toLowerCase(); if (s.indexOf(F.q.toLowerCase()) < 0) return false; }
          if (F.g && p.g !== F.g) return false;
          if (F.d && p.d !== F.d) return false;
          if (F.ty && p.ty !== F.ty) return false;
          if (F.th && p.th !== F.th) return false;
          return true;
        });
        document.getElementById("smeta").textContent = "共 " + res.length + " 篇";
        document.getElementById("slist").innerHTML = res.length ? res.slice(0, 400).map(function (p) {
          var ssub = [p.d, p.p, p.gl].filter(function (s) { return s && s.trim(); }).join(" · ");
          return '<a class="poem-row" href="#/p/' + enc(p.g) + "/" + enc(p.t) + '">' +
            '<span class="poem-row__main"><span class="poem-row__title">' + esc(p.t) + '</span>' +
            (ssub ? '<span class="poem-row__sub">' + esc(ssub) + "</span>" : "") + "</span>" +
            '<span class="poem-row__right">' +
            (p.ty ? '<span class="tag tag--type">' + esc(p.ty) + "</span>" : "") +
            (p.th ? '<span class="tag tag--theme">' + esc(p.th) + "</span>" : "") + "</span></a>";
        }).join("") : '<div class="empty"><span class="empty__icon">⌕</span>没有找到，换个关键字试试。</div>';
        document.querySelectorAll(".chip").forEach(function (c) { c.classList.toggle("is-on", F[c.getAttribute("data-f")] === c.getAttribute("data-v")); });
        updateSummary();
      }
      view.querySelectorAll(".chip").forEach(function (c) { c.addEventListener("click", function () { var f = c.getAttribute("data-f"); F[f] = (F[f] === c.getAttribute("data-v")) ? "" : c.getAttribute("data-v"); draw(); }); });
      document.getElementById("sq").addEventListener("input", function () { F.q = this.value.trim(); draw(); });
      draw();
    });
  }

  /* ---------- 全局搜索弹层 ---------- */
  var sInput = document.getElementById("search-input");
  var sPop = document.getElementById("search-pop");
  var sTimer = null;
  sInput.addEventListener("input", function () {
    var q = this.value.trim();
    clearTimeout(sTimer);
    if (!q) { sPop.hidden = true; return; }
    sTimer = setTimeout(function () {
      buildSearchIndex().then(function (list) {
        var ql = q.toLowerCase();
        var hits = list.filter(function (p) { return (p.t + " " + p.p + " " + p.d + " " + p.ty + " " + p.th + " " + p.gl).toLowerCase().indexOf(ql) >= 0; });
        if (!hits.length) { sPop.innerHTML = '<div class="search-pop__empty">没有找到「' + esc(q) + "」相关篇目</div>"; sPop.hidden = false; return; }
        sPop.innerHTML = hits.slice(0, 8).map(function (p) {
          return '<div class="search-pop__item" data-g="' + esc(p.g) + '" data-t="' + esc(p.t) + '">' +
            '<span class="search-pop__title">' + esc(p.t) + '</span>' +
            '<span class="search-pop__meta">' + esc(p.d) + " · " + esc(p.p) + " · " + esc(p.gl) + "</span></div>";
        }).join("") + '<div class="search-pop__count">共 ' + hits.length + " 条，回车查看全部</div>";
        sPop.hidden = false;
        sPop.querySelectorAll(".search-pop__item").forEach(function (el) {
          el.addEventListener("click", function () {
            location.hash = "#/p/" + enc(el.getAttribute("data-g")) + "/" + enc(el.getAttribute("data-t"));
            sPop.hidden = true; sInput.blur();
          });
        });
      });
    }, 160);
  });
  sInput.addEventListener("keydown", function (e) {
    if (e.key === "Enter") { var q = this.value.trim(); if (q) { location.hash = "#/search?q=" + enc(q); sPop.hidden = true; this.blur(); } }
    if (e.key === "Escape") { sPop.hidden = true; this.blur(); }
  });
  document.addEventListener("click", function (e) { if (!sPop.contains(e.target) && e.target !== sInput) sPop.hidden = true; });

  /* ---------- 随机 & 回顶 ---------- */
  document.getElementById("random-btn").addEventListener("click", function () {
    buildSearchIndex().then(function (list) {
      var withBody = list.filter(function (p) { return p.has; });
      var pool = withBody.length ? withBody : list;
      var p = pool[Math.floor(Math.random() * pool.length)];
      location.hash = "#/p/" + enc(p.g) + "/" + enc(p.t);
    });
  });
  document.getElementById("top-btn").addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });

  /* ---------- 路由 ---------- */
  function parseQuery(s) {
    var o = {}; (s || "").split("&").forEach(function (kv) { if (!kv) return; var p = kv.split("="); o[dec(p[0])] = dec(p[1] || ""); });
    return o;
  }
  function route() {
    var h = location.hash.replace(/^#\/?/, "");
    var qIdx = h.indexOf("?"), qs = qIdx >= 0 ? parseQuery(h.slice(qIdx + 1)) : {};
    if (qIdx >= 0) h = h.slice(0, qIdx);
    var parts = h.split("/").filter(Boolean).map(dec);
    document.title = "古诗诵读 · 实用知识库";
    if (!parts.length) return renderHome();
    if (parts[0] === "g" && parts[1]) return renderGrade(parts[1], qs);
    if (parts[0] === "p" && parts[1] && parts[2]) return renderPoem(parts[1], parts[2]);
    if (parts[0] === "search") return renderSearch(qs);
    renderHome();
  }
  window.addEventListener("hashchange", route);
  route();
})();
