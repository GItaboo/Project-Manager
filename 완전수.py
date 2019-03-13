'''
1000 이하의 완전수  -> 1부터 시작해서 1000이 되면 종료하도록 한다

자신의 약수의 합이 자신과 같아야 함 -> 약수를 구한다 + 약수들을 더한다

맞으면 yes 로 출력 -> 합이 수와 같은지 if 로 검증

'''a = int(input())
sum = 0

for x in range (1,a):

    if( a % x == 0 ):
        sum = sum + x

if(sum == a):
    print('yes')
else:
    print('no')


a = int(input())
sum = 0

for x in range (1,a):

    #sum = 모든 a % x == 0 의 합
    #x = 1부터 시작해서 a까지 +1
    #x = x + 1
    if( a % x == 0 ):
        sum = sum + x

if(sum == a):
    print('yes')
else:
    print('no')



