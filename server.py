from flask import Flask, render_template, session, redirect, request
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = "Getting Rich Ninja"

@app.route('/')
def form():
    if 'total_gold' not in session:
        session['total_gold'] = 0
        session['ledger'] = []
    return render_template("index.html")

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

@app.route("/process", methods = ["POST"])
def process_money():
    farm_gold = random.randint(10,20)
    cave_gold = random.randint(5,10)
    dojo_gold = random.randint(2,5)
    casino_gold = random.randint(-50, 50)
    session['time'] = datetime.now()
    if request.form['which_form'] == 'farm':
        session['total_gold'] += farm_gold
        message = f"Wow! You found {farm_gold} gold!"
        color = "green"
    elif request.form['which_form'] == 'cave':
        session['total_gold'] += cave_gold
        message = f"Wow! You found {cave_gold} gold!"
        color = "green"
    elif request.form['which_form'] == 'dojo':
        session['total_gold'] += dojo_gold
        message = f"Wow! You found {dojo_gold} gold!"
        color = "green"
    elif request.form['which_form'] == 'casino':
        session['total_gold'] += casino_gold
        if casino_gold > 0:
            message = f"Wow! You found {casino_gold} gold!"
            color = "green"
        else:
            message = f"Oh No! You lost {casino_gold} gold! Bummer!"
            color = "red"
    session['ledger'].append({'message': message, 'color' : color})
    return redirect("/")

        
        



if __name__ == "__main__":
    app.run(debug = True)