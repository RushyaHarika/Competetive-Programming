__all__=['add','add2']
"""when this module is imported if we specify "from prime2 impoet *" ,
only those contained in __all__ will be imported"""  
def add(a,b,c):
    print(a+b+c)
def add1(a,b,c):
    print(a+b+c)
def add2(a,b,c):
    print(a+b+c)

if __name__=='__main__':
    add(7,11,5)