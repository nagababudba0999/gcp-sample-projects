from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# Configuration for your Cloud SQL instance
db_host = ''
db_user = ''
db_password = ''
db_name = ''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        
        # Insert data into Cloud SQL
        db = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name, cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO users (first_name, last_name, phone_number, email)
            VALUES (%s, %s, %s, %s)
        """, (first_name, last_name, phone_number, email))
        db.commit()
        cursor.close()
        db.close()
        
        return render_template('success.html')
    
    return render_template('index.html')

@app.route('/fetch_data')
def fetch_data():
    # Fetch data from Cloud SQL
    db = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name, cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    db.close()
    
    return render_template('fetch_data.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
