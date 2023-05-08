import openai
from flask import Flask, redirect, rendor_templete, request, url_for
app=flask(_name_)
openai.api_key="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"
def training_data(data):
    return"""please predict text as positive or negitive.
    text: you are a bad man
    sentiment: negitive
    text: you are good man
    sentiment: positive
    text: {}
    sentiment: """.format(data.capitilzised())
 @app.route('/', methods=("Get", "POST"))
 def index():
     if request.method == "POST":
         data=request.form["data"]
         res=openai.completion.create(
         model="text-davinci-003",
         prompt="training.data"(data)
         tempratute=0.1)
         return redirect(url_for("index"),results=res.choices[0].text)
     result=request.args,get("result")
     return rendor_template("index.html", result=result)
   if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
