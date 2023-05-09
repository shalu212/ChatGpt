import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"

def training_data(data):
    return """please predict text as positive or negative.
    text: you are a bad man
    sentiment: negative
    text: you are good man
    sentiment: positive
    text: {}
    sentiment: """.format(data.capitalize())

@app.route('/', methods=("GET", "POST"))
def index():
    if request.method == "POST":
        data = request.form["data"]
        res = openai.Completion.create(ssh -i "authentication.pem" ubuntu@ec2-44-204-174-177.compute-1.amazonaws.com
            model="text-davinci-003",
            prompt=training_data(data),
            temperature=0.1
        )
        return redirect(url_for("index", result=res.choices[0].text))
    
    result = request.args.get("result")
    return render_template('index.html', result=result)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=9090, debug=True)

