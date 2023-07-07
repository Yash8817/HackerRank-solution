def timeConversion(input_time):

    am_or_pm = str(input_time[8:])
    hours = str(input_time[:2])
        
    if((am_or_pm == "AM") and (hours == "12")):
        return "00" + input_time[2:-2]

    elif input_time[8:] == "AM":
        return input_time[:-2]

    elif((am_or_pm == "PM") and (hours == "12")):
        return input_time[:-2]

    else:
        
        return str(int(input_time[:2]) + 12) + input_time[2:8]
    

input_time = input()

print(timeConversion(input_time))
