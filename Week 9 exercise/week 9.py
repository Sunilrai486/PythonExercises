# finding the majority element
def findthemajorityelement(numarray):
    """Finds the majority element in the array.

    Args:
        numarray (arr): Array of numbers.

    Returns:
        int: Returns the majority element.
    """
    if(len(numarray) > 0):
        numberfrequency = {}
        numarray.sort()
        majoritythreshold = len(numarray)/2
        for num in numarray:
            if(num in numberfrequency):
                numberfrequency[num] += 1
            else:
                numberfrequency[num] = 1
                
        maxfrequency = 0
        for numf in numberfrequency.items():
            if(numf[1] > maxfrequency):
                maxfrequency = numf[1]

        if(maxfrequency > majoritythreshold):
            for key, value in numberfrequency.items():
                if(value == int(maxfrequency)):
                    return key

print(findthemajorityelement([3,2,2,2,2,3]))