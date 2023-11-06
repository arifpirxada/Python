''' 1. To find the second lowest & second largest number in an list/array '''

def findSecondLowestLargestNum(arr):
    lowest = arr[0]
    largest = arr[0]

    secondLowest = arr[0]
    secondLargest = arr[0]

    for elem in arr:
        if elem < lowest:
            lowest = elem
        elif elem > largest:
            largest = elem
    
    for elem in arr:
        if elem != lowest and elem < secondLowest:
            secondLowest = elem
        elif elem !=largest and elem > secondLargest:
            secondLargest = elem

    return f"Second Lowest: {secondLowest}; Second Largest: {secondLargest}"


# print(findSecondLowestLargestNum([2,5,1,48,32,430,6,68, 100]))

''' 2. Write a Python program that accepts the user's first and last 
name and prints them in reverse order with a space between them.'''

def reverseName(firstName, lastName):
    fullName = f"{firstName} {lastName}"
    nameList = [char for char in fullName]
    reversedName = ""

    i = len(nameList) - 1
    while i != -1:
        reversedName = reversedName + nameList[i]
        i = i - 1

    return reversedName

# print(reverseName("Micheal", "Jorden"))

''' 3. Write a Python program that accepts a filename from the
user and prints the extension of the file. 
Sample filename : abc.java '''

def getExt(fileName):
    splitedName = fileName.split(".")
    print(splitedName[1])

# getExt("main.py")

''' 4. Write a Python program to find a list of integers with exactly
two occurrences of nineteen and at least three occurrences of five.
Return True otherwise False.
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True '''

def findNineteenAndFiveOccurences(arr):
    nineteen = 0
    five = 0

    for elem in arr:
        if elem == 19:
            nineteen += 1
        elif elem == 5:
            five += 1
    
    if nineteen == 2 and five > 2:
        return True
    else:
        return False

# print(findNineteenAndFiveOccurences([5,5,2,19,18,14,19]))

''' 5. Write a Python program to sum recursion lists.
Test Data: [1, 2, [3,4], [5,6]]'''

def recursionListSum(userList):
    totalSum = 0

    for elem in userList:
        if isinstance(elem, list):
            totalSum += recursionListSum(elem)
        else:
            totalSum += elem
    
    return totalSum
        
    
# print(recursionListSum([3,2,[4,[2],8],3, [3,5]]))
