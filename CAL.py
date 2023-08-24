def calculator():
    print("歡迎使用計算器！請輸入兩個數字和運算符號進行計算（+ - * /）。")
    num1 = int(input("請輸入第一個數字："))
    operator = input("請輸入運算符號：")
    num2 = int(input("請輸入第二個數字："))

    if operator == "+":
        result = num1 + num2
        print("計算結果：", result)
    elif operator == "-":
        result = num1 - num2
        print("計算結果：", result)
    elif operator == "*":
        result = num1 * num2
        print("計算結果：", result)
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            print("計算結果：", result)
        else:
            print("錯誤：除數不能為零！")
    else:
        print("錯誤：請輸入有效的運算符號！")

calculator()
