"""Simple Roman numeral conversion utilities.

This module provides:
- roman_to_int(s): convert a Roman numeral string to an integer
- int_to_roman(n): convert an integer (1..3999) to a Roman numeral

Run as a script to convert a user-provided value. If the input is all digits,
it will convert integer -> Roman. Otherwise it will attempt Roman -> integer.
"""

_VALUES = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000,
}

def roman_to_int(s: str) -> int:
  """Convert a Roman numeral string to an integer.

  Uses the standard rule where a smaller value before a larger value is
  subtracted (e.g., IV == 4).

  Raises ValueError on invalid characters or empty input.
  """
  if not s:
    raise ValueError("empty Roman numeral")

  s = s.strip().upper()
  total = 0
  i = 0
  while i < len(s):
    ch = s[i]
    if ch not in _VALUES:
      raise ValueError(f"invalid Roman numeral character: {ch}")
    val = _VALUES[ch]

    # lookahead for subtractive notation
    if i + 1 < len(s):
      next_ch = s[i + 1]
      if next_ch not in _VALUES:
        raise ValueError(f"invalid Roman numeral character: {next_ch}")
      next_val = _VALUES[next_ch]
      if val < next_val:
        total += (next_val - val)
        i += 2
        continue

    total += val
    i += 1

  return total


def int_to_roman(n: int) -> str:
  """Convert an integer to a Roman numeral (supports 1..3999).

  Raises ValueError for values outside the supported range.
  """
  if not isinstance(n, int):
    raise ValueError("int_to_roman requires an integer")
  if n <= 0 or n >= 4000:
    raise ValueError("int_to_roman supports values from 1 to 3999")

  parts = []
  mapping = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
  ]

  for value, numeral in mapping:
    while n >= value:
      parts.append(numeral)
      n -= value

  return ''.join(parts)


def main() -> None:
  user = input("Enter Roman numerals or an integer to convert: ").strip()
  if not user:
    print("No input provided. Exiting.")
    return

  # If the user entered an integer, convert to Roman
  if user.isdigit():
    val = int(user)
    try:
      roman = int_to_roman(val)
      print(f"{val} -> {roman}")
    except ValueError as exc:
      print(f"Error: {exc}")
    return

  # Otherwise try Roman -> int
  try:
    value = roman_to_int(user)
    print(f"{user.upper()} -> {value}")
  except ValueError as exc:
    print(f"Error: {exc}")


if __name__ == '__main__':
  main()