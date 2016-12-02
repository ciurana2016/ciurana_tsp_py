# ciurana_tsp_py
This is a submission for the "P vs NP" challenge by @Sirajology on [Youtube](https://youtu.be/9MvbNPQiEE8).


## Overview
On this challenge we where asked to do the traveling salesman problem (or TSP) without trying every possible path.

I based my code on [this](https://youtu.be/SC5CX8drAtU) video and worked out the functions by myself.

I don't use the original distances dictionary used on the challenge because I couldn't find a way to translate it to 2d coordinates, that is why I used a diferent dataset that can be found [here](http://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html).

Inside the "tsp.py" file are all the functions for the problem, the "challenge.py" file just imports them and plots the result.


## Dependencies
Only if you are going to run the "challenge.py" file, all the functions on the "tsp.py" file are done in pure python.

* matplotlib (http://matplotlib.org/users/installing.html)


## Usage
Just run:
```
python challenge.py
```
It takes 12 seconds to run on ( 2,6 GHz Intel Core i5 ), there is a comment in the code to adjust the number of iterations if you want.

You can also use the raw functions for your 2d data.


## Credits
Credits to [Siraj](https://github.com/llSourcell) and this [video](https://youtu.be/SC5CX8drAtU).