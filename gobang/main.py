# Author : CoffeeKiller
# filename : gobang.py
# createTime : 2023_11_13

finish = False
flagNum = 1
flagCh = '*'
x = 0
y = 0
print("\033[1;37;41m---------简易五子棋游戏（控制台版）---------\033[0m")

# 棋盘初始化
checkerboard = []
for i in range(10):
    checkerboard.append([])
    for j in range(10):
        checkerboard[i].append("-")


def msg():
    # 输出最后胜利的棋盘
    print("\033[1;37;44m--------------------------------")
    print("   1  2  3  4  5  6  7  8  9  10")
    for item in range(len(checkerboard)):
        print(chr(item + ord("A")) + " ", end=" ")
        for item2 in range(len(checkerboard[item])):
            print(checkerboard[item][item2] + " ", end=" ")
        print()
    print("--------------------------------\033[0m")
    # 输出获胜者
    if flagNum == 1:
        print("\033[32m*棋胜利！***\033[0m")
    else:
        print("\033[32mo棋胜利！***\033[0m")


while not finish:
    # 打印棋盘
    print("\033[1;30;46m--------------------------------")
    print("   1  2  3  4  5  6  7  8  9  10")
    for item in range(len(checkerboard)):
        print(chr(item + ord("A")) + " ", end=" ")
        for item2 in range(len(checkerboard[item])):
            print(checkerboard[item][item2] + " ", end=" ")
        print()
    print("--------------------------------\033[0m")
    # 判断当前下棋者
    if flagNum == 1:
        flagCh = "*"
        print("\033[1;37;40m请*输入棋子坐标（例如A1）：\033[0m", end=" ")
    else:
        flagCh = "o"
        print("\033[1;30;42m请o输入棋子坐标（例如J5）：\033[0m", end=" ")
    # 输入棋子的坐标
    str = input()
    ch = str[0]
    x = ord(ch) - 65
    y = int(str[1]) - 1
    # 判坐标上是否在棋盘之内
    if (x < 0 or x > 9) or (y < 0 or y > 9):
        print("\033[31m***您输入的坐标有误请重新输入！***\033[0m")
        continue
    # 判断坐标上是否有棋子
    if checkerboard[x][y] == "-":
        if flagNum == 1:
            checkerboard[x][y] = "*"
        else:
            checkerboard[x][y] = "o"
    else:
        print("\033[31m******您输入位置已经有其他棋子，请重新输入！\033[0m")
        continue
    # 判断棋子左侧
    if y - 4 >= 0:
        if (checkerboard[x][y - 1] == flagCh
                and checkerboard[x][y - 2] == flagCh
                and checkerboard[x][y - 3] == flagCh
                and checkerboard[x][y - 4] == flagCh):
            finish = True
            msg()

    # 判断棋子右侧
    if y + 4 <= 9:
        if (checkerboard[x][y + 1] == flagCh
                and checkerboard[x][y + 2] == flagCh
                and checkerboard[x][y + 3] == flagCh
                and checkerboard[x][y + 4] == flagCh):
            finish = True
            msg()

    # 判断棋子上方
    if x - 4 >= 0:
        if (checkerboard[x - 1][y] == flagCh
                and checkerboard[x - 2][y] == flagCh
                and checkerboard[x - 3][y] == flagCh
                and checkerboard[x - 4][y] == flagCh):
            finish = True
            msg()

    # 判断棋子下方
    if x + 4 <= 9:
        if (checkerboard[x + 1][y] == flagCh
                and checkerboard[x + 2][y] == flagCh
                and checkerboard[x + 3][y] == flagCh
                and checkerboard[x + 4][y] == flagCh):
            finish = True
            msg()

    # 判断棋子右上方向
    if x - 4 >= 0 and y - 4 >= 0:
        if (checkerboard[x - 1][y - 1] == flagCh
                and checkerboard[x - 2][y - 2] == flagCh
                and checkerboard[x - 3][y - 3] == flagCh
                and checkerboard[x - 4][y - 4] == flagCh):
            finish = True
            msg()

    # 判断棋子右下方向
    if x + 4 <= 9 and y - 4 >= 0:
        if (checkerboard[x + 1][y - 1] == flagCh
                and checkerboard[x + 2][y - 2] == flagCh
                and checkerboard[x + 3][y - 3] == flagCh
                and checkerboard[x + 4][y - 4] == flagCh):
            finish = True
            msg()

    # 判断棋子左上方向
    if x - 4 >= 0 and y + 4 <= 9:
        if (checkerboard[x - 1][y + 1] == flagCh
                and checkerboard[x - 2][y + 2] == flagCh
                and checkerboard[x - 3][y + 3] == flagCh
                and checkerboard[x - 4][y + 4] == flagCh):
            finish = True
            msg()

    # 判断棋子左下方向
    if x + 4 <= 9 and y + 4 <= 9:
        if (checkerboard[x + 1][y + 1] == flagCh
                and checkerboard[x + 2][y + 2] == flagCh
                and checkerboard[x + 3][y + 3] == flagCh
                and checkerboard[x + 4][y + 4] == flagCh):
            finish = True
            msg()
    flagNum *= -1 # 更换下棋者标记
