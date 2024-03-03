from flask import Flask, render_template, request
from .resorts import Resorts

app = Flask(__name__)

api_key= "9f6930e1d6505ed136bd2863a790dab8"

# Create instances of the Resort class
resort1 = Resorts(city_name="Breckenridge, Colorado")
resort2 = Resorts(city_name="Kirkwood, California")

resort1._get_weather_data(city_name="Breckenridge, Colorado")
resort2._get_weather_data(city_name="Kirkwood, California")

resorts = [resort1, resort2]

@app.route('/', methds=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']

        new_resort = Resorts(city_name=city)
        new_resort.get_weather()
        resorts.append(new_resort)
    
    return render_template('index.html', resorts=resorts)

if __name__ == '__main__':
    app.run(debug=True)
