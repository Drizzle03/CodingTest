# 게임 개발 : 개인 풀이
# 시뮬레이션 실패 ..
# 세로 * 가로
n, m = map(int, input().split())
# 플레이어 위치, 방향
x, y, d = map(int, input().split())

map_info = []
step = [(-1,0), (0,1), (1, 0), (0,-1)] #방향별 움직임
pre = [[0]*m for _ in range(n)] #가본 곳 체크

#방문한 칸 수 체크
cnt = 0

# 맵 입력
for i in range(n):
    temp = input().split()
    map_info.append(temp)

game = True
while game:
    #1. 현재 위치에서 방향을 기준으로 왼쪽 방향부터 차례로 갈 곳을 정함
    #4번 카운팅
    for i in range(4):
        d = (d + 3) % 4 #왼쪽 방향 이동 #1
        dx = x - step[d][1] #2
        dy = y - step[d][0] #2

        #맵을 벗어나지 않는다면
        if(dx>=0 and dx<m and dy>=0 and dy<n): 
            #가본적이 없고, 바다가 아니라면
            if(pre[dy][dx]==0 and map_info[dy][dx] !=1):
                x, y = dx, dy #한 칸 전진
                pre[y][x] = 1 #가봤다 체크
                cnt +=1
                break #for문 탈출
        
        #만약 네 방향 모두 이미 가봤다 or 바다다
        if(i == 3):
            #뒷방향이 바다인지 체크
            temp_d = (d+2)%4
            dx = x - step[temp_d][1]
            dy = y - step[temp_d][0]
            
            #뒷면이 바다라면 움직임을 끝냄
            if(dx>=0 and dx<m and dy>=0 and dy<n): 
                if(map_info[dy][dx] == 1):
                    game = False
                    break
                else:
                    #아니라면 뒤로 한 칸 돌아감
                    x, y = dx, dy
        print("현재 위치 ", x, y)
        print("카운팅",i,cnt)
        print(pre)

print(cnt)
                



    
    