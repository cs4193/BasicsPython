l1 = int(input("enter the side of triangle"))
l2 = int(input("enter the side of triangle"))
l3 = int(input("enter the side of triangle"))

if l1 == l2 == l3 :
    print("triangle is equilateral triangle ")
elif l1 == l2 or l2 == l3 or l3 == l1:
    print("triangle is isosceles triangle")
else :
    print("triangle is scaler triangle")