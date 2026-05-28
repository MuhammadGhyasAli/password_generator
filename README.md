# Random Password Generator

A CLI password generator that creates secure random passwords. Users specify a length and whether to include special characters. Built using Python's `random` and `string` modules.

## Features

- **Custom length** — Specify desired password length (minimum 4)
- **Letters + digits** — Always includes uppercase, lowercase, and numbers
- **Special characters** — Optional toggle (`!@#$%^&*`)
- **Guarantees** — At least one digit (and one special char if enabled)
- **Input validation** — Rejects non-numeric input, enforces minimum length

## How to Run

```bash
python password_generator.py
```

## Usage

1. Enter desired password length (minimum 4, or `0` to quit)
2. Choose `y` or `n` for special characters
3. Password is displayed; repeat for more passwords or enter `0` to exit

## Sample Session

```
===== PASSWORD GENERATOR =====
Password length (or 0 to quit): 12
Include special characters? (y/n): y
Generated password: a8$Rk2#mP9@x
----------------------------------------
Password length (or 0 to quit): 8
Include special characters? (y/n): n
Generated password: H3kL9mQ2
----------------------------------------
Password length (or 0 to quit): 0
Goodbye!
```

## Code Structure

- `generate_password(length, use_special)` — core generation function
- Character pool: `string.ascii_letters` + `string.digits` (+ specials if enabled)
- Guarantees: pre-pends one digit (and one special if enabled), then shuffles
- `random.choice()` for character selection
- `random.shuffle()` to randomize character order
