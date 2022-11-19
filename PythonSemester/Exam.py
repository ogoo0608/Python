'''
파이썬 기본 문법 활용 퀴즈
- 아이디와 비밀번호를 입력받아 맞으면 로그인 성공 그렇지 않으면 성공할 때까지 반복 !
- while문을 사용 !
'''

# My Solution (Exam - 1)

# DB로부터 가지고 온 값으로 가정

# _uname = 'hong'
# _passwd = '1234'

cnt = 0

while True :
    
    _uname = input("아이디를 입력하세요 : ")
    _passwd = input("비밀번호를 입력하세요 : ")
    
    if _uname == 'hong' and _passwd =='1234' :
        print("로그인 성공 ! 환영합니다.")
        exit()

    else :
        cnt = cnt + 1
        print("로그인 {}회 실패 !!" .format(cnt))
        
    if cnt >= 3 :
        print("프로그램을 종료합니다.")
        exit()
        
    
# Solution (Exam - 1)

_uname = 'hong'
_passwd = '1234'

login = False
cnt = 0
while (login == False) :
    uname = input ('# 아이디를 입력하세요 : ')
    passwd = input ('# 비밀번호를 입력하세요 : ')
    if ((uname == _uname) and (passwd == _passwd)) :
        login = True
        
    else :
        cnt += 1
        if (cnt >= 3) :
            print ('3회 이상 틀렸습니다. 종료합니다')
            exit()
        
        else :
            print('>>> 아이디 혹은 비밀번호가 틀렸습니다')

print('>> 로그인 성공')




'''
# 계산기 만들기
- 두 개의 숫자와 연산자를 입력받아 계산 결과를 출력
- 입력은 여러방식을 사용할 수 있음
- 지원되는 연산은 +, -, *, /
- 쉬는시간 포함해서 11:00 까지 문제를 풀어 봅시다.
- 희망자 발표
'''

# My Solution (Exam - 2)

while True :
    a = float(input('첫 번째 숫자 : '))
    b = float(input('두 번째 숫자 : '))
 
    if a == b == 0 :
        print('종료합니다.')
    c = input('연산자 : ')
    
    if c == '*' :
        d = a * b
        print('계산값은', d, '입니다.')
        continue
    
    if c == '+' :
        d = a + b
        print('계산값은', d, '입니다.')
        continue
    
    if c == '-' :
        d = a - b
        print('계산값은', d, '입니다.')
        continue
    
    if c == '/' :
        d = a / b
        print('계산값은', d, '입니다.')
        continue
 
    if c != '+' or c != '-' or c != '*' or c != '/' : 
        
        while True :
            
            print('지원하지 않는 연산자입니다.')
            c = input('연산자 : ')
 
            if c == '*' :
                d = a * b
                print('계산값은', d, '입니다.')
                exit()
            
            if c == '+' :
                d = a + b
                print('계산값은', d, '입니다.')
                exit()
            
            if c == '-' :
                d = a - b
                print('계산값은', d, '입니다.')
                exit()
            
            if c == '/' :
                d = a / b
                print('계산값은', d, '입니다.')
                exit()


# Solution (Exam - 2)

num1 = int(input("첫 번째 숫자 입력 : "))
num2 = eval(input("두 번째 숫자 입력 : "))

op = input("연산자 입력 : ")

result = 0

if op == '+' :
    result = num1 + num2
elif op == '-' :
    result = num1 - num2
elif op == '*' :
    result = num1 * num2
elif op == '/' :
    result = num1 / num2 
    
print("계산 결과 : %d %s %d = %d" % (num1, op, num2, result))

'''
-> 숫자 두 개를 한꺼번에 입력 받으려면 ????
num1, num2 = map(int, input("원하는 숫자 두 개를 입력하세요 (ex:10 20)).split()) # map 함수 ==> 집합형 데이터 안에 있는 모든 원소의 공통된 기능을 수행하도록 만들어줌
op = input("연산자 입력 : ")
result = 0
if op == '+' :
    result = num1 + num2
elif op == '-' :
    result = num1 - num2
elif op == '*' :
    result = num1 * num2
elif op == '/' :
    result = num1 / num2 
    
print("계산 결과 : %d %s %d = %d" % (num1, op, num2, result))
'''
