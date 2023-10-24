# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word 
    
    def isAnagram(self, wordToCheck):
       wordList = list(self.word)
       wordToCheckList = list(wordToCheck)
       
       wordList.sort()
       wordToCheckList.sort()
       
       for i in range(len(wordList)):
           if wordList[i] != wordToCheckList[i]:
               return False
       return True
    
    def match(self, words):
        """"Return a list of matches that are anagrams"""
        result = []
        
        for check in words:
            if self.isAnagram(check):
                result.append(check)
        
        return result