x = 10
y = 20
z = 30
op = None
if x > y and x > z:
    op = x
elif y > z:
    op = y
else:
    op = z
print(f"{max} is the greatest number")
