#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    return render_template('index.html', button_python=button_python,button_discord=button_discord,button_html=button_html)


#Результаты формы
@app.route('/submit', methods=['POST'])
def submit_form():
    #Создаём переменные для сбора информации
    email = request.form['email']
    text = request.form['text']
    

    #Записываем данных из формы в файл
    with open('form.txt', 'a') as f:
        f.write(f"{email}\n{text}\n")



    return render_template('index.html', 
                           #Помести переменные
                           email=email,
                           text=text
                           
                           )



if __name__ == "__main__":
    app.run(debug=True)
