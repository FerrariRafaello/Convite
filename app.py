from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def convite():
    return render_template('convite.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    name = data.get('name', '').strip()
    if not name:
        return jsonify({'status': 'fail', 'reason': 'Nome não enviado.'}), 400

    msg = MIMEText(f"Olá, você tem uma nova confirmação de presença:\nNome: {name}")
    msg['Subject'] = 'Confirmação de Presença'
    msg['From'] = 'bellazaqueu@gmail.com'
    msg['To'] = 'bellazaqueu@gmail.com'

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login('bellazaqueu@gmail.com', 'kaie apcx anxo mybq')
            server.send_message(msg)
        print(f"Email enviado para: {msg['To']} ({name})")
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        print("Erro ao enviar email:", e)
        return jsonify({'status': 'fail', 'reason': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
