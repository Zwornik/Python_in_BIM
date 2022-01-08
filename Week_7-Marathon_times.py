# Week 7 – Python Exercises
# Marathon Times - converts start and end of run time in strings, converts them to integers,
# calculates time of a run and print it back in HH:MM:SS format.

startTime = '10:45:45'
endTime = '13:03:25'
times = [startTime, endTime]
secTimes = []
realRunTime = [] # time in HH:MM:SS format


def convertToInt(time):
    secTime = time.split(':')
    secTime = int(secTime[0]) * 3600 + int(secTime[1]) * 60 + int(secTime[2])
    return secTime

for i in range(len(times)):
    secTimes.append(convertToInt(times[i]))

runTime = secTimes[1] - secTimes[0]

hours = runTime // 3600
mins = (runTime % 3600) // 60
secs = runTime % 60

print(f'\nThe time of your run was: {hours}:{mins}:{secs}')
