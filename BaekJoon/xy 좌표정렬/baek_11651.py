# 11651 y좌표로 정렬(같으면 x 좌표로 정렬)
import sys    

n=int(input())
li=[]

for i in range(n):
    [a,b]=map(int, sys.stdin.readline().split())
    li.append([a,b])

li.sort(key=lambda x: (x[1],x[0]))      #####

for i in li:
    print(i[0], i[1])