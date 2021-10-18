def func1():
    digit = input("Введите число") 
    reverse = digit[::-1] 
    if (digit==reverse):
        print("true")
    else:
        print("false")
        
def func2():
    lists = list(map(int,input().strip().split()))
    two =[]
    three = []
    five =[]
    i=0
    while i<len(lists):
        if lists[i]%2==0:
            two.append(lists[i])
        if lists[i]%3==0:
            three.append(lists[i])
        if lists[i]%5==0:
            five.append(lists[i])
        i+=1   
    print(list)
    print(two)
    print (three)
    print (five)

def func3():
    digit = input("Введите число ")
    reverse = digit[::-1]
    if digit[0]=="-":
               reverse = "-"+reverse
               print(int(reverse[0:len(reverse)-1]))
    else :
        print (int(reverse))

def func4():
    digit = int(input())
    n=int(input())
    epos = 0.000001
    A = digit
    digit1=1/n*(((n-1)*digit)+A/(digit**(n-1)))
    while abs(digit1-digit)>epos:
        digit=digit1
        digit1=1/n*(((n-1)*digit)+A/(digit**(n-1)))
    print(digit1)

def func5():
    digit = int(input())
    i = 1
    while i!=digit:
        if (i==1)or(i==digit):
            i+=1
            continue
        
        if digit%i==0:
            break
        i+=1

    if i==digit:
        print("true")
    else :
        print("false")

a =int(input("Выберите функцию \n 1-Написать функцию, которая на вход принимает int и возвращает true или false в зависимости является ли это число палиндром. \n 2- Написать функцию, которая принимает на вход список из положительных целочисленных элементов и возвращает три списка: \n 3- Написать функцию, принимающую на вход int, и число, обратное этому int \n 4 - Написать функцию, которая будет расчитывать квадратный корень n-ой степени методом Ньютона \n 5- Написать функцию, принимающую 1 аргумент — число от 0 до 100000, и возвращающую true, если оно простое, false если нет. \n "))

if a==1:
    func1()
if a==2:
    func2()
if a==3:
    func3()
if a==4:
    func4()
if a==5:
    func5()




