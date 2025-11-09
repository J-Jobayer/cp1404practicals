"""
project_management.py — Menu app for managing Projects.

Estimated time (actual): 2.0 hours.
- Design & skeleton: 20 min
- File I/O load/save (tab-delimited): 25 min
- Menu features (display/filter/add/update): 45 min
- Testing & tidy: 30 min
"""

from __future__ import annotations

from datetime import datetime, date
from pathlib import Path
from typing import Iterable, List

from project import (
    Project,
    COMPLETION_COMPLETE,
    DATE_OUT_FMT,
    CURRENCY_SYMBOL,
    CURRENCY_DECIMALS,
)

# ---------- App constants (no magic numbers/strings) ----------
APP_TITLE = "Welcome to Pythonic Project Management"

DEFAULT_FILENAME = "projects.txt"
DELIM = "\t"

# Header fields for file I/O
HEADER_FIELDS = (
    "Name",
    "Start Date",
    "Priority",
    "Cost Estimate",
    "Completion Percentage",
)

# Date parsing formats we accept from user/file
DATE_IN_FORMATS = ("%d/%m/%Y", "%d/%m/%y")

# Prompts
PROMPT_MAIN = ">>> "
PROMPT_LOAD = "Filename to load: "
PROMPT_SAVE = "Filename to save to: "
PROMPT_FILTER_DATE = "Show projects that start after date (dd/mm/yy or dd/mm/yyyy): "
PROMPT_ADD_NAME = "Name: "
PROMPT_ADD_START = "Start date (dd/mm/yy or dd/mm/yyyy): "
PROMPT_ADD_PRIORITY = "Priority: "
PROMPT_ADD_COST = f"Cost estimate: {CURRENCY_SYMBOL}"
PROMPT_ADD_COMPLETION = "Percent complete: "
PROMPT_UPDATE_CHOICE = "Project choice: "
PROMPT_UPDATE_PERCENT = "New Percentage: "
PROMPT_UPDATE_PRIORITY = "New Priority: "
PROMPT_QUIT_SAVE = f"Would you like to save to {DEFAULT_FILENAME}? "

# Display strings
GROUP_TITLE_INCOMPLETE = "Incomplete projects:"
GROUP_TITLE_COMPLETE = "Completed projects:"
INDENT = "  "

# Defaults
PRIORITY_DEFAULT = 1
COST_DEFAULT = 0.0
COMPLETION_DEFAULT = 0

# Indexing bounds
INDEX_MIN = 0  # first valid index

# Menu
MENU_LINES = (
    "- (L)oad projects",
    "- (S)ave projects",
    "- (D)isplay projects",
    "- (F)ilter projects by date",
    "- (A)dd new project",
    "- (U)pdate project",
    "- (Q)uit",
)
MENU_TEXT = "\n".join(MENU_LINES)

# Validation messages
MSG_INVALID_CHOICE = "Invalid choice"
MSG_INVALID_DATE = "Invalid date format."
MSG_INVALID_INT = "Invalid integer. Please try again."
MSG_INVALID_FLOAT = "Invalid number. Please try again."
MSG_OUT_OF_RANGE = "Choice out of range."
MSG_FILE_SAVED = "Saved {count} projects to {filename}"
MSG_FILE_LOADED = "Loaded {count} projects from {filename}"
MSG_THANKS = "Thank you for using custom-built project management software."


def main() -> None:
    print(APP_TITLE)

    projects: List[Project] = load_projects(DEFAULT_FILENAME)
    print(MSG_FILE_LOADED.format(count=len(projects), filename=DEFAULT_FILENAME))

    while True:
        print(MENU_TEXT)
        choice = input(PROMPT_MAIN).strip().lower()
        if choice == "l":
            filename = input(PROMPT_LOAD).strip()
            if filename:
                projects = load_projects(filename)
                print(MSG_FILE_LOADED.format(count=len(projects), filename=filename))
        elif choice == "s":
            filename = input(PROMPT_SAVE).strip()
            if filename:
                save_projects(filename, projects)
                print(MSG_FILE_SAVED.format(count=len(projects), filename=filename))
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            answer = input(PROMPT_QUIT_SAVE).strip().lower()
            if answer.startswith("y"):
                save_projects(DEFAULT_FILENAME, projects)
                print(MSG_FILE_SAVED.format(count=len(projects), filename=DEFAULT_FILENAME))
            print(MSG_THANKS)
            break
        else:
            print(MSG_INVALID_CHOICE)


# ---------- File I/O ----------

