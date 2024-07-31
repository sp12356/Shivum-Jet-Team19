# Filename - server.py
 
# Import flask and datetime module for showing date and time
from flask import Flask, jsonify
import datetime
 
x = datetime.datetime.now()
 
# Initializing flask app
app = Flask(__name__)
 
 
# Route for seeing a data
@app.route('/data')
def get_time():
    # Returning an api for showing in  reactjs
    return jsonify({
        'Name': "geek", 
        "Age": "22",
        "Date": x.strftime("%Y-%m-%d %H:%M:%S"), 
        "programming": "python"
    })
 
     
# Running app
if __name__ == '__main__':
    app.run(debug=True)
