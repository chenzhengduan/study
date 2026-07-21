import os

for g in ['01-\u5e7c\u513f\u56ed', '02-\u4e00\u5e74\u7ea7', '03-\u4e8c\u5e74\u7ea7', '04-\u4e09\u5e74\u7ea7', '05-\u56db\u5e74\u7ea7', '06-\u4e94\u5e74\u7ea7', '07-\u516d\u5e74\u7ea7']:
    path = 'docs/' + g
    files = sorted([f for f in os.listdir(path) if f.endswith('.md') and f != 'index.md'])
    print(f'{g}: {len(files)} poems')
    for f in files:
        print(f'  {f.replace(".md","")}')
    print()
