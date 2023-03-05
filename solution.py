def getMinimumOperationsForStrongPassword(s):

    nrOfMissingCharacters = 0
    
    if not any(c.islower() for c in s):
        nrOfMissingCharacters += 1
    if not any(c.isupper() for c in s):
        nrOfMissingCharacters += 1
    if not any(c.isdigit() for c in s):
        nrOfMissingCharacters += 1
    
    nrOfThreeRepeating = 0 # number of three repeating characters in a row
    secvSize = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            secvSize+=1
        else:
            
            nrOfThreeRepeating+=secvSize//3 # number of three repeating characters in a row from all repeating characters
            secvSize = 1
            
    nrOfThreeRepeating+=secvSize//3 # the final repeating characters in a row
            
    nrOfOperations = max(nrOfMissingCharacters, nrOfThreeRepeating)
    sizeDifference = max(0, 6 - len(s))  # minimum length is 6
    sizeDifference = max(sizeDifference, len(s) - 20)  # maximum length is 20
    nrOfOperations = max(nrOfOperations, sizeDifference)
    
    return nrOfOperations


def main():
    
    s = input("password: ")
    print(getMinimumOperationsForStrongPassword(s))
    
main()