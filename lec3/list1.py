#留言讀取程式01
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: #一行一行讀取
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 ==0:
			print(len(data))
		# print(len(data))
print('檔案讀取完了,總共有',len(data),'筆資料') #長度


#算留言平均數
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	# print(sum_len)
print('留言的平均長度',sum_len/len(data))

#篩選範例1
# new = []
# for d in data: #d是字串 data是list
# 	if len(d) < 100:
# 		new.append(d) #如果符合條件就裝進新的清單
# print('一共有', len(new), '筆資料長度小於100')
# print(new[0])


# #篩選練習1
#篩選reviews.txt中
#有提到"good"的留言 並計算數量
#最後顯示[第1則]留言

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good), '筆留言提到Good')
# print(good)

# #list comprehension
# good = [d for d in data if 'good' in d]


# good = [1 for d in data if 'good' in d]
# print(good) 

#list comprehension
# bad = ['bad' for d in data if 'good' in d]
# print(bad)

#origin
bad = []
for d in data:
	bad.append('bad' in d)
print(bad)

