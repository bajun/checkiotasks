FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    temp = str(number)
    lent =  len(temp)
    string_value = []
    if lent == 1:
        string_value = FIRST_TEN[int(number)-1]
    elif lent == 2:
        if (number in range(10,20)):
            string_value = SECOND_TEN[number-10]
        else:
            string_value.append(OTHER_TENS[(number/10)-2])
            if(number%10 != 0):
                string_value.append(FIRST_TEN[(number%10)-1])
            string_value = ' '.join(string_value)
    elif lent == 3 :
        string_value.append(FIRST_TEN[int(temp[0])-1])
        string_value.append(HUNDRED)
        t_number = int(temp[1]+temp[2])
        if (t_number in range(10,20)):
            string_value.append(SECOND_TEN[t_number-10])
        elif(t_number in range(1,10)):
            string_value.append(FIRST_TEN[int(t_number)-1])
        elif (t_number!=0):
            string_value.append(OTHER_TENS[(t_number/10)-2])
            if(t_number%10!=0):
                string_value.append(FIRST_TEN[(t_number%10)-1])
        string_value = ' '.join(string_value)
    
    return string_value
