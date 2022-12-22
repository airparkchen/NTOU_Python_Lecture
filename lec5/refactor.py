#refactor
#全部寫成function
#read_file() function
#user_input() 
#print_produects()
#write_file()

def read_file():
	products = []
	if os.path.isfule('products.csv'): #確認檔案在不在
		print('找到檔案了!')
		with open('products.csv', 'r', encoding = 'utf-8') as f:
			for line in f:
				if '產品,價格' in line:
					continue #繼續
				name, price = line.strip().split(',')  #拿什麼當作切割的標準
				products.append([name,price])
		print(f"products是{products}")
	else:
		print('找不到檔案....')

#讓使用者輸入
def user_input():
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		#
		products.append([name, price])
	print("products是:",products)

#顯示所有購買紀錄
def print_products():
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file():
	with open('products.csv', 'w', encoding = 'utf-8') as f: #打開檔案
		f.write('產品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') #寫入






#執行
read_file()
user_input()
print_products()
write_file()

