from math import floor

def compareTimes(player1: str, player2: str) -> list:
    time1 = timeToFloat(player1)
    time2 = timeToFloat(player2)
    
    if time1 > time2:
        return [player2, player1]
    if time1 < time2:
        return [player1, player2]
    # if the two times are equal, return in current order
    return [player1, player2]

def addTimes(player1: str, player2: str):
    return floatToTime(timeToFloat(player1) + timeToFloat(player2))

def subTimes(player1: str, player2: str):
    return floatToTime(timeToFloat(player1) - timeToFloat(player2))

def multTimes(player1: str, player2: str):
    return floatToTime(timeToFloat(player1) * timeToFloat(player2))

def divTimes(player1: str, player2: str):
    return floatToTime(timeToFloat(player1) / timeToFloat(player2))

def multTimes(player1: str, player2: str):
    return floatToTime(timeToFloat(player1) * timeToFloat(player2))

def modTimes(player1: str, player2: str):
    return floatToTime(timeToFloat(player1) % timeToFloat(player2))

def timeToFloat(player1: str):
    total = 0
    time1 = player1.split(":")
    time1 = [float(i) for i in time1]
    total += time1.pop()
    if time1:
        total += time1.pop() * 60 # seconds -> minutes
    if time1:
        total += time1.pop() * 60 * 60 # minutes -> hours
    if time1:
        total += time1.pop() * 60 * 60 * 24 # hours -> days
    return total

def floatToTime(num: float):
    timer = ""
    measures = [24, 60, 60, 1]
    factor = 1

    for measure in measures:
        factor *= measure
    for measure in measures:
        if floor(num/factor) < 10:
            timer += "0"
        timer += str(floor(num/factor))
        if factor != 1:
            timer += ":"
        if num >= factor:
            num %= measure
        factor /= measure
    return timer

if __name__ == "__main__":
    print(floatToTime(61))
    print(timeToFloat("01:01"))
    print(compareTimes("20:05", "15:19"))
    print(subTimes("40:41", "19:02"))

