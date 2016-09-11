valid = 4388576018410707;
invalid = 4388576018402626

def checkNumber(number):
    numberString = str(number)[::-1];
    evenNumberString = "";
    oddNumberString = "";
    count = 0;
    for number in numberString:
        if count % 2 == 0:
            evenNumberString = evenNumberString + number;
            count = count + 1;
        else:
            oddNumberString = oddNumberString + number;
            count = count + 1;

    oddNumberResult = 0;
    for number in oddNumberString:
        oddNumberResult = oddNumberResult + int(number);

    evenNumberResult = 0;

    for number in evenNumberString:
        evenNumberTemp = 0;
        evenNumberTemp = int(number) * 2;

        if len(str(evenNumberTemp)) == 2:
            tempstring = str(evenNumberTemp);
            evenNumberTemp = int(tempstring[0]) + int(tempstring[1]);

        evenNumberResult = evenNumberResult + evenNumberTemp;

    result = evenNumberResult + oddNumberResult;

    if result % 10 == 0:
        return True
    else:
        return False;


print(checkNumber(valid));
print(checkNumber(invalid));