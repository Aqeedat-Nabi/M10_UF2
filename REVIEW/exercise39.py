n = int(input("Enter the height of the triangle (positive integer): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")
