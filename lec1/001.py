# data type (種類)
# 資料型別
# 1. 整數 integer int (5,10,15,100)
# 2. 浮點數(小數) float (0.1, 5.2 , 10.65)
# 3. 布林值 boolean bool (True,False)
# 4. 字串 string str ('文字')

price = 10
pen = 0.38
rain = True
name = "Parker"
print(type(price))
print(type(pen))
print(type(rain))
print(type(name))
print(price,pen,rain,name)

# print (1)

# print("helloworld")

# a=1
# b='aabb'
# print(a,b)

# print("aaa""bbb")

# print("aaa","bbb")

# print("www","github","com",sep=".") #設置間隔符

import time

print("---Loading Example---")
print("Loading",end = "")
for i in range(20):
	print(".",end = '',flush = True)
	time.sleep(0.5)