"""
CP1404/CP5632 Practical - Wikipedia API demo.

"""

import wikipedia
from wikipedia import DisambiguationError, PageError


def main() -> None:
    """Prompt for page titles and display Wikipedia page info until blank input."""
    while True:
        title = input("Enter page title: ").strip()
        if title == "":
            print("Thank you.")
            break

        try:
            # autosuggest=False so we get more predictable behaviour
            page = wikipedia.page(title, autosuggest=False)
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        else:
            print(page.title)
            # Summary can be long; we can limit by sentences or just print full
            print(wikipedia.summary(page.title, sentences=3))
            print(page.url)
        print()  # blank line between queries


if __name__ == "__main__":
    main()
