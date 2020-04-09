from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

# Playing around - add CSS to the HTML rendered by the return statement
@app.route('/test')
def test_html():
    x = '<div style="text-align:center; background-color:#c0c0c0";><h1 style="color:blue;">This is blue test text that should be centered!</h1></div>'
    return x

@app.route('/<string:name>')
def hello_who(name):
    print(name)
    return 'hello ' + name 

# Playing around - change content rendering based on id value
@app.route('/user/<string:username>/<int:id>')
def show_user_profile(username, id):
    print(username)
    print(id)

    x = f'<div style="text-align:center; background-color:#c0c0c0";><h1 style="color:blue;">Hello {username}</h1></div>'
    y = f'<div style="text-align:center; background-color:#000000";><h1 style="color:orange;">Hello {username}</h1></div>'
    
    if id < 10:
        return x
    else:
        return y


#Debug Mode
if __name__ == '__main__':
    app.run(debug=True)