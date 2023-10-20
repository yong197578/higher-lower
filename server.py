from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0, 9)

@app.route("/")
def home():
    return ('<h1>Guess number 0 to 9</h1>'
            '<iframe src="https://giphy.com/embed/fDUOY00YvlhvtvJIVm" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/countdown-jmz-count-down-fDUOY00YvlhvtvJIVm">via GIPHY</a></p>')



@app.route("/<int:number>")
def high_low(number):

    if int(number) < random_num:
        return ('<h1 style="color:red">Too low, Try Again!</h1>'
                '<iframe src="https://giphy.com/embed/jD4DwBtqPXRXa" width="384" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/work-digging-jD4DwBtqPXRXa">via GIPHY</a></p>')
    elif int(number) > random_num:
        return ('<h1 style="color: purple">Too high, Try Again!</h1>'
                '<iframe src="https://giphy.com/embed/3o7abAHdYvZdBNnGZq" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/dog-puppy-dottie-3o7abAHdYvZdBNnGZq">via GIPHY</a></p>')
    else:
        return ('<h1 style="color: green">You found me!</h1>'
                '<iframe src="https://giphy.com/embed/gcXcSRYZ9cGWY" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/gcXcSRYZ9cGWY">via GIPHY</a></p>')



if __name__ == "__main__":
    app.run(debug=True)