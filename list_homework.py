myUniqueList = []
myLeftovers = []

def addToList(n):
    if n in myUniqueList:
        addToLeftovers(n)
        return False
    else:
        myUniqueList.append(n)
        return True

def addToLeftovers(n):
  myLeftovers.append(n)

# Test the addToList function
print(myUniqueList) # []
print(addToList(10)) # Returns True
print(myUniqueList) # [10]
print(myLeftovers) # []
# Adding the element that already exists
print(addToList(10)) # Returns False
print(myUniqueList) # [10]
print(myLeftovers) # [10]
# Adding a new element
print(addToList(11)) # Returns True
print(myUniqueList) # [10, 11]
print(myLeftovers) # [10]