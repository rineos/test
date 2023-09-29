def double_letters(input_string):
    doubled_string = ''
    for char in input_string:
        doubled_string += char * 2
    return doubled_string

user_input = input("Enter text: ")
if user_input:
    doubled_text = double_letters(user_input)
    print("double text:", doubled_text)
else:
    print("U didnt print text.")
