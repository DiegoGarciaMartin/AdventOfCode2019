MIN_VALUE = 359282
MAX_VALUE = 820401


def checkPasswordConditions(password) -> bool:
    """
    Checks if the password indicated meet the criterian settle
    """

    # Check the value is within the range given
    if password < MIN_VALUE or password > MAX_VALUE:
        return False

    # Check the digits never decrease
    strPassword = str(password)

    for index in range(len(strPassword) - 1):
        if int(strPassword[index]) > int(strPassword[index + 1]):
            return False

    # Check two adjacent digits are the same
    countMatchingDigits = 1
    for index in range(len(strPassword) - 1):
        if int(strPassword[index]) == int(strPassword[index + 1]):
            countMatchingDigits += 1
        elif countMatchingDigits == 2:
            return True
        else:
            countMatchingDigits = 1
    
    # if the 2 digits adjacent are in last positions
    if countMatchingDigits == 2:
        return True
    
    return False


def main():
    """
    Main function
    """

    allValuesRangeList = [n for n in range(MIN_VALUE, MAX_VALUE + 1)]
    possibleValuesList = [n for n in allValuesRangeList if checkPasswordConditions(n)]

    print('Result: ' + str(len(possibleValuesList)))


if __name__ == "__main__":
    main()