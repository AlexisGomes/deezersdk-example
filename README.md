# Creating the project 
## Set up project
- Create your virtual env
- Install packages
    pip install Flask
    pip install deezersdk
    
- create app.py
```bash
from flask import Flask
from deezersdk import deezersdk

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

- now add a settings file with your DEEZER_APP_ID and your DEEZER_APP_SECRET

## Login to deezer

Get code
 