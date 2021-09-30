def aqi_pollutant_calc(aqiHigh, aqiLow, pollutHigh, pollutLow, pollut):
     aqi = (aqiHigh - aqiLow) / (pollutHigh - pollutLow) * (pollut - pollutLow) + aqiLow
     return aqi

def low_high_finderPM2(PM2):
    if (PM2 >= 0) and (PM2 <= 12.0):
        lowPM2 = 0
        highPM2 = 12.0
        lowAQI = 0
        highAQI = 50
    elif (PM2 >= 12.1) and (PM2 <= 35.4):
        lowPM2 = 12.1
        highPM2 = 35.4
        lowAQI = 51
        highAQI = 100
    elif (PM2 >= 35.5) and (PM2 <= 55.4):
        lowPM2 = 35.5
        highPM2 = 55.4
        lowAQI = 101
        highAQI = 150
    elif (PM2 >= 55.5) and (PM2 <= 150.4):
        lowPM2 = 55.5
        highPM2 = 150.4
        lowAQI = 151
        highAQI = 200
    elif (PM2 >= 150.5) and (PM2 <= 250.4):
        lowPM2 = 150.5
        highPM2 = 250.4
        lowAQI = 201
        highAQI = 300
    elif (PM2 >= 250.5) and (PM2 <= 500.4):
        lowPM2 = 250.5
        highPM2 = 500.4
        lowAQI = 301
        highAQI = 500
    return lowPM2, highPM2, lowAQI, highAQI

def low_high_finderPM10(PM10):
    if (PM10 >= 0) and (PM10 <= 54):
        lowPM10 = 0
        highPM10 = 54
        lowAQI = 0
        highAQI = 50
    elif (PM10 >= 55) and (PM10 <= 154):
        lowPM10 = 55
        highPM10 = 154
        lowAQI = 51
        highAQI = 100
    elif (PM10 >= 155) and (PM10 <= 254):
        lowPM10 = 155
        highPM10 = 254
        lowAQI = 101
        highAQI = 150
    elif (PM10 >= 255) and (PM10 <= 354):
        lowPM10 = 255
        highPM10 = 354
        lowAQI = 151
        highAQI = 200
    elif (PM10 >= 355) and (PM10 <= 424):
        lowPM10 = 355
        highPM10 = 424
        lowAQI = 201
        highAQI = 300
    elif (PM10 >= 425) and (PM10 <= 604):
        lowPM10 = 425
        highPM10 = 604
        lowAQI = 301
        highAQI = 500
    return lowPM10, highPM10, lowAQI, highAQI

def low_high_finderNO2(NO2):
    if (NO2 >= 0) and (NO2 <= 53):
        lowNO2 = 0
        highNO2 = 53
        lowAQI = 0
        highAQI = 50
    elif (NO2 >= 54) and (NO2 <= 100):
        lowNO2 = 54
        highNO2 = 100
        lowAQI = 51
        highAQI = 100
    elif (NO2 >= 101) and (NO2 <= 360):
        lowNO2 = 101
        highNO2 = 360
        lowAQI = 101
        highAQI = 150
    elif (NO2 >= 361) and (NO2 <= 649):
        lowNO2 = 361
        highNO2 = 649
        lowAQI = 151
        highAQI = 200
    elif (NO2 >= 650) and (NO2 <= 1249):
        lowNO2 = 650
        highNO2 = 1249
        lowAQI = 201
        highAQI = 300
    elif (NO2 >= 1250) and (NO2 <= 2049):
        lowNO2 = 1250
        highNO2 = 2049
        lowAQI = 301
        highAQI = 500
    return lowNO2, highNO2, lowAQI, highAQI

def low_high_finderSO2(SO2):
    if (SO2 >= 0) and (SO2 <= 35):
        lowSO2 = 0
        highSO2 = 35
        lowAQI = 0
        highAQI = 50
    elif (SO2 >= 36) and (SO2 <= 75):
        lowSO2 = 36
        highSO2 = 75
        lowAQI = 51
        highAQI = 100
    elif (SO2 >= 76) and (SO2 <= 185):
        lowSO2 = 76
        highSO2 = 185
        lowAQI = 101
        highAQI = 150
    elif (SO2 >= 186) and (SO2 <= 304):
        lowSO2 = 186
        highSO2 = 304
        lowAQI = 151
        highAQI = 200
    elif (SO2 >= 305) and (SO2 <= 604):
        lowSO2 = 305
        highSO2 = 604
        lowAQI = 201
        highAQI = 300
    elif (SO2 >= 605) and (SO2 <= 1004):
        lowSO2 = 605
        highSO2 = 1004
        lowAQI = 301
        highAQI = 500
    return lowSO2, highSO2, lowAQI, highAQI

