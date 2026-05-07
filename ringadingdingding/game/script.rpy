# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image poor temp = Solid("#00aa00", xysize=(250, 600))
    image corrupt temp = Solid("#ff0000", xysize=(250, 600))
    image business temp = Solid("#0000aa", xysize=(250, 600))

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show poor temp with zoomin:
        xalign 0.15
        yalign 1.0
    
    show corrupt temp with zoomin:
        xalign 0.5
        yalign 1.0

    show business temp with zoomin:
        xalign 0.85
        yalign 1.0

    # These display lines of dialogue.

    y "Welcome to the business world!"

    # This ends the game.

    return
