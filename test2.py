def count_letters(input_string):
    # 全轉為小寫
    input_string = input_string.lower()
    letter_count = {}

    # 迴圈找字串中的每個字
    for char in input_string:
        if not char.isspace():
            # 使用setdefault方法來初始化字元的計數為0
            letter_count.setdefault(char, 0)
            letter_count[char] += 1
    # 將字典按照鍵值排序
    sorted_char_count = dict(sorted(letter_count.items()))
    return sorted_char_count

input_string = "Hello welcome to Cathay 60th year anniversary"
result = count_letters(input_string)

for letter, count in result.items():
    print(f"{letter} {count}")