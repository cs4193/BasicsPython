lstStr = ["str","asda","aaaa","ssar","aawera","aa","aaawa"]
count = 0
for x in lstStr:
    if len(x) > 2 and x[0] == x[len(x)-1]:
        count += 1

print(count)
