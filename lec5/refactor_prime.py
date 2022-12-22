#refactor
#全部寫成function
#read_file() function
#user_input() 
#print_produects()
#write_file()
import os

#讀取資料
def read_file(filename):
	products = []
	if os.path.isfile(filename): #確認檔案在不在
		print('找到檔案了!')
		with open(filename, 'r', encoding = 'utf-8') as f:
			for line in f:
				if '產品,價格' in line:
					continue #繼續
				name, price = line.strip().split(',')  #拿什麼當作切割的標準
				products.append([name,price])
		print(f"products是{products}")
	else:
		print('找不到檔案....')
	return products  #回傳我們需要的值

#讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		price = int(price)  #int
		products.append([name, price])
	print("products是:",products)
	return products

#顯示所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f: #打開檔案
		f.write('產品,價格\n')
		for p in products:
			f.write(str(p[0]) + ',' + str(p[1]) + '\n') #轉換成全部字串後寫入

#創建新檔案
def write_newfile(filename):
	products = []
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		#
		products.append([name, price])
	print("products是:",products)
	with open(filename, 'w', encoding = 'utf-8') as f: #打開檔案
		f.write('產品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') #寫入
	return products
	
#初始化文件
def initialize_file(filename):
	with open(filename, 'w', encoding = 'utf-8') as f: #打開檔案
		f.write('產品,價格\n')

# 創建新檔案/初始化文件
# write_newfile('products.csv')
# initialize_file('products.csv')
#執行
products = read_file('products.csv')
products = user_input(products)
print_products(products)
write_file('products.csv', products)

