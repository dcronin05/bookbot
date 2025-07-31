class stats():
    def get_book_text(file_path='books/frankenstein.txt'):
        file_contents = ''
        with open(file_path) as f:
            file_contents = f.read()
        return file_contents

    def get_book_word_count(file_path = 'books/frankenstein.txt'):
        words = open(file_path).read().split()
        return len(words)
