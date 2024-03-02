from flask import Flask, render_template
from resort import Resort

app = Flask(__name__)

@app.route('/')

# Create instances of the Resort class
resort1 = Resort(name="Breckenridge", city="Breckenridge, Colorado", api_key=api_key)
resort2 = Resort(name="Kirkwood", city="Kirkwood, California", api_key=api_key)

resort1.get_weather()
resort2.get_weather()

def index():
    return render_template('index.html', resorts=[resort1, resort2])

if __name__ == '__main__':
    app.run(debug=True)
