heart_rate = [ [ 72, 75, 71, 73], [ 91, 90, 94, 93], [ 130, 135, 139, 142], [ 120, 118, 110, 105, 100, 98]]

def calculate_average_heart_rates(heartRates):
    avgHeartRate = []
    for rates in heartRates:
        sum = 0
        for rate in rates:
            sum = sum + rate
        average = sum / len(rates)
        avgHeartRate.append(average)
    return avgHeartRate

print(calculate_average_heart_rates(heart_rate))
print()