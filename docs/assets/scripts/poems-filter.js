(function() {
  'use strict';

  var tbody = document.getElementById('poems-tbody');
  var wrapper = document.getElementById('poems-table-wrapper');
  var empty = document.getElementById('poems-empty');
  if (!tbody || !wrapper) return;

  var grade = wrapper.getAttribute('data-grade');
  var allPoems = typeof POEMS_DATA !== 'undefined' ? POEMS_DATA : [];

  function render(poems) {
    tbody.innerHTML = poems.map(function(p) {
      var path = p.path || (grade + '/' + p.title + '/');
      var sem = p.semester || '';
      var cls = 'poems-tr' + (sem ? ' poems-tr--' + sem : '');
      return '<tr class="' + cls + '" onclick="location.href=\'' + path + '\'">'
        + '<td class="poems-td-title"><a href="' + path + '">' + p.title + '</a></td>'
        + '<td>' + p.poet + '</td>'
        + '<td>' + p.dynasty + '</td>'
        + '<td>' + p.type + '</td>'
        + '<td>' + p.theme + '</td>'
        + (sem ? '<td><span class="poems-sem-badge poems-sem--' + sem + '">' + sem + '册</span></td>' : '')
        + '</tr>';
    }).join('');
    if (empty) {
      empty.style.display = poems.length === 0 ? '' : 'none';
    }
  }

  function filter() {
    var inputs = wrapper.querySelectorAll('.poem-filter');
    var filters = Array.prototype.map.call(inputs, function(inp) {
      return inp.value.trim().toLowerCase();
    });
    var matched = allPoems.filter(function(p) {
      var vals = [p.title, p.poet, p.dynasty, p.type, p.theme, p.semester || ''];
      return filters.every(function(fv, i) {
        if (!fv) return true;
        if (i === 5) return fv === '' || vals[i] === fv;
        return vals[i].toLowerCase().indexOf(fv) !== -1;
      });
    });
    render(matched);
  }

  wrapper.addEventListener('input', filter);
  wrapper.addEventListener('change', filter);
  render(allPoems);
})();
