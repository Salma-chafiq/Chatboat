<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ollama Chatbot - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2 {
            color: #333;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 5px;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <h1>Ollama Chatbot</h1>
    <p>Ollama Chatbot est une application interactive construite avec <strong>Streamlit</strong> et <strong>LangChain</strong>. Elle permet aux utilisateurs d'interagir avec un chatbot alimenté par le modèle <strong>LLaMA</strong> via <strong>Ollama</strong>.</p>
    
    <h2>📌 Prérequis</h2>
    <ul>
        <li>Python 3.11+</li>
        <li>Ollama installé (<a href="https://ollama.ai">Télécharger ici</a>)</li>
        <li>Git installé</li>
    </ul>
    
    <h2>🚀 Installation</h2>
    <h3>1️⃣ Cloner le dépôt</h3>
    <pre><code>git clone https://github.com/Salma-chafiq/Chatboat.git
cd Chatboat</code></pre>
    
    <h3>2️⃣ Créer un environnement virtuel</h3>
    <pre><code>python -m venv venv</code></pre>
    
    <h3>3️⃣ Activer l'environnement virtuel</h3>
    <p><strong>Sous Windows :</strong></p>
    <pre><code>venv\Scripts\Activate</code></pre>
    <p><strong>Sous macOS/Linux :</strong></p>
    <pre><code>source venv/bin/activate</code></pre>
    
    <h3>4️⃣ Installer les dépendances</h3>
    <pre><code>pip install -r requirements.txt</code></pre>
    
    <h2>💬 Exécution du Chatbot</h2>
    <p>Ouvrir un terminal dans VS Code ou votre éditeur préféré et exécuter la commande suivante :</p>
    <pre><code>streamlit run app.py</code></pre>
    <p>Une fois lancé, vous pourrez interagir avec le chatbot via l'interface Streamlit.</p>
    
    <h2>✨ Fonctionnalités</h2>
    <ul>
        <li>Interface interactive avec Streamlit.</li>
        <li>Gestion de l'historique des messages.</li>
        <li>Réponse rapide grâce à LLaMA via Ollama.</li>
        <li>Mesure du temps de réponse du chatbot.</li>
    </ul>
    
    <h2>📌 Améliorations possibles</h2>
    <ul>
        <li>Ajouter une persistance des conversations avec une base de données.</li>
        <li>Permettre le choix entre différents modèles d'IA.</li>
        <li>Intégrer une interface plus avancée avec des boutons et options supplémentaires.</li>
    </ul>
    
    <h2>📜 Licence</h2>
    <p>Ce projet est sous licence MIT.</p>
    
    <h2>👤 Auteur</h2>
    <p>Salma Chafiq</p>
</body>
</html>
