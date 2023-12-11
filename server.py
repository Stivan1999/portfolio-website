from flask import Flask, render_template, request, redirect, send_file
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Homepage.html')


@app.route('/<string:page_name>')
def load_html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', mode='a', newline="") as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",", quoting=csv.QUOTE_MINIMAL,
                                )
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("./thank_you.html")
    else:
        return 'Something went wrong!!'


@app.route('/download')
def download_file():
    file = "Youssef's Resume.docx"
    return send_file(file, as_attachment=True)
