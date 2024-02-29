from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        try:
            response = requests.get(url)
            return f'<pre>{response.text}</pre>'  # Display content in preformatted text
        except requests.exceptions.RequestException as e:
            return f'Error fetching the URL: {e}'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
