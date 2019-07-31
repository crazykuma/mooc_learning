"""
文件字符分布
描述
统计附件文件的小写字母a-z的字符分布，即出现a-z字符的数量，并输出结果。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

同时请输出文件一共包含的字符数量。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

注意输出格式，各元素之间用英文逗号（,）分隔。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

答案可能包含a-z共26个字符的分布，如果某个字符没有出现，则不显示，输出顺序a-z顺序。
"""
chars = 'abcdefghijklmnopqrstuvwxyz'
with open("latex.log", 'r') as f:
    s = f.readlines()

d = {}
count = 0
for line in s:
    # line = line.strip("\n")
    for c in line:
        count += 1
        if c in chars:
            d[c] = d.get(c, 0)+1
n = sorted(d.items(), key=lambda x: x[0])
f = ""
for k, v in n:
    f += ",{}:{}".format(k, v)
print("共{}字符{}".format(count, f))