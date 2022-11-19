# 1. 변수 선언과 출력


num1 = 10
num2 = 20

print (num1, num2)
print('num1 =', num1, 'num2 =', num2)
print('num1=', num1,' , ' 'num2=', num2, sep='')
print('num1=%d, num2=%d' % (num1,num2))
print(f'num1={num1}, num2={num2}') # 이게 더 좋은 방식 ..

# 2. 입력과 형 변환

num3 = int(input('num3=>'))
num4 = eval(input('num4=>'))

print('num3 + num4 =', num3+num4)

# 3. 연산자와 자료형

a = 100, 200, 300, 400
print(a)
print(a[3])


print(type(123)) # int
print(type('hello')) # str
print(type(12.2)) # float
print(type([1,2,3,4])) # List (배열) => 변경 가능
print(type((1,2,3,4))) # Tuple => 변경 불가능
print(type({10,20,30})) # Set
print(type({'a':10, 'b':20, 'c':30})) # Map (dict)
print(type(10>50)) # boolean 

# 외부 라이브러리 참조

import calendar
calendar.prmonth(2022,1) # prmonth : print month 라는 뜻 ,,

# 4. if

_uname = 'hong'
_passwd = '1234'

uname = input('# 아이디를 입력하세요: ')
passwd = input('# 비밀번호를 입력하세요: ')

if((uname == _uname) and (passwd == _passwd)) :
    print('>> 로그인 성공!!')
else :
    print('>> 로그인 실패!!')
    
# 5. for 

for i in range(3):
    print('Hello World')
    
for i in range(1,4,1):
    print(i, ': Hello World')
    
for i in range(0,5,1):
    print(i)

for i in [10,20,30]:
    print(i)
    
for i in range(1,11,1):
    print(i, end=' ')
    
    
    
    
    
    
'''
함수 예제 모음 
'''

def calc1(num1,num2,op) :
    
    result = 0

    if op == '+' :
        result = num1 + num2
    elif op == '-' :
        result = num1 - num2
    elif op == '*' :
        result = num1 * num2
    elif op == '/' :
        result = num1 / num2 
    return result

num1, num2 = map(int, input("원하는 숫자 두 개를 입력하세요").split())

op = input("연산자 입력 (+, -, *, /) : ")

print("계산 결과 : ", calc1(num1,num2,op))







# 파일 관련 예제
fin = open('test.txt','r',encoding='utf-8') # 상대 경로
while True:
    msg = fin.readline()
    if msg == '':break
    else: print(msg.strip()) # strip() == \n 라인 제거 가능.
    
print('========================')

fin = open('test.txt','r',encoding='utf-8') # 상대 경로
while (msg := fin.readline()) != '': # := 파이썬 3.8 부터 사용 가능 (왈러스 연산자)
    print(msg.strip())
fin.close()

print('========================')

fin = open('test.txt','r',encoding='utf-8') 
for msg in fin.readlines():
    print(msg.strip())
fin.close()

print('========================')







'''
함수 관련 예제
'''

# 함수 선언만 해두고 내용은 나중에 구현
def printAll():
    pass

# 인자가 두 개인 함수
def calc(num1, num2):
    return num1+num2

print('계산결과 : ', calc(200,300))
print('계산결과 : ', calc(num1=200, num2=300))

# 가변 인자
def total(*num):
    tot = 0
    for n in num:
        tot += n
    return tot

print(total(1,2,3))
print(total(20,20,30))

# 리턴이 여러 개인 경우
def addNum(*nums):
    tot = 0
    cnt = 0
    for n in nums:
        tot += n
        cnt += 1
    return cnt, tot

cnt, total = addNum(10,20,30)
print(cnt,tot)

# 전역 변수, 지역 변수, global 예제
num4 = 10
def VarTest():
    global num5
    num5 = 20
    global num4
    num4 = 100
    print('VarTest() : ', num4)
    
