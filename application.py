from flask import Flask, render_template, request, jsonify
import requests

application = Flask(__name__)
app = application

# This global variable will hold the current option that is selected in the tablet.
current_option = "duration"  # default option

@app.route('/')
def tablet():  # put application's code here
    return render_template('tablet.html')


@app.route('/set-data', methods=['POST'])
def set_data():
    global current_option
    current_option = request.form.get('data')
    return 'OK', 200


@app.route('/get-data')
def get_data():
    data = requests.get(
        url="https://api.sheety.co/e5585feb09ade54648bc9be7ec7082a4/justinsWorkouts/workouts",
        auth=("jman", "dexter")
    ).json()

    table = data['workouts']

    # filter the table data based on current_option
    if current_option == "duration":
        filtered_table = [[row['date'], row['exercise'], row['duration']] for row in table]
    elif current_option == "calories":
        filtered_table = [[row['date'], row['exercise'], row['calories']] for row in table]

    return jsonify({'option': current_option, 'data': filtered_table})

@app.route('/monitor')
def monitor():
    return render_template('monitor.html')



if __name__ == '__main__':
    app.run()
