# Python Refresher

A small personal project to refresh Python fundamentals: data types, data-structure manipulation, module imports, and object-oriented programming (OOP).

## Requirements

- Python 3.14 (or a recent version)

## Setup

```bash
# Clone the repo, then move into it
cd python_refresher

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate      # macOS / Linux
# venv\Scripts\activate       # Windows
```

No external dependencies are needed — the project relies only on the standard library.

## Project structure

```
python_refresher/
├── refresher.py                       # Basics: strings, lists, sets, tuples, dictionaries
├── refresher_oop.py                   # OOP: inheritance, polymorphism, encapsulation
└── imports/
    ├── grade_average_service.py       # Utility function: grade average
    ├── drink_selector.py              # Utility function: random choice
    ├── Enemy.py                        # Base class
    ├── Zombie.py                       # Subclass of Enemy
    └── Ogre.py                         # Subclass of Enemy
```

## Concepts covered

### `refresher.py` — The basics

- **Strings**: concatenation, f-strings, `.format()`
- **Lists**: creation, slicing, `append`, `insert`, `remove`, `pop`
- **Sets**: `add`, `update`, `discard`
- **Tuples**: creation and slicing
- **Dictionaries**: reading, adding/updating, deleting, iterating over keys and values
- **Module imports**: importing a single function and importing a whole module

### `refresher_oop.py` — Object-oriented programming

- **Encapsulation**: "private" attributes (`_attribute`) and getters
- **Inheritance**: `Zombie` and `Ogre` inherit from `Enemy` via `super()`
- **Polymorphism**: overriding the `talk()` and `special_attack()` methods
- A small turn-based battle (`battle`) that ties it all together

## Usage

Run the basics file:

```bash
python refresher.py
```

Run the OOP demo (the battle):

```bash
python refresher_oop.py
```

> Tip: in `refresher.py`, the function calls at the top of `__main__` are
> commented out. Uncomment the ones you want to try.
