
class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False
class WordDictionary:

    def __init__(self):
        self.root= TrieNode()    
        

    def addWord(self, word: str) -> None:
        cur=self.root
        for i in word:
            if i  not in cur.children:
                cur.children[i]=TrieNode()
            cur=cur.children[i]
        cur.word=True
                
        

    def search(self, word: str) -> bool:
        def dfs(node, word, index):
            if index == len(word):
                return node.word  # End of word, check if it's a valid word
                
            char = word[index]
            
            if char == '.':
                # Check all children if the character is '.'
                for child in node.children.values():
                    if dfs(child, word, index + 1):
                        return True
                return False
            else:
                # Proceed normally if it's a letter
                if char not in node.children:
                    return False
                return dfs(node.children[char], word, index + 1)

        # Start the DFS from the root of the Trie
        return dfs(self.root, word, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
