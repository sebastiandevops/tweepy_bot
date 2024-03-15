# tweepy_bot

![image](https://i0.wp.com/derechodelared.com/wp-content/uploads/2020/04/twittor-bots.jpg?fit=1438%2C809&ssl=1)

<p align="justify">When I was studying to become a Software Developer, I had to tweet at least once every day to accomplish one of the goals of the school in which I was taking the program. In order to do that, I decided to create a bot to perform that operation in an automated way every day. That is how I found Tweepy, a Python library which allows you to use Twitter API.</p>

<p align="justify">The purpose of the bot is to gather fascinating facts from a website that publishes daily historical events and occurrences. It accomplishes this by employing a web scraper that extracts data from the website's HTML files. The extracted information is then stored in a file for further processing. Using the Tweepy library, the bot accesses the stored data and crafts intriguing tweets. These tweets are then published on a regular basis, sharing intriguing and curious facts with the bot's followers.</p>

<p align="justify"><b>Process to create your first Twitter bot:</b>
    <ul>
        <li>Make sure you install Tweepy locally.</li>
        <li>Sign up as a Twitter developer to use its API.</li>
        <li>Use Tweepy to communicate with Twitter API.</li>
        <li>Write your bot.</li><li>Automate your bot using Crontab jobs.</li>
    </ul>
</p>

<p align="justify"><b>What is Tweepy?</b></p>
<p align="justify">Before we start lets briefly understand what this Python library is that lets you interact with Twitter API. <a href="https://github.com/tweepy/tweepy">Tweepy</a> is an open source project that creates a convenient and easy way to interact with Twitter API using Python. For that porpouse, tweepy includes different classes and methods to represent Twitter's models and API endpoints. With these methods and clases you can encode and decode data, make HTTP requests, paginate search results and implement an OAuth authentication mechanism, among other things. With that being said, let's start.</p>

<p align="justify"><b>Tweepy installation</b></p>
<p align="justify">According to the official repository, the easiest way to install the latest Tweepy version is by using <a href="https://pip.pypa.io/en/stable/">pip</a></p>

```
pip install tweepy
```

<p align="justify">You can also use Git to clone the repository and install the latest Tweepy development branch.</p>

```
git clone https://github.com/tweepy/tweepy.git
cd tweepy
pip install .
```

<p align="justify">And finally, you can also install Tweepy directly from the GitHub repository.</p>

```
pip install git+https://github.com/tweepy/tweepy.git
```

<p align="justify"><b>Authentication Credentials for Twitter API</b></p>
<p align="justify">First of all, you need to apply for a Twitter developer account. To do that you have to follow the next steps according to the <a href="https://developer.twitter.com/en/support/twitter-api/developer-account">Twitter developer account support.</a>
    <ul align="justify">
        <li>Log-in to Twitter and verify your email address. (Note that the email and phone number verification from your Twitter account may be needed to apply for a developer account, review on the Twitter help center: <a href="https://help.twitter.com/en/managing-your-account/cant-confirm-my-email-address">email address confirmation</a> or <a href="https://help.twitter.com/en/managing-your-account/how-to-add-a-phone-number-to-your-account">add phone number</a>.)</li>
        <li>Click <a href="https://developer.twitter.com/en/portal/dashboard">sign up</a> at developer.twitter.com to enter your developer account name, location and use case details.</li>
        <li>Review and accept the <a href="https://developer.twitter.com/en/developer-terms/agreement">developer agreement </a>and submit.</li>
        <li>Check your email to verify your developer account. Look for an email from developer-accounts@twitter.com that has the subject line: "Verify your Twitter Developer Account" Note: the developer-accounts@twitter.com email is not available for inbound requests.</li>
        <li>You should now have access to the Developer Portal to create a new App and Project with Essential access, or will need to continue your application with Elevated access</li>
        <li>If you apply for Elevated access (or Academic Research access) please continue to check your verified email for information about your application.</li>
    </ul>
</p>
<p align="justify">Finally, once you complete your application, go to the <a href="https://developer.twitter.com/en/portal/dashboard">developer portal dashboard</a> to review your account status and setup. And if it's successfully registered, the next step is create your first app.</p>

<p align="justify"><b>Create the application</b></p>
<p align="justify">Twitter lets you create authentication credentials to applications, not accounts. With that being said, you need to create an app to be able to make API requests. In this case, our app will be a bot that scrapes data from a website and publishes it as a tweet on your Twitter account.</p>

<p align="justify">To create your application, visit the <a href="https://developer.twitter.com/en/portal/dashboard">developer portal dashboard</a> select +Add App and provide the following information: app name, application description, website URL and all related information about how users will use your application.</p>

<p align="justify"><b>Authentication credentials</b></p>
<p align="justify">In order to create your authentication credentials, go to the <a href="https://developer.twitter.com/en/portal/dashboard">developer portal dashboard</a> select your application and the click on "keys and tokens". Once you are on your project page, select "Generate API Key and Secret" and also select "Access Token and Secret", keep in mind that the last one should be created with read and write permissions, which guarantees that our bot can write tweets for you using the Twitter API. Don't forget to store the keys so you can use it later in our configuration file for Twitter Authentication.</p>


<p align="justify"><b>Architecture</b></p>
<p align="justify">The TweepyBot consists of three main modules: config.py, models.py, and services.py.</p>

<p align="justify"><b>config.py</b></p>
<p align="justify">This module handles the authentication to the Twitter API. It uses the tweepy.Client class from the Tweepy library to create an instance of the authenticated Twitter API. The required authentication credentials (consumer key, consumer secret, access token, and access token secret) are obtained from environment variables. If the authentication is successful, the API instance is returned.</p>

```python
#!/usr/bin/python3

# tweepy-bots/bots/config.py
import tweepy
import os


def create_api():
    """
    Authenticates to the Twitter API using the provided environment variables.

    Returns:
        tweepy.Client: An instance of the authenticated Twitter API.

    Raises:
        Exception: If an unexpected error occurs during authentication.

    Note:
        Before calling this function, ensure that the following environment
        variables are set:
        - TWITTER_CONSUMER_KEY: The Twitter API consumer key.
        - TWITTER_CONSUMER_SECRET: The Twitter API consumer secret.
        - TWITTER_ACCESS_TOKEN: The Twitter API access token.
        - TWITTER_ACCESS_TOKEN_SECRET: The Twitter API access token secret.
    """
    consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    try:
        api = tweepy.Client(
                  consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token=access_token,
                  access_token_secret=access_token_secret
              )
        print("Successfully authenticated!")
        return api
    except Exception as e:
        print(f'Error during authentication: {e}')
```


<p align="justify"><b>models.py</b></p>

<p align="justify">This module contains the TweepyBot class, which represents the Twitter bot powered by Tweepy. It has various attributes and methods to handle the tweet generation and posting.</p>

<p align="justify"><b>Attributes:</b>
    <ul align="justify">
        <li><code>api:</code> The instance of the authenticated Twitter API obtained from the config.py module.</li>
        <li><code>hashtag:</code> The hashtag to be included in the tweet.</li>
        <li><code>date_format:</code> The format for the date to be included in the tweet (either "esp" or "eng").</li>
        <li><code>data:</code> The data to populate the tweet.</li>
        <li><code>line:</code> The desired line. It can be either "longest" or "random". Default is None. If None, the tweet line will be random.</li>
        <li><code>text:</code> The custom text to be included in the tweet, overriding other tweet components if provided.</li>
        <li><code>source:</code> The data source for the tweet.</li>
        <li><code>cleaner:</code> A boolean indicating whether to execute a data cleaner.</li>
    </ul>
</p>

<p align="justify"><b>Methods</b>
    <ul align="justify">
        <li><code>get_formatted_date():</code> Retrieves the formatted date for the tweet.</li>
        <li><code>prepare_tweet():</code> Retrieves the line to be posted on Twitter by combining the tweet components based on the provided attributes.</li>
        <li><code>post_tweet(text):</code> Publishes a tweet or thread using the Twitter API.</li>
        <li><code>__str__():</code> Returns a string representation of the TweepyBot object.</li>
    </ul>
</p>

```python
#!/usr/bin/env python3

from app.services import get_line, split_string
from app.config import create_api

from datetime import datetime
# import locale
from babel.dates import format_date
from babel.numbers import format_decimal


class TweepyBot:
    """
    A class representing a Twitter bot powered by Tweepy.

    Attributes:
        api: The Twitter API object used for interacting
             with the Twitter platform.
        hashtag: The hashtag to be included in the tweet.
        date_format: The format for the date (either "esp" or "eng").
                     Default is None.
        data: The data to populate the tweet.
        line: The desired line. It can be either "longest" or "random".
              Default is None. If None, the tweet line will be random.
        text: The custom text to be included in the tweet.
              Overrides other tweet components if provided.
        source: The data source for the tweet.
        cleaner: A boolean indicating whether to execute a data cleaner.
                 False by default.

    Methods:
        get_formatted_date():
            Create a formatted date.
            Returns:
                A string with the formatted date.

        prepare_tweet():
            Retrieves the line to post on Twitter, combining the tweet
            components based on the provided attributes.
            Returns:
                A string representing the tweet content.

        post_tweet(mystr):
            Publishes a tweet or thread using the Twitter API.
            Args:
                mystr: The string to be published as a tweet.

    Usage:
        # Create an instance of TweepyBot
        bot = TweepyBot(api=create_api(), hashtag="🤖", date_format=None,
                        data=None, text=None, source=None, cleaner=False)

        # Retrieve the tweet content
        tweet_content = bot.get_tweet()

        # Post the tweet
        bot.post_tweet(tweet_content)
    """
    def __init__(
        self,
        api=create_api(),
        hashtag="🤖",
        date_format=None,
        text=None,
        data=None,
        line=None,
        source=None,
        cleaner=False
    ):
        self.api = api
        self.hashtag = hashtag
        self.date_format = date_format
        self.text = text
        self.data = data
        self.line = line
        self.source = source
        self.cleaner = cleaner

    def get_formatted_date(self):
        """
        Create a formatted date.

        Returns:
            str: The formatted date.
        """
        try:
            if self.date_format is None:
                return None
            elif self.date_format == "esp":
                # Get the current date
                current_date = datetime.now()

                # Format the date components separately
                day = format_decimal(current_date.day, format='##')
                month = format_date(current_date, format='MMMM', locale='es')

                # Format the date as "month day"
                # Create the formatted date with "de" separator
                formatted_date = f"{day} de {month}"

            elif self.date_format == "eng":
                # Get the current date
                current_date = datetime.now()

                # Format the date as "month day"
                formatted_date = current_date.strftime("%B %d")
            else:
                raise ValueError("Invalid date format")
        except ValueError as e:
            print(f"Error {e}")
            return None

        return formatted_date

    def prepare_tweet(self):
        """
        Retrieves the line to post on Twitter, combining the tweet components
        based on the provided attributes.

        Returns:
            A string representing the tweet content.
        """
        try:
            if self.text is not None:
                text = f'{self.hashtag} {self.text}'
            elif self.data is None and self.text is None:
                text = "Default tweet."
            else:
                text = get_line(
                    self.hashtag,
                    self.get_formatted_date(),
                    self.data,
                    self.line,
                    self.source,
                    self.cleaner
                )
            return text
        except Exception as e:
            # Handle the exception (e.g., log the error or display a message)
            print(f"An error occurred while generating the tweet: {str(e)}")
            return None

    def post_tweet(self, text):
        """
        Publishes a tweet or thread using the Twitter API.

        Args:
            text: The string to be published as a tweet or thread.
        """
        try:
            if len(text) <= 240:
                response = self.api.create_tweet(text=text)
                responseStr = "\n************ Response Object ************\
                               \n{}".format(response)
                print(responseStr.lstrip())
            else:
                tweets = split_string(text)
                n_tweets = len(tweets)
                logs = []
                if n_tweets > 1:
                    firstStr = tweets[0] + " [1/%s]" % (str(n_tweets))
                    response = self.api.create_tweet(text=firstStr)
                    i = 2
                    for tweet in tweets[1:]:
                        otherStr = tweet + " [%s/%s]" % (str(i), str(n_tweets))
                        logs.append(response)
                        response = self.api.create_tweet(
                            text=otherStr,
                            in_reply_to_tweet_id=response.data['id']
                        )
                        i += 1
                    logs.append(response)
                for i, item in enumerate(logs, start=1):
                    logsStr = "\n************ Response Object ************\
                               \nResponse {}: {}\n".format(i, item)
                    print(logsStr.lstrip())
            print("Tweeted successfully!")
        except Exception as e:
            print(f"An error occurred while creating the tweet: {str(e)}")

    def __str__(self):
        """repr method.

        Args:
            None

        """
        representation = "\n[TweepyBot]\
                          \nAPI: {}\
                          \nHashtag: {}\
                          \nDate format: {}\
                          \nData: {}\
                          \nSource: {}\
                          \nCleaner: {}\n".format(self.api,
                                                  self.hashtag,
                                                  self.date_format,
                                                  self.data,
                                                  self.source,
                                                  self.cleaner)
        return representation


if __name__ == "__main__":
    pass
```

<p align="justify"><b>services.py</b></p>
<p align="justify">This module contains helper functions used by the TweepyBot class to generate and post tweets.</p>

<p align="justify"><b>Functions</b>
    <ul align="justify">
        <li><code>get_line(hashtag, date_format, data, line, source, cleaner):</code> Retrieves a line to be tweeted based on the provided parameters. It reads the data file, optionally applies a cleaner, and formats the line.</li>
        <li><code>read_file(data, line, cleaner):</code> Reads the file and optionally cleans the line if the cleaner flag is set.</li>
        <li><code>split_string(string):</code> Splits a string into segments based on Twitter's character limit.</li>
    </ul>
</p>

```python
#!/usr/bin/env python3

import random


def get_line(hashtag, formatted_date, data, line, source, cleaner):
    """
    Retrieve a line to be tweeted based on the provided parameters.

    Args:
        hashtag (str): The hashtag for the tweet.
        formatted_date (str): Should be "eng" or "esp".
        data (str): The path to the data file to be read.
        source (str): The data source.
        cleaner (bool): Indicates whether to clean the source file.

    Returns:
        str: The line to be tweeted.
    """
    try:
        text = read_file(data, line, cleaner)
        if formatted_date is None:
            text = f'{hashtag}: {text} {source}'
        else:
            text = f'{hashtag}, {formatted_date}, {text} {source}'
        return text
    except FileNotFoundError as e:
        print(f"Error: File '{data}' not found. {str(e)}")
    except Exception as e:
        print(f"An error occurred while retrieving the tweet line: {str(e)}")
    return None


def read_file(data, line, cleaner):
    """
    Read the file and optionally clean the line if cleaner is True.

    Args:
        data (str): The data to read from the file.
        line: The desired line. It can be either "longest" or "random".
              Default is None. If None, the tweet line will be random.
        cleaner (bool): Indicates whether to clean the source file.

    Returns:
        str: The text to populate the tweet.
    """
    with open(data, 'r') as filename:
        lines = filename.readlines()
    try:
        if line == "longest":
            # Find the longest line
            if len(lines) > 1:
                myline = max(lines, key=len)
            elif len(lines) == 1:
                myline = lines[0]
            else:
                raise ValueError("No lines found in the file.")
        elif line == "random" or line is None:
            if len(lines) > 0:
                myline = random.choice(lines)
            else:
                raise ValueError("No lines found in the file.")
    except ValueError as e:
        e = "line should be either random, longest or None"
        print(f"Error: {e}")
        myline = ""

    if cleaner:
        lines.remove(myline)
        with open(data, 'w') as filename:
            filename.writelines(lines)

    text = myline.strip()
    return text


def split_string(string):
    """
    Split the string into segments based on Twitter's character limit.

    Args:
        string (str): The string to be split.

    Returns:
        list: List of strings representing the segmented tweets.
    """
    tweets = []

    if len(string) <= 234:
        tweets.append(string)
    else:
        remaining_string = string
        while len(remaining_string) > 234:
            # First 240 characters from remaining_string
            new_string = remaining_string[:234]
            # Find the last space within the first 240 characters
            last_space_index = new_string.rfind(' ')
            if last_space_index != -1:
                # Truncate to the last space
                new_string = new_string[:last_space_index]
            tweets.append(new_string)
            # Remaining characters after second_string
            remaining_string = remaining_string[len(new_string):].strip()

        if len(remaining_string) > 0:
            tweets.append(remaining_string)

    return tweets
```


<p align="justify">Now let's create our data scraper using bash!</p>

<p align="justify"><b>Data scraper</b></p>

```bash
#!/usr/bin/env bash
# Secuence

# Get the URL argument passed to the script
url=$1

# Define the directory path
dir="$HOME"/projects/tweepy_bot/scrapers

# Remove the existing hoy_en_la_historia.txt file
rm -rf "$dir"/hoy_en_la_historia.txt

# Fetch the content from the given URL, convert it to plain text, remove extra spaces, and save it to data.txt
echo $(curl --silent "$url" | htmlq --text | html2text) | tr -s ' ' | sed '/./G' > "$dir"/data.txt

# Insert a new line before either a 2 to 4 digit number followed by a hyphen or a space, followed by a 2 to 4 digit number, followed by "a.C. -" in data.txt
sed -i -E 's/([0-9]{2,4} -| [0-9]{2,4} a\.C\. -)/\n\1/g' "$dir"/data.txt

# Remove empty lines from data.txt
sed -i '/^\s*$/d' "$dir"/data.txt

# Insert a new line after the last period in data.txt
sed -i '$ s/\./.\n/' "$dir"/data.txt

# Filter out lines containing 'See All', 'SHOW', 'Efemérides' from output.txt and remove lines shorter than or equal to 140 characters, save the result to hoy_en_la_historia.txt
grep -v -e 'See All' -e 'SHOW' -e 'Efemérides' "$dir"/data.txt | grep -vE '^.{,140}$' > "$dir"/hoy_en_la_historia.txt

# Replace ' - ' with ', ' in hoy_en_la_historia.txt
sed -i 's/ - /, /g' "$dir"/hoy_en_la_historia.txt

# remove all possible spaces at the end of the line
sed -i 's/[[:blank:]]*$//' "$dir"/hoy_en_la_historia.txt

# removes any leading white spaces at the beginning of each line in the file.
sed -i 's/^[[:space:]]*//' "$dir"/hoy_en_la_historia.txt

# remove the content after the last dot (excluding the dot itself), but only if the line does not end with a parenthesis symbol.
sed -i -E '/\)\s*$/!s/\.[^.]*$/\./' "$dir"/hoy_en_la_historia.txt

# Remove the temporary output* and datos* files
rm -rf "$dir"/data.txt
```

<p align="justify">Here's a brief summary of the functionality of the provided bash script</p>
<p align="justify">The script takes a URL as an argument and assigns it to the <code>url</code> variable. It sets the directory path where the data will be stored in the <code>dir</code> variable. The script removes any existing <code>hoy_en_la_historia.txt</code> file in the specified directory. It retrieves data from the specified URL using <code>curl</code>, processes the HTML response using <a href="https://github.com/mgdm/htmlq">htmlq</a> and <a href="https://pypi.org/project/html2text/">html2text</a> (make sure you install first both packages, follow the hyperlinks to see the installation instructions), and stores the result in a temporary file called <code>data.txt</code>.</p>

<p align="justify">The script performs various transformations on the data.txt file using sed, tr, and grep commands to extract and format the desired data. Let's go through the commands used in the script one by one:</p>

<p align="justify"><code>url=$1</code>: This command assigns the first argument passed to the script to the variable <code>url</code>. It allows you to provide a URL as an argument when executing the script.</p>

<p align="justify"><code>dir="$HOME/projects/tweepy_bot/scrapers"</code>: This command sets the directory path where the data will be stored. It assigns the specified path to the variable <code>dir</code>.</p>

<p align="justify"><code>rm -rf "$dir"/hoy_en_la_historia.txt</code>: This command removes any existing <code>hoy_en_la_historia.txt</code> file in the specified directory <code>$dir</code>.</p>

<p align="justify"><code>echo $(curl --silent "$url" | htmlq --text | html2text) | tr -s ' ' | sed '/./G' > "$dir"/data.txt</code>: This command retrieves the HTML content from the specified URL using <code>curl</code>, processes it using <code>htmlq</code> and <code>html2text</code>, and saves the result in a temporary file called <code>data.txt</code>. The <code>echo</code> command and subsequent pipeline manipulate the text by removing excessive spaces and adding line breaks.</p>


<p align="justify"><code>sed -i -E 's/([0-9]{3,4} -)/\n\1/g' "$dir"/data.txt</code>: <code>([0-9]{3,4} -)</code> is the pattern that matches either a 3-digit or 4-digit sequence followed by a space and a dash. The captured group is then inserted into the replacement string <code>\n\1</code> to add a newline before the matched pattern.</p>

<p align="justify"><code>sed -i '/^\s*$/d' "$dir"/data.txt</code>: This command is used to delete empty lines in the file. <code>/^\s*$/</code> is a regular expression pattern that matches empty lines. The <code>^</code> represents the start of a line, <code>\s*</code> matches zero or more whitespace characters, and <code>$</code> represents the end of a line. <code>/d</code> is the sed command to delete the matched lines.</p>

<p align="justify"><code>sed -i '$ s/\./.\n/' "$dir"/data.txt</code>: <code>$</code> matches the last line of the file. <code>s/\./.\n/</code> finds the first occurrence of a dot <code>\.</code> on the last line and replaces it with the dot followed by a newline <code>.\n</code>.</p>

<p align="justify"><code>grep -v -e 'See All' -e 'SHOW' -e 'Efemérides' "$dir"/data.txt | grep -vE '^.{,60}$' > "$dir"/hoy_en_la_historia.txt</code>: This command filters out lines in <code>hoy_en_la_historia.txt</code> that contain certain keywords (See All, SHOW, Efemérides). It also removes lines that are shorter than or equal to 60 characters.</p>

<p align="justify"><code>sed -i 's/ - /, /g' "$dir"/hoy_en_la_historia.txt</code>: This is a substitution command that searches for the pattern "space-dash-space" <code> - </code> and replaces it with a comma and a space <code>, </code>.</p>

<p align="justify"><code>rm -rf "$dir"/data*</code>: This command removes all temporary files starting with <code>data</code> in the specified directory <code>$dir</code> to clean our workspace.</p>

<p align="justify">It saves the final formatted data into the <code>hoy_en_la_historia.txt</code> file, which is the file that we are using the get the data for our bot.</p>

### Functionalities
<p align="justify">The TweepyBot provides the following functionalities:
    <ul align="justify">
        <li>Authentication to the Twitter API using environment variables.</li>
        <li>Generation of tweets based on the specified components (hashtag, date, data, text, source) and formatting.</li>
        <li>Posting of tweets using the Twitter API, handling both single tweets and threaded tweets for longer content.</li>
        <li>Support for cleaning the source data file by removing already used lines.</li>
        <li>Formatting of dates in English or Spanish based on the specified date format.</li>
    </ul>
</p>

<p align="justify">To use the <code>TweepyBot</code>, you can create an instance of the <code>TweepyBot</code> class with the required parameters and then call the <code>get_tweet()</code> method to retrieve the tweet content. Finally, you can call the <code>post_tweet()</code> method to publish the tweet.</p>

<p align="justify">Example usage:</p>

```
# Create an instance of TweepyBot
bot = TweepyBot(api=create_api(), hashtag="🤖", date_format=None, data=None, text=None, source=None, cleaner=False)

# Retrieve the tweet content
tweet_content = bot.prepare_tweet()

# Post the tweet
bot.post_tweet(tweet_content)
```


<p align="justify">Now let's create the script to call our main bot module from a bash script that will be automated using crontab linux package.</p>

<p align="justify"><b>Bot runner</b></p>

```python
❯ cat tests_bot.py
#!/usr/bin/env python3

import os
import time

from app.models import TweepyBot
# from app.services import get_date


if __name__ == '__main__':

    maxtries = 8    # 8 * 15 minutes = about 2 hours total of waiting,
    home = os.getenv("HOME")
    project_path = '%s/projects/tweepy_bot' % (home)
    data = '%s/scrapers/history.txt' % (project_path)

    hashtag = "🤖 #Historia"

    for i in range(maxtries):
        try:
            bot = TweepyBot(
                data=data,
                text="This is a test",
                source="[Wikipedia®]"
            )
            tweet_content = bot.prepare_tweet()
            bot.post_tweet(tweet_content)
            print(bot.__str__())
            break
        except Exception as i:
            time.sleep(900)
            print("fail", i)

```

<p align="justify">We are about to finish, lets check the bash script that we will use to automate our bot using crontab.</p>

<p align="justify"><b>Cron Tweet script</b></p>

```bash
# cron_script.sh
#!/usr/bin/env bash
url="https://www.hoyenlahistoria.com/efemerides.php"
cd $HOME/tweepy_bot || exit
./scrapers/scraper.sh $url
python3 bot_runner.py
```

<p align="justify"><code>url="https://www.hoyenlahistoria.com/efemerides.php"</code>: This line assigns the <a href="https://www.hoyenlahistoria.com/efemerides.php">website url</a> to the variable <code>url</code>. It specifies the website from which the scraper will fetch data.</p>

<p align="justify"><code>cd $HOME/tweepy_bot || exit</code>: This line changes the current directory to out <code>tweepy_bot</code> project workspace. If the directory change is unsuccessful (for example, if the directory doesn't exist), the script exits.</p>

<p align="justify"><code>./scrapers/scraper.sh $url</code>: This line executes the shell script <code>scraper.sh</code> located in the scrapers directory. The script takes the value of the <code>url</code> variable as an argument and it will be the script that performs all text file operations that allows us to have a clean file to make out bot tweet for us in readability way.</p>

<p align="justify"><code>python3 bot_runner.py</code>: This line executes the Python script <code>bot_runner.py</code>. It runs the script responsible for running the bot, which performs the operations based on the data fetched by the scraper.</p>

<p align="justify">In summary, this script sets the URL, changes the directory to the appropriate location, executes the scraper script with the specified URL, and then executes the bot runner script to perform operations based on the scraped data.</p>

<p align="justify">Finally, let's check our cronjob file.</p>

<p align="justify"><b>Crontab job</b></p>

<p align="justify">In order to automate out bot we'll use a cronjob. The Cron daemon is a built-in Linux utility that runs processes on your system at a scheduled time. Cron reads the crontab (cron tables) for predefined commands and scripts. By using a specific syntax, you can configure a cron job to schedule scripts or other commands to run automatically.</p>

<p align="justify">Cron reads the configuration file and the daemon uses a specific syntax to interpret the lines in the crontab configuration. Let's see the syntax to understand the basic components to make it work.</p>

<p align="justify"><a href="https://phoenixnap.com/kb/set-up-cron-job-linux">Here</a> you can find a detail Cron Jobs in Linux explanation but for the porpuses of our lab, i just to that you keep in mind the file components, now let's check our cron file.</p>

```bash
API_KEY=[your api key]
API_SECRET_KEY=[your api secret key]
ACCESS_TOKEN=[your access token]
ACCESS_TOKEN_SECRET=[your access token secret]
# m h dom mon dow command
0 6 * * * bash $HOME/tweepy_bot/cron_script.sh
```

<p align="justify">To edit this file just type in your terminal <code>crontab -e</code> which will open an editor with the default configuration. Just copy and paste the content at the end of the file. Make sure to replace your keys within the fields.</p>

<p align="justify">Let's briefly check the crontab script:</p>

<p align="justify">The <code>m h dom mon dow</code> fields represent the minute, hour, day of the month, month, and day of the week, respectively. In this case, <code>0 6 * * *</code> indicates that the specified command should run at 6:00 AM every day. <code>$HOME/tweepy_bot/cron_script.sh</code> is the path to the shell script that contains the necessary commands to run the bot, in our case we call our Cron Tweet script that we created previously.

<p align="justify">In summary, the <code>crontab</code> file is configured to execute the cron_script.sh shell script at 6:00 AM every day, which in turn runs the necessary commands to automate the bot.</p>

<p align="justify"><b>This is how should look our project tree</b></p>

```bash
~/tweepy_bot
❯ tree -I __pycache__
.
├── app
│   ├── config.py
│   ├── models.py
│   └── services.py
├── bot_runner.py
├── cronjobs
│   ├── tweet.sh
│   ├── tweet_v2_english.sh
│   └── tweet_v2.sh
├── README.md
├── scrapers
│   ├── britannica_scraper.sh
│   ├── history.txt
│   ├── hoy_en_la_historia_scraper.sh
│   ├── hoy_en_la_historia.txt
│   ├── on_this_day_scraper.sh
│   └── today_in_history.txt
└── tests_bot.py

4 directories, 21 files
```

<p align="justify">Now we're done with our first twitter bot!</p>

<p align="justify"><b>Conclusion</b></p>
<p align="justify">Creating a Twitter bot using Tweepy and the Twitter API has been a rewarding experience. Through the use of Tweepy's Python library and the authentication credentials provided by the Twitter developer account, I was able to automate the process of tweeting daily. By fetching data from a website, composing tweets, and formatting them appropriately, the bot script fulfilled the requirements of my school program. The implementation of Crontab jobs ensured the bot's automation, allowing for consistent and timely tweets. Overall, this project has not only deepened my understanding of APIs, data scraping, and automation but has also strengthened my skills as a software developer.</p>
