from pcoll.actionList import createList
from pexc.custEx import AssessScoreNotGTMaxException

def getStudentScoreValidate() :
  s = createList([1,3,4,5,34,65,3,20])
  for sc in s:
    if sc>40 :
        raise AssessScoreNotGTMaxException()


if __name__ == "__main__" :
    print("mian started for exceptions")
    try :
       getStudentScoreValidate()
    except AssessScoreNotGTMaxException as ae:
       print("wrong score may be exeeded score")
       print()
    else :
       print("else not exception")
    finally :
      print("allway")