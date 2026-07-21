import os

def get_poems(grade_dir):
    files = sorted([f for f in os.listdir(grade_dir) if f.endswith('.md') and f != 'index.md'])
    poems = []
    for f in files:
        with open(os.path.join(grade_dir, f), 'r', encoding='utf-8') as fh:
            content = fh.read()
        lines = content.split('\n')
        poet = dynasty = ptype = theme = ''
        for line in lines:
            if line.startswith('poet:'): poet = line.split(':',1)[1].strip()
            if line.startswith('dynasty:'): dynasty = line.split(':',1)[1].strip()
            if line.startswith('type:'): ptype = line.split(':',1)[1].strip()
            if line.startswith('theme:'): theme = line.split(':',1)[1].strip()
        title = f.replace('.md', '')
        poems.append((title, poet, dynasty, ptype, theme))
    return poems

def create_index(grade_dir, grade_label, kicker):
    poems = get_poems(grade_dir)
    lines = []
    lines.append('---')
    lines.append('standalone_title: "' + grade_label + '\u53e4\u8bd7 - \u53e4\u8bd7\u8bf5\u8bfb"')
    lines.append('hide:')
    lines.append('  - navigation')
    lines.append('  - toc')
    lines.append('---')
    lines.append('')
    lines.append('<div class="poems-hub poems-grade-hub">')
    lines.append('')
    lines.append('<nav class="poems-topbar">')
    lines.append('  <span class="poems-topbar__title"><a href="../">\u53e4\u8bd7\u8bf5\u8bfb</a></span>')
    lines.append('  <a href="../">\u5168\u90e8\u5e74\u7ea7</a>')
    lines.append('  <span class="poems-topbar__search">\U0001F50D \u641c\u7d22</span>')
    lines.append('</nav>')
    lines.append('')
    lines.append('<section class="poems-hero poems-hero--grade">')
    lines.append('  <p class="poems-kicker">' + kicker + '</p>')
    lines.append('  <h1>' + grade_label + '\u53e4\u8bd7</h1>')
    lines.append('  <p>\u90e8\u7f16\u7248\u6559\u6750' + grade_label + '\u5fc5\u80cc\u53e4\u8bd7\u6587\u6c47\u603b\u3002</p>')
    lines.append('</section>')
    lines.append('')
    lines.append('<section class="poems-section">')
    lines.append('  <div class="poems-section-heading">')
    lines.append('    <div><p class="poems-eyebrow">POEMS</p><h2>\u672c\u5e74\u7ea7\u7bc7\u76ee</h2></div>')
    lines.append('    <p>\u4ece\u9876\u90e8\u641c\u7d22\u6846\u53ef\u6309\u8bd7\u4eba\u3001\u671d\u4ee3\u3001\u7c7b\u578b\u5feb\u901f\u7b5b\u9009\u3002</p>')
    lines.append('  </div>')
    lines.append('  <div class="poems-list">')
    for title, poet, dynasty, ptype, theme in poems:
        link = title + '/'
        desc = dynasty + ' \u00b7 ' + poet + ' \u00b7 ' + ptype + ' \u00b7 ' + theme
        lines.append('    <a class="poems-list-item" href="' + link + '"><strong>' + title + '</strong><span>' + desc + '</span></a>')
    lines.append('  </div>')
    lines.append('</section>')
    lines.append('')
    lines.append('</div>')
    lines.append('')
    
    with open(os.path.join(grade_dir, 'index.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print('Created index.md for ' + grade_label + ' with ' + str(len(poems)) + ' poems')

create_index('docs/08-\u521d\u4e2d', '\u521d\u4e2d', 'JUNIOR HIGH')
create_index('docs/09-\u9ad8\u4e2d', '\u9ad8\u4e2d', 'SENIOR HIGH')
