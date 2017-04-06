import sys



def case1():
    print sys.exc_info()

def case2():

    try:
        no_var
    except NameError, e:
        print str(e)
        print sys.exc_info()
        print sys.exc_info()[:2] + (None, 2)
        print sys.exc_info()[:2]


case1()
case2()


def arr_fn(*ff):
    lst = [1,]
    lst.extend(ff)
    print lst

arr_fn(1, 2)