def load_projects(filename: str) -> List[Project]:
    """Load projects from a tab-delimited file with a header line."""
    path = Path(filename)
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        return []

    projects: List[Project] = []
    # Skip header
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(DELIM)]
        if len(parts) != len(HEADER_FIELDS):
            continue
        name_str, start_str, priority_str, cost_str, completion_str = parts
        try:
            start = parse_date(start_str)
            priority = int(priority_str)
            cost = float(cost_str)
            completion = int(completion_str)
        except ValueError:
            continue
        projects.append(Project(
            priority=priority,
            name=name_str,
            start_date=start,
            cost_estimate=cost,
            completion=completion
        ))
    return projects


def save_projects(filename: str, projects: Iterable[Project]) -> None:
    """Save projects to a tab-delimited file with header."""
    with open(filename, "w", encoding="utf-8") as f:
        print(DELIM.join(HEADER_FIELDS), file=f)
        for p in projects:
            row = DELIM.join((
                p.name,
                p.start_date.strftime(DATE_OUT_FMT),
                str(p.priority),
                f"{p.cost_estimate:.{CURRENCY_DECIMALS}f}",
                str(p.completion),
            ))
            print(row, file=f)


# ---------- Helpers / UI actions ----------

def display_projects(projects: List[Project]) -> None:
    """Display incomplete and completed projects; each group sorted by priority."""
    incomplete = sorted((p for p in projects if not p.is_complete()))
    complete = sorted((p for p in projects if p.is_complete()))

    print(GROUP_TITLE_INCOMPLETE)
    if not incomplete:
        print(f"{INDENT}(none)")
    for p in incomplete:
        print(f"{INDENT}{p}")

    print(GROUP_TITLE_COMPLETE)
    if not complete:
        print(f"{INDENT}(none)")
    for p in complete:
        print(f"{INDENT}{p}")


def filter_by_date(projects: List[Project]) -> None:
    """Ask for a date and display only projects starting after it, sorted by date."""
    raw = input(PROMPT_FILTER_DATE).strip()
    try:
        after = parse_date(raw)
    except ValueError:
        print(MSG_INVALID_DATE)
        return
    filtered = sorted((p for p in projects if p.start_date >= after), key=lambda p: p.start_date)
    for p in filtered:
        print(p)


def add_new_project(projects: List[Project]) -> None:
    """Prompt for fields and append a new Project."""
    print("Let's add a new project")
    name = input(PROMPT_ADD_NAME).strip()
    start = input(PROMPT_ADD_START).strip()
    priority = safe_int(input(PROMPT_ADD_PRIORITY).strip(), default=PRIORITY_DEFAULT)
    cost = safe_float(input(PROMPT_ADD_COST).strip(), default=COST_DEFAULT)
    completion = safe_int(input(PROMPT_ADD_COMPLETION).strip(), default=COMPLETION_DEFAULT)

    try:
        start_date = parse_date(start)
    except ValueError:
        start_date = date.today()

    projects.append(Project(
        priority=priority,
        name=name,
        start_date=start_date,
        cost_estimate=cost,
        completion=completion
    ))


def update_project(projects: List[Project]) -> None:
    """List projects with indices; allow updating completion and/or priority."""
    indexed = sorted(enumerate(projects), key=lambda t: (t[1].name.lower(), t[1].start_date))
    for idx, proj in indexed:
        print(f"{idx} {proj}")

    try:
        choice = int(input(PROMPT_UPDATE_CHOICE).strip())
    except ValueError:
        print(MSG_INVALID_INT)
        return

    if not (INDEX_MIN <= choice < len(projects)):
        print(MSG_OUT_OF_RANGE)
        return

    project = projects[choice]
    print(project)

    new_completion = input(PROMPT_UPDATE_PERCENT).strip()
    if new_completion != "":
        project.completion = safe_int(new_completion, default=project.completion)
        if project.completion > COMPLETION_COMPLETE:
            project.completion = COMPLETION_COMPLETE
        if project.completion < COMPLETION_DEFAULT:
            project.completion = COMPLETION_DEFAULT

    new_priority = input(PROMPT_UPDATE_PRIORITY).strip()
    if new_priority != "":
        project.priority = safe_int(new_priority, default=project.priority)


# ---------- Utility ----------

def parse_date(text: str) -> date:
    """Parse a date string using allowed input formats."""
    last_error: Exception | None = None
    for fmt in DATE_IN_FORMATS:
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError as e:
            last_error = e
    raise ValueError(str(last_error) if last_error else MSG_INVALID_DATE)


def safe_int(text: str, default: int) -> int:
    try:
        return int(text)
    except (TypeError, ValueError):
        return default


def safe_float(text: str, default: float) -> float:
    try:
        return float(text)
    except (TypeError, ValueError):
        return default


if __name__ == "__main__":
    main()
