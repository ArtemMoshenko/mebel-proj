from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return "Колонизация Марса"

@app.route('/index')
def index2():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def index3():
    return render_template("promotion.html")

@app.route('/image_sample')
def image4():
    return render_template("image_sample.html")

@app.route('/promotion_image')
def image5():
    return render_template("promotion_image.html")

@app.route('/astronaut_selection')
def image6():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1>Анкета претендента</h1>
                                <h2>на участие в миссии</h2>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="name" class="form-control" id="name" aria-describedby="emailHelp" placeholder="Введите фамилию" name="email">
                                        <input type="2name" class="form-control" id="2name" placeholder="Введите имя" name="password">
                                        <h1> 
                                        
                                        </h1>
                                        <input type="email" class="form-control" id="email" placeholder="Введите почту" name="email">
                                    
                                        <h1> 
                                        
                                        </h1>
                                        
                                        <div class="form-group">
                                            <label for="classSelect">Какое у Вас образование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                              <option>Высшее</option>
                                              <option>Нет образования</option>
                                            </select>
                                         </div>
                                        <h1> 
                                        
                                        </h1>
                                        <div class="form-group">
                                            <label for="form-check">Ваша профессия?</label>
                                            
                                                <div class="form-group form-check">
                                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                    <label class="form-check-label" for="acceptRules">инженер-исследователь</label>
                                                </div>
                                                
                                                <div class="form-group form-check">
                                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                    <label class="form-check-label" for="acceptRules">пилот</label>
                                                </div>
                                                
                                                <div class="form-group form-check">
                                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                    <label class="form-check-label" for="acceptRules">строитель</label>
                                                </div>
                                                
                                                <div class="form-group form-check">
                                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                    <label class="form-check-label" for="acceptRules">экзобиолог</label>
                                                </div>
                                                
                                                <div class="form-group form-check">
                                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                    <label class="form-check-label" for="acceptRules">врач</label>
                                                </div>
                                                
                                                <div class="form-group form-check">
                                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                    <label class="form-check-label" for="acceptRules">инженер по терраформированию</label>
                                                </div>
                                                
                                                <div class="form-group form-check">
                                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                    <label class="form-check-label" for="acceptRules">специалист по радиационной защите</label>
                                                </div>
                                                
                                                <div class="form-group form-check">
                                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                    <label class="form-check-label" for="acceptRules">астрогеолог</label>
                                                </div>
                                                
                                                <div class="form-group form-check">
                                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                    <label class="form-check-label" for="acceptRules">гляциолог</label>
                                                </div>
                                                
                                                <div class="form-group form-check">
                                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                    <label class="form-check-label" for="acceptRules">инженер жизнеобеспечения</label>
                                                </div>
                                                
                                                <div class="form-group form-check">
                                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                    <label class="form-check-label" for="acceptRules">метеоролог</label>
                                                </div>
                                                
                                                
                                              </label>
                                            </div>
                                        <h1> 
                                        
                                        </h1>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <h1> 
                                        
                                        </h1>
                                        <div class="form-group">
                                            <label for="about">Почему хотите принять участие></label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <h1> 
                                        
                                        </h1>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <h1> 
                                        
                                        </h1>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <h1> 
                                        
                                        </h1>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готов остаться на Марсе))</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')