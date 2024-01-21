floor_areas = ["Dining Room", 10.15, "Hallway", 9.56, "Room 1",
               12.34, "Terrace", 15.55, "Toilet", 7.98, "Kitchen",
               12, "Room 2", 12.23]

print(f"\n The second item (AREA of Dining Room) is : {floor_areas[1]} ")

print(f"\n The last item (AREA of Room2) is : {floor_areas[-1]} ")

terrace_area = floor_areas.index("Terrace")
print(f"\n The AREA of terrace is : {floor_areas[terrace_area + 1]} ")

print(f"\n The items from 1st to 3rd are  : {floor_areas[0:3]} ")

print(f"\n The items from 3rd to last are  : {floor_areas[2:]} ")

r1 = floor_areas.index("Room 1")
r2 = floor_areas.index("Room 2")
totalArea = floor_areas[r1 + 1]+ floor_areas[r2 + 1]
print(f"\n The total are of Room 1 and Room 2 is : {totalArea} ")

toilet_area = floor_areas.index("Toilet")
floor_areas[toilet_area + 1] = 10.56
print(f"\n The new list after toilet's area modification : \n{floor_areas} ")

floor_areas.extend(["Inner Patio" , 2.78])
print(f"\n The new list : \n{floor_areas}")

total_floor_area = sum(floor_areas[1::2])
print(f"\n The total are of the apartment is : {total_floor_area}")
