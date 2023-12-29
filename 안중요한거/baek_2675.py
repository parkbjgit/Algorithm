n=int(input())

for _ in range(n):
    count, str = input().split()
    count = int(count)
    
    for x in str:
        print(x*int(count), end='')     #옆으로 붙임
    print()    