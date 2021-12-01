import os 

def calculateCoordenatesWirePath(wirePath) -> dict:

    coordenates = dict()

    coordX = 0
    coordY = 0
    step = 0
    count = 0
    
    for indication in wirePath:

        indicationDistance = int(indication[1:len(indication)])
        count = 0
        
        if indication[0] == 'U':    # Up
            while count < indicationDistance:
                coordY += 1
                step += 1
                coord = str(coordX) + ',' + str(coordY)
                if coordenates.get(coord, -1) == -1:
                    coordenates[coord] = step
                count += 1
        elif indication[0] == 'D':  # Down
            while count < indicationDistance:
                coordY -= 1
                step += 1
                coord = str(coordX) + ',' + str(coordY)
                if coordenates.get(coord, -1) == -1:
                    coordenates[coord] = step
                count += 1
        elif indication[0] == 'L':  # Left
            while count < indicationDistance:
                coordX -= 1
                step += 1
                coord = str(coordX) + ',' + str(coordY)
                if coordenates.get(coord, -1) == -1:
                    coordenates[coord] = step
                count += 1
        elif indication[0] == 'R':  # Right
            while count < indicationDistance:
                coordX += 1
                step += 1
                coord = str(coordX) + ',' + str(coordY)
                if coordenates.get(coord, -1) == -1:
                    coordenates[coord] = step
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
    if coordenatesWire2.get(coord1, -1) != -1:
        intersectionPoints.append(coord1)


# Calculate minimum  Manhattan distance
minimumDistance = 0
distance = 0
stepsWire1 = 0
stepsWire2 = 0
for intersection in intersectionPoints:

    stepsWire1 = coordenatesWire1.get(intersection, 0)
    stepsWire2 = coordenatesWire2.get(intersection, 0)
    distance = stepsWire1 + stepsWire2

    if minimumDistance == 0 or distance < minimumDistance:
        minimumDistance = distance

    
print('Distance: ' + str(minimumDistance))