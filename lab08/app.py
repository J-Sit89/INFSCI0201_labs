from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import apod_api

app = Flask(__name__)
app.secret_key = 'your_secret_key' 


@app.route('/')
def home():
    try:
        apod_data = apod_api.get_apod()
        return render_template('home.html', apod=apod_data)
    except Exception as e:
      
        return render_template('error.html', message="Error fetching today's APOD. Please try again later.")


@app.route('/history', methods=['GET', 'POST'])
def history():
    today = datetime.now().date() 
    selected_date = None

    if request.method == 'POST':
        selected_date = request.form.get('date')  
        
    return render_template('history.html', today=today, selected_date=selected_date)

    
if __name__ == '__main__':
    app.run(debug=True)
