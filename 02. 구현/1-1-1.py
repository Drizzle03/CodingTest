#서적 풀이
n = int(input())
x, y = 1, 1
plans = input().split() #기본이 리스트 형태이므로

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        #루프를 돌면서 움직임이 일치한다면
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간 제약 확인
    if nx<1 or ny<1 or nx>n or ny >n:
        continue
    x,y = nx,ny
print(x,y)