# 중복순열

# from itertools import product
# data=['a','b','c']

# result=list(product(data,repeat=2))

# print(result)


#조합

from itertools import combinations
data=['a','b','c']

result=list(combinations(data,2))       #3C2=3

print(result)


# 중복조합
# from itertools import combinations_with_replacement
# data=['a','b','c']

# result=list(combinations_with_replacement(data,2))

# print(result)

