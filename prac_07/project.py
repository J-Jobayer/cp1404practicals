"""
project.py — Project class for Project Management exercise.

Estimated time: 2.0 hours (design 0.5h, coding 1.0h, testing/refactor 0.5h).
"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import date

# ---------- Domain constants (no magic numbers) ----------
COMPLETION_COMPLETE = 100
DATE_OUT_FMT = "%d/%m/%Y"  # single source for display formatting
CURRENCY_SYMBOL = "$"
CURRENCY_DECIMALS = 2


@dataclass(order=True)
class Project:
    """Represent a project item.

    Ordering is by priority (lower number = higher priority) via dataclass(order=True).
    """
    priority: int
    name: str
    start_date: date
    cost_estimate: float
    completion: int  # 0–100

    def is_complete(self) -> bool:
        """Return True if project is complete."""
        return self.completion >= COMPLETION_COMPLETE

    def __str__(self) -> str:
        cost_str = f"{CURRENCY_SYMBOL}{self.cost_estimate:,.{CURRENCY_DECIMALS}f}"
        start_str = self.start_date.strftime(DATE_OUT_FMT)
        return (f"{self.name}, start: {start_str}, "
                f"priority {self.priority}, estimate: {cost_str}, "
                f"completion: {self.completion}%")
