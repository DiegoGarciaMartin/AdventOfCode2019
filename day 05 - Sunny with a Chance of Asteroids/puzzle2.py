import os 

def main():
    """
    Main function
    """

    # Change cwd to work in vscode
    cwdPartsList = os.getcwd().split('\\')

    if cwdPartsList[(cwdPartsList.__len__() - 1)] != 'day 05 - Sunny with a Chance of Asteroids':
        # set the cwd to 'day 05 - Sunny with a Chance of Asteroids'
        os.chdir('day 05 - Sunny with a Chance of Asteroids')

    # -----------------------------------

    file = open('input.txt', 'r')
    programIntcodeStr = file.read()
    file.close()

    listProgramIntcodes = programIntcodeStr.split(',')
        
    input = 5
    output = None

    instruction = None
    value1 = None
    value2 = None
    pointerInstruction = 0

    while True:

        instruction = str(listProgramIntcodes[pointerInstruction])
        
        if instruction == '99':
            break

        instruction = instruction.zfill(5)
        
        # OpCode 1 or 2
        if instruction[4] == '1' or instruction[4] == '2': 

            if instruction[2] == '0':
                value1 = int(listProgramIntcodes[int(listProgramIntcodes[pointerInstruction+1])])
            else:
                value1 = int(listProgramIntcodes[pointerInstruction+1])

            if instruction[1] == '0':
                value2 = int(listProgramIntcodes[int(listProgramIntcodes[pointerInstruction+2])])
            else:
                value2 = int(listProgramIntcodes[pointerInstruction+2])

            result = 0
            if instruction[4] == '1':
                result = value1 + value2
            elif instruction[4] == '2':
                result = value1 * value2

            listProgramIntcodes[int(listProgramIntcodes[pointerInstruction+3])] = result

            pointerInstruction += 4

        # OpCode 3
        elif  instruction[4] == '3':
            listProgramIntcodes[int(listProgramIntcodes[pointerInstruction + 1])] = input
            pointerInstruction += 2

        # OpCode 4
        elif  instruction[4] == '4':
            output = listProgramIntcodes[int(listProgramIntcodes[pointerInstruction + 1])]
            pointerInstruction += 2     

        # OpCode 5 or 6
        elif  instruction[4] == '5' or instruction[4] == '6': 

            if instruction[2] == '0':
                value1 = int(listProgramIntcodes[int(listProgramIntcodes[pointerInstruction+1])])
            else:
                value1 = int(listProgramIntcodes[pointerInstruction+1])

            if instruction[1] == '0':
                value2 = int(listProgramIntcodes[int(listProgramIntcodes[pointerInstruction+2])])
            else:
                value2 = int(listProgramIntcodes[pointerInstruction+2])

            if (instruction[4] == '5' and value1 != 0) or (instruction[4] == '6' and value1 == 0):
                pointerInstruction = value2
            else:
                pointerInstruction += 3

        # OpCode 7 or 8
        elif  instruction[4] == '7' or instruction[4] == '8': 

            if instruction[2] == '0':
                value1 = int(listProgramIntcodes[int(listProgramIntcodes[pointerInstruction+1])])
            else:
                value1 = int(listProgramIntcodes[pointerInstruction+1])

            if instruction[1] == '0':
                value2 = int(listProgramIntcodes[int(listProgramIntcodes[pointerInstruction+2])])
            else:
                value2 = int(listProgramIntcodes[pointerInstruction+2])

            if (instruction[4] == '7' and value1 < value2) or (instruction[4] == '8' and value1 == value2):
                listProgramIntcodes[int(listProgramIntcodes[pointerInstruction + 3])] = 1
            else:
                listProgramIntcodes[int(listProgramIntcodes[pointerInstruction + 3])] = 0

            pointerInstruction += 4

    
    print('Result: ' + str(output))


if __name__ == "__main__":
    main()