# Canyoning Portugal Web App

#### VIDEO DEMO:
    https://youtu.be/4vJdlTMjVNo

#### Description:
    My name is Rui Pereira, and I'm excited to present my final project submission for CS50P Introduction to Programming with Python. This project addresses my personal passion for canyoning by providing a comprehensive guide to various rivers, including associated weather conditions.

    Project Overview:

    This web application allows users to explore information about canyoning rivers in Portugal. In this web application users can start choosing a city, afterwards they can select a river within that city, then view detailed information about the selected river, and even if want to they can download a pdf contaning a more detailed information about the river.

## Project Structure

The project is structured as follows:

- **app.py**: This file is store in the main project folder, its the main python script orchestrating the whole program.
- **static/**: Folder containing static files (e.g., stylesheets).
- **static/styles.css**: file that contains all the style for every visual 'upgrade' on each template.
- **templates/**: Folder containing HTML templates.
- **templates/index.html**: the main template the user sees when using the web app allowing them to se every available city based on information given by the database
- **templates/choose_river.html**: the template the user sees when using the web app allowing them to se every available river on the chosen city, this information is given based on the database.
- **templates/view_river.html**: the template the user sees when using the web app after choosing the river, and getting all the information about the river and gives the option for the user to see the .pdf file containing a more technical guide through the river
- **canyonings.db**: SQLite database file. This database stores information of every city that has available and trustworthy croquis. The database schema is structed on 2 tables
table city (id INTEGER PRIMARY KEY, Name TEXT NOT NULL);
table river (id INTEGER PRIMARY KEY AUTOINCREMENT, city_id INTEGER, start_coord TEXT, end_coord TEXT, river_length INTEGER, highest_rappel INTEGER, croqui TEXT, name TEXT, FOREIGN key(city_id) REFERENCES city(id));

## Getting Started

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the Flask application:

    ```bash
    python app.py
    ```

## Dependencies

- Flask
- CS50 (for SQLite database access)

## Usage

1. Visit the main page and choose a city.
2. Select a river in the chosen city.
3. View detailed information about the selected river.

## Contributing

If you'd like to contribute to this project, please follow the standard GitHub fork and pull request workflow.
