
movie = {'name':'Saving Private Ryan', #電影名稱
         'year':1998, #電影上映年份
         'director':'Steven Spielberg',#導演
         'Writer': 'Robert Rodat', #編劇
         'Stars':['Tom Hanks', 'Matt Damon', 'Tom Sizemore'],#明星
         'Oscar':['Best Director','Best Cinematography','Best Sound','Best Film Editing','Best Effects, Sound Effects Editing']
         #獲得的奧斯卡獎項
        }
# print(movie)
#dict_1 = {}
#dict_2 = dict()
# print(movie['cash'])
# print(movie.get("cash")) #return NONE
# print(movie.get("cast","not found"))

# #add
#dictName[key] = value
movie_1 = {}
movie_1['star'] = "Tom Hank" #新增key-value
print(movie_1)

# #add multi 
# #original_dict.update(new_dict)
#如果一次要update很多value 用update method就會比較方便
temp_dict = {'writer': 'Robert Rodat', #編劇
         'stars':['Tom Hanks', 'Matt Damon', 'Tom Sizemore'],#明星
         'Oscar ':['Best Director','Best Cinematography','Best Sound','Best Film Editing','Best Effects, Sound Effects Editing']
         }
movie_1.update(temp_dict)
print(movie_1)

# #del
# #del dict_name['key']

del movie_1['star']
print(movie_1)

# #other
# #計算字典中的元素個數
print(len(movie_1))

# # 印出字典裡的所有 key value
# dict_name.keys()
# dict_name.values()
#檢查指定的 key 是否存在於字典中
'key' in dict_name