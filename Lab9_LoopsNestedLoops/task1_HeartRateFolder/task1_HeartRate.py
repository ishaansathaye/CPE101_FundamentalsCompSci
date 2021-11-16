heart_rate = [[ 72, 75, 71, 73], [ 91, 90, 94, 93], [ 130, 135, 139, 142], [ 120, 118, 110, 105, 100, 98]]

def calculate_average_heart_rates(heartRates):
    avgHeartRate = []
    for rates in heartRates:
        sum = 0
        for rate in rates:
            sum = sum + rate
        average = sum / len(rates)
        avgHeartRate.append(average)
    return avgHeartRate

print()
print(calculate_average_heart_rates(heart_rate))
print()

def test_calcAverageHeartRate():
    heart_rate = [[ 72, 75, 71, 73]]
    assert calculate_average_heart_rates(heart_rate) == [72.75], "Should be 72.75"
    heart_rate = [[ 91, 90, 94, 93]]
    assert calculate_average_heart_rates(heart_rate) == [92.0], "Should be 92"
    heart_rate = [[ 130, 135, 139, 142]]
    assert calculate_average_heart_rates(heart_rate) == [136.5], "Should be 136.5"
    heart_rate = [[ 120, 118, 110, 105, 100, 98]]
    assert calculate_average_heart_rates(heart_rate) == [108.5], "Should be 108.5"

test_calcAverageHeartRate()
print("Everything Passed.")
print()