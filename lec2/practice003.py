'''
密碼重試程式
password = 'a123456'
讓使用者重復輸入密碼
最多輸入3次 
如果正確 就印出 "登入成功"
如果不正確 就印出 "密碼錯誤! 還有 n 次機會" 
'''
password = 'a123456'
times = 3 #剩餘機會
while True:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break #逃出迴圈
	else:
    elif XX:
    while :
		times = times - 1
		print('密碼錯誤! 還有', times,'次機會')
		if times ==0:
			break #注意Block

# password = 'a123456'
# times = 3 #剩餘機會
# while times > 0:
# 	times = times - 1
# 	pwd = input('請輸入密碼: ')
# 	if pwd == password:
# 		print('登入成功!')
# 		break #逃出迴圈
# 	else:
# 		print('密碼錯誤!')
# 		if times > 0:
# 			print(f'還有{times}次機會')


