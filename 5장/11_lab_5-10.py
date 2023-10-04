'''
    작성일 : 2023년 10월 4일
    작성자 : 학과 학번 이름
    설명 :  사용자가 입력하는 숫자의 합
            교재 133 페이지
        
    문제 분석 : y가 입력 되면 계속 반복한다.
               y 가 아니면 종료한다.
               입력 받은 수의 합계를 계속 계산한다.
    
    필요한 변수 : sum = 0, answer = 'y',  num (입력 받아 저장)
'''
sum = 0 
answer = 'y' 

# 대답이 y 이면 무한 반복
while answer == 'y':   # y가 아니면 종료
    num = int(input('숫자를 입력하시오: ')) 
    sum += num   # 합계 계산
    answer = input('계속하시겠습니까?(y/n): ') 
    # if answer == 'n' :
    #     break

print('합계는 : ', sum)