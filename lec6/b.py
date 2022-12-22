# b.py
from a import Fibonacci
x = Fibonacci(5)  #這裡會執行a.py 
#然後執行裡面的的 def Fibonacci這個function
#這裡回到b.py這個程式了!
print(f"我是b.py裡的x是{x}")#我印出第五項 也就是5


print("我現在執行的是b.py的東西!")
print(f"現在的__name__是{__name__}") 