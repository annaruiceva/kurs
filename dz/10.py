from math import sqrt, pi, e, factorial

signs = {"-", "+", "*", "/", "^", "#", "!"}
error = "Введено некорректное выражение"
result = False
def operation(num1,num2, sign):
    try:
        match sign:
            case "+":
                return num1+num2
            case "-":
                return num1-num2
            case "*":
                return num1*num2
            case "/":
                return int(num1/num2) if (num1/num2)%1==0 else num1/num2
            case "^":
                return num1**num2
            case "#":
                if num1 == True:
                    if (sqrt(num2))%1==0:
                        return int(sqrt(num2))
                    else:
                        return (sqrt(num2))
            case "!":
                if num2 == True:
                    return factorial(num1)
        print(error)
    except ValueError:
         print(error)

def findSign(str):
    try:
        return list(set(s) & signs)[0]
    except IndexError:
        print("Неизвестный оператор")
        return

def getNum(n, result):

    num = pi if n == "pi" else e if n == "e" else result if n == "res" else True if n=="" else None
    if num == False:
        print("res еще не определен")
        return
    if num is None:
        try:
            num = int(n)
        except:
            try:
                num1 = float(n)
            except:
                print(error)
                return
    return num

while True:
    s = input("Введите выражение. чтобы остановиться введите STOP\n").replace(" ", "").replace("-/", "#")
    if s == "STOP":
        break
    sign = findSign(s)
    if not sign:
        continue
    number = s.split(sign)
    if len(number) != 2:
        print("чисел больше 2")
        continue

    num1 = getNum(number[0],result)
    num2 = getNum(number[1],result)

    if (not num1) or (not num2):
        continue
    pre_result = operation(num1,num2,sign)
    if not pre_result:
        continue
    result = pre_result
    print("Ответ: ",result)

