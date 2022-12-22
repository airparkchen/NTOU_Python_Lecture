import random
# random.randint(x, y) 會產生一個 x～y 之間的隨機整數。

ans = random.randint(0, 100)
mode = input("請輸入難易度(Easy,Hard,God):")
mode = mode.title()
if mode == "Easy":
	t = 20
elif mode == "Hard":
	t = 10
elif mode == "God":
	t = 5
else:
	print("請輸入Easy,Hard,God其中之一")
print(f"遊戲難度為:{mode}")
print("遊戲開始!")
while t > 0 :
	t = t - 1
	your_ans = input("請輸入答案: ")
	your_ans = int(your_ans)
	if your_ans == ans:
		print("恭喜答對了!!")
		break
	elif your_ans > ans:
		print("再小一點!")
		print(f"剩餘{t}次")
	elif your_ans < ans:	
		print("再大一點!")
		print(f"剩餘{t}次")
	else:
		print("請輸入數字!")
		print(f"剩餘{t}次")
print(f"答案是{ans}遊戲結束!")