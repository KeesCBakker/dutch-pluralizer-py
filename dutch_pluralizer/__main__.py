import argparse
from pprint import pprint
from . import pluralize, pluralize_advanced, singularize, could_be_plural, singularize_advanced

def print_result(answer: str, verbose: bool, action: str, word: str):
    if answer:
        print(answer)
    elif verbose:
        print(f"Could not {action} '{word}'.")


def main():

    parser = argparse.ArgumentParser(description='Generates Dutch plural and singular nouns in a very imperfect way using Hunspell dictionaries. Why imperfect? Because the Dutch language is full of exceptions.')
    parser.add_argument('word', help='The word.')
    parser.add_argument("-p",  "--pluralize", help="pluralizes the word.", action="store_true")
    parser.add_argument("-pa", "--pluralize_advanced", help="shows advanced pluralization output.", action="store_true")
    parser.add_argument("-s",  "--singularize", help="singularizes the word.", action="store_true")
    parser.add_argument("-sa", "--singularize_advanced", help="shows advanced singularization output.", action="store_true")
    parser.add_argument("-v",  "--verbose", help="Shows an error message when a word could not be processed.", action="store_true")

    args = parser.parse_args()

    word = args.word

    do_pluralize = args.pluralize or (not args.singularize and not args.pluralize_advanced)

    if do_pluralize:
        answer = pluralize(word)
        print_result(answer, args.verbose, "pluralize", word)
    
    if args.singularize:
        answer = singularize(word)
        print_result(answer, args.verbose, "singularize", word)
    
    if args.pluralize_advanced:
        answer = pluralize_advanced(word)
        pprint(vars(answer))

    if args.singularize_advanced:
        answer = singularize_advanced(word)
        pprint(vars(answer))


if __name__ == "__main__":
    main()