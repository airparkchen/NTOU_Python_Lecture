#else if 另外如果
age = input('請輸入年齡: ')
age = int(age)
if age < 13 :
	print('國小')
elif age >= 13 and age < 18:
	print('國高中')
elif age >= 18 and age < 22:
	print('大學')
else:
	print('社會人')