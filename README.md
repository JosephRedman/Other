# Other
A text editor, like no Other!

---

Welcome to Other! This text editor was built for the JAM 1 computer, but it can run anywhere without an emulator since it is written in Python with no dependencies.

---

## How to Use

1. **Run the Program**: Double-click `runme.bat`. A console window will open, sized to 80x25.

2. **Initial Screen**:
   When the program starts, you'll see this:
   ```
      Current File: No File Open.                              Other text editor



















>

   The title bar at the top shows the current file. If you open `test.txt`, it will look like this:

   ```
      Current File: test.txt                                   Other text editor
   ```

3. **Commands**:
   - **Open a File**: Enter `o <FILENAME>`. For example: `o test.txt`.
   - **Edit a Line**: Once a file is open, its contents are displayed in the area below the title bar. Line numbers (which can be toggled with `ln true` and `ln false`) make editing easy. To edit a line, use `e <LINENUMBER>`. This will prompt:
     ```
     <linenumber: >
     ```
     Enter the new content for that line. This REPLACES all text in that line with what you have entered, so be carefull.

---

