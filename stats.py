def wordcount (howManyWords):
    totalWords = 0
    for count in howManyWords.split():
        totalWords += 1
    #print(f"{totalWords} words found in the document")
    return totalWords

def charactercount (howManyEach):
    characterDictionary = {}
    characters = list(howManyEach.lower())
    for char in characters:
        if char in characterDictionary:
            characterDictionary[char] += 1
        else:
            characterDictionary[char] = 1
    #print(characterDictionary)
    return characterDictionary

def sortTheDictionary (dirtSort):
    sorted_list = []
    for char, count in dirtSort.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
