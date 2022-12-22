#二維清單
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []
	p.append(name)
	p.append(price)

	products.append(p)
print("products是:",products)

# print("products[0][1]是:"+products[0][1])

# # #快速
# products = []
# while True:
# 	name = input('請輸入商品名稱: ')
# 	if name == 'q':
# 		break
# 	price = input('請輸入商品價格: ')
# 	# p = []
# 	# p.append(name)
# 	# p.append(price)
# 	p = [name, price]
# 	products.append(p)
# print("products是:",products)

# #fastest
# products = []
# while True:
# 	name = input('請輸入商品名稱: ')
# 	if name == 'q':
# 		break
# 	price = input('請輸入商品價格: ')
# 	products.append([name, price])
# print("products是:",products)

#prove
# for p in products:
# 	print(f"現在 p 是{p}!")
# 	print(f"現在products是{products}!")
# 	print("-----------")