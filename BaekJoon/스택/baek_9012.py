n=int(input())

for _ in range(n):
    stk=[]
    s=input()
    isVPS=True

    for ch in s:
        if ch=='(':     #여는 괄호는 스택에 추가
            stk.append(ch)

        if ch==')':     #닫는 괄호면 스택에서 pop
            if stk:
                stk.pop()
            elif not stk:
                isVPS=False
                break

    if isVPS and not stk:   #아직 true이고 스택이 비어있다면
        print('YES')

    elif not isVPS or stk:  #이미 false이거나 스택에 (가 있는 경우
        print('NO')

    