import textwrap

def case1():
    code = "['acb']"
    d = eval(code)
    print d

def case2():

    code = """\
    [i for i in range(10)]"""
    textwrap.dedent(code)
    d = eval(code)
    print d

if __name__ == '__main__':
    case1()
    case2()

    print eval("__import__('os').getcwd()")