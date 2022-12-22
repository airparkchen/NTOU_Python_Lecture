# import time

# print("---Loading Example---")
# print("Loading",end = "")
# for i in range(20):
# 	print(".",end = '',flush = False)
# 	time.sleep(0.5)

#flush 類似於重新整理
import time
# f = open("123.txt", "w")
# print("123456789", file = f)
# time.sleep(20)

f = open("123.txt", "w")
print("123456789",file = f, flush = True)
time.sleep(20)

