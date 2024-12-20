import json
import os
import time

import Api

BASE_SOURCE_FILE = 'Storage/animals_data.json'
BASE_ANIMAL = 'Fox'


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_html_file(file_path: str) -> str:
    """ Loads a Html file """
    file = open(file_path, "r")
    content = file.read()
    file.close()
    return content


def write_file(file_path: str, content: str) -> None:
    """ Loads a Html file """
    file = open(file_path, "w")
    content = file.write(content)
    file.close()


def fetch_data(animals_datas: list[dict]) -> list[dict]:
    return [
        {
            "Name": animal_data.get("name", False),
            "Diet": animal_data["characteristics"].get("diet", False),
            "Type": animal_data["characteristics"].get("type", False),
            "skin_type": animal_data["characteristics"].get("skin_type", False),
            "Location": animal_data["locations"][0] if animal_data["locations"] else False,
        }
        for animal_data in animals_datas
    ]


def generate_string_output(animals_datas: list[dict]) -> str:
    output = ""
    for animal_data in animals_datas:
        name = animal_data.get("Name", "")
        diet = animal_data.get("Diet", "")
        type_ = animal_data.get("Type", "")
        location = animal_data.get("Location", "")

        output += '<li class="cards__item">\n'
        if name:
            output += f'  <div class="card__title">{name}</div>\n'
        output += '  <p class="card__text">\n'
        if diet:
            output += f'    <strong>Diet:</strong> {diet}<br/>\n'
        if location:
            output += f'    <strong>Location:</strong> {location}<br/>\n'
        if type_:
            output += f'    <strong>Type:</strong> {type_}<br/>\n'
        output += '  </p>\n'
        output += '</li>\n'

    return output


def set_dynamic_data(static_file: str, dynamic_data: str) -> str:
    return static_file.replace("__REPLACE_ANIMALS_INFO__", dynamic_data)


def get_skin_types(animals_datas: list[dict]) -> set:
    skin_types = set()
    for animal_data in animals_datas:
        skin_type = animal_data.get("characteristics", {}).get("skin_type")
        if skin_type:
            skin_types.add(skin_type)
    return skin_types


def show_available_skins() -> None:
    skin_types = get_skin_types(load_data(BASE_SOURCE_FILE))
    print("Available skin types:")
    for skin_type in skin_types:
        print(f"- {skin_type}")


def get_final_animal_data() -> list[dict]:
    return fetch_data(load_data(BASE_SOURCE_FILE))


def is_file_exist(file_path =BASE_SOURCE_FILE):
    return  os.path.isfile(file_path)


def create_source_data():

    while not is_file_exist():
        response_data = Api.process_fetching_data_from_API(BASE_ANIMAL)
        if response_data:
            write_file(BASE_SOURCE_FILE, response_data)
            break
        else:
            print("Waiting for data from API...")
            time.sleep(5)


def create_animals_page():
    create_source_data()
    animals_data = get_final_animal_data()
    dynamic_data = generate_string_output(animals_data)
    static_file = read_html_file("views/animals_template.html")
    new_html_content = set_dynamic_data(static_file, dynamic_data)
    write_file("views/animals.html", new_html_content)


def run_create_filtered_animals_page():
    animals_data = get_final_animal_data()
    show_available_skins()
    selected_skin_type = input("\nEnter a skin type from the above list: ")
    filtered_data = filter_animals(animals_data, "skin_type", selected_skin_type)
    dynamic_data = generate_string_output(filtered_data)
    print(filtered_data)
    print(dynamic_data)
    static_file = read_html_file("views/animals_template.html")
    new_html_content = set_dynamic_data(static_file, dynamic_data)
    write_file(f"{selected_skin_type}-animals.html", new_html_content)


def filter_animals(animals_data: list[dict], key: str, value: str) -> list[dict]:
    """
    Filters the list of animals based on a key-value pair.

    :param animals_data: List of animal dictionaries.
    :param key: The key to filter on (e.g., "skin_type").
    :param value: The value to match for the given key (e.g., "Fur").
    :return: A filtered list of animal dictionaries.
    """
    return [animal for animal in animals_data if animal.get(key) == value]


def main():

     create_animals_page()


if __name__ == "__main__":
    main()
