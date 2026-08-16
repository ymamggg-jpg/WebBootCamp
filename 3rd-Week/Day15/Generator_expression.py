
# ==================== Generator expression ====================
numbers = range(1_000_000)  # 1000000

# Using () instead of [] creates a generator, not a list.
# The generator computes and yields one value at a time (O(1) memory),
# instead of building the entire list in memory first (O(n) memory, ~10% slower here).
total = sum(
    number ** 2
    for number in numbers  # if we used [] it would fill the whole list first
)

print(total)


# ==================== Mutable vs Immutable ====================
# Lists are MUTABLE: you can change them in place
items = ["Python", "Git"]
items.append("Django")

# Strings are IMMUTABLE: .title() doesn't change "name" in place,
# it returns a NEW string, which we then reassign to "name"
name = "Sara"
name = name.title()

print(items)
print(name)


# ==================== Shared reference (aliasing) ====================
original = ["Python", "Git"]
alias = original          # "alias" is NOT a copy — it points to the SAME list object

alias.append("Django")

print(original)   # original is also changed, because alias and original are the same object


# ==================== Shallow copy ====================
original = ["Python", "Git"]
clone = original.copy()   # creates a NEW list object with the same top-level items
clone.append("Django")

print(original)          # unaffected, since clone is a separate list
print(clone)
print(original is clone)  # False -> they are two different list objects

# Shallow copy pitfall: it only copies the OUTER list.
# Nested objects (like the inner lists here) are still shared between original and clone.
original = [["Sara", 90], ["Omar", 85]]

clone = original.copy()
clone[0][1] = 95   # modifies the inner list, which is shared with "original"

print(original)
print(clone)
print(original[0] is clone[0])  # True -> the inner lists are still the SAME object


# ==================== Deep copy ====================
from copy import deepcopy

original = [["Sara", 90], ["Omar", 85]]
clone = deepcopy(original)   # recursively copies EVERYTHING, including nested lists

clone[0][1] = 95   # only affects clone's inner list now

print(original)
print(clone)
print(original[0] is clone[0])  # False -> deepcopy made fully independent inner lists