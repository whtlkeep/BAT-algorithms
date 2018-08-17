"""
一、题目
    实现一个字典树or前缀树，包含insert、search和startswith功能
二、知识讲解
    参考:
        https://www.cnblogs.com/bonelee/p/8830825.html

"""


class Node():
    def __init__(self):
        self.childs = [None] * 26
        self.isLeaf = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        self.inserthelper(word, self.root)

    def inserthelper(self, word, node):
        if node == Node:
            return
        if len(word) == 0:
            node.isLeaf = True
            return
        index = ord(word[0]) - ord('a')
        if node.childs[index] is None:
            node.childs[index] = Node()
        self.inserthelper(word[1:], node.childs[index])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self.searchhepler(word, self.root)

    def searchhepler(self, word, node):
        if node is None:
            return False
        if len(word) == 0:
            return node.isLeaf
        index = ord(word[0]) - ord('a')
        return self.searchhepler(word[1:], node.childs[index])

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.startsWithhelper(prefix, self.root)

    def startsWithhelper(self, prefix, node):
        if node is None:
            return False
        if len(prefix) == 0:
            return True
        index = ord(prefix[0]) - ord('a')
        return self.startsWithhelper(prefix[1:], node.childs[index])


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))
