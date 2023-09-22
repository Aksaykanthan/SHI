
from flask import Flask, request, render_template
import google.generativeai as palm


palm.configure(api_key='AIzaSyAzplS0hwYRZ459sPcxF6APUWHOdI0Igd8')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name



app = Flask(__name__)

chats = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["user_input"]
        
        answer = palm.generate_text(model=model,prompt=prompt,temperature=0,max_output_tokens=800)
        
        chat = {"question" : prompt,"answer":answer.result}
        chats.append(chat)        
        
        return render_template("home.html",chats=chats)
    else:
        return render_template("home.html")
    
    


if __name__ == "__main__":
    app.run(debug=True)