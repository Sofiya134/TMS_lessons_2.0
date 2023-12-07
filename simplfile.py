def write_file():
    with open("my_favorite_animal.txt", "w") as file:
        list_a =['Sofiya', 'Cat', 13]
        for i in list_a:
            file.write(f"{i}\n")
write_file()