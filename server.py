from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def main():
    return render_template("index.html", numberx = 4, numbery = 4, color1 = 'red', color2 = 'black')

@app.route('/4')
def four():
    return render_template("index.html", numberx = 4, numbery = 2, color1 = 'red', color2 = 'black')

@app.route('/<x>/<y>')
def ints(x,y):
    return render_template("index.html", numberx = int(x)//2, numbery = int(y)//2, color1 = 'red', color2 = 'black')

@app.route('/<x>/<y>/<color1>/<color2>')
def intsColor(x,y,color1,color2):
    return render_template("index.html", numberx = int(x)//2, numbery = int(y)//2, color1 = str(color1), color2 = str(color2))


if __name__== "__main__":
    app.run(debug=True)