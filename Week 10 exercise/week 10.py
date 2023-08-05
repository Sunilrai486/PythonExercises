import math

#converts string to number.
def convertstringtonumber(stringvalue):
    numbertoappend = 0
    if("0" in stringvalue):
        numbertoappend = 0
    elif("1" in stringvalue):
        numbertoappend = 1
    elif("2" in stringvalue):
        numbertoappend = 2
    elif("3" in stringvalue):
        numbertoappend = 3
    elif("4" in stringvalue):
        numbertoappend = 4
    elif("5" in stringvalue):
        numbertoappend = 5
    elif("6" in stringvalue):
        numbertoappend = 6
    elif("7" in stringvalue):
        numbertoappend = 7
    elif("8" in stringvalue):
        numbertoappend = 8
    elif("9" in stringvalue):
        numbertoappend = 9
    return numbertoappend

#converts number array to a single string
def convertnumarraytostring(numberarray):
    result = ""
    for res in numberarray:
        if(res == 1):
            result += "1"
        elif(res == 2):
            result += "2"
        elif(res == 3):
            result += "3"
        elif(res == 4):
            result += "4"
        elif(res == 5):
            result += "5"    
        elif(res == 6):
            result += "6"
        elif(res == 7):
            result += "7"
        elif(res == 8):
            result += "8"
        elif(res == 9):
            result += "9"   
        elif(res == 0):
            result += "0"
    return result

#multiply the string inputs
def multiplystringinput(string1, string2):
    numarray = []
    for str1 in string1:         
        numbertoappend = convertstringtonumber(str1)
            
        if(len(numarray) > 0):
            numarray[0] = numarray[0] * 10 + numbertoappend
        else:
            numarray.append(numbertoappend)
            
    for str2 in string2:
        numbertoappend = convertstringtonumber(str2)

        if(len(numarray) > 1):
            numarray[1] = numarray[1] * 10 + numbertoappend
        else:
            numarray.append(numbertoappend)
    
    mulres: int = numarray[0] * numarray[1]
    
    print(mulres)
    
    resultnumarray = []
    i=0; 
    while i<=(mulres):
        print(i, mulres)
        a = math.floor(mulres%10)
        print(a)
        resultnumarray.append(a)
        mulres = mulres/10
        i += 1
        if(mulres < i):
            resultnumarray.append(mulres)
    
    arrayrev = resultnumarray[::-1]
    
    result = convertnumarraytostring(arrayrev)
    
    return result

number1 = "10"
number2 = "200000"
print(type(number1), number1, type(number2), number2)
mulresult = multiplystringinput(number1, number2)
print(mulresult, type(mulresult))
