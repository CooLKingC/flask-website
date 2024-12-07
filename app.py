from flask import Flask,render_template,request,redirect
import os


basedir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(basedir, 'template')

app = Flask(__name__,template_folder=template_dir)

LANGUAGES = ["Java","C","Python","C++"]
REGISTRANTS= {}



@app.route("/")
def index() :
    return render_template("index.html",languages=LANGUAGES)


@app.route("/greet",methods=["POST"])
def greet() :
    name = request.form.get("name")
    return render_template("greet.html",name = name)


@app.route("/register",methods=["POST"])
def register() :
    # if not request.form.get("name") :
    #     return render_template("RegisterError.html")

    # for language in request.form.getlist("language") :
    #     if language not in LANGUAGES :
    #         return render_template("RegisterError.html")
    name = request.form.get("name") 
    if not name :
        return render_template("RegisterError.html")
    
    language = request.form.get("language")
    if not language or language not in LANGUAGES :
        return render_template("RegisterError.html")
    
    REGISTRANTS[name] = language 

    # return render_template("RegisterSuccess.html")
    return redirect("/registry")


@app.route("/registry")
def registry() :
    return render_template("registry.html",registrants=REGISTRANTS)
    

if __name__ == '__main__' :
    app.run(debug=True)