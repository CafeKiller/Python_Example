import this
import turtle

if __name__ == '__main__':
    print(this)

    ##
    # 程序员之禅
    # The Zen of Python, by Tim Peters
    #
    # Beautiful is better than ugly.
    # Explicit is better than implicit.
    # Simple is better than complex.
    # Complex is better than complicated.
    # Flat is better than nested.
    # Sparse is better than dense.
    # Readability counts.
    # Special cases aren't special enough to break the rules.
    # Although practicality beats purity.
    # Errors should never pass silently.
    # Unless explicitly silenced.
    # In the face of ambiguity, refuse the temptation to guess.
    # There should be one-- and preferably only one --obvious way to do it.
    # Although that way may not be obvious at first unless you're Dutch.
    # Now is better than never.
    # Although never is often better than *right* now.
    # If the implementation is hard to explain, it's a bad idea.
    # If the implementation is easy to explain, it may be a good idea.
    # Namespaces are one honking great idea -- let's do more of those!
    # #

    # turtle 是python 内置的一个绘制模块(海龟绘图)
    # 详细可参考: https://docs.python.org/zh-cn/3/library/turtle.html

    turtle.pensize(4)
    turtle.pencolor('deepskyblue')

    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

    turtle.home()
    turtle.mainloop()

    a, b, c, d, e = 100, 3.14, 1 + 5j, "hello", True
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))

    num1 = int(input('num1 = '))
    num2 = int(input('num2 = '))
    print("%d + %d = %d" % (num1, num2, num1 + num2))