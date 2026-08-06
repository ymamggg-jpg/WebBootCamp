

print("WELCOME!, In this program i'll count the amount of even & odd numbers in a specific range")
max_number = input("Enter the maximum number").strip()
even = 0
odd = 0
counter = 1

for counter in range (1 , max_number):
    print(counter)
    #counter += 1
    if counter % 2 == 0 :
        print(f"That's an even number {counter}")
        even += 1
    else:
        print(f"that's an odd number {counter}")
        odd += 1
print(f"You have in total {even} even numbers and {odd} odd numbers")

    