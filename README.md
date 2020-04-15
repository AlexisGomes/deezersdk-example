**This is a small flask project to use the [deezersdk](https://github.com/AlexisGomes/deezersdk)** 

## Set up the project
- Create your virtual env
- Install packages
    ```bash
    pip install Flask
    pip install deezersdk
    ```    
- Create a file settings.py following the example in `settings.example.py` 
and replace it with your Deezer's application informations. 
- Start the server with 
    ```bash 
    python app.py
    ```

## Login to Deezer's API
My local server run on `http://127.0.0.1:5000/`

- Go to the default route `/`
- This will open a pop to login to your Deezer account.
- You will then be redirected to `/deezer/login` if it's a success
- This will redirect you to `/deezer`, witch will find your first playlist and play it.


**For more informations and details on the use of the sdk, you take a look at the [READ ME](https://github.com/AlexisGomes/deezersdk)** 

 