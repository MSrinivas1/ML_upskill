def createList(t):
  l = list(t)
  printList(l)
  return l

def printList(l):
  for i in l:
    print(type(i))
    print(i)

def actionList(listvalue, actionValue ):
  listvalue.pop(actionValue)

if __name__ == "__main_":

  print("main started")

  print(createList({12,12}), "from main")  # get list from set

  print(createList((12,12)), "from main")  # get list from tuple

  print(createList({1:"srinivas",12:"srin"}), "from main")  # get list from dust
  
  list = ["srinivas","srin"]
  print(type(list))
  try: 
    actionList(listvalue = list, actionValue = 1)
  except IndexError:
    print("Un usal")
  else :
    print("default")
  finally:
    print("default from finally")

