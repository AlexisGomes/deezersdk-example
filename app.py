from flask import Flask, redirect, request
from deezersdk import deezersdk
from settings import DEEZER_APP_ID, DEEZER_APP_SECRET, DEEZER_REDIRECT_URI

app = Flask(__name__)


@app.route('/')
def default():
    url = deezersdk.Deezer.get_oauth_login_url(app_id=DEEZER_APP_ID, redirect_uri=DEEZER_REDIRECT_URI)
    return redirect(url)


@app.route('/deezer/login')
def deezer_login_completed():
    code = request.args.get('code')
    result = deezersdk.Deezer.get_oauth_token(app_id=DEEZER_APP_ID, app_secret=DEEZER_APP_SECRET, code=code)
    if result == 'wrong code':
        return redirect('/')
    return redirect(f'/deezer?token={result}')


@app.route('/deezer')
def deezer():
    token = request.args.get('token')
    deezer = deezersdk.Deezer(app_id=DEEZER_APP_ID, app_secret=DEEZER_APP_SECRET, token=token)

    playlists = deezer.get_my_playlists()
    url = deezer.get_widget(playlist=playlists[0])
    return redirect(url)


if __name__ == '__main__':
    app.run(use_reloader=True)
