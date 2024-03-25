#https://velog.io/@kjy2134/%EB%B0%B1%EC%A4%80-9663-N-Queen-%ED%8C%8C%EC%9D%B4%EC%8D%AC
#https://tral-lalala.tistory.com/104

def sol(k):
    global n,cnt

    if k==n:
        cnt+=1
        return

    for i in range(n):
        if not used_c[i] and not used_up[k+i] and not used_down[(n-1)+k-i]:
            used_c[i]=True
            used_up[k+i]=True
            used_down[(n-1)+k-i]=True
            sol(k+1)
            used_c[i]=False     #다시 false로 초기화
            used_up[k+i]=False
            used_down[(n-1)+k-i]=False
            

n=int(input())

maps=[[0]*n for _ in range(n)]

used_c=[False]*n

used_up=[False]*(2*(n-1)+1)

used_down=[False]*(2*(n-1)+1)

cnt=0

sol(0)
print(cnt)