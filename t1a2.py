f = open('testPassage.txt','r')
text = f.read()
f.close()
punctuation = ['\n','.',',','/','?','!','\"','\'',':',';']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
wordList = text.split(' ')
for y in punctuation:
    wordList = [item.strip(y) for item in wordList]
wordList = [item.lower() for item in wordList]
noOfWords = len(wordList) #
totalCharacters = 0
for x in wordList:
    totalCharacters += len(x)
averageLength = totalCharacters / noOfWords #
wordCount = {} #
for x in wordList:
    if x in wordCount:
        wordCount[x] += 1
    else:
        wordCount[x] = 1
letterCount = {} #
for l in alphabet:
    letterCount[l] = 0
for x in wordList:
    l = x[0]
    if l in alphabet:
        letterCount[l] += 1
print(f"The number of words in this passage is {noOfWords}")
print(f"The average number of characters per word is {averageLength}")
print('Here are the counts for each word in this passage:\n')
print(wordCount)
print('\n')
print('Here are the counts for the number of words starting with each letter of the alphabet:\n')
print(letterCount)
