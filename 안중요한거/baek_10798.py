################2차원 배열로 행렬 세로읽기
import sys

words = []
for i in range(5):  
  word = sys.stdin.readline().rstrip()
  words.append(word)

for i in range(15): 
  for j in range(5): 
    if i < len(words[j]):
      print(words[j][i], end="")


#자세한 설명 블로그
#https://ymd-memo.tistory.com/54