#確認檔案在不在
#read_file()
import os # operating system作業系統
def read_file(filename):
	products = []
	if os.path.isfile(filename): #相對路徑 絕對路徑
		print('找到檔案了!')
		with open(filename, 'r', encoding = 'utf-8') as f:
			for line in f:
				if '產品,價格' in line:
					continue #繼續
				name, price = line.strip().split(',')  #拿什麼當作切割的標準
				products.append([name,price])
		print(f"products是{products}")

	else:
		print('檔案不存在!')
	return products

def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		#
		products.append([name, price])
		print("products是:",products)

def print_products(products):
	#顯示所有購買紀錄
	for p in products:
		print(p[0], '的價格是', p[1])

def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f: #打開檔案
		f.write('產品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') #寫入

#執行
products = read_file('products.csv')
user_input(products)
print_products(products)
write_file('products.csv', products)
