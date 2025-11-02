"""
languages.py - CP1404 prac_06
Estimate: 8 minutes
Actual: <record after you finish>

Creates several ProgrammingLanguage objects, prints one, and lists the dynamically typed languages.
"""

# If running from project root with a 'prac_06' package:
from prac_06.programming_language import ProgrammingLanguage
# If running this file from inside the same folder as programming_language.py, use:
# from programming_language import ProgrammingLanguage

def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Check __str__ works by printing python
    print(python)

    languages = [python, ruby, visual_basic]

    print("\nThe dynamically typed languages are:")
    for lang in languages:
        if lang.is_dynamic():
            print(lang.name)

if __name__ == "__main__":
    main()
