# a.py
#先不加name main
def Fibonacci(n): #費氏數列 0 1 1 3 5 7 ...
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 2) + Fibonacci(n - 1)
for i in range(6):
    print(Fibonacci(i))

print("我現在執行的是a.py的東西!")
print(f"現在的__name__是{__name__}") 