VarTest()
print(num4)
# print(num5)==> 함수 안에 있는 변수는 호출 할 수 없음 .. but global 을 사용하면 가능해짐 !! 
print(num5)




'''
turtle Ex
'''

import turtle as t

t.shape('arrow')
t.title('Hello Turtle')

t.forward(200)


# 프로그램이 계속 실행되어 있도록 함. 이벤트 대기 상태
scr = t.Screen()
scr.mainloop()


<br>

> end='[구분자]' 를 이용한 출력

<br>

end='[구분자]'는 print 함수로 문구를 출력하고, 마지막에 \n이 아닌 다른 값으로 설정 가능

<br>

```py
print('Hello', end='')
print('World')
# Hello World
```

<br>

> sep='[구분자]' 를 이용한 출력

<br>

sep='[구분자]'를 사용하면 print 함수 내에 여러 문구열을 표시할 때, 그 사이에 출력할 구분자를 표시할 수 있다.

<br>

```py
print('010', '1234', '5678', sep='-')
# 010-1234-5678
```

<br>


<br>

## [파이썬 기초] 1. 강좌 개요 및 들여쓰기, 출력, 데이터 타입, 변수, 주석

<br>

```py
# 식별자

Korean_Score = 80
Math_Score = 70

print(Korean_Score + Math_Score)
```

<br>

### Indentation

<br>

- 파이썬은 들여쓰기가 매우 중요함.

```py
for a in range(10):
    print(a)
    print(---------)
```

<br>

### String 

<br>

```py
print("Hello")
print('Hello')

print(type(3.0 * 5.0))
>>> <Class 'float'>
```

<br>

### 간단한 실습

<br>

```
23를 7로 나눈 나머지를 출력하는 코드를 작성하세요.
(23을 7로 나눈 나머지를 상수값으로 입력하는 것이 아니라 연산자를 사용하시기 바랍니다.)
```
```py
x = 23/7 

print(x) 
```

<br>

```
아래와 같은 출력이 나올 수 있도록 출력 부분을 작성해 주세요. (3.3333부분은 x를 소수 4자리까지 출력하여야 하며 하나의 print() 함수로 구성해 주세요.)
```
```py
x=10/3
print(f'\\ta\n\\n{x:.4f}') # 출력부분
```

<br>

```
input을 이용하여 키와 몸무게를 입력 받고 총합을 구하여라.
```
```py
x=input('Enter a height: ')
y=input('Enter a weight: ')
print(float(x)+float(y))
```

<br>

### 미션

<br>

```
파이썬(Python)의 특징 중 옳지 않은 것을 고르시오.
```
```
Open source
Dynamically-typed
Object-oriented
Compiler =====> X
```

<br>

```py
print("1"+"1") # 여기에는 (문자열 1) + (문자열 1) 을 출력할 수 있도록 해주세요.
print(1+1) # 여기에는 숫자 1+ 숫자 1을 출력할 수 있도록 해주세요.
```

<br>

```
식별자(Identifier)의 특징 중 옳지 않은 것을 고르시오.
```
```
대소문자를 구분한다.
숫자로 시작하여 사용할 수 없다.
특수 문자를 사용할 수 없다. =====> X
키워드 (Keyword)를 사용할 수 없다.
```

<br>

```
다음 코드의 결과로 옳은 것을 고르시오.
x=int(1/4)
print(x)
```
```
0
```

<br>

```
다음 코드의 결과로 옳은 것을 고르시오.
x=5.7>3
print(x)
```
```
True
```

<br>

```
“Hello world”를 5번 출력하세요. (print 당 하나씩 총 5번의 print를 사용하여야 합니다.)
```
```
print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")
```

<br>

```
“Msg 1”을 5번, “Msg 2”를 2번 출력하세요.
```
```
print("Msg 1")
print("Msg 1")
print("Msg 1")
print("Msg 1")
print("Msg 1")
print("Msg 2")
print("Msg 2")
```

<br>

```
다음 코드의 결과로 옳은 것을 고르시오.
x=input(‘How old are you?’); type(x)

How old are you? 26
```
```
str
```

