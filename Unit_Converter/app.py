from flask import Flask, render_template, request

app = Flask(__name__)

def convert_length(value, from_unit, to_unit):
    # Convert everything to meters first
    to_meters = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1,
        'km': 1000,
        'inch': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mile': 1609.34
    }
    
    value_in_meters = value * to_meters[from_unit]
    result = value_in_meters / to_meters[to_unit]
    return round(result, 4)

def covert_weight(value, from_unit, to_unit):
    # convert everything to grams first
    to_grams = {
        'mg': 0.001,
        'g': 1,
        'kg': 1000,
        'oz': 28.3495,
        'lb': 453.592
    }
    value_in_grams = value * to_grams[from_unit]
    result = value_in_grams / to_grams[to_unit]
    return round(result, 4)

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'C' and to_unit == 'F':
        return round((value * 9/5) + 32, 2)
    elif from_unit == 'F' and to_unit == 'C':
        return round((value - 32) * 5/9, 2)
    elif from_unit == 'C' and to_unit == 'K':
        return round(value + 273.15, 2)
    elif from_unit == 'K' and to_unit == 'C':
        return round(value - 273.15, 2)
    elif from_unit == 'F' and to_unit == 'K':
        return round((value - 32) * 5/9 + 273.15, 2)
    elif from_unit == 'K' and to_unit == 'F':
        return round((value - 273.15) * 9/5 + 32, 2)
@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = temperature_conversion(value, from_unit, to_unit)
    return render_template('temperature.html', result=result)



@app.route('/weight', methods=['GET', 'POST'])
def weight():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = covert_weight(value, from_unit, to_unit)
    return render_template('weight.html', result=result)

@app.route('/length', methods=['GET', 'POST'])
def length():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = convert_length(value, from_unit, to_unit)
    return render_template('length.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

