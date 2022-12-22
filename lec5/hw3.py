# print('請投入現金,只接受15,50,100元,按q退出投幣')
products = []
def cash(drink_0,money_0):
	money_0 = int(money_0)
	drink_price = [10, 15, 30]
	temp = drink_0 - 1#暫時的記數工具
	change = money_0 - drink_price[temp]  #零錢
	if change < 0:
		print(f"錢不夠!還剩下{moeny_0}")
		return money_0
	else:
		print(f"找零{change}元")
	return change

money = input("請投入現金,只接受15,50,100元,按q退出投幣:)\n輸入數字:  ")
money = int(money)
# print(type(money))
# print(money)
if money == 'q':
	exit()
elif money == 15 or money == 50 or money == 100:
	print(f"您輸入的金錢是{money}元")
	while True:
		print('飲料＆售價：柳橙汁 10元,礦泉水15元,牛奶30元')
		print('請輸入[數字]選擇想購買的飲料（柳橙汁：1,礦泉水：2,牛奶：3,退出：q')
		drink = input('輸入數字：')
		drink = int(drink)# "1" ==> 1
		if drink == 1 : #True
			print('購買柳橙汁花費10元！')
			money = cash(drink,money) #計算能不能購買? & 找錢?
		#money 50 drink 2  15$
		elif drink == 2:
			# print('購買礦泉水花費15元！')
			# money = cash(drink,money) 
		elif drink == 3:
			print('購買牛奶花費30元！')
			money = cash(drink,money) 
		else:
			print("請輸入要求的數字!")
			continue
else:
	print("請輸入15,50,100元,或按q退出投幣")

 # def cash(coin2):
 # 	return 50 - 15
 # def cash(coin3):
 # 	return coin3 - 30

		# def cash(coin1):
 		# 	return coin1 - 10
		# print(cash([15, 50, 100]))