def low_high_finderCO2(CO2):
    if (CO2 >= 0) and (CO2 <= 4.4):
        lowCO2 = 0
        highCO2 = 4.4
        lowAQI = 0
        highAQI = 50
    elif (CO2 >= 4.5) and (CO2 <= 9.4):
        lowCO2 = 4.5
        highCO2 = 9.4
        lowAQI = 51
        highAQI = 100
    elif (CO2 >= 9.5) and (CO2 <= 12.4):
        lowCO2 = 9.5
        highCO2 = 12.4
        lowAQI = 101
        highAQI = 150
    elif (CO2 >= 12.5) and (CO2 <= 15.4):
        lowCO2 = 12.5
        highCO2 = 15.4
        lowAQI = 151
        highAQI = 200
    elif (CO2 >= 15.5) and (CO2 <= 30.4):
        lowCO2 = 15.5
        highCO2 = 30.4
        lowAQI = 201
        highAQI = 300
    elif (CO2 >= 30.5) and (CO2 <= 50.4):
        lowCO2 = 30.5
        highCO2 = 50.4
        lowAQI = 301
        highAQI = 500
    return lowCO2, highCO2, lowAQI, highAQI

def categorizeAQI(inputAQI):
    if inputAQI >= 0 and inputAQI <= 50:
        finalCat = "Good"
    if inputAQI >= 51 and inputAQI <= 100:
        finalCat = "Moderate"
    if inputAQI >= 101 and inputAQI <= 150:
        finalCat = "Unhealthy for Sensitive Groups"
    if inputAQI >= 151 and inputAQI <= 200:
        finalCat = "Unhealthy"
    if inputAQI >= 201 and inputAQI <= 300:
        finalCat = "Very Unhealthy"
    if inputAQI >= 301 and inputAQI <= 500:
        finalCat = "Hazardous"
    return finalCat

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

lowerPM2, higherPM2, lowAQIPM2, highAQIPM2 = low_high_finderPM2(pollutPM2)
lowerPM10, higherPM10, lowAQIPM10, highAQIPM10 = low_high_finderPM10(pollutPM10)
lowerNO2, higherNO2, lowAQINO2, highAQINO2 = low_high_finderNO2(pollutNO2)
lowerSO2, higherSO2, lowAQISO2, highAQISO2 = low_high_finderSO2(pollutSO2)
lowerCO, higherCO, lowAQICO, highAQICO = low_high_finderCO2(pollutCO)

aqiPM2 = round(aqi_pollutant_calc(highAQIPM2, lowAQIPM2, higherPM2, lowerPM2, pollutPM2))
aqiPM10 = round(aqi_pollutant_calc(highAQIPM10, lowAQIPM10, higherPM10, lowerPM10, pollutPM10))
aqiNO2 = round(aqi_pollutant_calc(highAQINO2, lowAQINO2, higherNO2, lowerNO2, pollutNO2))
aqiSO2 = round(aqi_pollutant_calc(highAQISO2, lowAQISO2, higherSO2, lowerSO2, pollutSO2))
aqiCO = round(aqi_pollutant_calc(highAQICO, lowAQICO, higherCO, lowerCO, pollutCO))

print()
print("Location:", locationName)
print()
print("PM2 AQI:", aqiPM2, "*" + categorizeAQI(aqiPM2) + "*")
print("PM10 AQI:", aqiPM10, "*" + categorizeAQI(aqiPM10) + "*")
print("NO2 AQI:", aqiNO2, "*" + categorizeAQI(aqiNO2) + "*")
print("SO2 AQI:", aqiSO2, "*" + categorizeAQI(aqiSO2) + "*")
print("CO AQI:", aqiCO, "*" + categorizeAQI(aqiCO) + "*")
print()

finalAQI = round((aqiPM2 + aqiPM10 + aqiNO2 + aqiSO2 + aqiCO) / 5)
print("Average AQI:", finalAQI, "*" + categorizeAQI(finalAQI) + "*")
print()