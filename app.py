from chalice import Chalice

app = Chalice(app_name='myChalice')

@app.route('/')
def index():
    return {'hello': 'world',
            'name': 'brijesh'}

