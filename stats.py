class Stats:
    def get_book_text(self, file_path='books/frankenstein.txt'):
        file_contents = ''
        with open(file_path) as f:
            file_contents = f.read()
        return file_contents

    def get_book_word_count(self, file_path = 'books/frankenstein.txt'):
        words = open(file_path).read().split()
        return len(words)

    def get_letter_counts(self, file_path = 'books/frankenstein.txt'):
        for letter in self.get_book_text():
            print(letter)
