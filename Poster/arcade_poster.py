import arcade


WIDTH = 650
HEIGHT = 800


def types_of_malware():
    # List
    arcade.draw_text("Here are some most common types of malware:", 20, 645, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("1. Adware", 40, 630, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("2. Virus", 40, 615, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("3. Keyloggers", 40, 600, arcade.color.SMOKY_BLACK, 12)
    # Definition adware
    arcade.draw_text("Adware is the least dangerous and most lucrative Malware. It displays ads on your ",
                     20, 585, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("computer.", 20, 570, arcade.color.SMOKY_BLACK, 12)
    # Definition virus
    arcade.draw_text("A virus is a contagious program or code that attaches itself to another piece of software,",
                     20, 555, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("and then reproduces itself when that software is run. Most often this is spread by sharing ",
                     20, 540, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("software or files between computers.", 20, 525, arcade.color.SMOKY_BLACK, 12)
    # Definition Kevloggers
    arcade.draw_text("A kevloggers records everything you type on your PC in order to glean your log-in names, ",
                     20, 510, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("passwords, and other sensitive information, and send it on to the source of the keylogging ",
                     20, 495, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("program. Many times keyloggers are used by corporations and parents to acquire ",
                     20, 480, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("computer usage information.", 20, 465, arcade.color.SMOKY_BLACK, 12)


def definition_of_what_is_malware():
    arcade.draw_text("Malware, or malicious software, is any program or file that is harmful to a computer user.",
                     20, 705, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("Types of malware can include computer viruses, worms, Trojan horses and spyware.",
                     20, 690, arcade.color.SMOKY_BLACK, 12)


def square_point(x, y):
    arcade.draw_point(x, y, arcade.color.BLUE, 5)


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    # Title
    arcade.draw_text("__________________", 247, 750, arcade.color.BLACK, 15)
    arcade.draw_text("Malware Prevention", 250, 750, arcade.color.BLACK, 15)
    # What is malware
    square_point(10, 725)
    arcade.draw_text("What is Malware", 20, 720, arcade.color.BLACK, 13)
    # Definition of what is malware
    definition_of_what_is_malware()
    # Types of malware
    square_point(10, 665)
    arcade.draw_text("Types of Malware", 20, 660, arcade.color.BLACK, 13)
    # Lists of malwars
    types_of_malware()

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Poster - Malware Prevention")
    arcade.set_background_color(arcade.color.LIGHT_GRAY)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
