from flask import Flask, render_template_string
import threading
import datetime

app = Flask(__name__)

@app.route('/')
def display_date():
    current_date = datetime.datetime.now().strftime("%d-%m-%y")
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Webpage</title>
        <style>
            body {
            font-family: Arial, sans-serif;
            background-color: #ffa500;
            margin: 0;
            padding: 20px;
            }

            .styled-paragraph {
            color: #ffff00;
            font-size: 18px;
            line-height: 1.6;
            background-color: #800000;
            padding: 10px;
            border-radius: 5px;
            max-width: 1000px;
            margin: 0 auto;
            
            .styled-paragraph .date {
                margin-top: 30px;
                font-size: 18px;
                color: yellow;
            }
            .styled-paragraph .logo {
                margin: 0;
                padding: 0;
                float: left;
                width: 5px;
            }
        </style>
    </head>
    <body>
        <img src="./static/images/MyLogo.png" alt="Logo" style="width:60px;height:60px;">
         <img src="./static/images/programming.gif" alt="Logo" class="logo">
        <div class="styled-paragraph">
              <h2><center>Webpage built on Flask and deployed on Render Cloud App</center></h2>
     <p class="styled-paragraph">
     <strong>The Post(s)/Blogs published by Dutt Venkata Kalluri are a must read for all age groups</strong>.<br><br>
        <b>"The Intersection of Ancient Wisdom and Modern Technology"</b><br> - 
        Wonderful perspective connecting our ancient 
        wisdom of truth to modern day technology, absolutely necessary to remind the people in India.<br><br>
       <b>"Transforming for Tomorrow: Navigating Digital Transformation in a Digital World"</b> - Another wonderful post. 
       Well explained about the pitfalls in the course of digital transformation, 
       if all heads do not come together. Digital payments/transactions done through UPI in India is one such example of
       digital transformation executed successfully. From a barber shop to a jewellery store, all it takes for a person 
       is to carry a smart phone with UPI app installed. Carrying wrinkled notes,small change, 
       slanging match/argument..for not getting change..are days gone by.. <br><br>
       <b>"The Importance of a Strong Data Foundation for AI/ML Success" </b> - Very pertinent questions 
       raised in this post.<br><br>
       <b>"A Day in the Life in 2040: The Dawn of a New Era"</b> - Gives a sneak peek into what the technological changes 
        holds for future generation.
        This post is in perfect alignment with what the Indian Prime minister talks about viksit Bharat 2047.
        <br><br>Keep writing such wonderful and useful information sir.</p><br><br>     
           <center><h2>{{ current_date }}</center></h2>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, current_date=current_date)

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)


# Function to run the Flask application
#def run_app():
#   app.run(host='0.0.0.0', port=5000)

# Run the Flask application in a separate thread
#thread = threading.Thread(target=run_app)
#thread.start()
