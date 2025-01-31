parking_lot = [
    [0, 0, 0, 0, 0],
    [0, 2, 1, 1, 2],
    [0, 1, 1, 2, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 2, 2, 1]
]
open_spots = 0
for row in range(len(parking_lot)):
    for col in range(len(parking_lot[row])):
        if parking_lot[row][col] == 2:
            open_spots += 1
print(f"There are {open_spots} open spots.")