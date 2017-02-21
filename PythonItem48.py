
#sorts without creating a new list.
def mySortV1(theList):
   i = 0
   for i in range(0,len(theList)-1):
      x = min(theList[i:])
      countX = theList.count(x)
      if (countX>1):
         while x in theList:
            theList.remove(x)
         while (countX>0):
            theList.insert(i,x)
            i+=1
            countX-=1
         if (i < len(theList)):
             return theList
         else:
            return i
      else:
         theList.remove(x)
         theList.insert(i,x)
         i+=1
   return theList

#creates a new list of sorted items as it goes.
def mySortV2(theList):
   i=0
   x=0
   sorted=[]
   for i in range(0,len(theList)):
      x = min(theList)
      theList.remove(x)
      sorted.insert(i,x)
   theList = sorted
   return theList
      

listOne = [67, 45, 2, 13, 1, 998]
listTwo = [89, 23, 33, 45, 10, 12, 45, 45, 45]
print("unsorted",listOne)
print("sorted V1",mySortV1(listOne))
print("\nunsorted",listTwo)
print("sorted V1",mySortV1(listTwo))

print("\n------------------------------------------------------\n")

listOne = [67, 45, 2, 13, 1, 998]
listTwo = [89, 23, 33, 45, 10, 12, 45, 45, 45]
print("unsorted",listOne)
print("sorted V2",mySortV2(listOne))
print("\nunsorted",listTwo)
print("sorted V2",mySortV2(listTwo))
