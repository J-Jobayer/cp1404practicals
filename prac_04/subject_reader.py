"""
CP1404 Practical Suggested Solution
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display neatly."""
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)


def load_subjects(filename=FILENAME):
    """Load data from file formatted like: code,lecturer,number_of_students."""
    subjects = []
    # Use context manager and utf-8-sig to safely handle BOM if present
    with open(filename, encoding="utf-8-sig") as input_file:
        for line in input_file:
            line = line.strip()
            if not line:
                continue  # skip blank lines
            parts = [p.strip() for p in line.split(",")]
            if len(parts) != 3:
                continue  # skip malformed lines
            # Convert student count to int
            parts[2] = int(parts[2])
            subjects.append(parts)
    return subjects


def display_subjects(subjects):
    """Display subject data nicely."""
    for subject in subjects:
        # Match the sample’s formatting (code, lecturer padded to 12, students width 3)
        print("{} is taught by {:12} and has {:3} students".format(*subject))
        # Or with f-string (kept commented to mirror sample):
        # code, lecturer, students = subject
        # print(f"{code} is taught by {lecturer:12} and has {students:3} students")


if __name__ == "__main__":
    main()
