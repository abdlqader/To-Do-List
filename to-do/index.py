from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__, template_folder="templates")

todos =[{"task":"study", "done":False}]



#home
@app.route("/")
def index():
    return render_template("templates.html", todos=todos)

#addition
@app.route("/add", methods=["POST"])
def add():
    todo = request.form['todo']
    todos.append({"task":todo, "done": False})
    return redirect(url_for("index"))

#editing
@app.route("/edit/<int:index>", methods =["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo['task'] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)
    
#strike
@app.route("/check/<int:index>")
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for("index"))

#deleting
@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))


if __name__ =='__main__':
    app.run(debug=True)

