words = ['apple', 'banana', 'berry', 'cherry', 'dates', 'strawberry', 'fig']
min_len = 6


def check_len(w):
    return len(w)>min_len


op = list(filter(check_len, words))
print(op)
print("*************filters using lambda************************")

lam1 = lambda w:len(w)>min_len
op1 = list(filter(lam1,words))
print(op1)