# pass is used to skip teh code

for i in range(1,10):
    if i ==5:
        pass
    else:
        print(i)

'''o/p
1
2
3
4
6
7
8
9
'''

# continues with the next iteration of the loop
for i in range(1,10):
    if i % 2 == 0:
        print("found even number", i)
        continue
    print("found odd number",i)

'''o/p
found odd number 1
found even number 2
found odd number 3
found even number 4
found odd number 5
found even number 6
found odd number 7
found even number 8
found odd number 9

'''