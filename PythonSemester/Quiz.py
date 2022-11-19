# My solution (Quiz - 1)

# def printReport(students, scores) :
#     total = 0
#     avg = 0
    
#     for i in range(0, len(students), 1) :
#         print(students[i], '\t', sep='', end='')
#         for k in range(0, len(scores), 1) :
#             print(scores[i][k], '\t', end='')
#             total += scores[i][k]
#         avg = total // len(scores)
#         print(total, '\t', avg, sep='',)
#         total, avg = 0, 0
        
# students = ['홍길동', '김사랑', '나대장']
# scores = [[90,85,91],[92,95,88],[87,94,96]]

# printReport(students, scores)

def printReport(stu_list, score_list) :
    for i, score in enumerate(score_list) :
        print(stu_list[i], score[0], score[1], score[2], sep='\t', end='\t')
        hap = sum(score)
        avg = hap / len(score)
        print('총점 : ', hap, '평균 :', int(avg), sep='\t')
        print('')
        
students = ['홍길동', '김사랑', '나대장']
scores = [[90,85,91],[92,95,88],[87,94,96]]


printReport(students, scores) 


# Solution (Quiz - 1)

students = ['홍길동', '김사랑', '나대장']
scores = [[90,85,91],[92,95,88],[87,94,96]]

# 방법 1 : 중첩 for문 사용

def printReport() :
    for i in range(0, len(students)):
        print(students[i],end='\t')
        for j in range(0,3) :
            print(scores[i][j], end='\t')
        total = sum(scores[i])
        print('%d\t%d' % (total, total/len(scores[i])))
        
printReport()

# 방법 2 : 인덱스를 이용한 단일 for문 사용

def printReport2():
    for i in range(len(students)):
        total = sum(scores[i])
        print('%s\t%d\t%d\t%d\t%d' % (students[i], scores[i][0], scores[i][1], scores[i][2], scores[i][3], total, int(total/3), sep='\t'))
        
printReport2()

# 방법 3 : enumerate 사용 ==> 중요

def printReport3() :
    for i, sc in enumerate(scores) :
        total = sum(sc)
        print(students[i], sc[0], sc[1], sc[2], total, int(total/len(sc)), sep='\t')
        
printReport3()

# 방법 4 : zip과 unpacking을 사용하는 방법 ==> unpacking : 원소를 분해해서 각각의 데이터로 만들어줌 ==> 중요

def printReport4() : 
    for st, sc in zip(students,scores) :
        total = sum(sc)
        print(st, *sc, total, int(total/len(sc)), sep='\t')
        
printReport4()



# My solution (Quiz - 2)

# 202135317 김정준

students = {2021001:'홍길동', 2020100:'김사랑', 2021002:'나대장'}

scores = {2021001:[90,85,91],2020100:[92,95,88],2021002:[87,94,96]}

sub = ["자바", "C언어", "파이썬"]

total = 0

def searchData() :
    
         key = input(" ## 조회할 학번을 입력하세요 : ")
        
         if (key in students.keys()) :
             
             print()
             
             total = 0
             
         else : 
             print(" 죄송합니다. 해당 학번이 존재하지 않습니다. ")
            
 searchData
            
 def printAll() :
     global total 
     print(" ## 학생 성적 리스트 ##")
     print("학번\t이름\t자바\tC언어\t파이썬\t총점\t평균")
     for key in students.keys() :
         total sum(socres[key])
         print(key,students[key], *scores[key], total, int(total/len(scores[key]), sep='\t'))


searchData()
printAll()


# Solution (Quiz - 2)

# 202135317 김정준

students = {2021001:'홍길동', 2020100:'김사랑', 2021002:'나대장'}

scores = {2021001:[90,85,91],2020100:[92,95,88],2021002:[87,94,96]}

major = ["JAVA", "C", "Python"]

total = 0

def searchData(sid):
    global total
    if (sid in students.keys()):
        print(f"학번 : {sid}, \t이름:{students[sid]}")
        for i in range(len(scores[sid])):
            print(f"{major[i]}:{scores[sid][i]},", end='\t')
            total += scores[sid][i]
        print(f"\n총점 : {total},\t평균 : {int(total/len(scores[sid]))}")
        total = 0
    else : 
        print("죄송합니다. 해당 정보가 없습니다.")
        
def printAll():
    global total
    print('## 학생 성적 리스트 ##')
    print('학번\t이름\tJAVA\tC\tPython\t총점\t평균')
    total = 0
    for id, st, sc in zip(students.keys(), students.values(), scores.values()):
        total = sum(sc)
        print(id, st, *sc, total, int(total/len(sc)), sep='\t')
        
Num = int(input("## 조회할 학번을 입력하세요."))

searchData(Num)
printAll()


# My Solution (Quiz - 3)

'''
- 키보드로 저장할 파일명을 입력받아 파일을 오픈. w 모드로 오픈 !!
- while로 계속 내용을 읽어 읽은 내용을 파일에 저장
- q를 입력하면 작성한 내용을 저장하고 종료
- 11시까지 마감
'''

Fname = "" + input("파일명을 입력하세요 (확장자) : ")

outFp = None
outStr = ""

outFp = open(Fname, "w", encoding="UTF-8")

while True:
    outStr = input("내용을 입력하세요 (q - 저장 및 종료) : ")
    if outStr == "q":break
    
    else:
        outFp.writelines(outStr + "\n")
          
outFp.close()

print("저장했습니다.")


# Solution (Quiz - 3)

'''
- 키보드로 저장할 파일명을 입력받아 파일을 오픈. w 모드로 오픈 !!
- while로 계속 내용을 읽어 읽은 내용을 파일에 저장
- q를 입력하면 작성한 내용을 저장하고 종료
- 11시까지 마감
'''

print('## 노트패드 v1.0 ##')
fname = input('# 저장할 파일명을 입력하세요 : ')

with open(fname, 'w', encoding='UTF-8') as f:
    while ((msg := input()) != 'q'):
        f.writelines(msg + '\n')
f.close()
Footer


