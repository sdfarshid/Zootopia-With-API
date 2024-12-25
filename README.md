# Animals Web Page Generator

This project is a Python-based application designed to fetch, process, and generate a dynamic web page showcasing information about animals. The application uses data from the API Ninjas Animals API and creates an HTML file with the retrieved information.

## Features

- Fetch animal data from the API Ninjas Animals API.
- Save fetched data locally in JSON format.
- Dynamically generate an HTML page displaying animal information.

## Prerequisites

Before running this project, ensure you have the following installed on your system:

- Python 3.9 or above
- `pip` package manager

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and set the following environment variables:

   ```env
   API_KEY=your_api_key_here
   Template_PATH=views/animals_template.html
   BASE_SOURCE_FILE=Storage/animals.json
   ```

## Usage

1. **Run the main script:**

   ```bash
   python animals_web_generator.py
   ```

    - Enter the name of an animal when prompted.
    - The application fetches data from the API, processes it, and generates an `animals.html` file in the `views/` directory.


## Dependencies

This project uses the following Python libraries:

- `requests`: For making HTTP requests to the API.
- `python-dotenv`: For loading environment variables from the `.env` file.

To install these dependencies, run:

```bash
pip install -r requirements.txt
```

## API Information

This project uses the [API Ninjas Animals API](https://api-ninjas.com/api/animals) to fetch data about animals. Ensure you have a valid API key and include it in the `.env` file as `API_KEY`.

## Error Handling

- If the animal data doesn't exist in the API, the application raises an error:

  ```
  <h2>The animal {animal_name} doesn't exist.</h2>
  ```
- For existing data, the application uses locally saved data unless the user opts to fetch new data.

## Generated HTML Example

The dynamically generated HTML will include:

- Name
- Diet
- Type
- Location

For example:

```html
<li class="cards__item">
  <div class="card__title">Lion</div>
  <p class="card__text">
    <strong>Diet:</strong> Carnivore<br/>
    <strong>Location:</strong> Africa<br/>
    <strong>Type:</strong> Mammal<br/>
  </p>
</li>
```

## License

This project is licensed under the MIT License.

