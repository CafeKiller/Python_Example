
if __name__ == '__main__':

    # 摄氏度转华氏度

    c = float(input('请输入一个摄氏度 = '))
    f = c * (9/5) + 32
    print("华氏度为:%.2f, 摄氏度为:%.2f" % (f , c))

    ##
    # 在使用print函数输出时，也可以对字符串内容进行格式化处理，
    # 上面print函数中的字符串%1.f是一个占位符，稍后会由一个float类型的变量值替换掉它。
    # 同理，如果字符串中有%d，后面可以用一个int类型的变量值替换掉它，而%s会被字符串的值替换掉。
    # 除了这种格式化字符串的方式外，还可以用下面的方式来格式化字符串，
    # 其中{f:.1f}和{c:.1f}可以先看成是{f}和{c}，
    # 表示输出时会用变量f和变量c的值替换掉这两个占位符，
    # 后面的:.1f表示这是一个浮点数，小数点后保留1位有效数字。
    # #

    # f = float(input('请输入一个摄氏度 = '))



