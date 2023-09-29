text = input("enter text: ")

reversed_text = text[::-1]

print("text in reverse order:", reversed_text)

while True:
    user_input = input("enter text (or 'exit' for quit): ")

    if user_input.lower() == 'exit':
        break

    reversed_text = user_input[::-1]
    print("text in reverse order:", reversed_text)