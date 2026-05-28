# Random Password Generator

A CLI password generator that creates secure random passwords. Users specify length and whether to include special characters.

## Features

- Generates password with letters and digits (base)
- Optional special characters (`!@#$%^&*`)
- Guarantees at least one digit (and one special char if enabled)
- Input validation: minimum length 4, non-numeric rejection

## How to Run

```bash
python password_generator.py
```

## Usage

1. Enter desired password length (minimum 4)
2. Choose `y` or `n` for special characters
3. Password is displayed; repeat or enter `0` to quit
