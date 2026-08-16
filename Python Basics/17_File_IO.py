# ============================================================
# ==> FILE HANDLING
# ============================================================

"""
Python provides several functions and methods to manipulate files.

Before performing operations on a file, we must first open it.
"""


# ============================================================
# 1. OPENING A FILE
# ============================================================

"""
The open() function opens a file.

Syntax:
open(filename, mode)

By default, open() returns a file object that can be used to
read from or write to the file depending on the selected mode.
"""

file=open("example_file.txt","w")
file.write("Hello World!")
file.close()


# ============================================================
# 2. FILE MODE: r (READ)
# ============================================================

"""
The r mode opens a file for reading only.

It gives an error if the file does not exist.
"""

with open("example_file.txt","r") as file:
    contents=file.read()
    print(contents)


# ============================================================
# 3. FILE MODE: w (WRITE)
# ============================================================

"""
The w mode opens a file for writing.

If the file does not exist, a new file is created.
If the file already exists, its previous contents are replaced.
"""

with open("write_example.txt","w") as file:
    file.write("Hello World!")


# ============================================================
# 4. FILE MODE: a (APPEND)
# ============================================================

"""
The a mode opens a file for appending.

New content is added to the end of the file.
If the file does not exist, a new file is created.
"""

with open("append_example.txt","a") as file:
    file.write("Hello from append mode.\n")


# ============================================================
# 5. FILE MODE: x (CREATE)
# ============================================================

"""
The x mode is used to create a new file.

If the file already exists, Python raises FileExistsError.

To keep this example safe to run repeatedly, a unique file name
is used.
"""

create_file_name="newly_created_example.txt"

try:
    with open(create_file_name,"x") as file:
        file.write("This file was created using x mode.")
except FileExistsError:
    print("The file already exists.")


# ============================================================
# 6. FILE MODE: t (TEXT)
# ============================================================

"""
The t mode is used to handle text files.

Text mode is the default mode, so r and rt, or w and wt,
behave the same for text files.
"""

with open("text_example.txt","wt") as file:
    file.write("This is a text file.")


# ============================================================
# 7. FILE MODE: b (BINARY)
# ============================================================

"""
The b mode is used to handle binary files such as images and PDFs.

Binary data is read and written as bytes.
"""

with open("binary_example.bin","wb") as file:
    file.write(b"Python")


# ============================================================
# 8. CLOSING FILES
# ============================================================

"""
After completing file operations, a file can be closed using
the close() method.
"""

file = open("close_example.txt","w")
file.write("File closing example.")
file.close()

print("File closed:", file.closed)


# ============================================================
# 9. with STATEMENT
# ============================================================

"""
The with statement is used to handle files conveniently.

It automatically closes the file after the block finishes.
"""

with open("with_example.txt", "w") as file:
    file.write("The with statement closes the file automatically.")


# ============================================================
# 10. readlines() METHOD
# ============================================================

"""
The readlines() method reads all lines from a file and returns
them as a list of strings.
"""

with open("readlines_example.txt","w") as file:
    file.write("First line\n")
    file.write("Second line\n")
    file.write("Third line\n")

with open("readlines_example.txt","r") as file:
    lines=file.readlines()
    print(lines)


# ============================================================
# 11. writelines() METHOD
# ============================================================

"""
The writelines() method writes a sequence of strings to a file.

It does not automatically add newline characters.
"""

lines=["First line\n","Second line\n","Third line\n"]

with open("writelines_example.txt","w") as file:
    file.writelines(lines)


# ============================================================
# 12. seek() METHOD
# ============================================================

"""
The seek() method moves the file pointer to a specific position.

Syntax:
file.seek(offset)
"""

with open("seek_example.txt","w") as file:
    file.write("Python Programming")

with open("seek_example.txt","r") as file:
    file.seek(7)
    print(file.read())


# ============================================================
# 13. tell() METHOD
# ============================================================

"""
The tell() method returns the current position of the file pointer.
"""

with open("tell_example.txt","w") as file:
    file.write("Python Programming")

with open("tell_example.txt","r") as file:
    print("Initial position:",file.tell())
    file.read(6)
    print("Position after reading 6 characters:",file.tell())


# ============================================================
# 14. truncate() METHOD
# ============================================================

"""
The truncate() method is used to resize a file to a specified size.

Syntax:
file.truncate(size)
"""

with open("truncate_example.txt","w") as file:
    file.write("Hello, this is a test file.")

with open("truncate_example.txt","r") as file:
    print(file.read())