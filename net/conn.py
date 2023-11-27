from flask import Flask, request
from bs4 import BeautifulSoup
import socket, requests, threading
import ngrok

global url_s
ip = "192.168.1.8:8080"

def host(): 
     
     url_ngk = ngrok.connect(ip) 
     url_ngrok = url_ngk.url()  
     print(url_ngrok)  
     url_s = url_ngrok
     input()

th1 = threading.Thread(target=host)

app = Flask(__name__)

# ngrok_server = input("Ngrok: ")

# response = requests.get(ngrok_server) 

listener = ngrok.connect("192.168.1.8:8080")
f = listener.url()
    # Output ngrok url to console
print(f"Ingress established at {listener.url()}")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        response = requests.get(url_s).text
        print(username, password)
        print(response)

        g = BeautifulSoup(response.text, "html.parser") 
        
        for i in g.find_all("type"):
            print(i)

  
    else:
        return """
<!DOCTYPE html>
<html>

<head>
    <title>Окно входа</title>
    <style>
        body {
            background-color: #f2f2f2;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 300px;
            margin: 100px auto;
            background-color: white;
            border: 1px solid #ccc;
            padding: 20px;
            text-align: center;
        }

        h1 {
            margin-top: 0;
        }

        input[type=text],
        input[type=password] {
            width: 100%;
            padding: 12px 20px;
            margin: 8px 0;
            display: inline-block;
            border: 1px solid #ccc;
            box-sizing: border-box;
        }

        button {
            background-color: #4CAF50;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            cursor: pointer;
            width: 100%;
        }

        button:hover {
            opacity: 0.8;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>Регистрация</h1>
        <form action="register" method ="POST">
            <input type="text" placeholder="Логин" name="username" required><br>
            <input type="password" placeholder="Пароль" name="password" required><br>
            <button type="submit">Войти</button>
        </form>
    </div>
</body>
</html>
        """
   
    
if __name__ == '__main__':
    th1.start()
    app.run(debug=True, host = '0.0.0.0', port=8080)  
    # Establish connectivity

