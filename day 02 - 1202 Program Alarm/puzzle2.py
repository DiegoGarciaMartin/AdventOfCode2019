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


found = False

for noun in range(0, len(listProgramIntcodes)):
    for verb in range(0, len(listProgramIntcodes)):

        listProgramIntcodesAux = listProgramIntcodes.copy()

        listProgramIntcodesAux[1] = noun
        listProgramIntcodesAux[2] = verb

        try:
            for x in range(0, len(listProgramIntcodesAux), 4):

                opcode = listProgramIntcodes[x]

                if opcode == '99':
                    break

                value1 = int(listProgramIntcodesAux[int(listProgramIntcodesAux[x+1])])
                value2 = int(listProgramIntcodesAux[int(listProgramIntcodesAux[x+2])])
                result = 0

                if (opcode == '1'):
                    result = value1 + value2
                elif (opcode == '2'):
                    result = value1 * value2

                listProgramIntcodesAux[int(listProgramIntcodesAux[x+3])] = result
        except:
            pass
        
        if (int(listProgramIntcodesAux[0]) == 19690720):
            found = True
            listProgramIntcodes[1] = noun
            listProgramIntcodes[2] = verb
            break

    if found:
        break


result = 100 * int(listProgramIntcodes[1]) + int(listProgramIntcodes[2])

print('Result: ' + str(result))