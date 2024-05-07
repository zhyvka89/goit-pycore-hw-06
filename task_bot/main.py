from handlers import parse_input, add_contact, change_contact, show_all, show_phone

def main():
  contacts = {}
  print("Welcome to the assistant bot!")
  while True:
    user_input = input("Enter a command: ")
    command, *args = parse_input(user_input)

    if command in ["close", "exit"]:
      print("Good bye!")
      break

    elif command == "hello":
      print("How can I help you?")
    elif command == "add":
      print(add_contact(args, contacts))
    elif command == "change":
      print(change_contact(args, contacts))
    elif command == "phone":
      print(show_phone(args, contacts))
    elif command == "all":
      print(show_all(contacts))
    else:
      print("Invalid command.")

if __name__ == "__main__":
  main()
