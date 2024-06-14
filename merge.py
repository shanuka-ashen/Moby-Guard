def merge_files(smali_solution, smali_code):
    try:
        # Read content from the smali_solution file
        with open(smali_solution, 'r') as file1:
            smali_solution_content = file1.read()

        # Read content from the smali_code file
        with open(smali_code, 'r') as file2:
            smali_code_content = file2.read()

        # Append content of the smali_solution file to the smali_code file
        merged_content = smali_code_content + '\n' + smali_solution_content

        # Write the merged content back to the smali_code file
        with open(smali_code, 'w') as file2:
            file2.write(merged_content)

        print("Merged content successfully.")

    except FileNotFoundError:
        print("One or both of the files not found.")
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
if __name__ == "__main__":
    #smali_solution = input("Enter the path of the smali_solution file: ")
    #smali_code = input("Enter the path of the smali_code file: ")
    
    smali_solution = "magiskDetect.txt"
    smali_code = "MainActivity.smali"

    merge_files(smali_solution, smali_code)
