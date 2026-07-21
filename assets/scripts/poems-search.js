(function () {
  "use strict";

  var index = null;
  var indexUrl = null;

  function resolveIndexUrl() {
    // site root derived from canonical URL: find the first path segment that
    // starts with a digit (grade dir). Everything before it is the site root.
    // For the home page (no grade dir in URL), the canonical IS the site root.
    var can = document.querySelector('link[rel="canonical"]');
    if (can && can.href) {
      var u = can.href.split("?")[0].split("#")[0];
      var parts = u.split("/").filter(Boolean);
      var rootIdx = parts.length;
      for (var i = 3; i < parts.length; i++) {
        if (/^\d/.test(parts[i])) { rootIdx = i; break; }
      }
      // if no grade dir found, the site root is the canonical directory itself
      // (strip trailing segment only if it's a page slug, but for home canonical
      // equals site root, so keep all non-empty path segments under host)
      // For home page canonical = https://host/study/ -> parts ['https:', '', 'host', 'study']
      // site root should be https://host/study -> slice(0, 4)
      // For poem page canonical = https://host/study/03-.../静夜思/ -> rootIdx=4 -> slice(0,4)
      return parts.slice(0, rootIdx).join("/") + "/search/search_index.json";
    }
    // fallback: derive from pathname
    var path = location.pathname.replace(/\\/g, "/");
    var segs = path.split("/").filter(Boolean);
    var rootIdx = segs.length;
    for (var i = 0; i < segs.length; i++) {
      if (/^\d/.test(segs[i])) { rootIdx = i; break; }
    }
    var prefix = segs.slice(0, rootIdx).join("/");
    return (prefix ? "/" + prefix : "") + "/search/search_index.json";
  }

  function loadIndex(cb) {
    if (index) return cb(index);
    var url = resolveIndexUrl();
    indexUrl = url;
    var x = new XMLHttpRequest();
    x.open("GET", url, true);
    x.onload = function () {
      try { index = JSON.parse(x.responseText); } catch (e) { index = { docs: [] }; }
      cb(index);
    };
    x.onerror = function () { index = { docs: [] }; cb(index); };
    x.send();
  }

  function escapeHTML(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function siteRoot() {
    var can = document.querySelector('link[rel="canonical"]');
    if (can && can.href) {
      var u = can.href.split("?")[0].split("#")[0];
      var parts = u.split("/").filter(Boolean);
      var rootIdx = parts.length;
      for (var i = 3; i < parts.length; i++) {
        if (/^\d/.test(parts[i])) { rootIdx = i; break; }
      }
      return parts.slice(0, rootIdx).join("/");
    }
    // fallback: derive from pathname (find first digit-starting segment)
    var path = location.pathname.replace(/\\/g, "/");
    var segs = path.split("/").filter(Boolean);
    var rootIdx = segs.length;
    for (var i = 0; i < segs.length; i++) {
      if (/^\d/.test(segs[i])) { rootIdx = i; break; }
    }
    var prefix = segs.slice(0, rootIdx).join("/");
    return location.origin + (prefix ? "/" + prefix : "");
  }

  function highlight(text, terms) {
    var html = escapeHTML(text);
    terms.forEach(function (t) {
      if (!t) return;
      var re = new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "gi");
      html = html.replace(re, '<mark>$1</mark>');
    });
    return html;
  }

  function search(query) {
    if (!index) return [];
    var terms = (query || "").trim().split(/[\s\u3000、，。]+/).filter(Boolean);
    if (!terms.length) return [];
    var scored = [];
    index.docs.forEach(function (d) {
      var loc = d.location || "";
      // skip the site root index page (guide text would pollute results)
      if (loc === "" || loc === "./" || loc === "/" || !loc.match(/\//)) return;
      // skip grade index pages (location like "03-二年级/")
      if (/^\d/.test(loc) && loc.replace(/\/+$/,"").split("/").length === 1) return;
      var title = d.title || "";
      var text = (d.text || "").replace(/<[^>]+>/g, " ");
      var score = 0;
      terms.forEach(function (t) {
        var tl = t.toLowerCase();
        if (title.toLowerCase().indexOf(tl) >= 0) score += 100;
        if (text.toLowerCase().indexOf(tl) >= 0) score += 10;
      });
      if (score > 0) {
        var loc = d.location;
        if (loc.indexOf("/") !== 0) loc = "/" + loc;
        scored.push({ loc: loc, title: title, text: text.slice(0, 80), score: score, terms: terms });
      }
    });
    scored.sort(function (a, b) { return b.score - a.score; });
    return scored.slice(0, 30);
  }

  function buildUI() {
    if (document.querySelector(".poems-search-overlay")) return;
    var overlay = document.createElement("div");
    overlay.className = "poems-search-overlay";
    overlay.innerHTML =
      '<div class="poems-search-modal">' +
      '<div class="poems-search-bar">' +
      '<input type="search" placeholder="搜诗名、诗人、朝代、类型…" autocomplete="off" />' +
      '<button class="poems-search-close" aria-label="关闭">✕</button>' +
      '</div>' +
      '<ol class="poems-search-results"></ol>' +
      '</div>';
    document.body.appendChild(overlay);

    var input = overlay.querySelector("input");
    var results = overlay.querySelector(".poems-search-results");
    var closeBtn = overlay.querySelector(".poems-search-close");

    function close() { overlay.classList.remove("is-open"); input.value = ""; results.innerHTML = ""; }
    function open() { overlay.classList.add("is-open"); setTimeout(function () { input.focus(); }, 30); }

    overlay.addEventListener("click", function (e) { if (e.target === overlay) close(); });
    closeBtn.addEventListener("click", close);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") close();
    });

    var debounce = null;
    input.addEventListener("input", function () {
      clearTimeout(debounce);
      debounce = setTimeout(function () {
        var q = input.value;
        if (!q.trim()) { results.innerHTML = ""; return; }
        loadIndex(function () {
          var hits = search(q);
          if (!hits.length) {
            results.innerHTML = '<li class="poems-search-empty">没有匹配的结果</li>';
            return;
          }
          results.innerHTML = hits.map(function (h) {
            var href = h.loc;
            if (href.charAt(0) === "/") href = href.slice(1);
            var fullHref = siteRoot() + "/" + href;
            return '<li><a href="' + fullHref + '">' +
              '<strong>' + highlight(h.title, h.terms) + '</strong>' +
              '<span>' + highlight(h.text, h.terms) + '</span>' +
              '</a></li>';
          }).join("");
        });
      }, 120);
    });

    // expose open
    document.querySelectorAll(".poems-topbar__search").forEach(function (el) {
      el.style.cursor = "pointer";
      el.addEventListener("click", open);
    });

    // pinyin toggle for poem pages
    document.querySelectorAll(".poem-pinyin-toggle").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var body = btn.closest(".poem-body");
        if (!body) return;
        var on = body.classList.toggle("is-pinyin");
        btn.setAttribute("aria-pressed", on ? "true" : "false");
        btn.innerHTML = on
          ? '<span class="poem-pinyin-toggle__icon"> 拼</span>隐藏拼音'
          : '<span class="poem-pinyin-toggle__icon"> 拼</span>显示拼音';
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", buildUI);
  } else {
    buildUI();
  }
})();