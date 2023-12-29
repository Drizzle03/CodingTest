#큰 수의 법칙
#개인 풀이

#배열의 크기, 숫자 덧셈 횟수, 연속 덧셈 제한
n, m, k = map(int, input().split())
ary = list(map(int,input().split()))

#정렬
ary.sort(reverse=True)

#가장 큰 수, 두 번째 수 가져옴
n1 = ary[0]
n2 = ary[1]

sum = 0

for i in range(1,m+1):
    if(i % k == 0 ):
        sum+=n2
    else:
        sum += n1

print(sum)