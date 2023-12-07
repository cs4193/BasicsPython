# F, M -> S

class Father:
    def father_money(self):
        return "5"
    def info(self):
        print("father method")

class Mother:
    def mother_money(self):
        return "10"
    def info(self):
        print("mother method")


class Son(Father, Mother):
    pass
class Daughter(Mother, Father):
    pass


son = Son()
print("father money inherited",son.father_money())
print("mother money inherited",son.mother_money())
son.info()      # if common method is present in both parents then method from first parent is picked i.e. Father
daughter = Daughter()
daughter.info()  # if common method is present in both parents then method from first parent is picked i.e. Mother
