# ==================== List comprehension: basic filter ====================
numbers = [1, 2, 3, 4, 5]   # the source expression/iterable

# List comprehension = [expression for item in iterable if condition]
squares = [
    number ** 2
    for number in numbers
    if number % 2 == 1        # clause: only keep odd numbers
    # else:                    # "else" isn't used for filtering here (that needs
    #                           # a different form: expr if cond else expr2)
]

print(squares)  # [1, 9, 25]


# ==================== List comprehension: transform every item ====================
prices = [10, 25, 40]

# No "if" here, so every price is transformed (no filtering, just mapping)
prices_with_vat = [
    round(price * 1.15, 2)
    for price in prices
]

print(prices_with_vat)


# ==================== List comprehension: filter only (no transform) ====================
scores = [42, 67, 91, 58, 75]

# Keep the score as-is ("append" it) only if it passes the condition
passing_scores = [
    score
    for score in scores
    if score >= 60
]

print(passing_scores)


# ==================== List comprehension: clean + filter strings ====================
raw_names = [" ymam", "OMAR", "", "lina"]

clean_names = [
    name.strip().title()   # remove extra spaces, then capitalize each word
    for name in raw_names
    if name.strip()          # skip empty/blank names
]
print(clean_names)

# Note: "if name.strip()" works because an empty string is "falsy" in Python,
# so blank names are automatically filtered out.


# ==================== List comprehension: nested loops (all combinations) ====================
numbers = [1, 2, 3]
letters = ["A", "B", "C"]

# Two "for" clauses = nested loop, produces every (number, letter) combination
pairs = [
    (number, letter)
    for number in numbers
    for letter in letters
]
print(pairs)


# ==================== List comprehension: conditional expression (ternary) ====================
scores = [42, 67, 91]

# "value if condition else other_value" placed BEFORE the "for" = a ternary
# expression applied to every item (this is transforming, not filtering)
labels = [
    "pass" if score >= 60 else "retry"
    for score in scores
]

print(labels)


# ==================== Set comprehension ====================
emails = [
    "SARA@EXAMPLE.COM",
    "  omar@example.com",
    "lina@school.sa"
]

# {expression for item in iterable} -> a set comprehension
# Using {} instead of [] automatically removes duplicate domains
doamins = {
    email.split("@")[1].lower()
    for email in emails
}

print(doamins)


# ==================== Dict comprehension ====================
numbers = range(1, 6)

# {key: value for item in iterable} -> a dict comprehension
squares = {
    number: number ** 2
    for number in numbers
}

print(squares)