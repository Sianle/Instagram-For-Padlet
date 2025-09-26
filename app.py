#app.py
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Instagram for Padlet</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background: #f0f0f0;
                }
                h1 {
                    font-size: 3em;
                    color: #333;
                }
            </style>
        </head>
        <body>
            <h1>Instagram for padlet</h1>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
