from flask import Flask, render_template, request, redirect, url_for
from models.physics_model import PhysicsModel
from controllers.physics_controller import PhysicsController

app = Flask(__name__)

physics_model = PhysicsModel()
physics_controller = PhysicsController(physics_model)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = physics_controller.respond(user_input)
        return render_template('chat.html', user_input=user_input, response=response)
    return render_template('chat.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True)