from app import app

@app.route('/')
def index():
    return 'lo que queramos'