<br>

<br>

## [파이썬 기초] 2. 통제문 (if, while, for문), range 함수, f-string

<br>

```
input 의 리턴 ==> str 
```

<br>

```py
no1 = input() 
no2 = input()

print(no1 + no2)
print(type(no1))
```

&darr;

```py
no1 = input() 
no2 = input()

print(int(no1) + int(no2)) # no1 no2 자체가 int 타입으로 변경된 것은 아님

no1 = int(no1) # 이렇게 해야 변경되는 것임

print(type(no1))
```

<br>

### 제어문 &rarr; 프로그램 실행의 흐름 제어

<br>

**분기문 : 실행의 흐름을 조건에 따라 선택적인 코드의 실행**

&darr;

&rarr; `if, elif, else`

<br>

### 1. True, False : 이분법적 분기 (if, else)

```py
x = int(input())

if x%2 == 0 :
    print("짝수")

else :
    print("홀수")
```

<br>

- 문법 정리

<br>

```
if 조건식 : ==> 반드시 True or False로 판별되어야 함
    (조건이 참일 경우 실행할 코드)

else :
    (조건이 거짓일 경우 실행할 코드)
```

<br>

### 2. 다중 분기 : 2개 이상의 경우의 수로 분기되는 경우

<br>

```py
no = int(input())

# W : 슛 A : 달리기 S : 태클 D : 정지

if key == 'W':
    print("슛")

else :
    if key == "A":
        print("달리기")
    else :
        if key == "S": # W or A 가 아닌 나머지 모든 경우
            print("태클")
        else : 
            if key == "D":
                print("정지")

                else :
                    print("아무 동작 X)
```

&uarr; 아주 안 좋은 코드 !!

<br>

```py
# elif 활용 (else + if) 
if key == "W":
    print("슛")
elif key == "A":
    print("달리기")
elif key == "S":
    print("태클")
elif key == "D":
    print("정지")
else : 
    print("아무 동작 X")
```
&uarr; **가독성**이 좋은 코드 !! 

<br>

### 반복문 : 코드의 일정 영역을 반복적으로 실행하는 구문

<br>

```
문제) 화면에 서초 AI 칼리지를 10번 출력해라 !!
```
```py
print("서초 AI 칼리지")
print("서초 AI 칼리지")
print("서초 AI 칼리지")
print("서초 AI 칼리지")
print("서초 AI 칼리지")
print("서초 AI 칼리지")
print("서초 AI 칼리지")
print("서초 AI 칼리지")
print("서초 AI 칼리지")
print("서초 AI 칼리지")
```

&uarr; 에바

<br>

```py
for i in range(0,10):
    print("서초 AI 칼리지")
```

&uarr; 굳

<br>

#### 반복문의 세 가지 요소 &rarr; 초기값 + 조건 + 증감

<br>

```
Ex_ 나는 오늘부터 매일 소주를 1병씩 죽는 날까지 먹겠다. 
```
```
초기값 (~부터) : 시작값 : 2022.03.30
조건 (~까지) : 종료값 : ??? (죽는날)
증감 (간격) : 시작과 끝 사이에서 얼마만큼 반복할 것인지 (주기) : 매일
```

<br>

```
Ex_ 화면에 A ~ Z 를 출력하겠다.
```
```
초기값 : A
조건 : Z까지
증감 : 한 문자씩
```

<br>

```
Ex_ 2000년도 이후 우리 학교 학생들의 평균 취업율을 출력.
```
```
초기값 : 2000년
조건 : 2021년
증감 : 1년
```

<br>

### While : 프로그래밍 언어의 최초의 반복문

<br>

```py
while 조건식:
    실행코드

== 1부터 10까지 화면에 출력해라. ==

# 초기값 : 1, 조건 : <=10, 증감 : 1씩 증가

i = 1 #  초기값

while i <= 10 : # 조건
    print(i)
    i += 1 # 증감
```
```py
for i in range(1, 11, 1) : # 초기값, 조건, 증감
    print(i)
```

