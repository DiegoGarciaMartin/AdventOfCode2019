import os 

# Change cwd to work in vscode
cwdPartsList = os.getcwd().split('\\')

if cwdPartsList[(cwdPartsList.__len__() - 1)] != 'day 02 - 1202 Program Alarm':
    # set the cwd to 'day 02 - 1202 Program Alarm'
    os.chdir('day 02 - 1202 Program Alarm')

# -----------------------------------

file = open('input.txt', 'r')
programIntcodeStr = file.read()
file.close()

listProgramIntcodes = programIntcodeStr.split(',')

listProgramIntcodes[1] = 12
listProgramIntcodes[2] = 2

for x in range(0, len(listProgramIntcodes), 4):

    opcode = listProgramIntcodes[x]

    if opcode == '99':
        break

    value1 = int(listProgramIntcodes[int(listProgramIntcodes[x+1])])
    value2 = int(listProgramIntcodes[int(listProgramIntcodes[x+2])])
    result = 0

    if (opcode == '1'):
        result = value1 + value2
    elif (opcode == '2'):
        result = value1 * value2

    listProgramIntcodes[int(listProgramIntcodes[x+3])] = result
    
print('Result: ' + str(listProgramIntcodes[0]))