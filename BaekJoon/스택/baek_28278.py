import sys
input=sys.stdin.readline

N=int(input())  #명령개수 입력
stack=[]

for _ in range(N):
    command=input().rstrip()    #명령어를 배열로 취급?
    
    if len(command)>2:  
        stack.append(int(command[2:]))  #명령어 이외에 추가숫자가 있으면 스택에 추가

    elif command=='2':      #2번 명령어는 스택에 정수가 있다면 맨위 정수빼고 출력
        if len(stack)!=0:
            print(stack.pop())
        else:
            print(-1)

    elif command=='3':  #스택안의 정수 개수 출력
        print(len(stack))

    elif command=='4':
        if len(stack)==0:   #스택에 정수가 없으면 1출력
            print(1)
        else:
            print(0)

    elif command=='5':  
        if len(stack)!=0:       #스택에 정수가 있으면 맨위 정수만 출력
            print(stack[-1])
        else:
            print(-1)
