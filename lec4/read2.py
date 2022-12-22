#跳過標題 跳過XX 
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '產品,價格' in line:
			continue #繼續
		name, price = line.strip().split(',')  #拿什麼當作切割的標準
		products.append([name,price])
print(f"products是{products}")