import requests
from flask import Flask,render_template,session,url_for,redirect,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

class input(FlaskForm):
    inptfield=StringField(validators=[DataRequired()],render_kw={"placeholder": "Type the keywords for eg. 'Wikipedia'"})
    submit=SubmitField("   Search   ")


Your_X_Mashape_Key = "5kidG3tsX2mshNBg7cfZ6dI2o8C2p1ytRzqjsnRtVXPE5laLTX";

#The query parameters: (update according to your search query)
count = 10 #the number of items to return
q = "Donald%20Trump" #the search query
q=""
autoCorrect = True #autoCorrectspelling
projectpath={}


response=requests.get("https://contextualwebsearch-websearch-v1.p.mashape.com/api/Search/WebSearchAPI?q={}&count={}&autocorrect={}".format(q, count, autoCorrect),
headers={
"X-Mashape-Key": Your_X_Mashape_Key,
"Accept": "application/json"
}
).json()

#Get the numer of items returned
totalCount = response["totalCount"];

#Get the list of most frequent searches related to the input search query
#relatedSearch = response[&#39;relatedSearch&#39;]
 
#Go over each resulting item
'''for webPage in response["value"]:

#Get the web page metadata
    url = webPage["url"]
    title = webPage["title"]
    description = webPage["description"]
    keywords = webPage["keywords"]
    provider = webPage["provider"]["name"]
    datePublished = webPage["datePublished"]

    #Get the web page image (if exists)
    imageUrl = webPage["image"]["url"]
    imageHeight = webPage["image"]["height"]
    imageWidth = webPage["image"]["width"]
    
    thumbnail = webPage["image"]["thumbnail"]
    thumbnailHeight = webPage["image"]["thumbnailHeight"]
    thumbnailWidth = webPage["image"]["thumbnailWidth"]
    
'''
@app.route('/',methods=['GET','POST'])
def index():
    form=input()
    if form.validate_on_submit():
        return redirect(url_for('page2'))
    else:
        return render_template('main.html',form=form)

@app.route('/page2',methods=['GET','POST'])
def page2():
    form=input()
    #return render_template('page2.html',form=form,url=url,title=title,desc=description,keywords=keywords,provider=provider)
    return render_template('page2.html',response=response,form=form)
    #An example: Output the webpage url, title and published date:
#print("Url: %s. Title: %s. Published Date:%s." % (url, title, datePublished))

@app.route('/handle_data', methods=['POST'])
def handle_data():
    form=input()
    projectpath = request.form['inptfield']
    #print(projectpath)
    #return projectpath
    words=projectpath.split(" ")
    q=''
    for word in words:
        if(q==''):
            q=word
        else:
            q=q+"%20"+word
    response=requests.get("https://contextualwebsearch-websearch-v1.p.mashape.com/api/Search/WebSearchAPI?q={}&count={}&autocorrect={}".format(q, count, autoCorrect),
headers={
"X-Mashape-Key": Your_X_Mashape_Key,
"Accept": "application/json"
}
).json()
    return render_template('page2.html',response=response,form=form)

if __name__=='__main__':
    app.run(debug='True')
