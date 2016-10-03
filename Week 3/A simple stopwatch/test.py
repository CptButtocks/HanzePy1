from stop_watch import StopWatch
size = 1000000
stopWatch = StopWatch()
sum = 0
for i in range(1, size + 1):
    sum += i
stopWatch.stop()
print("The loop time is", stopWatch.get_elapsed_time(), "milliseconds")
