# Exception is an abnormal event during the execution of a program
# Error is a mistake by Dev/ caused by failure of specific code

print("Start")
try:
    # code which will give some exception
    a = 10/0
except Exception as e:
    print("An exception was handled :",e)

print("End")