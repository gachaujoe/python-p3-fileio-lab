# def write_file(file_name, file_content):
#     pass

# def append_file(file_name, append_content):
#     pass

# def read_file(file_name):
#     pass


# def write_file(file_name, file_content):
#     # Add .txt extension to the file name
#     with open(f"{file_name}.txt", "w") as file:
#         file.write(file_content)


# def append_file(file_name, append_content):
#     # Add .txt extension to the file name
#     with open(f"{file_name}.txt", "a") as file:
#         file.write(append_content + "\n")  # Append a newline for readability


# def read_file(file_name):
#     # Add .txt extension to the file name
#     with open(f"{file_name}.txt", "r") as file:
#         return file.read()

def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)


def append_file(file_name, append_content):
    with open(f"{file_name}.txt", "a") as file:
        file.write("\n" + append_content)  # Prepend a newline for better formatting


def read_file(file_name):
    with open(f"{file_name}.txt", "r") as file:
        return file.read()
