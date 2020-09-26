from flask import Flask,render_template

app=Flask(__name__)

#@app.route('/home/<string:name>')
#getting parameters from the url
@app.route('/')
def index():
    return render_template('index.html')

all_post=[{
    "name":"JENIL",
    "lastname":"Mehta",
    'hobby':'swimming'
},
{
   "name":"saumya",
    "lastname":"Mehta" ,
    'hobby':'coding'
}]
@app.route('/post')
def post():
    return render_template('post.html',post=all_post)
@app.route('/home/<string:name>/<int:age>')
def hello(name,age):
    return name +", " + str(age)

@app.route('/get',methods=['GET'])
def get():
    return "Get called"

if __name__=="__main__":
    app.run(debug=True)
