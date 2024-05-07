from flask import Flask, render_template
from lanche import lanches

app = Flask(__name__)
joelho = lanches("Joelho", "R$5,90 reais", "O preparo da massa é bem simples. Feita à base de batata, ela também ganha ovo, óleo, leite, açúcar e sal como ingredientes.","/static/images/joelho2.jpg",1 )
bolodepote = lanches("Bolo de Pote", "R$ 7,90 reais", "os bolos de pote são mais molhadinhos para garantir que as garfadas no potinho trarão um doce cremoso e fácil de degustar","/static/images/bolodepote2.jpg",2)
paodequeijo = lanches("Pão de Queijo","R$5 reais", "consiste basicamente em um tipo de biscoito de polvilho azedo ou doce acrescido de ovos, sal, óleo vegetal e queijo","/static/images/paodequeijo2.webp",3 )
catalogolanches = [joelho, bolodepote, paodequeijo]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lanche')
def lanchenois():
    return render_template('catalogodelanches.html', lanches = catalogolanches)

@app.route('/opinioes')
def forms():
    return render_template('forms.html')


@app.route("/lanches/<int:id>")
def lanche(id:int):
    for lanche in catalogolanches:
        if lanche.id == id:
            return render_template("lanchesdesc.html", lanche=lanche)
    return "<h1>Ops! Lanche não encontrado!</h1>"
if __name__ == '__main__':
    app.run()