from database import Database

from flask import Flask, g, json, render_template, redirect, request, session
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)

DATABASE_PATH = 'goats.db'

app = Flask(__name__)
app.secret_key = b'demokeynotreal!'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = Database(DATABASE_PATH)
    return db


@app.teardown_appcontext
def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

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
    return render_template('regions/africa.html')

@app.route('/america')
def america():
    return render_template('continents/america.html')

@app.route('/europe')
def europe():
    return render_template('regions/europe.html')

@app.route('/oceania')
def oceania():
    return render_template('regions/oceania.html')


############################### regions ##################################

# asia

@app.route('/middle_east')
def middle_east():
    return render_template('regions/asia/middle_east.html')

@app.route('/indochina')
def indochina():
    return render_template('regions/asia/indochina.html')

@app.route('/far_east')
def far_east():
    return render_template('regions/asia/far_east.html')

@app.route('/indian_peninsula')
def indian_peninsula():
    return render_template('regions/asia/indian_peninsula.html')

# america

@app.route('/north_america')
def north_america():
    return render_template('regions/america/north_america.html')

@app.route('/central_america')
def central_america():
    return render_template('regions/america/central_america.html')

@app.route('/south_america')
def south_america():
    return render_template('regions/america/south_america.html')

############################### trips ##################################

# oceania

@app.route('/sidney')
def sidney():
    return render_template('trips/sidney.html')

@app.route('/new_zealand')
def new_zealand():
    return render_template('trips/new_zealand.html')

@app.route('/west_papua')
def west_papua():
    return render_template('trips/west_papua.html')

# europe

@app.route('/baltics')
def baltics():
    return render_template('trips/baltics.html')

@app.route('/iberian_peninsula')
def iberian_peninsula():
    return render_template('trips/iberian_peninsula.html')

@app.route('/rome')
def rome():
    return render_template('trips/rome.html')

# africa

@app.route('/kenya_uganda')
def kenya_uganda():
    return render_template('trips/kenya_uganda.html')

@app.route('/egypt')
def egypt():
    return render_template('trips/egypt.html')

@app.route('/tunisia')
def tunisia():
    return render_template('trips/tunisia.html')

# middle east
 
@app.route('/istanbul')
def istanbul():
    return render_template('trips/istanbul.html')

@app.route('/jordan')
def jordan():
    return render_template('trips/jordan.html')


# indochina

@app.route('/thailand')
def thailand():
    return render_template('trips/thailand.html')

@app.route('/vietnam_cambodia')
def vietnam_cambodia():
    return render_template('trips/vietnam_cambodia.html')


# indian peninsula 

@app.route('/n_india_nepal')
def n_india_nepal():
    return render_template('trips/n_india_nepal.html')

@app.route('/sri_lanka')
def sri_lanka():
    return render_template('trips/sri_lanka.html')
 
# far east

@app.route('/japan')
def japan():
  return render_template('trips/japan.html')

@app.route('/south_korea')
def south_korea():
  return render_template('trips/south_korea.html')
 

# south america

@app.route('/peru_bolivia')
def peru_bolivia():
    return render_template('trips/peru_bolivia.html')

@app.route('/argentina')
def argentina():
    return render_template('trips/argentina.html')


# central america 

@app.route('/mexico')
def mexico():
    return render_template('trips/mexico.html')

@app.route('/cuba')
def cuba():
    return render_template('trips/cuba.html')
 
#Evan 
# @app.route('/login')
# def login():
#     return render_template('login.html')


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





@app.route('/signup', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        typed_password = request.form['password']
        if name and username and typed_password:
            encrypted_password = pbkdf2_sha256.encrypt(
                typed_password, rounds=200000, salt_size=16)
            get_db().create_user(name, username, encrypted_password)
            return redirect('/login')
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        typed_password = request.form['password']
        if username and typed_password:
            user = get_db().get_user(username)
            if user:
                if pbkdf2_sha256.verify(typed_password, user['encrypted_password']):
                    session['user'] = user
                    return redirect('/')
                else:
                    message = "Incorrect password, please try again"
            else:
                message = "Unknown user, please try again"
        elif username and not typed_password:
            message = "Missing password, please try again"
        elif not username and typed_password:
            message = "Missing username, please try again"
    return render_template('login.html', message=message)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


@app.route('/wishlist')
def wishlist():
    return render_template('wishlist.html')


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
