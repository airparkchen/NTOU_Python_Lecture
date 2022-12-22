#留言讀取程式
data = []
with open('reviews.txt', 'r') as f:
	for line in f: #一行一行讀取
		data.append(line)

		# print(len(data))
print(len(data)) #長度

# print(data[0])
# print("------------")
# print(data[1])

#留言讀取程式01
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: #一行一行讀取
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 == 0:
			print(len(data))
		# print(len(data))
print('檔案讀取完了,總共有',len(data),'筆資料') #長度


# #算留言平均數
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	# print(sum_len)
print('留言的平均長度',sum_len/len(data))