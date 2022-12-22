# def add(x, y):
# 	return x + y

# result = add(3, 4)
# print(result)

#計算清單的平均數
def average(numbers):
	avg = sum(numbers) / len(numbers) #sum可以對清單做加總    /除法會轉成浮點數
	return avg 

a = average([1, 2, 3])
print(a)

# #fast
def average(numbers):
	return sum(numbers) / len(numbers) 

print(average([1, 2, 3]))
print(average([13, 23, 33]))
print(average([10, 25, 366]))