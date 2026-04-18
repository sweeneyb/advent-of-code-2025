import string

class Solution:
    letters = {}

    def __init__(self):
        for l in string.ascii_lowercase:
            self.letters[l] = 0

    def push(self, magazine: str):
        for i in magazine:
            self.letters[i] += 1

    def dequeue(self, ransomNote: str) -> bool:
        for i in ransomNote:
            letter = self.letters[i]
            if letter == 0:
                return False
            else:
                self.letters[i] -= 1
        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        self.push(magazine)
        if ( self.dequeue(ransomNote) ):
            return True
        else:
            return False

if __name__ == "__main__":
    print("hello")