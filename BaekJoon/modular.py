# import sys

# a,b,c=map(int,sys.stdin.readline().split())

# def multi(a,n):     #a^b  %c    n=b     10^11 %12
#     if n==1:
#         return a%c
    
#     else:
#         tmp=multi(a, n//2)
#         if n%2 == 0:
#             return (tmp*tmp) %c
#         else:
#             return (tmp*tmp*a) %c


# print(multi(a,b))
#################################

# from collections import deque

# n=int(input())
# deque=deque([i for i in range(1,n+1)])


# while len(deque) != 1:
#     deque.popleft()     #제일 위에 카드 버리기  1버리기
#     if len(deque)==1:
#         break

#     move_num=deque.popleft()
#     deque.append(move_num)

# print(deque[0])


import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time=time.time()
        result=func(*args, **kwargs)
        end_time=time.time()
        print(f"실행시간: {end_time-start_time:.5f}초")
        return result
    return wrapper

@timer_decorator
def example_function():
    time.sleep(1)

example_function()