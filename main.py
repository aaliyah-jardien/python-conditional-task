speed = int(input("Enter speed here in kilometres: "))
current = float(input("Please enter your average speed in km/h: "))
points = (speed - current)/5

if speed < 60:
    print("OK")
elif speed == 60:
    print("OK")

if points > 12:
    print("demerit: " + str(points))
else:
    print("Time to go to jail!")


