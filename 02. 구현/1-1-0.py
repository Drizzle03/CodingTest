#개인 풀이 : 상하좌우
n = int(input())
cmd = list(map(str,input().split()))

x, y = 1, 1

for i in cmd:
    if(i=="L" and x>1):
        x-=1
    if(i=="R" and x<n):
        x +=1
    if(i=="U" and y>1):
        y-=1
    if(i=="D" and y<n):
        y +=1

print(y,x)
