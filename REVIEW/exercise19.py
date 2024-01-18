areas_floor = ["Dining Room", 10.15, "Hallway", 9.56, "Room 1",
               12.34, "Terrace", 15.55, "Toilet", 7.98, "Kitchen",
               12, "Room 2", 12.23]

print(f" The second item (AREA of Dining Room) is : {areas_floor[1]} ")

print(f" The last item (AREA of Room2) is : {areas_floor[-1]} ")

print(f" The AREA of terrace is : {areas_floor[7]} ")

print(f" The items from 1st to 3rd are  : {areas_floor[0:3]} ")

print(f" The items from 3rd to last are  : {areas_floor[3:]} ")

totalArea = areas_floor[5] + areas_floor[13]

print(f" The total are of Room 1 and Room 2 is : {totalArea} ")

modifiedToiletArea = 10.56
areas_floor[9] = modifiedToiletArea

print(f" The new list of area is : {areas_floor} ")