sentence="It is raining cats and dogs"
list1=sentence.split(" ")

#-----------------------------------
targetlist=[len(i) for i in list1]
print "=======Using List Comprehension---------"
print targetlist

#-----------------------------------
def calc(x):
    return len(x)

targetlist=map(calc,list1)
print "=======Using map and function---------"
print targetlist

#-----------------------------------
targetlist=map(lambda x: len(x),list1)
print "=======Using map and lambda---------"
print targetlist
