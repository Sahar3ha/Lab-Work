#
Distance = 4
bus_speed = 25/60    #converted mph to mpm(miles per minute) -> 0.41 mpm
wait_time = 2
bus_stops = 10
waiting = wait_time * bus_stops #20

bus_time = Distance / bus_speed 
bus_totaltime = bus_time + waiting

speed1 = 7/60       #converted mph to mpm(miles per minute)
speed2 = 15/60
time_7mpm = speed1*2
time_15mpm = speed2*2
jog_totaltime = time_7mpm + time_15mpm

if bus_totaltime>jog_totaltime:
    print(f"Bus will be Faster than Jogging.")
elif bus_totaltime<jog_totaltime:
    print(f"Jogging will be Faster than Travelling by Bus.")
else:
    print(f"Both Jogging and Travelling by Bus take same time.")