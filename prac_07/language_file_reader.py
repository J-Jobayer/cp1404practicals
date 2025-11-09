from programming_language import ProgrammingLanguage

DATA_FILE = "languages.csv"

def str_to_bool(text: str) -> bool:
    """Convert typical CSV boolean-ish strings to True/False."""
    return text.strip().lower() in {"true", "t", "yes", "y", "1"}

def load_languages(filename: str) -> list[ProgrammingLanguage]:
    """Load programming languages from a CSV file (with header)."""
    languages = []
    with open(filename, "r", encoding="utf-8") as in_file:
        header = in_file.readline()  # ignore header
        for line in in_file:
            if not line.strip():
                continue  # skip blanks
            # Expected columns: Name,Typing,Reflection,Year,PointerArithmetic
            parts = [p.strip() for p in line.split(",")]
            if len(parts) < 5:
                raise ValueError(f"Row has {len(parts)} columns, expected 5: {line!r}")
            name, typing, reflection_text, year_text, pointer_text = parts[:5]
            reflection = str_to_bool(reflection_text)
            pointer_arithmetic = str_to_bool(pointer_text)
            year = int(year_text)
            languages.append(ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic))
    return languages

def main():
    languages = load_languages(DATA_FILE)

    print("All languages:")
    for language in languages:
        print(" ", language)

    print("\nDynamically typed languages:")
    for language in languages:
        if language.is_dynamic():
            print(" ", language.name)

    print("\nLanguages with reflection:")
    for language in languages:
        if language.reflection:
            print(" ", language.name)

    print("\nLanguages with pointer arithmetic:")
    for language in languages:
        if language.pointer_arithmetic:
            print(" ", language.name)

if __name__ == "__main__":
    main()
