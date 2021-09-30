# def aqi_pollutant_calc(aqiHigh, aqiLow, pollutHigh, pollutLow, pollut):
#     aqi = (aqiHigh - aqiLow) / (pollutHigh - pollutLow) * (pollut - pollutLow) + aqiLow
#     return aqi

# print(round(aqi_pollutant_calc(100, 51, 35.4, 12.1, 30.1)))
# print()

print()
locationName = input("Enter the location name: ")

correctValue = False
while correctValue == False:
    pollutPM2 = int(input("Enter the pollutant concentration for the PM2.5 monitor: "))
    if pollutPM2 < 0 or pollutPM2 > 500.4:
        correctValue = False
        print()
        print("ERROR: the PM2.5 monitor value is not in the bounds!")
        print()
    else:
        correctValue = True

correctValue = False
while correctValue == False:
    pollutPM10 = int(input("Enter the pollutant concentration for the PM10 monitor: "))
    if pollutPM10 < 0 or pollutPM10 > 604:
        correctValue = False
        print()
        print("ERROR: the PM10 monitor value is not in the bounds!")
        print()
    else:
        correctValue = True

correctValue = False
while correctValue == False:
    pollutNO2 = int(input("Enter the pollutant concentration for the NO2 monitor: "))
    if pollutNO2 < 0 or pollutNO2 > 2049:
        correctValue = False
        print()
        print("ERROR: the NO2 monitor value is not in the bounds!")
        print()
    else:
        correctValue = True

correctValue = False
while correctValue == False:
    pollutSO2 = int(input("Enter the pollutant concentration for the SO2 monitor: "))
    if pollutSO2 < 0 or pollutSO2 > 1004:
        correctValue = False
        print()
        print("ERROR: the SO2 monitor value is not in the bounds!")
        print()
    else:
        correctValue = True

correctValue = False
while correctValue == False:
    pollutCO = int(input("Enter the pollutant concentration for the CO monitor: "))
    if pollutCO < 0 or pollutCO > 50.4:
        correctValue = False
        print()
        print("ERROR: the CO monitor value is not in the bounds!")
        print()
    else:
        correctValue = True

def low_high_finderPM2(PM2):
    if (PM2 >= 0) and (PM2 <= 12.0):
        lowPM2 = 0
        highPM2 = 12.0
    elif (PM2 >= 12.1) and (PM2 <= 35.4):
        lowPM2 = 12.1
        highPM2 = 35.4
    elif (PM2 >= 35.5) and (PM2 <= 55.4):
        lowPM2 = 35.5
        highPM2 = 55.4
    elif (PM2 >= 55.5) and (PM2 <= 150.4):
        lowPM2 = 55.5
        highPM2 = 150.4
    elif (PM2 >= 150.5) and (PM2 <= 250.4):
        lowPM2 = 150.5
        highPM2 = 250.4
    elif (PM2 >= 250.5) and (PM2 <= 500.4):
        lowPM2 = 250.5
        highPM2 = 500.4
    return lowPM2, highPM2

def low_high_finderPM10(PM10):
    if (PM10 >= 0) and (PM10 <= 54):
        lowPM10 = 0
        highPM10 = 54
    elif (PM10 >= 55) and (PM10 <= 154):
        lowPM10 = 55
        highPM10 = 154
    elif (PM10 >= 155) and (PM10 <= 254):
        lowPM10 = 155
        highPM10 = 254
    elif (PM10 >= 255) and (PM10 <= 354):
        lowPM10 = 255
        highPM10 = 354
    elif (PM10 >= 355) and (PM10 <= 424):
        lowPM10 = 355
        highPM10 = 424
    elif (PM10 >= 425) and (PM10 <= 604):
        lowPM10 = 425
        highPM10 = 604
    return lowPM10, highPM10

def low_high_finderNO2(NO2):
    if (NO2 >= 0) and (NO2 <= 53):
        lowNO2 = 0
        highNO2 = 53
    elif (NO2 >= 54) and (NO2 <= 100):
        lowNO2 = 54
        highNO2 = 100
    elif (NO2 >= 101) and (NO2 <= 360):
        lowNO2 = 101
        highNO2 = 360
    elif (NO2 >= 361) and (NO2 <= 649):
        lowNO2 = 361
        highNO2 = 649
    elif (NO2 >= 650) and (NO2 <= 1249):
        lowNO2 = 650
        highNO2 = 1249
    elif (NO2 >= 1250) and (NO2 <= 2049):
        lowNO2 = 1250
        highNO2 = 2049
    return lowNO2, highNO2

def low_high_finderSO2(SO2):
    if (SO2 >= 0) and (SO2 <= 35):
        lowSO2 = 0
        highSO2 = 35
    elif (SO2 >= 36) and (SO2 <= 75):
        lowSO2 = 36
        highSO2 = 75
    elif (SO2 >= 76) and (SO2 <= 185):
        lowSO2 = 76
        highSO2 = 185
    elif (SO2 >= 186) and (SO2 <= 304):
        lowSO2 = 186
        highSO2 = 304
    elif (SO2 >= 305) and (SO2 <= 604):
        lowSO2 = 305
        highSO2 = 604
    elif (SO2 >= 605) and (SO2 <= 1004):
        lowSO2 = 605
        highSO2 = 1004
    return lowSO2, highSO2

def low_high_finderCO2(CO2):
    if (CO2 >= 0) and (CO2 <= 4.4):
        lowCO2 = 0
        highCO2 = 4.4
    elif (CO2 >= 4.5) and (CO2 <= 9.4):
        lowCO2 = 4.5
        highCO2 = 9.4
    elif (CO2 >= 9.5) and (CO2 <= 12.4):
        lowCO2 = 9.5
        highCO2 = 12.4
    elif (CO2 >= 12.5) and (CO2 <= 15.4):
        lowCO2 = 12.5
        highCO2 = 15.4
    elif (CO2 >= 15.5) and (CO2 <= 30.4):
        lowCO2 = 15.5
        highCO2 = 30.4
    elif (CO2 >= 30.5) and (CO2 <= 50.4):
        lowCO2 = 30.5
        highCO2 = 50.4
    return lowCO2, highCO2