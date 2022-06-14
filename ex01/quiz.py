import random

lst = [
    a = input("サザエの旦那の名前は？")
    if a == "マスオ" or a == "ますお":
        print("正解！")
    else:
        print("出直してこい")

    b = input("カツオの妹の名前は？")
    if b == "ワカメ" or b == "わかめ":
        print("正解!")
    else:
        print("出直してこい")

    c = input("タラオはカツオから見てどんな関係？")
    if c == "甥" or c == "おい" or c == "甥っ子" or c == "おいっこ":
        print("正解！")
    else:
        print("出直してこい")
    ]
print(random.randint(lst))


import random
a = 'ABCDEFG'

print(a.replace(random.sample(a,2),''))
