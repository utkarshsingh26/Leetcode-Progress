from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        
        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            word, counter = queue.popleft()

            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + char + word[i+1:]

                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((newWord, counter+1))
                    
                    if newWord == endWord:
                        return counter+1
            
        return 0