# Unit Converter

A simple web application built with Flask that converts between different units of measurement: length, weight, and temperature.

## Features

- **Length Converter**: millimeter, centimeter, meter, kilometer, inch, foot, yard, mile
- **Weight Converter**: milligram, gram, kilogram, ounce, pound
- **Temperature Converter**: Celsius, Fahrenheit, Kelvin
- Clean, responsive UI with custom CSS styling
- Simple navigation between converters

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Jinja2 (templating)

## Project Structure

```
Unit_Converter/
│
├── app.py
├── templates/
│   ├── length.html
│   ├── weight.html
│   └── temperature.html
└── static/
    ├── style.css
    └── background.jpg
```

## How to Run

1. Clone the repository:
   ```
   git clone <your-repo-url>
   cd Unit_Converter
   ```

2. Install Flask:
   ```
   python -m pip install flask
   ```

3. Run the app:
   ```
   python app.py
   ```

4. Open your browser and go to:
   ```
   http://127.0.0.1:5000/length
   ```

## How It Works

Each conversion page has a form where the user enters a value and selects the units to convert from and to. When the form is submitted, Flask processes the input using a conversion function and returns the result on the same page.

- **Length and Weight**: Values are converted to a base unit (meters / grams) first, then to the target unit.
- **Temperature**: Direct formulas are used for each conversion pair (Celsius, Fahrenheit, Kelvin).

## Author

Built by Jo as a learning project for Flask and web development fundamentals.

## Project Page

[roadmap.sh project](https://roadmap.sh/projects/unit-converter)
