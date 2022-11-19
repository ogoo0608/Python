# Lab02-01.py

num1 = 100
num2 = 200

result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = num1 / num2

print (num1, "+" , num2 , "=" , result1)
print (num1, "-" , num2 , "=" , result2)
print (num1, "*" , num2 , "=" , result3)
print (num1, "/" , num2 , "=" , result4)


# Lab02-02.py

print(" ## 택배를 보내기위한 정보를 입력하세요 ##")
personName = input("받는 사람 : ")
personAddress = input("주소 : ")
weight = int(input("무게(g) : "))

print(" ** 받는 사람 ==> ", personName)
print(" ** 주소 ==> ", personAddress)
print(" ** 배송비 ==>", weight*5, "원")


# Lab03-02.py

sales = 0

sales -= 900 * 10
sales -= 3500 * 5

sales += 1800 * 2
sales += 4000 * 4
sales += 1500 * 1
sales += 2000 * 4
sales += 1800 * 5

print("오늘 총 매출액은",sales, "원 입니다")


# Lab03-03.py

python = 3
mobile = 2
excel = 1

A = 4.5
A0 = 4.0
B = 3.5

average = ((python * B) + (mobile * A0) + (excel * A)) / (python + mobile + excel)

print("평균 학점 :",average)


# Lab04-01.py

ww='트와이스'

print('원본 문자열 ==>', ww)

print("반대 문자열 ==> ", end='')

print(ww[3], end='')
print(ww[2], end='')
print(ww[1], end='')
print(ww[0], end='')


# Lab04-02.py

ww = 'Python'

print('원본 문자열 ==>', ww)

ss = ""

ss += ww[0].lower()
ss += ww[1].upper()
ss += ww[2].upper()
ss += ww[3].upper()
ss += ww[4].upper()
ss += ww[5].upper()


print('반대 문자열 ==>', ss)


# Lab05-01.py

age = int(input("나이를 입력 ==>"))

if age >= 18 :
    print("즐거운 시간 되세요 ^^!")

else :
    print("집에 갈 시간이네요 ^^?")

print("협조 감사합니다")
Footer


# Lab05-02.py

import random

myhand = input("나의 가위/바위/보 ==>")

pchand = random.choice(["가위", "바위", "보"])
print("컴퓨터의 가위/바위/보", pchand)

if myhand == "가위" :
    if pchand == "가위" :
        print("비겼습니다.")
    elif pchand == "바위":
        print("졌습니다. ㅠㅠ")
    elif pchand == "보":
        print("이겼습니다. ^^")
elif myhand == "바위" :
    if pchand == "보":
        print("졌습니다. ㅠㅠ")
    elif pchand == "가위":
        print("이겼습니다. ^^")
    elif pchand == "바위":
        print("비겼습니다.")
elif myhand == "보" :
    if pchand == "가위":
        print("졌습니다. ㅠㅠ")
    elif pchand == "바위":
        print("이겼습니다. ^^")
    elif pchand == "보":
        print("비겼습니다.")

else :
    print("가위/바위/보 중 하나를 내세요 .. ^^")
    
 

# Lab06-01.py

i = 0
fact = 1
students_num = 5

for i in range(1, students_num + 1, 1):
    fact = fact * i

print("A, B, C, D, E 학생들을 순서대로 세우는 경우의 수 : " , fact)


# Lab06-02.py


i = 0
k = 0

for i in range(2, 10, 1):
    for k in range(1, 10, 1):
        print(i, "X", k, "=", i*k)
        
        
        
        
# Lab06-03.py

import random

count = 0
diceA, diceB, diceC = 0, 0, 0

while True:
    count += 1
    diceA = random.randint(1,6)
    diceB = random.randint(1,6)
    diceC = random.randint(1,6)

    if (diceA == diceB) and (diceB == diceC):
        break

print("3개 주사위는 모두", diceA, "입니다.")
print("같은 숫자가 나오기까지", count, "번 던졌습니다.")


# Lab06-04.py

import random

computer, user = 0, 0

for i in range (1, 11, 1) :
    computer = random.randint(1,5)
    print("게임", i, "회 : ", end='')
    user = int(input("컴퓨터가 생각한 숫자는? (숫자는 1부터 5까지입니다.) : "))

    if computer == user :
        print("맞혔네요. 축하합니다 .. ^^!!")
        break

    else :
        print("아까워요", computer, "였는데요. 다시 해보세요. ㅠ")
        continue

print("게임을 마칩니다.")


# Lab07-01.py

import random

wiseSay = [
"삶이 있는 한 희망은 있다",
"언제나 현재에 집중할 수 있다면 행복할 것이다",
"신은 용기있는 자를 결코 버리지 않는다",
"피할 수 없으면 즐겨라",
"행복한 삶을 살기 위해 필요한 것은 거의 없다",
"내일은 내일의 태양이 뜬다",
"행복은 습관이다. 그것을 몸에 지녀라",
"1퍼센트의 가능성, 그것이 나의 길이다",
"작은 기회로부터 종종 위대한 업적이 시작된다" ]

today = random.randint(0, len(wiseSay)-1)

print("오늘의 명언 ==>", wiseSay[today])

