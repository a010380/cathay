def change_digits(number_list):
    # 檢查輸入的數字
    if len(number_list) != 5:
        raise ValueError("請提供包含5個2位數字的串列")
    for num in number_list:
        if 10 <= num <= 99:
            print(num)
        else:
            raise ValueError("請提供包含5個2位數字的串列")
        if isinstance(num, int):
            pass
        else:
            raise ValueError("請提供包含5個2位數字的串列")
    # 交換
    result = [int(str(num)[1] + str(num)[0]) for num in number_list]

    return result

# 測試函數
input = [53, 64, 75, 19, 92]
output = change_digits(input)
print("輸入串列:", input)
print("輸出串列:", output)