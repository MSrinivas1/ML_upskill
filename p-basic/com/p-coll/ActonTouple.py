

def tupleAction() :
    """ """
    t = tuple([1,3,2,5,7])
    printTuple(t)

def tupleAction(t) :
    """ """
    print(type(t))
    print(len(t))
    t = tuple(t)
    printTuple(t)

def printTuple(t):
    for k in t:
        print(k)


if __name__ == "__main__":
    print(__name__)
    
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

