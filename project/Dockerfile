FROM python:3

COPY MainScores.py ./
COPY Utils.py ./
COPY Scores.txt ./
COPY templates/Scores.html ./templates/Scores.html
COPY ./requirements.txt /requirements.txt


RUN pip install -r requirements.txt

CMD [ "python3", "./MainScores.py" ] 
