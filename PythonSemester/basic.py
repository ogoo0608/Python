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
