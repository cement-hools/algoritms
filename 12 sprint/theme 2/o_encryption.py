# Простой подход состоит в том, чтобы пройти от начала строки,
# рассматривая подстроки длины, равной длине данного слова,
# а затем проверить, содержит ли эта подстрока все символы слова.

s = 'abcsdfacba'
template = 'abc'
template_set = set(template)
len_temp = len(template)
cnt = 0
print(template_set)
i = 0
while len_temp + i <= len(s):

    res_s = s[i:len_temp + i]
    res_set = set(res_s)
    if template_set == res_set:
        cnt += 1
    i += 1

print(cnt)
