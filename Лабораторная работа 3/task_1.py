src = not False and True or False and not True

# True and True or False and False # избавляемся от отрицаний
# True or True # избавляемся от логического "И"
# True # избавляемся от логического "ИЛИ"

result = True

print(src == result)
