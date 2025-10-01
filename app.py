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
            <!-- 확대/축소 막기 -->
            <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
            <title>Instagram</title>
            <style>
            :root{
            --bg: #000000;
            --btn: #0064E0;
            --muted: rgba(255,255,255,0.58);
            --input-border: rgba(255,255,255,0.2);
    }
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background: #000000;
                }
                h1 {
                    font-size: 3em;
                    color: #ffffff;
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
