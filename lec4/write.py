#字串運算(加法、乘法)
# a = "abc" * 3
# print(a)

products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print("products是:",products)

#顯示商品對應價格
for p in products:
	print(p[0], '的價格是', p[1])

# # #寫入檔案
# with open('products.txt', 'w') as f: #打開檔案
# 	f.write('產品,價格\n')
# 	for p in products:
# 		f.write(p[0] + ',' + p[1] + '\n') #寫入\
# #close

# # #亂碼
with open('products.csv', 'w', encoding = 'utf-8') as f: #打開檔案
	f.write('產品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') #寫入\