from stats import Stats

def main():
    stats = Stats()
    print(f'{stats.get_book_word_count()} words found in the document')


if __name__ == "__main__":
    main()
