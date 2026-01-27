#FileNotFound

try:
    file = open("a_file.txt")
    dict = {"hi": 8}
    print(dict["hsiod"])

except FileNotFoundError as error_message:
    file = open("a_file.txt", "w")
    file.write("Hello")
    file.close()
    print(f"There was an error {error_message}")

except KeyError as error_message:
    print(f"The key just doesnt exit: {error_message}")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File is closed")




