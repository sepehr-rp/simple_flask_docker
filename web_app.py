import random
import os
from datetime import datetime
import psutil
from flask import Flask, render_template

app = Flask(__name__)




def monitoring():
    return  psutil.cpu_percent(), psutil.virtual_memory().percent

def get_color():
    colors = ['lime ', 'teal', 'aqua', 'antiquewhite', 'aquamarine', 'bisque', 'lightcyan', 'lightgreen', 'yellow', 'white', 'pink']
    i = random.randint(0, len(colors)-1)
    return colors[i]

@app.route('/')
def home():
    date = datetime.now()
    cpu, ram = monitoring()
#    cwd = os.getcwd()+"/statics/styles.css"

    my_date = date.strftime("%m/%d/%Y, %H:%M:%S")
    return render_template('index.html', utc_dt=my_date, cpu=cpu, ram=ram, col1=get_color(), col2=get_color(), col3=get_color())

if __name__ == "__main__":
    app.run(debug=True)
