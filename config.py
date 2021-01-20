from flask import Flask
from flaskext.mysql import MySQL


app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'KyrylS.mysql.pythonanywhere-services.com'
app.config['MYSQL_DATABASE_USER'] = 'KyrylS'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Stukalov12'
app.config['MYSQL_DATABASE_DB'] = 'KyrylS$hrdeb_db'


mysql = MySQL()
mysql.init_app(app)