"""

CHARACTER PALETTE
You can copy the necessary characters for drawing cards from here.

Horizontal lines:  │

Vertical lines:  ─

Corners of a card:  ┐  ┌  ┘  └

Intersections of two cards:

    if card1_height == card2_height:  ┬  ┴

    if card1_height < card2_height:  ┤

    if card1_height > card2_height:  ├

"""


def card_drawer():
    print("This program will draw two cards next to each other.")
    print("─" * 20)

    print("Texts must not be empty.")
    card1_text = input("Text of first card: ")
    card2_text = input("Text of second card: ")
    print("─" * 20)

    ##############################
    # INSERT YOUR CODE HERE
    # Assign proper values to card1_min_width and card2_min_width here.
    # They are length of the corresponding text + 2.
    # For example, if card1_text contains 5 characters, then card1_min_width must be 7.
    card1_min_width = len(card1_text) + 2
    card2_min_width = len(card2_text) + 2
    # DO NOT EDIT THE CODE UNDER THIS LINE.
    ##############################

    print("Width of first card must be at least " + str(card1_min_width) + ".")
    card1_width = int(input("Width of first card: "))
    print("Width of second card must be at least " + str(card2_min_width) + ".")
    card2_width = int(input("Width of second card: "))
    print("─" * 20)

    print("Heights must be odd and at least 3.")
    card1_height = int(input("Height of first card: "))
    card2_height = int(input("Height of second card: "))
    print("─" * 20)

    ##############################
    # INSERT YOUR CODE HERE
    # Assign the proper value to is_invalid.
    # Check if there is at least one problem in the inputs.
    # I added two conditions, add more to the line below.
    is_invalid = len(card1_text) == 0 or len(card2_text) == 0 or card1_width < card1_min_width or \
                 card2_width < card2_min_width or card1_height < 3 or card2_height < 3 or card1_height % 2 == 0 or \
                 card2_height % 2 == 0


    # DO NOT EDIT THE CODE UNDER THIS LINE.
    ##############################

    if is_invalid:
        print("ERROR: Invalid inputs.")

    else:

        if card1_height == card2_height:

            ##############################
            # INSERT YOUR CODE HERE
            # Case 1
            # You can add as many new lines as you need.
            text1_width = len(card1_text)
            text2_width = len(card2_text)

            first_spaces1 = " " * ((card1_width - text1_width - 2) // 2)
            second_spaces1 = " " * (card1_width - len(first_spaces1) - text1_width - 2)
            first_spaces2 = " " * ((card2_width - text2_width - 2) // 2)
            second_spaces2 = " " * (card2_width - len(first_spaces2) - text2_width - 2)
            top_line = "┌" + "─" * (card1_width - 2) + "┬" + "─" * (card2_width - 2) + "┐"
            bottom_line = "└" + "─" * (card1_width - 2) + "┴" + "─" * (card2_width - 2) + "┘"
            empty_line = "│" + " " * (card1_width - 2) + "│" + " " * (card2_width - 2) + "│"
            text_line = "│" + first_spaces1 + card1_text + second_spaces1 + "│" + first_spaces2 + card2_text + second_spaces2 + "│"
            print(top_line, int(((card1_height - 3) / 2)) * ("\n" + empty_line), "\n", text_line,
                  int(((card1_height - 3) / 2)) * ("\n" + empty_line), "\n", bottom_line, sep="")

            # DO NOT EDIT THE CODE UNDER THIS LINE.
            ##############################


        elif card1_height > card2_height:

            ##############################
            # INSERT YOUR CODE HERE
            # Case 2
            # You can add as many new lines as you need.
            card1_top_line = "┌" + "─" * (card1_width - 2) + "┐"
            card1_bottom_line = "└" + "─" * (card1_width - 2) + "┘"
            card1_empty_line = "│" + " " * (card1_width - 2) + "│"
            connection_top_line1 = "│" + " " * (card1_width - 2) + "├" + "─" * (card2_width - 2) + "┐"
            connection_bottom_line1 = "│" + " " * (card1_width - 2) + "├" + "─" * (card2_width - 2) + "┘"
            together_empty_line = "│" + " " * (card1_width - 2) + "│" + " " * (card2_width - 2) + "│"

            text1_width = len(card1_text)
            text2_width = len(card2_text)
            first_spaces1 = " " * ((card1_width - text1_width - 2) // 2)
            second_spaces1 = " " * (card1_width - len(first_spaces1) - text1_width - 2)
            first_spaces2 = " " * ((card2_width - text2_width - 2) // 2)
            second_spaces2 = " " * (card2_width - len(first_spaces2) - text2_width - 2)
            text_line = "│" + first_spaces1 + card1_text + second_spaces1 + "│" + first_spaces2 + card2_text + second_spaces2 + "│"
            print(card1_top_line, ("\n" + card1_empty_line) * int(((card1_height - 3 - card2_height) / 2)), "\n",
                  connection_top_line1, ("\n" + together_empty_line) * int(((card2_height - 3) / 2)), "\n", text_line,
                  ("\n" + together_empty_line) * int(((card2_height - 3) / 2)), "\n", connection_bottom_line1,
                  ("\n" + card1_empty_line) * int(((card1_height - 3 - card2_height) / 2)), "\n", card1_bottom_line, sep="")

            # DO NOT EDIT THE CODE UNDER THIS LINE.
            ##############################


        else:

            ##############################
            # INSERT YOUR CODE HERE
            # Case 3
            # You can add as many new lines as you need.
            card2_top_line = " " * (card1_width - 1) + "┌" + "─" * (card2_width - 2) + "┐"
            card2_bottom_line = " " * (card1_width - 1) + "└" + "─" * (card2_width - 2) + "┘"
            card2_empty_line = " " * (card1_width - 1) + "│" + " " * (card2_width - 2) + "│"
            connection_top_line2 = "┌" + "─" * (card1_width - 2) + "┤" + " " * (card2_width - 2) + "│"
            connection_bottom_line2 = "└" + "─" * (card1_width - 2) + "┤" + " " * (card2_width - 2) + "│"
            together_empty_line = "│" + " " * (card1_width - 2) + "│" + " " * (card2_width - 2) + "│"

            text1_width = len(card1_text)
            text2_width = len(card2_text)
            first_spaces1 = " " * ((card1_width - text1_width - 2) // 2)
            second_spaces1 = " " * (card1_width - len(first_spaces1) - text1_width - 2)
            first_spaces2 = " " * ((card2_width - text2_width - 2) // 2)
            second_spaces2 = " " * (card2_width - len(first_spaces2) - text2_width - 2)
            text_line = "│" + first_spaces1 + card1_text + second_spaces1 + "│" + first_spaces2 + card2_text +\
                        second_spaces2 + "│"
            print(card2_top_line, ("\n" + card2_empty_line) * int(((card2_height - 3 - card1_height) / 2)), "\n",
                  connection_top_line2, ("\n" + together_empty_line) * int(((card1_height - 3) / 2)), "\n", text_line,
                  ("\n" + together_empty_line) * int(((card1_height - 3) / 2)), "\n", connection_bottom_line2,
                  ("\n" + card2_empty_line) * int(((card2_height - 3 - card1_height) / 2)), "\n", card2_bottom_line, sep="")

            # DO NOT EDIT THE CODE UNDER THIS LINE.
            ##############################
