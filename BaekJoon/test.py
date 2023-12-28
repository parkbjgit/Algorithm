#과제 안내신분..? 백준 5597#
input_li=[]
for i in range(1,29):         #28개 입력받기
    num =  int(input())
    input_li.append(num)

check_li=list(i for i in range(1,31))

result_li = [num for num in check_li if num not in input_li]

for k in result_li:
    print(k)




#행렬 덧셈 백준 2738#
A, B = [], []

N,M = map(int, input().split())         #row= x좌표     column= y좌표

for row in range(N):
    row =  list(map(int, input().split()))
    A.append(row)

for row in range(N):
    row =  list(map(int, input().split()))
    B.append(row)

for row in range(N):
    for column in range(M):
        print(A[row][column]+B[row][column], end=' ')
    print()



