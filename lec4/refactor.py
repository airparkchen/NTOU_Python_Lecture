products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '產品,價格' in line:
			continue #繼續
		name, price = line.strip().split(',')  #拿什麼當作切割的標準
		products.append([name,price])
print(f"products是{products}")

#refactor
# read_file('products.csv')
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '產品,價格' in line:
			continue #繼續
			name, price = line.strip().split(',')  #拿什麼當作切割的標準
			products.append([name,price])
	print(f"products是{products}")
	#return

#read_file('products.csv')