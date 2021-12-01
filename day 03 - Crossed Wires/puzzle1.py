import os 

def calculateCoordenatesWirePath(wirePath) -> dict:

    coordenates = dict()

    coordX = 0
    coordY = 0
    count = 0
    
    for indication in wirePath:

        indicationDistance = int(indication[1:len(indication)])
        count = 0
        
        if indication[0] == 'U':    # Up
            while count < indicationDistance:
                coordY += 1
                coordenates[str(coordX) + ',' + str(coordY)] = True
                count += 1
        elif indication[0] == 'D':  # Down
            while count < indicationDistance:
                coordY -= 1
                coordenates[str(coordX) + ',' + str(coordY)] = True
                count += 1
        elif indication[0] == 'L':  # Left
            while count < indicationDistance:
                coordX -= 1
                coordenates[str(coordX) + ',' + str(coordY)] = True
                count += 1
        elif indication[0] == 'R':  # Right
            while count < indicationDistance:
                coordX += 1
                coordenates[str(coordX) + ',' + str(coordY)] = True
                count += 1

    return coordenates
    



# Change cwd to work in vscode
cwdPartsList = os.getcwd().split('\\')

if cwdPartsList[(cwdPartsList.__len__() - 1)] != 'day 03 - Crossed Wires':
    # set the cwd to 'day 03 - Crossed Wires'
    os.chdir('day 03 - Crossed Wires')

# -----------------------------------

file = open('input.txt', 'r')
wiresPathList = file.readlines()
file.close()


# Calculate coordenates of the wire's path in the grid
coordenatesWire1 = calculateCoordenatesWirePath(wiresPathList[0].split(','))
coordenatesWire2 = calculateCoordenatesWirePath(wiresPathList[1].split(','))


# Calculate intersection points
intersectionPoints = list()

for coord1 in coordenatesWire1:
    if coordenatesWire2.get(coord1, False):
        intersectionPoints.append(coord1)


# Calculate minimum  Manhattan distance
minimumDistance = 0
distance = 0
coordList = None
coordX = 0
coordY = 0
for intersection in intersectionPoints:

    coordList = intersection.split(',')
    coordX = abs(int(coordList[0]))
    coordY = abs(int(coordList[1]))
    distance = coordX + coordY

    if minimumDistance == 0 or distance < minimumDistance:
        minimumDistance = distance

    
print('Distance: ' + str(minimumDistance))