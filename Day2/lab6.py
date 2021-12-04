#
total_distance=4 #in miles
bus_speed=25 #25miles per hour
total_stops=10
time_waste=total_stops*2 #2 minutes at each stops
time_per_mile=(1/25)*60

total_time_covered=(time_per_mile*total_distance)+time_waste

#time taken on foot


time_taken_for_2_miles_at_7mph= (1/7)*60 #in minutes
time_taken_for_2_miles_at_15mph= (1/15)*60 #in minutes
time_covered_by_foot = time_taken_for_2_miles_at_15mph + time_taken_for_2_miles_at_7mph
if (total_time_covered<time_covered_by_foot):
    print(f"Bus is faster")
else:
    print(f"By foot is faster")