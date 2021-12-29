#MainScores.py

#Scores.html located in subdirectory "templates"
# run from command line :
#python3 -m venv venv
# .venv/bin/activate
#export FLASK_APP=MainScores.py
#flask run --host=0.0.0.0
# run from PC:
#http://zil56do01v:5000/


import subprocess
from flask import Flask, render_template, flash, request , session
#from wtforms import Form, TextField
from wtforms import Form
from Utils import scorefile, screen_cleaner, bad_return_code


app = Flask(__name__)
#app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

class Scores(Form):

 @app.route('/',   methods=['GET', 'POST'])
 def score_server():

    form = Scores(request.form)

    with open(scorefile,"r") as f:
      SCORENEW=str(f.read())
      print(f"SCORENEW is ", SCORENEW)
      f.close()
  
    htmlfile="templates/Scores.html"
    COMMAND = ""
    COMMAND += "grep  \"The score is \" " + htmlfile  + " |  awk -F\> '{print $3}' | awk -F\< '{print $1}' "
    #print(COMMAND)
    SCOREPREVIUOS = int(subprocess.check_output(COMMAND, shell=True).rstrip())
    SCOREPREVIUOS = str(SCOREPREVIUOS)
    #print(f"SCOREPREVIUOS is ", SCOREPREVIUOS)

    with open(htmlfile,"r") as f:
     HTML=f.read()
     f.close()
     #print(f"HTML is ", HTML)

     HTML=HTML.replace(SCOREPREVIUOS,SCORENEW)
     #print(f"HTML is ", HTML)
     with open(htmlfile,"w") as f:
      f.write(HTML)
      f.close()
    
    return render_template('Scores.html', form=form)


          # MAIN #

if __name__ == "__main__":

 #app.run()
 app.run(host='0.0.0.0', port=5000)
