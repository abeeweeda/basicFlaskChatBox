from flask import Flask , request, render_template
import mysql.connector

app = Flask(__name__)
app.debug = True



def saveTweet(data):
    cnx = mysql.connector.connect(user='username', password='password',
                              host='hostname',
                              database='dbname')
    cursor = cnx.cursor()
    addTweet = "insert into tweets(name, tweet) values(%s, %s)"
    dataTweet = (data[0], data[1])
    cursor.execute(addTweet, dataTweet)
    cnx.commit()



def retrieveTweets():
    cnx = mysql.connector.connect(user='username', password='password',
                              host='hostname',
                              database='dbname')
    tweets = []
    cursor = cnx.cursor()
    query = "select name, tweet from tweets"
    cursor.execute(query)
    for data in cursor:
        tweets.append(data)
    #cursor.close()
    return tweets

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        textAreaData = retrieveTweets()
        data=None
        return render_template('Home.html', data=data, textAreaData=textAreaData)
    else:
        nm = request.form['nm']
        mssg = request.form['txt']
        data = [nm, mssg]
        saveTweet(data)
        textAreaData = retrieveTweets()

        return render_template('Home.html', data=data, textAreaData=textAreaData)

