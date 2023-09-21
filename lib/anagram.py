class Anagram:
    def __init__(self, word):
        
        self.sorted_word = sorted([letter for letter in word])

    def match(self, anagram):
        x = []

        for word in anagram:
            if sorted([letter for letter in word]) == self.sorted_word:
                x.append(word)

        return x



  


