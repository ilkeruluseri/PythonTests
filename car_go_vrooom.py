import time
track_length = int(input("Track length: "))
for i in range(track_length):
    print((track_length - i) * " " + "🏎")
    print("-" * track_length)
    time.sleep(0.1)
