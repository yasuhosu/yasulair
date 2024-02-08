def replace_characters(input_string, char_mapping):
    input_string = input_string.upper()

    for old_char, new_char in char_mapping.items():
        input_string = input_string.replace(old_char, new_char)
    return input_string

def process_file(input_file, char_mapping, output_file=None,):
    with open(input_file, 'r') as f:
        input_string = f.read()
    
    output_string = replace_characters(input_string, char_mapping)

    if output_file is None:
        output_file = "output.txt"
    
    with open(output_file, 'w') as f:
        f.write(output_string)
    print("Processing complete. Output written to:", output_file)


### copy the input text file filepath here: (output is going to be saved in this file's directory)
input_file = "C:/Users/felix/Desktop/nostril.txt" 

### change the characters u wanna change here:
char_mapping = {
    'O': '0',
    'I': '1',
    'E': '3',
    'S': '5',
    'B': '8',
    'A': '4',
    'G': '9',

}

process_file(input_file, char_mapping)
