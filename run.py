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


############################### continents ##################################

@app.route('/asia')
def asia():
    return render_template('continents/asia.html')

@app.route('/africa')
def africa():
    return render_template('trips/africa.html')

@app.route('/america')
def america():
    return render_template('continents/america.html')

@app.route('/europe')
def europe():
    return render_template('trips/europe.html')

@app.route('/oceania')
def oceania():
    return render_template('trips/oceania.html')


############################### trips ##################################

# asia

@app.route('/middle_east')
def middle_east():
    return render_template('trips/asia/middle_east.html')

@app.route('/indochina')
def indochina():
    return render_template('trips/asia/indochina.html')

@app.route('/far_east')
def far_east():
    return render_template('trips/asia/far_east.html')

@app.route('/indian_peninsula')
def indian_peninsula():
    return render_template('trips/asia/indian_peninsula.html')

# america

@app.route('/north_america')
def north_america():
    return render_template('trips/america/north_america.html')

@app.route('/central_america')
def central_america():
    return render_template('trips/america/central_america.html')

@app.route('/south_america')
def south_america():
    return render_template('trips/america/south_america.html')


#Evan 
@app.route('/login')
def login():
    return render_template('login.html')


#Evan
@app.route('/details')
def details():
    return render_template('details.html')


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
