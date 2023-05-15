import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"

def training_data(data):
    return f"question: {data}\n" \
           f"answer: "

def generate_answer(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.1,
        max_tokens=50
    )
    return response.choices[0].text.strip()

@app.route('/', methods=("GET", "POST"))
def index():
    if request.method == "POST":
        data = request.form["data"]
        prompt = training_data(data)
        result = generate_answer(prompt)
        return redirect(url_for("index", result=result))

    result = request.args.get("result")
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)

