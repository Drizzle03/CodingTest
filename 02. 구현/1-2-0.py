#개인 풀이 : 시각
#정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중
#3이 하나라도 포함되는 모든 경우의 수를 구함

#시각 입력 받음
n = int(input())
cnt = 0

#시간
for h in range(0, n+1):
    for m in range(0, 60):
        for s in range(0, 60):
            time_str = str(h)+str(m)+str(s)
            for i in time_str:
                if(i == '3'):
                    cnt+=1
                    break

print(cnt)