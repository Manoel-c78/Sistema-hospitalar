from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "chave_secreta_hospitalar"  # Necessário para usar mensagens flash

# Simulação de banco de dados de profissionais de saúde
USUARIOS_VALIDOS = {
    "1-PE": {"senha": "1010", "nome": "Dr. Lucas", "cargo": "Médico"},
    "2-PE": {"senha": "2020", "nome": "Enf. João Santos", "cargo": "Enfermeiro"},
    "3-PE": {"senha": "3030", "nome": "Esdras", "cargo": "Almoxarifo"}
}


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        registro = request.form.get("registro")
        senha = request.form.get("senha")

        # Validação do login
        if registro in USUARIOS_VALIDOS and USUARIOS_VALIDOS[registro]["senha"] == senha:
            nome = USUARIOS_VALIDOS[registro]["nome"]
            return f"<h1>Bem-vindo(a), {nome}!</h1><p>Acesso concedido ao Prontuário Eletrônico.</p>"
        else:
            flash("Registro Profissional ou senha incorretos.", "danger")

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)