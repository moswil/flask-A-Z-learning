from app import app


@app.route('/')
def index():
    return 'Hello World'


@app.route('/home')
def home():
    return {'home': True}
