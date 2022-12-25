from flask import Flask, request, redirect, flash, render_template, send_from_directory
from werkzeug.utils import secure_filename
from gpt_summarize import summarize_bullet_points
from pdf_reader import pdf_to_text
import os
import PyPDF2

app = Flask(__name__, static_url_path='/static')

key = "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"


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:

            # Read the file
            text = pdf_to_text(file, 3000)

            # Summarize the text
            summary = summarize_bullet_points(text, key)

            #return the summary with new lines between each bullet point
            return '<br>'.join(summary)

            return page

    return render_template('summarize.html')


if __name__ == '__main__':
    app.run()
