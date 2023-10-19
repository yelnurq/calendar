from flask import Flask, render_template, request

events = [
    {
        'title':'Конференция',
        'start':'2023-10-27',
        'end':'2023-10-27'
},
    {
        'title':'Обед',
        'start':'2023-10-27T13:00',
        'end':'2023-10-27T13:00'
    },
    {
        'title':'Экзамен СФЕК',
        'start':'2023-10-06',
        'end':'2023-10-12'
    },
    {
        'title':'Посвящение в колледже',
        'start':'2023-10-28',
        'end':'2023-10-28'
    },
    {
        'title':'Начинается',
        'start':'2023-10-28T16:00',
        'end':'2023-10-28T18:00'
    },
    {
        'title':'Дежурство',
        'start':'2023-10-29T13:40',
        'end':'2023-10-30'
    },
    {
        'title': 'Дежурство',
        'start': '2023-10-01T13:40',
        'end': '2023-10-02'
    },
]




app = Flask(__name__)


@app.route('/test')
def test():
    return render_template('tet.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calendar')
def calendar():  # put application's code here
    return render_template('cal.html', events=events)

@app.route('/add', methods=["POST","GET"])
def add():
    if request.method == 'POST':
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']

        events.append(
            {
                'title':title,
                'start':start,
                'end':end,
            },
        )
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
