import data_fetcher


def create_animals_page(animal_name: str):
    dynamic_data = data_fetcher.prepare_data_process(animal_name)

    static_file = data_fetcher.read_html_file("views/animals_template.html")
    new_html_content = set_dynamic_data(static_file, dynamic_data)

    data_fetcher.write_file("views/animals.html", new_html_content)
    print("Website was successfully generated to the file animals.html.")


def set_dynamic_data(static_file: str, dynamic_data: str) -> str:
    return static_file.replace("__REPLACE_ANIMALS_INFO__", dynamic_data)


def main():
    try:
        animal_name = input("Enter a name of an animal: ")
        create_animals_page(animal_name)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
