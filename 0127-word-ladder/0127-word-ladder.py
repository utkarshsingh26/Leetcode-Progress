from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        
        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            word, steps = queue.popleft()

            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + char + word[i+1:]

                    if new_word == endWord:
                        return steps + 1
                    
                    if new_word in wordSet:
                        wordSet.remove(new_word)
                        new_steps = steps + 1
                        queue.append((new_word, new_steps))
                
        
        return 0
        
