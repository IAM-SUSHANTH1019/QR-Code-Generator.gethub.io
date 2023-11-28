# from flask import Flask, render_template, request
# from PIL import Image, ImageTk
# import qrcode
# import io
# import base64

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/generate_qr', methods=['POST'])
# def generate_qr():
#     data = request.form.get('text_entry')

#     if data:
#         # Generate QR Code
#         img = qrcode.make(data)
#         res_img = img.resize((280, 250))

#         # Convert to base64
#         buffered = io.BytesIO()
#         res_img.save(buffered, format="PNG")
#         img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

#         return render_template('index.html', qr_image=img_str)
#     else:
#         return render_template('index.html', warning='Enter Data in Entry First')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request
from PIL import Image
import qrcode
import io
import base64

app = Flask(__name__)

# History list to store previously generated QR codes
history = []

@app.route('/')
def home():
    return render_template('index.html', history=history)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form.get('text_entry')

    if data:
        # Generate QR Code
        img = qrcode.make(data)
        res_img = img.resize((280, 250))

        # Convert to base64
        buffered = io.BytesIO()
        res_img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

        # Add entry to history
        history.append({'data': data, 'qr_image': img_str})

        return render_template('index.html', qr_image=img_str, history=history, data=data)
    else:
        return render_template('index.html', warning='Enter Data in Entry First', history=history)

if __name__ == '__main__':
    app.run(debug=True)
