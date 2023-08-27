import game


def show_simple_addition(first, second):
    total = first + second
    print(f"The total sum of {first} and {second} is {total}")


print('This is just showing a message on the command line')

show_simple_addition(15668, 15669)

# This is a comment since the line starts with #
# The definition of "game" comes from  importing the game file above
# where you see 'import game'
world = game.World()

# len is a method that you can use to get the length of an array, object, etc.
number_of_characters = len(world.characters)
print(f"There are currently {number_of_characters} characters in the world")

# you can append / add things to an array
world.characters.append("tank1")
number_of_characters = len(world.characters)
print(f"Now there are {number_of_characters} characters in the world")