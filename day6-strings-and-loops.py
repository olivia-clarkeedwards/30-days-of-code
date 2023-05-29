def printEvenAndOddChars(s):
    even_string = ""
    odd_string = ""
    
    for index in range(len(s)):
        if index % 2 == 0:
            even_string += s[index]
        else:
            odd_string += s[index]

    print(f"{even_string} {odd_string}")
    

def processInput():
    numInputs = int(input())

    for _ in range(numInputs):
        str = input()

        printEvenAndOddChars(str)

processInput()