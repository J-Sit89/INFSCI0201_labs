from flask import Flask, render_template, request, url_for
import segno
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_data_uri = None
    input_message = None

    if request.method == 'POST':
        # Get the message from the form
        input_message = request.form['data']
        
        # Generate the QR code
        qr = segno.make(input_message)
        
        # Save QR code to a binary stream
        buffer = io.BytesIO()
        qr.save(buffer, kind='png', scale=4, border=10)
        buffer.seek(0)

        # Encode image as base64 string
        qr_data_uri = "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render_template('index.html', qr_data_uri=qr_data_uri, input_message=input_message)

if __name__ == '__main__':
    app.run(debug=True)
