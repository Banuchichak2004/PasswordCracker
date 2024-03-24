import hashlib
from urllib.request import urlopen


def mywordlist(url):
    try:
        wordlistfile = urlopen(url).read()
    except Exception as e:
        print("Error! While reading the wordlist: ", e)
        exit()
    return wordlistfile


def hasing (password):
    result = hashlib.sha256(password.encode())
    return result.hexdigest()


def BruteForce(guessedPass, actualPass):
    for gpass in guessedPass:
        if hash(gpass) == actualPass:
            print("The password is: ", gpass)
            exit()

url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
actualpassword = 'easy'
actualpasswordhash = hash(actualpassword)
wordlist = mywordlist(url).decode('UTF-8')
guessedPass = wordlist.split('\n')

BruteForce(guessedPass, actualpasswordhash)
print("Password could not be found.")
