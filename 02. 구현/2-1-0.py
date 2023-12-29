#왕실의 나이트 : 개인풀이
move = [(-2, 1), (-2,-1), (2, 1), (2, -1), (1, -2), (1, 2), (-1,-2), (-1,2)]
pos = input()
x = ord(pos[0])-96
y = int(pos[1])
cnt = 0

for dx, dy in move:
    if(x+dx>0 and x+dx<=8 and y+dy>0 and y+dy<=8):
        cnt+=1

print(cnt)