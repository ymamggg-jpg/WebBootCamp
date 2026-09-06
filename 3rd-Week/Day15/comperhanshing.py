# ==================== Lab 1: for-loop vs list comprehension ====================
numbers = [1, 2, 3, 4, 5]
squred_numbers = []

for number in numbers:
    squred_numbers.append(number ** 2)   # build the squared list one item at a time

    print(squred_numbers)                # NOTE: this prints on every loop iteration (5 times),
                                          # not just once at the end

    # NOTE: "for numbers in numbers" reuses the outer variable name "numbers" as the
    # loop variable, which shadows/overwrites the original list while looping.
    # It still works here because nothing else needs the original "numbers" afterward,
    # but it's safer to use a different name (e.g. "for n in numbers").
    comp_numbers = [number ** 2 for numbers in numbers]
    print(comp_numbers)                  # also prints 5 times, once per outer iteration


# ==================== Lab 2: transform every item (add VAT) ====================
prices = [10, 25, 40]

prices_with_vat = [
    round(price * 1.15, 2)  # price * 1.15
    for price in prices
]

print(prices_with_vat)


# ==================== Lab 3: string case transformations ====================
names = ["SaRa", "ArEej", "nasser", "Mashael"]

lower = [name.lower() for name in names]     # all lowercase

upper = [
    name.upper()          # all uppercase
    for name in names
]

titled = [
    name.title()          # capitalize each name properly
    for name in names
]

print(lower, upper, titled)


# ==================== Lab 4: Celsius to Fahrenheit conversion ====================
c_temp = [20, 33, 15, 0]
f_temp = [
    (temp * 1.8 + 32)
    for temp in c_temp
]
print(f_temp)


# ==================== Lab 5: flatten a nested list (loop vs comprehension) ====================
nested_list = [[1, 2], [3, 4], [5, 6]]
flattend_list = []

# Manual approach: nested for-loops
for row in nested_list:
    for column in row:
        flattend_list.append(column)

print(flattend_list)

# Same result using a nested list comprehension
comp_flattend_list = [
    column
    for row in nested_list
    for column in row
]

print(flattend_list)  # NOTE: this prints "flattend_list" again instead of
                       # "comp_flattend_list" — both hold the same values here,
                       # but this line doesn't actually show the comprehension's result


# ==================== Lab 5 (duplicate label): pass/fail labeling ====================
scores = [45, 55, 65, 75, 86, 95]
passing_score = [
    "Pass" if score >= 60 else "Failed"   # ternary expression inside the comprehension
    for score in scores
]
print(passing_score)


# ==================== Lab 7: set comprehension (normalize + dedupe) ====================
skills = ["Python", "Git", "PYTHON", "SQL", "git"]

# .lower().title() normalizes casing so "Python"/"PYTHON" and "Git"/"git"
# are treated as duplicates; the set automatically removes the repeats
skills_set = {
    skill.lower().title()
    for skill in skills
}
print(skills_set)


# ==================== Lab 8: list of dictionaries via comprehension ====================
list_name = ["Sara", "Dalal", "Nouf", "Taif"]
counted_letters = [
    {"name": name, "count": len(name)}   # build a small dict per name
    for name in list_name
]
print(counted_letters)


# ==================== Lab 9: generator expression (lazy evaluation) ====================
new_names = ["Mada", "Nouf", "Ymam", "Mashael"]

# Parentheses () instead of [] make this a GENERATOR, not a list —
# values are computed one at a time, only when requested
upp = (
    name.upper()
    for name in new_names
)

print(next(upp))   # gets the 1st value: "MADA"
print(next(upp))   # gets the 2nd value: "NOUF"
# print(list(upp))  # would consume the rest of the generator into a list
print("-" * 5)

# The for-loop continues from where next() left off (3rd item onward),
# since a generator can only be iterated through once
for x in upp:
    print(x)