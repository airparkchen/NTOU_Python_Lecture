# 讀取檔案&儲存 把電腦上的資料txt csv....在程式中讀取並儲存 
# products = []
# with open('products.csv', 'r', encoding = 'utf-8') as f:
# 	for line in f:
# 		s = line.split(',')  #拿什麼當作切割的標準
# 		name = s[0]
# 		price = s[1]


#fast
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		name, price = line.strip().split(',')  #拿什麼當作切割的標準
		print(f"我是line:{line}")
		products.append([name, price])
print("products是:",products)
