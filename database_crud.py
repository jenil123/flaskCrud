from flask import Flask,render_template,request,redirect

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'

db=SQLAlchemy(app)


class PersonalInfo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    lastname=db.Column(db.String(100),nullable=True)
    hobby=db.Column(db.Text,nullable=False,default='N/A')
    data_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return "Personal Info "+ str(self.id)



@app.route('/')

def index():
    return render_template('index.html')
#CREATE AND ADD TO THE DATABASE
@app.route('/posts',methods=['GET','POST'])
def posts():
    print(request.method)
    if request.method=='POST':
        post_name=request.form['name']
        post_lastname=request.form['lastname']
        post_hobby=request.form['hobby']
        new_info = PersonalInfo(name=post_name,lastname=post_lastname,hobby=post_hobby)
        print(new_info)
        db.session.add(new_info)
        db.session.commit()
        return redirect('/posts')
    else:
        all_post=PersonalInfo.query.order_by(PersonalInfo.data_posted).all()
        #print(all_post)
        return render_template('post.html',post=all_post)



@app.route('/posts/delete/<int:id>')
def delete(id):
    post_id=PersonalInfo.query.get_or_404(id)
    db.session.delete(post_id)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    post_id=PersonalInfo.query.get_or_404(id)
    if request.method=='POST': 
        post_id.name=request.form['name']
        post_id.lastname=request.form['lastname']
        post_id.hobby=request.form['hobby']
        #new_info = PersonalInfo(name=post_name,lastname=post_lastname,hobby=post_hobby)
       # print(new_info)
        #db.session.add(new_info)
        #db.session.commit()
        db.session.commit()
        return redirect('/posts')
    else:
        #all_post=PersonalInfo.query.order_by(PersonalInfo.data_posted).all()
        #print(all_post)
        return render_template('edit.html',post=post_id)
    

@app.route('/posts/new',methods=['GET','POST'])
def new_post():
    if request.method=='POST':
        post_name=request.form['name']
        post_lastname=request.form['lastname']
        post_hobby=request.form['hobby']
        new_info = PersonalInfo(name=post_name,lastname=post_lastname,hobby=post_hobby)
        print(new_info)
        db.session.add(new_info)
        db.session.commit()
        return redirect('/posts')
    else:
        all_post=PersonalInfo.query.order_by(PersonalInfo.data_posted).all()
        #print(all_post)
        return render_template('new-post.html')
if __name__=="__main__":
    app.run(debug=True)
