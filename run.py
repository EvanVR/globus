# Danai Roumelioti, dr3248@drexel.edu
# CS530: dr3248, Assignment 2 

from database import Database

from flask import Flask, g, json, render_template, request

# DATABASE_PATH = 'dev/bikes.db'

app = Flask(__name__)

# def get_db():
    # db = getattr(g, '_database', None)
    # if db is None:
        # db = Database(DATABASE_PATH)
    # return db

# @app.teardown_appcontext
# def close_connection(exception):
    # db = getattr(g, '_database', None)
    # if db is not None:
        # db.close()
 

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/asia')
def asia():
    return render_template('asia.html')

@app.route('/africa')
def africa():
    return render_template('africa.html')

@app.route('/america')
def america():
    return render_template('america.html')

@app.route('/europe')
def europe():
    return render_template('europe.html')

@app.route('/oceania')
def oceania():
    return render_template('oceania.html')

# @app.route('/rent')
# def rent():
    # return render_template('rent.html')
# 
# def generate_response():
    # bikes = get_db().get_bikes()
    # return json.jsonify(bikes)
# 
# 
# @app.route('/api/get_bikes', methods=['GET'])
# def api_get_bikes():
    # return generate_response()
    
 
# @app.route('/api/update_bike', methods=['POST'])
# def api_update_bike():
    # id = request.form.get('id')
    # availability = request.form.get('available')
    # get_db().update_bike(id, availability)
    # return generate_response()
# 
# 
# @app.route('/api/reset_bikes', methods=['POST'])
# def api_reset_bikes():
    # get_db().reset_bikes()
    # return generate_response()
   

############################################################

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
