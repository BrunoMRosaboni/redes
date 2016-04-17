import json, os, random, requests, sys
from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html')

@app.route('/random/')
def proxy_example():
    r = requests.get("http://quotes.stormconsultancy.co.uk/random.json").content
    # sys.stderr.write("jd:" + str(r))
    r_dict = json.loads(r)    
    
    quote = r_dict['quote']
    author = r_dict['author']

    return render_template('random.html')

@app.route('/hello/',methods=['POST'])
def hello(name=None):	
    user = request.form.get('username')
    return render_template('hello.html', name=user)    

@app.context_processor
def gerador():    
    r = requests.get("http://quotes.stormconsultancy.co.uk/random.json").content
    # sys.stderr.write("jd:" + str(r))
    r_dict = json.loads(r)    
    
    quote = r_dict['quote']
    author = r_dict['author']
    return dict(quote=quote+" -"+author)


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)