from flask import Flask, render_template, redirect, request
  
# creates a Flask application 
app = Flask(__name__) 
  
  
@app.route("/") 
def loginpage(): 
    return render_template('index.html') 

@app.post("/login") 
def login(): 
    if ((request.form['username']=="username") & (request.form['password']=="password")):
        return redirect("/success.html", code=200)
    else:
        return redirect("/failed.html", code=200)
  
@app.route("/failed.html") 
def failedpage(): 
    return render_template('failed.html') 

@app.route("/success.html") 
def successpage():
    return render_template('success.html') 

# run the application 
if __name__ == "__main__": 
    app.run(debug=True)
