# Important: Before running this script, please run the notebook in Task_1_2 folder that generate the database
# used for query in this app. Then provide the correct link to the database at line No.
from flask import Flask, render_template,request
import sqlite3
# now initialize a flask app
app = Flask(__name__)
#now starting the server and the app
# This small code basically implements the API endpoint.
@app.route('/')
def home():

    return render_template('home.html')
# This piece of code can be considered as the backend implementation or database implementation
@app.route('/list')
def list():
    con = sqlite3 .connect('F:\Coding_task\Task_1_2\database_MovieRatings.db')
    con.row_factory = sqlite3.Row
    cur= con.cursor()
    query = """select *
               from movies
               where year >= ? AND year <=?
               AND rating >= ? AND rating <=?
               AND genres like ?;
            """
# instead of using a form to directly take user input and replacing it in the parametrized query (this can be dangerous
# as database is vulnerable to SQL injection. The parameters are directly provided as directory. Another approach will
# be to generate a form to take user input and then request these forms to get the parameters as dict. oder list.
#lower year range
    year_low = int(1995)
#upper year range
    year_high = int(2000)
#lower rating range
    rating_low = float(3.0)
#upper rating range
    rating_high = float(3.5)
#genre, in order to get a combination of different genre, write % at start and end of genre name
    genres = str('Drama')
#pass in the param to the cursor for execution agains the database
    param = (year_low, year_high,rating_low,rating_high,genres)
    cur.execute(query,param)
    rows = cur.fetchall()
    return render_template("list.html",rows=rows)


if __name__ == '__main__':
    # '0.0.0.0' = 127.0.0.1 i.e. localhost
    # port = 5000 : we can modify it for localhost
    #debug allow preloading when there are changes
    app.run(host='0.0.0.0', port=5000, debug=True) # local webserver : app.run()

