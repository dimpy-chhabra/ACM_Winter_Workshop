from twython import Twython

APP_KEY = 'aW2MqyfnZ0SMOLt3kHi7ktlIo'
APP_SECRET = 'dM0zSgA02Ge6gKNRgHPyg3SUdJyqjNFG0DSjKT3jP3UXbS22Iv'
OAUTH_TOKEN = '793573526183608320-MZfwPF7whoKlESeMchI3AyFtjtF4UF5'
OAUTH_TOKEN_SECRET = 'iU0fFXE0DujIbp3GU1swD8TyGKi3lVCVN16H7QvUDbEez'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

timeline = twitter.get_home_timeline()

print timeline

