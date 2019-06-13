# in python we have except . not catch
# try:
#     {}
# except:

var_1 = input("enter the value of first number: ")
var_2 = input("enter the value of second number: ")

try:
    var_1 = int(var_1)
    var_2 = int(var_2)

    if(var_2 != 0):
        result = var_1 / var_2
        print("division Result is : ",result)
    else:
        print("value of second variable cannot be zero.")

except ValueError:
    print("can only enter integers")