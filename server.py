from flask import Flask, render_template

app=Flask(__name__)

@app.route('/',methods=['GET'])
def tableroInicial(x=8,y=8,color1="lightyellow",color2="purple"):
    return render_template('index.html',x=x,y=y,color1=color1,color2=color2)

@app.route('/4',methods=['GET'])
def segundoTablero(x=8,y=4,color1="lightyellow",color2="purple"):
    return render_template('index.html',x=x,y=y,color1=color1,color2=color2)

@app.route('/<int:x>/<int:y>',methods=['GET'])
def tablero_tamaño_variable(x,y,color1="lightyellow",color2="purple"):
    return render_template('index.html',x=x,y=y,color1=color1,color2=color2)

@app.route('/<int:x>/<int:y>/<color1>/<color2>',methods=['GET'])
def tablero_variable_total(x,y,color1,color2):
    return render_template('index.html',x=x,y=y,color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True)