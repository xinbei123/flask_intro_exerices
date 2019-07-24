"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = [
    'smell-bad', 'noisy', 'annoying', 'dumb']


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi This is my homepage.</title>
      </head>
      <body>
        <a href="/hello">start here!</a>
      </body>
    </html>

    """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type = "radio" name="compliments" value="awesome">Awesome</input>
          <input type = "radio" name="compliments" value="terrific">Terrific</input>
          <input type = "radio" name="compliments" value="fantastic">Fantastic</input>
          <input type="submit" value="Submit">
        </form>
        <form action="/diss"> 
        What's your name? <input type="text" name="person">
        <select name = "insults">
            <option value = "smell-bad">Smells Bad</option>
            <option value = "noisy">Noisy</option>
            <option value = "annoying">Annoying</option>
            <option value = "dumb">Dumb</option>
        </select>
        <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """
@app.route("/diss")
def insult_person():
    """Greet person with insult"""

    player = request.args.get("person")

    insult = request.args.get("insults")

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, insult)

@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliments")


    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)






if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
