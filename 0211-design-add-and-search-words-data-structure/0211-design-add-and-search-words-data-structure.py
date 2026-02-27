class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        
        curr.end_of_word = True

    def search(self, word: str) -> bool:

        def dfs(index, node):
            if index == len(word):
                return node.end_of_word
            
            ch = word[index]

            if ch == '.':
                for child in node.children.values():
                    if dfs(index+1, child):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                node = node.children[ch]

                return dfs(index+1, node)
                    
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)