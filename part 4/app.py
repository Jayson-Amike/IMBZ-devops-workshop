from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# A secret key is required to use Flask's flash messaging
app.secret_key = 'your_secret_key_here' 

@app.route('/', methods=['GET', 'POST'])
def index():
    greeting = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if name:
            greeting = f"Hello, {name}! Welcome to your Flask app."
            flash('Name submitted successfully!', 'success')
        else:
            flash('Please enter a valid name.', 'danger')
            
    return render_template('index.html', greeting=greeting)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # Debug mode allows the server to auto-reload when you change code
    app.run(host='0.0.0.0', port=5000, debug=True)