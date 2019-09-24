from flask import Flask,render_template
app = Flask(__name__)

posts = [
    {
        'movie_name':'Ramleela',
        'lan':'Hindi',
        'female_cast':'Deepika Padukon',
        'male_cast':'Ranveer Singh'

    },
    {
        'movie_name':'Three idiots',
        'lan':'Hindi',
        'female_cast':'Kareena Kapoor',
        'male_cast':'Amir khan'

    }
]

@app.route("/")
@app.route("/home")
def HelloWorld():
    return render_template('home1.html',posts=posts,title='Test3')

@app.route("/about")
def About():
    return  render_template("About.html",title='Test2')

app.run()