<br>

```
Ex_ 구구단 7단을 화면에 출력.
```
```py
for i in range(7, 64, 7):
    print(i)
```
```py
for i in range(1, 10,1):
    print(7 * i)
```

<br>

#### 다양한 경우

<br>

```py
for i in range(5) : # 조건만 들어감 (초기값 : 0, 증감 : 1)
    print(i)
```

<br>

```py
for i in range(1,5) : # 초기값 : 1, 조건 : <5 (증감은 마찬가지로 1)
    print(i)
```

<br>

```py
for i in range(1,5,2) :
    print(i)
```

<br>

#### 실수의 경우

<br>

```py
for i in range(1.5, 10, 1.5) :
    print(i)
```
```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_31500/4259729063.py in <module>
----> 1 for i in range(1.5, 10, 1.5) :
      2     print(i)

TypeError: 'float' object cannot be interpreted as an integer
```
```
range() 함수가 내분을 사용하는데, 이 과정에서 float 와 int 가 충돌을 한다.
```

<br>

### 실습

<br>

```
input을 이용하여 자연수를 입력 받고 
if, elif, else를 이용하여 주어진 자연수가 홀수인지 짝수인지 판단하여라
```
```py
a = int(input('Enter an integer : '))
b = a%2

if b == 0 :
    print("짝수")
else :
    print("홀수")
```

<br>

```
민수는 마트에서 사과 x개와 바나나 y개를 사려고 한다. 
사과와 바나나의 가격이 각각 1.35달러, 2.67달러 일 때 총 계산해야 할 금액을 
소수 둘째 자리에서 반올림하여 소수 첫자리까지 표현하는 코드를 작성하세요.
```
```py
apple = 1.35
banana = 2.67
x = int(input())
y = int(input())
print(f'{x*apple+y*banana:.1f}')
```

<br>

```
while을 이용하여
1^2 + 2^2 + 3+2 + ... + x^2 <1000를 만족하는 x를 구하여라.
```
```py
x = 0; y = 0

while y < 1000 :
    x += 1
    y += x ** 2
print(x-1)
```

<br>

```
아래와 같이 nn단을 출력하는 반복문 코드를 작성하세요.
nn단이란 구구단에서 1 x 1에서 n x n까지만 나타낸 것.
구구단의 두 피연산자가 1이상 n이하이다.
각 단이 끝난 후에는 한 줄 띄기
(해당 위치에 print()를 추가하면 된다.) 가 있어야 한다.
```
```py
아래는 n=5일 때, 오오단의 예시이다.

1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15

4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
```
```py
n = int(input())

for i in range(1, n+1) :
    for j in range(1, n+1) :
        print(f'{i} x {j} = {i*j}')
```

<br>

```
for을 이용하여 [76점, 59점, 95점, 87점, 61점] 
채점 결과의 총합과 평균을 구하여라.
```
```py
x = [76, 59, 95, 87, 61]

y = 0

for i in range(len(x)) :
    y += x[i]

print(y)
print(y/len(x))
```

<br>

```
시작 값과 끝 값을 입력받아

시작 값 이상 끝 값 미만에 있는 모든 짝수를 차례로 출력하는 코드를 작성하세요.

한 space 씩 뛰어서 출력하기 위해 print(start, end=’ ‘)를 활용하세요.
```
```py
start_value = int(input())
end_value = int(input())

#출력 부분
for i in range(start_value, end_value):
    if i%2==0:
        print(i, end=' ') # 한 space 씩 뛰어서 출력하는 출력문
```


<br>

```
반복문을 사용하여 내부는 ‘+’, 
가장자리는 ‘*’인 아래와 같은 다이아몬드를 만드세요. 
( 매 행 두 번째 * 이후로는 공백이 아니고 개행을 바로 해주시기 바랍니다. )
```
```py
n = 20
for i in range(n):
	# space
	for j in range(n-i):
		print(' ',end='')
	print('*',end='')
	for j in range(2*i):
		print('+',end='')
	print('*')
for k in range(n+1):
	# space
	for j in range(k):
		print(' ',end='')
	print('*',end='')
	for j in range(2*(n-k)):
		print('+',end='')
	print('*')

```

