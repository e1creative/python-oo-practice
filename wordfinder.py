"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    def __init__(self, file_path):
        self.file_path = file_path

        self.file = open(self.file_path, 'r')

        print(f"{self.read_words()} words read")

        self.file.seek(0)
        
        self.all_text = self.file.read().splitlines()


    def read_words(self):
        self.word_count = 0
       
        for line in self.file:
            self.word_count += 1

        return self.word_count

    def random(self):
        return random.choice(self.all_text)


class SpecialWordFinder(WordFinder):
    def __init__(self, file_path):
        super().__init__(file_path)

    def read_words(self):
        self.word_count = 0

        for line in self.file:
            if line == "" and not line.startswith("#"):
                self.word_count += 1

        return self.word_count
