import re

#wordCount = 0

def firstOccurIndex(strArrSource, strDest):
    for index in range(0, len(strArrSource)):
        m = re.search("[%s]" % strArrSource[index], strDest, re.DOTALL)
        #print (m.start().)
        return m.start()

def segVowelCons(string):
    lenStr = len(string)
    strArrVowel = []
    strArrCons = []

    for index in range(0, lenStr):
        c = string[index]
        if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
            if c not in  strArrVowel:
                strArrVowel.extend(c) 
        else:
            if c not in  strArrCons:
                strArrCons.extend(c)

    return strArrVowel, strArrCons

def segString(indexStart, inString):
    wordCount = 0
    
    for count1 in range(indexStart+1, (len(inString)+1)):
        letter = inString[indexStart:count1]
        wordRepeat = 0
        if letter in inString:
            wordRepeat = occurCount(letter, inString)
            #print("letter,wordRepeat",letter,wordRepeat)
            #print ("wordCnt before", wordCount)
            wordCount = wordCount + wordRepeat
            #print("wordCount after", wordCount)
    return wordCount

def occurCount(letter, string):
    return string.count(letter)

def minion_game(string):
    #Test string
    #string = "bbbbbbbbssssssss"
    kevin = 0
    stuart = 0

    # Segregate vowels and Consonants
    strArrVowel, strArrCons = segVowelCons(string)
    #print ("strArrVowel", "strArrCons", strArrVowel, strArrCons)

    # Set the output of Kevin/Stuart to zero if there is no occurance of vowel/consonant.     
    if strArrVowel != []:
        vowelLen = len(strArrVowel)
        #print("Vowel count:",vowelLen)
    else:
        #There is no vowel in the given string hence Kevin cannot frame any word
        vowelLen = 0
        kevin = 0

    if strArrCons != []:
        consLen = len(strArrCons)
        #print("Cons count:",consLen)
    else:
        #There is no vowel in the given string hence Stuart cannot frame any word
        consLen = 0
        stuart = 0

    if vowelLen != 0:
        #Identify first occurance of a char in the string
        for occurPos in range (0, len(strArrVowel)):
            indexVowel = firstOccurIndex(strArrVowel[occurPos], string)
            kevinPart = segString(indexVowel, string) 
            kevin += kevinPart
            #print("Kevin",kevin)
 
    if consLen != 0:
        for occurPos in range (0, len(strArrCons)):
            indexCons = firstOccurIndex(strArrCons[occurPos], string)
            stuartPart = segString(indexCons, string)
            stuart += stuartPart
            #print("Stuart", stuart)

    #Decide winner based on score
    if kevin > stuart:
        print("Kevin",kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    elif kevin == stuart:
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)