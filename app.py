from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask + Traefik</title>
        <style>
            /* Fondo oscuro futurista */
            body {
                margin: 0;
                padding: 0;
                background: #0f172a;
                color: #f8fafc;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
            }

            .container {
                text-align: center;
                padding: 2rem;
                background: rgba(30, 41, 59, 0.7);
                border-radius: 24px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.5);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255,255,255,0.1);
                animation: fadeIn 1.5s ease-out;
            }

            /* Animación del texto con degradado y luces de neón */
            h1 {
                font-size: 3rem;
                font-weight: 800;
                margin-bottom: 1rem;
                background: linear-gradient(45deg, #38bdf8, #c084fc, #f472b6);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-size: 200% auto;
                animation: shine 4s linear infinite, glow 2s ease-in-out infinite alternate;
            }

            /* Animación del Cohete flotando */
            .rocket {
                display: inline-block;
                font-size: 4rem;
                animation: float 3s ease-in-out infinite;
                margin-top: 10px;
            }

            /* Subtítulo dinámico */
            p {
                font-size: 1.2rem;
                color: #94a3b8;
                letter-spacing: 1px;
            }

            /* Keyframes para los efectos */
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }

            @keyframes shine {
                to { background-position: 200% center; }
            }

            @keyframes glow {
                from { text-shadow: 0 0 10px rgba(192, 132, 252, 0.2); }
                to { text-shadow: 0 0 25px rgba(56, 189, 248, 0.6), 0 0 10px rgba(244, 114, 182, 0.4); }
            }

            @keyframes float {
                0% { transform: translateY(0px) rotate(0deg); }
                50% { transform: translateY(-15px) rotate(5deg); }
                100% { transform: translateY(0px) rotate(0deg); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>¡Hola Mundo desde Flask con Traefik!</h1>
            <div class="rocket">🚀</div>
            <p>Estado: <strong>DESPLEGADO CON ÉXITO</strong></p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)