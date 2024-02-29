from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use the OPENAI_API_KEY from the .env file
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)



app = Flask(__name__)





@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Example: Extract all paragraph texts
            paragraphs = soup.find_all('body')
            extracted_text = '\n'.join([p.get_text() for p in paragraphs])
            summarize_text = getOpenAIresponse(extracted_text)
            #print("here's the summary")
            #print(summarize_text)
            
            # Display extracted text in preformatted text
            return f'<p>{summarize_text}</p>'
        except requests.exceptions.RequestException as e:
            return f'Error fetching the URL: {e}'
    else:
        return render_template('index.html')




def getOpenAIresponse(pageText):
    completion = client.chat.completions.create(
    model="gpt-4-32k-0613",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that summarizes text. Summarize this -"},
        {"role": "user", "content": pageText}
    ]
    )

    return (completion.choices[0].message.content)
    




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)


