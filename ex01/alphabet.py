import random
import datetime

NUM_OF_TRIAL = int(input("何回繰り返しますか"))
NUM_OF_ALL_CHARS = 10
NUM_OF_ABS_CHARS = 2

alphabets = [chr(c+65) for c in range(26)]
all_char_lst = random.sample(alphabets,NUM_OF_ALL_CHARS)
abs_char_lst = random.sample(all_char_lst,NUM_OF_ABS_CHARS)
pre_char_lst = [c for c in all_char_lst if c not in abs_char_lst]
print(f"対象文字：{all_char_lst}")
print(f"欠損文字：{abs_char_lst}")
print(f"表示文字：{pre_char_lst}")

a = int(input("欠損文字はいくつあるでしょうか？："))

if a == 2:
    b = input("正解です。それでは具体的に欠損文字を１つずつ入力してください：")
    if b == abs_char_lst:
        c = input("二つ目の文字を入力してください：")
        if c == abs_char_lst:
            print("正解です")
        else:
            print("不正解です。")
    else:
        print("不正解です")
else:
    print("不正解です。またチャレンジしてください")