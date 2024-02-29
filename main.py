from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Example: Extract all paragraph texts
            paragraphs = soup.find_all('p')
            extracted_text = '\n'.join([p.get_text() for p in paragraphs])
            print(paragraphs)
            print(extracted_text)
            # Display extracted text in preformatted text
            return f'<pre>{extracted_text}</pre>'
        except requests.exceptions.RequestException as e:
            return f'Error fetching the URL: {e}'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
