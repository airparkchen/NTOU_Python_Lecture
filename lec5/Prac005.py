#販賣機
#做一個販賣機 只可以投 15 50 100元 或是按q離開
#販賣的東西有 柳橙汁 10元, 礦泉水 15元 , 牛奶 30元
#利用function 進行 是否可以購買的運算 並顯示餘額


def buy_drink(drink, price, money):
	if money <= price:
		print("餘額不足喔!")
		print(f"還需要{price - money}元!")
	elif money == price:
		print(f"購買了{drink}花費{price}元!")
	else:
		print(f"購買了{drink}花費{price}元!")
		print(f"餘額{money - price}元")



money = input("請投入現金,只接受15,50,100元,按q退出投幣:)\n輸入數字:  ")
if money == 'q':
	exit()
# elif money == "15" or "50" or "100":
elif money == "15" or money == "50" or money == "100":
	print(f"您輸入的金錢是{money}元")
else:
	print("請輸入15,50,100元,或按q退出投幣")
	exit()
print("飲料&售價: 柳橙汁 10元, 礦泉水 15元 , 牛奶 30元 ")
drink = input("請輸入[數字]選擇想購買的飲料(柳橙汁: 1 , 礦泉水 : 2 , 牛奶 : 3 ,退出 : q) \n輸入數字:  ")
if drink == 'q':
	exit()
elif drink == "1":
	buy_drink('柳橙汁', 10, int(money) )
elif drink == "2":
	buy_drink('礦泉水', 15, int(money) )
elif drink == "3":
	buy_drink('牛奶', 30, int(money) )
else:
	print("請輸入要求的數字或輸入q離開")

print("謝謝光臨!")
