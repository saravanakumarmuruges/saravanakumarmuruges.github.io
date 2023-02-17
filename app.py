from flask import Flask, render_template, url_for, request, redirect
import csv
from flask_flatpages import FlatPages
app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/works.html')
def blogs():
    return render_template('works.html')


# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n{email},{subject},{message}')
#
#
# def write_to_csv(data):
#     with open('database.csv', newline='', mode='a') as database2:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow([email, subject, message])
#
#
# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         try:
#             data = request.form.to_dict()
#             write_to_csv(data)
#             return redirect('/thankyou.html')
#         except Exception as e:
#             err = e
#             return 'did not save to database'
#     else:
#         return 'something went wrong. Try again!'


if __name__ == '__main__':
    app.run(port=8000)
