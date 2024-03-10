###############################################################################
# DONE: 1.
#
#   In this module, we are going to create various shape functions (similar to
#   the one where you made a triangle in your coding exercises).
#
#   For this _TODO_, we are going to make simple rectangles.
#
#   Write a function called rectangle() that takes two parameters:
#       - height    <-- int
#       - width     <-- int
#
#   So, if given a height of 3 and a width of 4 it would print:
#
#       ****
#       ****
#       ****
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def rectangle(height, width):
    for _ in range(height):
        print("*" * width)

rectangle(3, 4)
###############################################################################
# DONE: 2.
#
#   For this _TODO_, write a function called inverted_triangle() that takes one
#   parameter:
#       - size      <-- int
#
#   This will be very similar to your triangle function from before, but, this
#   time, inverted. So if given a size of 4, it would print:
#
#       ****
#       ***
#       **
#       *
#
#   NOTE: there are no blank lines
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def inverted_triangle(size):
    for i in range(size, 0, -1):
        print("*" * i)


inverted_triangle(4)
###############################################################################
# DONE: 3.
#
#   For this _TODO_ write a function called box() that takes two parameters:
#       - height    <-- int
#       - width     <-- int
#
#   If given a height of 4 and width of 5, it would print:
#
#       *****
#       *   *
#       *   *
#       *****
#
#   NOTE: There are sizes that are too small for boxes, so the smallest box
#   that you can have is a 3x3. To make sure this function doesn't try to
#   create a box too small, write some logic that prints this:
#       "Invalid Box Size"
#   if the function is given any dimension smaller than 3.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def box(height, width):
    if height < 3 or width < 3:
        print("Invalid Box Size")
    else:
        for i in range(height):
            if i == 0 or i == height - 1:
                print("*" * width)
            else:
                print("*" + " " * (width - 2) + "*")

box(4, 5)
###############################################################################
# DONE: 4.
#
#   For this _TODO_, write a function called main() that calls each of your
#   functions above. It should print these shapes in order:
#
#       1) a rectangle of height 3 and width 5
#       2) an inverted triangle of size 7
#       3) a box of height 4 and width 6
#
#   Make sure you call your main() function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def main():
    print("Rectangle of height 3 and width 5:")
    rectangle(3, 5)

    print("\nInverted triangle of size 7:")
    inverted_triangle(7)

    print("\nBox of height 4 and width 6:")
    box(4, 6)

if __name__ == "__main__":
    main()