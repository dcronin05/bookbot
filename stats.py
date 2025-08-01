class Stats:
    def __init__(self, fp):
        self.FILE_PATH = fp
        self.HEADING = '============ BOOKBOT ============'
        self.ANALYZING = f'Analyzing book found at {self.FILE_PATH}...'
        self.WORD_HEADING = '----------- Word Count ----------'
        self.FOUND = f'Found {self.get_book_word_count()} total words'
        self.CHAR_HEADING = '--------- Character Count -------'

    def get_book_text(self):
        file_contents = ''
        with open(self.FILE_PATH) as f:
            file_contents = f.read()
        return file_contents

    def get_book_word_count(self):
        words = open(self.FILE_PATH).read().split()
        return len(words)

    def get_letter_counts(self):
        letter_counts = {}
        for letter in self.get_book_text():
            lower_char = letter.lower()
            if lower_char.isalpha():
                lower_letter = lower_char
            else: continue
            try:
                letter_counts[lower_letter] += 1
            except KeyError:
                letter_counts[lower_letter] = 1
        return letter_counts

    def sort_letter_counts(self, letter_counts):
        char_counts = []
        for letter in letter_counts:
          char_counts.append({'char': letter, 'num': letter_counts[letter]})
        char_counts.sort(reverse=True, key=lambda x: x['num'])
        return char_counts

    def print_report(self):
        char_counts = self.sort_letter_counts(self.get_letter_counts())

        print(self.HEADING)
        print(self.ANALYZING)
        print(self.WORD_HEADING)
        print(self.FOUND)
        print(self.CHAR_HEADING)
        for char in char_counts:
            print(f"{char['char']}: {char['num']}")
