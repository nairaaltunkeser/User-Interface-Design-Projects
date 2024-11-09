from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/iso1')
def iso1():
    return render_template('iso1.html')

@app.route('/iso2')
def iso2():
    return render_template('iso2.html')

@app.route('/iso3')
def iso3():
    return render_template('iso3.html')

@app.route('/iso_quiz')
def iso_quiz():
    iso_images = ['ISO100.png', 'ISO200.png', 'ISO400.png', 'ISO800.png', 'ISO1600.png']
    random_iso_image = random.choice(iso_images)
    return render_template('iso_quiz.html', random_iso_image=random_iso_image)


@app.route('/shutter_1')
def shutter_1():
    return render_template('shutter_1.html')

@app.route('/shutter_2')
def shutter_2():
    return render_template('shutter_2.html')

@app.route('/shutter_3')
def shutter_3():
    return render_template('shutter_3.html')

@app.route('/shutter_4')
def shutter_4():
    return render_template('shutter_4.html')

@app.route('/shutter_5')
def shutter_5():
    return render_template('shutter_5.html')

@app.route('/shutter_quiz')
def shutter_quiz():
    speeds = ['500', '250', '125', '60', '30', '15', '8', '4', '2']
    images = ['shutter_1-' + speed + '.png' for speed in speeds]

    items = list(zip(speeds, images))
    random.shuffle(items)  # Shuffle the list of tuples

    return render_template('shutter_quiz.html', items=items)


@app.route('/aperture_1')
def aperture_1():
    return render_template('aperture_1.html')

@app.route('/aperture_2')
def aperture_2():
    return render_template('aperture_2.html')

@app.route('/aperture_3')
def aperture_3():
    return render_template('aperture_3.html')

@app.route('/aperture_4')
def aperture_4():
    return render_template('aperture_4.html')

@app.route('/aperture_quiz')
def aperture_quiz():
    aperture_images = [
        'aperture_f2.png',
        'aperture_f4.png',
        'aperture_f5.png',
        'aperture_f8.png',
        'aperture_f11.png',
        'aperture_f16.png'
    ]
    random_aperture_image = random.choice(aperture_images)
    return render_template('aperture_quiz.html', random_aperture_image=random_aperture_image)


@app.route('/quiz_1')
def quiz_1():
    return render_template('quiz_1.html')
@app.route('/quiz_2')
def quiz_2():
    return render_template('quiz_2.html')
@app.route('/quiz_3')
def quiz_3():
    return render_template('quiz_3.html')
@app.route('/results_1')
def results_1():
    return render_template('results_1.html')

if __name__ == '__main__':
    app.run(debug=True)
