# First ask the player questions to determine deck parameters.
print("How many basic lands do you want to run?")
basics = int(input())
print("This program will tell you how many basic lands to run of each type.")
print("How many White symbols are in your deck?")
whites = int(input())
print("How many Blue symbols are in your deck?")
blues = int(input())
print("How many Red symbols are in your deck?")
reds = int(input())
print("How many Black symbols are in your deck?")
blacks = int(input())
print("How many Green symbols are in your deck?")
greens = int(input())
total = whites + blues + reds + blacks + greens

# Determine correct number of basic lands for each mana type and define them.
plainsnum = round((whites / total) * basics)
islandsnum = round((blues / total) * basics)
swampsnum = round((blacks / total) * basics)
mountainsnum = round((reds / total) * basics)
forestsnum = round((greens / total) * basics)

# Displays the optimal number of each basic land based on the math above.
print(f"With {basics} basic lands you should use the following pile.")
print(f"Plains: {plainsnum}")
print(f"Islands: {islandsnum}")
print(f"Swamps: {swampsnum}")
print(f"Mountains: {mountainsnum}")
print(f"Forests: {forestsnum}")

# Displays action to take if rounding error happens.
landtotal = plainsnum + islandsnum + swampsnum + mountainsnum + forestsnum
if basics - landtotal != 0: # only shows if the number of lands suggested does not match amount desired.
    print("There is a rounding error,")
if basics - landtotal > 0:
    print(f"add {basics - landtotal} land to a pile.")
if basics - landtotal < 0:
    print(f"remove {landtotal - basics} land from a pile.")
print()
print("Program made by Erect Pineapple.")
input()
