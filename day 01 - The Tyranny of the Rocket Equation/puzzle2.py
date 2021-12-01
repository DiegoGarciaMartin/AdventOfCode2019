import os 

def calculateFuelRequiredByFuel(fuel):
    fuelRequired = int(int(fuel)/3) - 2

    if (fuelRequired <= 0):
         return 0
    else:
        return fuelRequired + calculateFuelRequiredByFuel(fuelRequired)



# Change cwd to work in vscode
cwdPartsList = os.getcwd().split('\\')

if cwdPartsList[(cwdPartsList.__len__() - 1)] != 'day 01 - The Tyranny of the Rocket Equation':
    # set the cwd to 'day 01 - The Tyranny of the Rocket Equation'
    os.chdir('day 01 - The Tyranny of the Rocket Equation')

# -----------------------------------

file = open('input2.txt', 'r')
listModulesMasses = file.readlines()
file.close()

totalFuelRequired = 0

for mass in listModulesMasses:
    fuelRequired = int(int(mass)/3) - 2
    totalFuelRequired += fuelRequired
    totalFuelRequired += calculateFuelRequiredByFuel(fuelRequired)

print('Total fuel requirement: ' + str(totalFuelRequired))