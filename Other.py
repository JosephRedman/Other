# Nano-like text editor for the JAM-1 computer

# Terminal size constants
CONSOLE_COLUMNS = 80
CONSOLE_LINES = 25

# Default filename for no file open
NO_FILENAME = "No File Open."

# Line numbers toggle
show_line_numbers = True

# Functions
def filename_padding(filename):
    """Shortens or pads the filename to fit within 40 characters."""
    return filename[:34] + "...   " if len(filename) > 37 else filename.ljust(40)

def generate_titlebar(filename):
    """Generates the title bar with the current filename."""
    return f"   Current File: {filename_padding(filename)}   Other text editor   "

def console_format(text, flip=False):
    """Formats text with foreground and background colors."""
    if flip:
        return f"\033[47m\033[30m{text}\033[0m"  # White background, black text
    return f"\033[40m\033[97m{text}\033[0m"    # Black background, white text

def screen_render(sizex, sizey, filename, has_file):
    """Renders the screen with either a file or placeholder content."""
    titlebar = generate_titlebar(filename if has_file else NO_FILENAME)
    print(console_format(titlebar, True))
    
    if has_file:
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(console_format(f"Error: File '{filename}' not found!", True))
            return

        for i in range(sizey - 2):
            if i < len(lines):
                content = lines[i].strip().ljust(sizex)
                if show_line_numbers:
                    content = f"{i + 1}|{content}"
                print(content)
            else:
                print(" " * sizex)
    else:
        for _ in range(sizey - 2):
            print(" " * sizex)

def line_edit(line_number, filename):
    """Edits a specific line in the file."""
    edit_content = input(f"{line_number}: ")
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    while len(lines) < line_number:
        lines.append('\n')

    lines[line_number - 1] = edit_content + '\n'

    with open(filename, 'w') as file:
        file.writelines(lines)

    screen_render(CONSOLE_COLUMNS, CONSOLE_LINES, filename, True)

def parse_edit_command(command):
    """Parses and executes an edit command."""
    line_number = int(command[1:])
    screen_render(CONSOLE_COLUMNS, CONSOLE_LINES, filename, True)
    line_edit(line_number, filename)

def parse_open_command(command):
    """Parses and executes an open command."""
    filename = command[2:]
    screen_render(CONSOLE_COLUMNS, CONSOLE_LINES, filename, True)
    return filename

def parse_ln_command(command):
    """Parses and executes the ln (line number toggle) command."""
    global show_line_numbers
    if command == "ln true":
        show_line_numbers = True
    elif command == "ln false":
        show_line_numbers = False
    else:
        print("Invalid ln command. Use 'ln true' or 'ln false'.")

def get_command(current_filename):
    """Processes user input commands."""
    command = input(">")
    match command.split()[0]:  # Match the first word of the command
        case "e":
            parse_edit_command(command)
        case "o":
            return parse_open_command(command)
        case "ln":
            parse_ln_command(command)
        case _:
            screen_render(CONSOLE_COLUMNS, CONSOLE_LINES, current_filename, False)
            print("Invalid Command")
    return current_filename

# Main Loop
filename = ""
running = True

screen_render(CONSOLE_COLUMNS, CONSOLE_LINES, filename, False)

while running:
    filename = get_command(filename)
