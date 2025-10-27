def beer_countdown(bottles):
    """
    Prints the lyrics to the "bottles of beer" song,
    starting from the specified number of bottles.
    """
    def bottle_text(count):
        """Returns the correct singular or plural form of 'bottle'."""
        return "bottle" if count == 1 else "bottles"

    while bottles > 0:
        # First line of the verse
        print(f"{bottles} {bottle_text(bottles)} of beer on the wall, "
              f"{bottles} {bottle_text(bottles)} of beer.")

        bottles -= 1

        # Second line of the verse
        if bottles > 0:
            print(f"Take one down, pass it around, "
                  f"{bottles} {bottle_text(bottles)} of beer on the wall.\n")
        else:
            print("Take one down, pass it around, no more bottles of beer on the wall!\n")

# Main program
try:
    num = int(input("How many bottles of beer are on the wall? "))
    if num < 0:
        print("Please enter a non-negative number.")
    else:
        beer_countdown(num)
        print("Time to buy more beer!")
except ValueError:
    print("Invalid input. Please enter a number.")
