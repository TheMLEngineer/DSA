def fn3():
    print('Three')

def fn2():
    fn3()
    print('Two')
    
def fn1():
    fn2()
    print('One')

fn1()