#確認檔案在不在
import os # operating system作業系統

if os.path.isfile('products.csv'): #相對路徑 絕對路徑
	print('找到檔案了!')
else:
	print('檔案不存在!')


#讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '產品,價格' in line:
			continue #繼續
		name, price = line.strip().split(',')  #拿什麼當作切割的標準
		products.append([name,price])
print(f"products是{products}")

#讓使用者輸入
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	#
	products.append([name, price])
print("products是:",products)

#顯示所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f: #打開檔案
	f.write('產品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') #寫入