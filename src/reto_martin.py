#Logic-2 > lucky_sum


#Given 3 int values, a b c, return their sum. 
#However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. 
#So for example, if b is 13, then both b and c do not count.

#Function to coding bat
def lucky_sum(a, b, c):
    x=0
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        lista=[a,b,c]
        for i in lista:
            if i!=13:
                x=i+x
            else:
                break
    return x
