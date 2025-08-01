from stats import Stats
import sys

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    stats = Stats(sys.argv[1])
    stats.print_report()


if __name__ == "__main__":
    main()
