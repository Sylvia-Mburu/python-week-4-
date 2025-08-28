# File Handling and Error Handling Assignment

    # Ask the user for a filename
    filename = input("Enter the name of the file you want to read: ")

    # Open the file for reading
    file = open(filename, "r")
    content = file.read()
    file.close()

    # Modify the content (here we change it to uppercase)
    new_content = content.upper()

    # Write the new content to another file
    new_filename = "new_" + filename
    new_file = open(new_filename, "w")
    new_file.write(new_content)
    new_file.close()

    print("The modified file has been saved as", new_filename)

# If the file is not found
except FileNotFoundError:
    print("The file was not found. Please check the name and try again.")

# Any other error
except Exception as e:
    print("Something went wrong:", e)
