# 集合的运算
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

#  & 交集运算
result = s1 & s2
print(result)

# | 并集运算
result = s1 | s2
print(result)

# - 差集运算
result = s1 - s2
print(result)

# ^ 异或集
result = s1 ^ s2
print(result)

# <= 检查是否是子集
result = {3, 4, 5} <= {3, 4, 5, 6}
result = {3, 4, 5} <= {3, 4}
print(result)

# < 检查是否真子集
result = {1, 2, 3} < {1, 2, 3}
result = {1, 2, 3} < {1, 2, 3, 4, 5}
print(result)

# >= 检查是否是超集
result = {3, 4, 5} >= {3, 4, 5, 6}
result = {3, 4, 5} >= {3, 4}
print(result)

# > 检查是否真超集
result = {1, 2, 3} > {1, 2, 3}
result = {1, 2, 3, 4, 5} > {1, 2, 3}
print(result)
