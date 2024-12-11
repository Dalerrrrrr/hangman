def digit_multiplication(expression):

    def Multy_nums(nums):
        result=1
        for i in nums:
            result*=int(i)
        return result

    if "+" in expression:
        count1=expression.split("+") #делаем из строки список
        num1=Multy_nums(count1[0])
        num2=Multy_nums(count1[-1])
        return num1+num2
    elif "-" in expression:
        count1=expression.split("-") #делаем из строки список
        num1=Multy_nums(count1[0])
        num2=Multy_nums(count1[-1])
        return num1-num2
    else:

        return Multy_nums(expression)


expression1 = "53+5"
expression2 = "266-66"
expression3 = "555"

print(digit_multiplication(expression1))  # 20
print(digit_multiplication(expression2))  # 36
print(digit_multiplication(expression3))  # 125