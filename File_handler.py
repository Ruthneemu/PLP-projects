import os

sample_content = "This is the original text.\nLet's make it all uppercase!"
with open("original.txt", "w") as file:
    file.write(sample_content)
print("Created 'original.txt' with sample content.")
print("-" * 20)

original_file_name = "original.txt"
processed_file_name = "modified.txt"

try:
    with open(original_file_name, "r") as file_to_read:
        lines = file_to_read.readlines()
        
    print(f"Read content from '{original_file_name}'.")

    modified_lines = [line.upper() for line in lines]

    with open(processed_file_name, "w") as file_to_write:
        file_to_write.writelines(modified_lines)

    print(f"Successfully wrote modified content to '{processed_file_name}'.")
    print("-" * 20)
    print("Content of the new file:")
    
    with open(processed_file_name, "r") as check_file:
        print(check_file.read())

except FileNotFoundError:
    print(f"Error: The file '{original_file_name}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    if os.path.exists(original_file_name):
        os.remove(original_file_name)
    if os.path.exists(processed_file_name):
        os.remove(processed_file_name)
