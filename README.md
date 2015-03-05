# MinneapolisFact Twitter Bot

This is the magic that makes [@MinneapolisFact](https://twitter.com/MinneapolisFact) run. Sorry, it's just a really basic python script, nothing fancy.

## Contributing

In case you don't know, MinneapolisFact is a twitter bot that tweets facts about Milwaukee, WI, as if they were actually about Minneapolis. It has a sister twitter account at [@MilwaukeeFacts](https://twitter.com/MilwaukeeFacts) which is not run by or technically affliated with MinneapolisFact.

If you'd like to add facts, just update the `facts.txt` file and send a pull request.

## Running Yourself

You can use this script as a basis for your own Random Fact twitter bot. The setup is pretty simple.


```
$ git clone git@github.com:dragonmantank/minneapolisfact.git
$ cd minneapolisfact
$ virtualenv venv
$ source venv/bin/activate
$ pip install python-twitter
$ cp OAuthSettings.py.dist OAuthSettings.py
```

Replace the contents of `facts.txt` with whatever facts you want to tweet. Just make sure each tweet is less than 140 characters, and on their own lines.

You will also need to create a Twitter application, and fill in the OAuthSettings.py file you created above. Then just invoke it with

```
venv/bin/python Facts.py
```

You can hook it up to a cron job so that it posts on a regular basis.