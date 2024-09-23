

def tupleAction() :
    """ create simple tuple class """
    t = tuple([1,3,2,5,7])
    printTuple(t)
    

def tupleAction(t) :
    """ convert collection tuple, list, set and dist to tuple """
    print(type(t))
    print(len(t))
    t = tuple(t)

    #printTuple(t)
    actionOntouple(t)

def printTuple(t):
    """ print touple class """
    for k in t:
        print(k)
def actionOntouple(t):
    """ tuple only support count and index"""
    print("count value",t.count(36))
    for i in range(0, len(t)):
        print("from index ", format(t[i]))
    
if __name__ == "__main__":
    print(__name__)
    a = "12"
    b = tuple(a)
    """ tuple can accept tuple """
    tupleAction(()) 

    """ tuple can accept List """
    tupleAction([]) 
    
    """ tuple can accept set """
    tupleAction({}) 
    
    """ tuple can accept tuple """
    tupleAction((1,'srinivas',36,'srinivas')) 

    """ tuple can accept list """
    tupleAction([1,'srinivas',36,'srinivas']) 
    
    """ tuple can accept set """
    tupleAction({1,'srinivas',36,'srinivas'}) 

    """ tuple can allow dictionary """
    tupleAction({"name":"srinivas","age":32})

