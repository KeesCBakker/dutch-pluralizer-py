import argparse
import sys
from pprint import pprint
from . import pluralize, pluralize_advanced, singularize, could_be_plural, singularize_advanced


def print_result(answer: str, verbose: bool, action: str, word: str):
    if answer:
        print(answer)
    elif verbose:
        print(f"Could not {action} '{word}'.")


def process_word(word: str, do_pluralize: bool, do_singularize: bool, do_pluralize_advanced: bool, do_singularize_advanced: bool, verbose: bool, pipe: bool = False):
    if not word:
        if pipe:
            print()
        return

    def handle(action: str, fn):
        try:
            answer = fn(word)
            if answer:
                print(answer)
            elif pipe:
                print()
            elif verbose:
                print(f"Could not {action} '{word}'.")
        except Exception:
            if pipe:
                print()
            elif verbose:
                print(f"Could not {action} '{word}'.")

    if do_pluralize:
        handle("pluralize", pluralize)
    if do_singularize:
        handle("singularize", singularize)
    if do_pluralize_advanced:
        try:
            answer = pluralize_advanced(word)
            pprint(vars(answer))
        except Exception:
            pass
    if do_singularize_advanced:
        try:
            answer = singularize_advanced(word)
            pprint(vars(answer))
        except Exception:
            pass


def main():
    parser = argparse.ArgumentParser(description='Generates Dutch plural and singular nouns in a very imperfect way using Hunspell dictionaries. Why imperfect? Because the Dutch language is full of exceptions.')
    parser.add_argument('word', nargs='?', help='The word. Omit to read from stdin.')
    parser.add_argument("-p",  "--pluralize", help="pluralizes the word.", action="store_true")
    parser.add_argument("-pa", "--pluralize_advanced", help="shows advanced pluralization output.", action="store_true")
    parser.add_argument("-s",  "--singularize", help="singularizes the word.", action="store_true")
    parser.add_argument("-sa", "--singularize_advanced", help="shows advanced singularization output.", action="store_true")
    parser.add_argument("-v",  "--verbose", help="Shows an error message when a word could not be processed.", action="store_true")

    args = parser.parse_args()

    do_pluralize = args.pluralize or (not args.singularize and not args.pluralize_advanced and not args.singularize_advanced)
    do_singularize = args.singularize
    do_pluralize_advanced = args.pluralize_advanced
    do_singularize_advanced = args.singularize_advanced
    verbose = args.verbose

    if args.word:
        process_word(args.word, do_pluralize, do_singularize, do_pluralize_advanced, do_singularize_advanced, verbose)
    elif not sys.stdin.isatty():
        for line in sys.stdin:
            word = line.strip()
            process_word(word, do_pluralize, do_singularize, do_pluralize_advanced, do_singularize_advanced, verbose, pipe=True)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()