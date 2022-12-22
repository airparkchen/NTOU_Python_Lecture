#讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		s = line.strip().split(',')  #拿什麼當作切割的標準
		products.append(s)
print(products)
		




# while True:
# 	name = input('請輸入商品名稱: ')
# 	if name == 'q':
# 		break
# 	price = input('請輸入商品價格: ')
# 	#
# 	products.append([name, price])
# print("products是:",products)
