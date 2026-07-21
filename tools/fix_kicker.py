import os

GRADE_INFO = {
    '01-\u5e7c\u513f\u56ed': '\u5e7c\u513f\u56ed',
    '02-\u4e00\u5e74\u7ea7': '\u4e00\u5e74\u7ea7',
    '03-\u4e8c\u5e74\u7ea7': '\u4e8c\u5e74\u7ea7',
    '04-\u4e09\u5e74\u7ea7': '\u4e09\u5e74\u7ea7',
    '05-\u56db\u5e74\u7ea7': '\u56db\u5e74\u7ea7',
    '06-\u4e94\u5e74\u7ea7': '\u4e94\u5e74\u7ea7',
    '07-\u516d\u5e74\u7ea7': '\u516d\u5e74\u7ea7',
}

KICKERS = {
    '01-\u5e7c\u513f\u56ed': 'GRADE K',
    '02-\u4e00\u5e74\u7ea7': 'GRADE 1', 
    '03-\u4e8c\u5e74\u7ea7': 'GRADE 2',
    '04-\u4e09\u5e74\u7ea7': 'GRADE 3',
    '05-\u56db\u5e74\u7ea7': 'GRADE 4',
    '06-\u4e94\u5e74\u7ea7': 'GRADE 5',
    '07-\u516d\u5e74\u7ea7': 'GRADE 6',
}

for dir_name, label in GRADE_INFO.items():
    path = 'docs/' + dir_name + '/index.md'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    kicker = KICKERS[dir_name]
    # Replace the kicker line
    import re
    content = re.sub(r'<p class="poems-kicker">[^<]+</p>', '<p class="poems-kicker">' + kicker + '</p>', content)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed kicker for ' + label)

print('Done')
