"""
Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.
"""
def findWordsContaining(self, words, x):
        l=[]
        for i in range(len(words)):
            if x in words[i]:
                l.append(i)
        return l