<br>




### 미션

<br>

```
지는 가위바위보란 아래와 같은 룰을 따르는 게임을 말합니다.

1. 게임 참가자는 진행자를 대상으로 가위바위보를 져야합니다.
2. 진행자가 먼저 가위바위보를 외치며 내면 그 다음 템포에서 바로 지는 것을 내야합니다.
3. 잘못내면 패배하게 됩니다.


진행자가 낸 것을 입력받아 지는 가위바위보로 옳은 결과를 출력하세요.


예를 들어, 진행자가 ‘가위’를 낼 경우, ‘보’를 출력해야 합니다.
```
```py
a = input()

if a == '바위' :
    print('가위')
    
elif a == '가위' :
    print('보')
    
elif a == '보' :
    print('바위')
    
else :
    print('패배')
```

<br>

```
점수 변환기

한 과목에서 학생들의 최종 점수가 나왔습니다. 

교수님은 이 점수를 가지고 학생들에게 학점 A, B, C, D, F 중 하나를 부여합니다.

A: 80점 이상
B: 60점 이상 80점 미만
C: 40점 이상 60점 미만
D: 20점 이상 40점 미만
F: 20점 미만

위와 같은 조건으로 입력된 점수를 등급으로 변환하세요.

예를 들어, 70을 입력하면 B가 출력되어야 합니다.

```
```py
score = int(input())

if score > 80 :
    print("A")
elif 60 < score < 80 :
    print("B")
elif 40 < score < 60 :
    print("C")
elif 20 < score < 40 :
    print("D")
elif score < 20 :
    print("F")
```

<br>

```
다음 코드의 밑줄의 내용으로 옳지 않을 것을 고르시오.

If _________:
```
```
x=y
```

<br>

```
시험 합격 문구 작성하기

어제 진행되었던 자격증 시험의 채점이 끝이 났습니다.

이 자격증 시험에서는 70점 이상의 경우 합격, 그 아래의 경우 불합격이 됩니다.

하지만 결과표에 점수만 나와있고 합격/불합격 여부가 나와있지 않습니다.

점수를 입력받으면 합격, 불합격 문구가 출력되는 프로그램을 작성해 봅시다.
```
```py
# 점수를 입력받는 코드입니다. 수정하실 필요는 없습니다.

score = int(input())

# 아래에 점수에 따라서 문구를 출력하는 코드를 작성해봅시다.

if score >= 70 :
    print("축하드립니다! 합격입니다.")
else :
    print("안타깝습니다. 불합격입니다.")
```

<br>

```
1부터 N까지 출력하기

어떠한 수가 입력되면 1부터 차례대로 N까지 출력되는 프로그램을 작성해 봅시다.
```
```py
# 정수 N을 입력받는 코드입니다. 수정하실 필요는 없습니다.

n = int(input())

# 아래에 1부터 n까지 출력하는 코드를 작성해봅시다.
# print(n,end=" ")


for n in range(1, n+1, 1) :
    print(n, end=" ")
```

<br>

```
과제제출 프로그램

교수님께서는 93개의 과제를 내주셨습니다.

과제는 이메일로 다음과 같은 파일 이름으로 하지 않으면 0점으로 하겠다고 엄포를 놓으셨습니다.

과제3.doc
과제4.doc
.
.
.
과제95.doc

그래서 파일이름을 출력하는 프로그램을 만들어 보았지만 잘 되지 않았습니다.

여러분이 코드를 수정하여 올바르게 출력되도록 해 봅시다!
```
```py
# 아래의 코드를 수정하여 올바른 파일명이 출력되도록 해봅시다.

for i in range(3, 96, 1) :
    print('과제', i, '.doc', sep = "")
```

<br>
