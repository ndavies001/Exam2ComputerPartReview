###############################################################################
# DONE: 1.
#
#   In this module, we will be creating a way for you to be able to assign
#   tasks to each of the seven dwarves for their day at work.
#
#   First, for this _TODO_, create a function called response() that takes one
#   parameter:
#       - name      <-- str
#
#   This function will return the response of whichever dwarf's name is given
#   as the parameter. For example, if given the dwarf, Sleepy, it might return
#   something like:
#       "Zzzzzzzzzz....."
#
#   To do this, use a match case statement to match the name of the dwarf and
#   return a response. Pick *three* dwarves to have unique responses and the
#   rest should have a generic response of:
#       "Heigh-Hoooooo!!!""
#
#   Here is a list of the dwarf names for reference:
#       1) Happy
#       2) Doc
#       3) Grumpy
#       4) Dopey
#       5) Bashful
#       6) Sleepy
#       7) Sneezy
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def response(name):
    match name:
        case "Happy":
            return "Smile, it's a beautiful day!"
        case "Doc":
            return "Let me analyze the situation."
        case "Grumpy":
            return "Bah! Humbug."
        case _:
            return "Heigh-Hoooooo!!!"

###############################################################################
# DONE: 2.
#
#   Now, we need a function to handle the assigning of tasks.
#
#   For this _TODO_, write a function called work_order() that takes one
#   parameter:
#       - name      <-- str
#
#   This function should take the name of the dwarf and prompt the user to
#   assign them a task. So, if given the dwarf, Sleepy, it should prompt the
#   user to enter in a task for Sleepy like this:
#       "Please give Sleepy a task: "
#   
#   No need for logic on this one, just use the parameter to make the prompt.
#
#   This function should return a tuple that conains two items
#       1) the name of the dwarf
#       2) the task that the user gave the dwarf
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def work_order(name):
    task = input(f"Please give {name} a task: ")
    return (name, task)

###############################################################################
# DONE: 3.
#
#   Now, let's put things together.
#
#   Write a function called main() that gets the ball rolling.
#
#   This function should fulfill these requirements:
#
#       1) It should have a list of the dwarf names
#       2) It should loop through the list of names using a for loop that would
#          work with any number of dwarves (it should *NOT* only work if there
#          are seven).
#       3) For each dwarf, it should prompt the user to assign a task for that
#          dwarf using the function you defined above.
#       4) The dwarf should then respond according to your function above.
#       5) Once it has gone through all of the dwarves, it should then print
#          out a list of all the work orders (with name and task). Make sure
#          you keep track of them as you go. (HINT: an accumulator pattern
#          might be helpful)
#
#   Make sure you call your main() function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def main():
    dwarf_names = [
        "Happy", "Doc", "Grumpy", "Dopey", "Bashful", "Sleepy", "Sneezy"
    ]
    work_orders = []

    for dwarf in dwarf_names:
        task = work_order(dwarf)
        response_text = response(dwarf)
        work_orders.append(task)
        print(response_text)

    print("\nWork Orders:")
    for order in work_orders:
        print(f"{order[0]}: {order[1]}")
if __name__ == "__main__":
    main()