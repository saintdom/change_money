# dss

re = []


# 定义找零钱函数
def change(m, o, i, res):
    if m == 0:
        re.append("方案" + str(len(re)+1) + "：" + res[:-1])  # 截去最后面的+号
        return 1
    elif m < 0 or i < 0:
        return 0
    return change(m, o, i - 1, res) + change(m - o[i], o, i, res + str(o[i]) + "+")


if __name__ == "__main__":
    money = 80
    options = [1, 5, 10, 20, 50, 100]
    result = ""
    change(money, options, len(options) - 1, result)
    print("共" + str(len(re)+1) + "种方案：")
    print(re)
