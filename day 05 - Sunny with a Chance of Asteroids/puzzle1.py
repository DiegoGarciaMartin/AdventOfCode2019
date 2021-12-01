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
        
    input = 1
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

        elif  instruction[4] == '3':
            listProgramIntcodes[int(listProgramIntcodes[pointerInstruction + 1])] = input
            pointerInstruction += 2

        elif  instruction[4] == '4':
            output = listProgramIntcodes[int(listProgramIntcodes[pointerInstruction + 1])]
            pointerInstruction += 2      
    
    print('Result: ' + str(output))


if __name__ == "__main__":
    main()