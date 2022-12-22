#嘗試讀取ex1.txt
#將50筆隨機整數(0, 100)寫入ex1.txt中
#並統計ex1.txt中 >50有幾個
#再統計ex1.txt中 並將{其中}偶數的數字列出來

import random

data = []
with open('ex1.txt', 'w') as f:   #a附加 刪除f.truncate(0)
	for i in range(50):
		print(f"正在執行第{i+1}次")
		r = random.randint(0, 100)
		print(r, file = f) 
		data.append(r)

print(f"總共有{len(data)}個數字")
count = 0
even = []
for n in data:
	n = int(n)
	if n > 50:
		count += 1 #count = count + 1
		if n % 2 == 0:
			even.append(n)
print(f"總共有{count}個數字大於50")
print("其中大於50且是偶數的有:")
print(even)


