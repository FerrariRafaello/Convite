# Convite de Aniversário Interativo – Flask + Python

Este é um projeto de convite de aniversário interativo construído com **Python (Flask)** no backend e HTML/CSS/JS moderno no frontend. Ao confirmar presença, o nome é enviado via e-mail para o organizador automaticamente.

## Tecnologias utilizadas

- **Backend:** Python 3, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Email:** smtplib com Gmail (senha de app)
- **Template engine:** Jinja2 (padrão Flask)
- **Hospedagem:** pode ser executado localmente ou em qualquer serviço de deploy Python

## ️ Como executar localmente

1. **Clone o repositório**
   ```bash
   git clone https://github.com/SEU_USUARIO/SEU_REPO.git
   cd convite-aniversario-flask
Instale as dependências

bash
Copy code
pip install -r requirements.txt
Configure a senha de app

Gere uma senha de app no Google App Passwords

Substitua no arquivo app.py:

python
Copy code
server.login('SEU_EMAIL@gmail.com', 'SUA_SENHA_DE_APP')
Execute o servidor

bash
Copy code
python app.py
Acesse em http://127.0.0.1:5000/

Estrutura do projeto
markdown
Copy code
convite-aniversario-flask/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── templates/
    └── convite.html
Sobre o envio de e-mail
Ao confirmar presença, o nome digitado é enviado automaticamente para o e-mail configurado.

É necessário usar senha de app do Gmail.

Licença
MIT License – Livre para uso, modificação e aprendizado.

=======
# convite
>>>>>>> c0c00d87583a1f931691e25007764ce8554f99f5
