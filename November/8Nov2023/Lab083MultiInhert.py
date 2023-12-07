# Multilevel Inheritance
#Level - GrandFather -> Father -> Son

class Grandparent:
    def grandparent_method(self):
        return "Grandparent's method"


class Parent(Grandparent):
    def parent_method(self):
        return "Parent's method"


class Child(Parent):
    def child_method(self):
        return "Child's method"

print("************Grandparent Class*********************")
grandpaa = Grandparent()
print(grandpaa.grandparent_method())

print("************Parent Class*********************")
father = Parent()
print(father.parent_method())
print(father.grandparent_method())     # Parent inherits the methods and attributes of grandparent

print("************Son Class*********************")
son = Child()
print(son.child_method())
print(son.parent_method())     # Son inherits the methods and attributes of Parent
print(son.grandparent_method())    # Son inherits the methods and attributes of grandparent