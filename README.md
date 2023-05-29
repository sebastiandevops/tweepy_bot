# tweepy_bot

![image](https://i0.wp.com/derechodelared.com/wp-content/uploads/2020/04/twittor-bots.jpg?fit=1438%2C809&ssl=1)

<p>When I was studying to become a Software Developer, I had to tweet at least once every day to accomplish one of the goals of the school in which I was taking the program. In order to do that, I decided to create a bot to perform that operation in an automated way every day. That is how I found Tweepy, a Python library which allows you to use Twitter API.</p>

<p>The purpose of the bot is to gather fascinating facts from a website that publishes daily historical events and occurrences. It accomplishes this by employing a web scraper that extracts data from the website's HTML files. The extracted information is then stored in a file for further processing. Using the Tweepy library, the bot accesses the stored data and crafts intriguing tweets. These tweets are then published on a regular basis, sharing intriguing and curious facts with the bot's followers.</p>

<p><b>Process to create your first Twitter bot:</b>
    <ul>
        <li>Make sure you install Tweepy locally.</li>
        <li>Sign up as a Twitter developer to use its API.</li>
        <li>Use Tweepy to communicate with Twitter API.</li>
        <li>Write your bot.</li><li>Automate your bot using Crontab jobs.</li>
    </ul>
</p>

<p><b>What is Tweepy?</b></p>
<p>Before we start lets briefly understand what this Python library is that lets you interact with Twitter API. <a href="https://github.com/tweepy/tweepy">Tweepy</a> is an open source project that creates a convenient and easy way to interact with Twitter API using Python. For that porpouse, tweepy includes different classes and methods to represent Twitter's models and API endpoints. With these methods and clases you can encode and decode data, make HTTP requests, paginate search results and implement an OAuth authentication mechanism, among other things. With that being said, let's start.</p>

<p><b>Tweepy installation</b></p>
<p>According to the official repository, the easiest way to install the latest Tweepy version is by using <a href="https://pip.pypa.io/en/stable/">pip</a></p>

```
pip install tweepy
```

<p>You can also use Git to clone the repository and install the latest Tweepy development branch.</p>

```
git clone https://github.com/tweepy/tweepy.git
cd tweepy
pip install .
```

<p>And finally, you can also install Tweepy directly from the GitHub repository.</p>

```
pip install git+https://github.com/tweepy/tweepy.git
```

<p><b>Authentication Credentials for Twitter API</b></p>
<p>First of all, you need to apply for a Twitter developer account. To do that you have to follow the next steps according to the <a href="https://developer.twitter.com/en/support/twitter-api/developer-account">Twitter developer account support.</a>
    <ul>
        <li>Log-in to Twitter and verify your email address. (Note that the email and phone number verification from your Twitter account may be needed to apply for a developer account, review on the Twitter help center: <a href="https://help.twitter.com/en/managing-your-account/cant-confirm-my-email-address">email address confirmation</a> or <a href="https://help.twitter.com/en/managing-your-account/how-to-add-a-phone-number-to-your-account">add phone number</a>.)</li>
        <li>Click <a href="https://developer.twitter.com/en/portal/dashboard">sign up</a> at developer.twitter.com to enter your developer account name, location and use case details.</li>
        <li>Review and accept the <a href="https://developer.twitter.com/en/developer-terms/agreement">developer agreement </a>and submit.</li>
        <li>Check your email to verify your developer account. Look for an email from developer-accounts@twitter.com that has the subject line: "Verify your Twitter Developer Account" Note: the developer-accounts@twitter.com email is not available for inbound requests.</li>
        <li>You should now have access to the Developer Portal to create a new App and Project with Essential access, or will need to continue your application with Elevated access</li>
        <li>If you apply for Elevated access (or Academic Research access) please continue to check your verified email for information about your application.</li>
    </ul>
</p>
<p>Finally, once you complete your application, go to the <a href="https://developer.twitter.com/en/portal/dashboard">developer portal dashboard</a> to review your account status and setup. And if it's successfully registered, the next step is create your first app.</p>

<p><b>Create the application</b></p>
<p>Twitter lets you create authentication credentials to applications, not accounts. With that being said, you need to create an app to be able to make API requests. In this case, our app will be a bot that scrapes data from a website and publishes it as a tweet on your Twitter account.</p>

<p>To create your application, visit the <a href="https://developer.twitter.com/en/portal/dashboard">developer portal dashboard</a> select +Add App and provide the following information: app name, application description, website URL and all related information about how users will use your application.</p>

<p><b>Authentication credentials</b></p>
<p>In order to create your authentication credentials, go to the <a href="https://developer.twitter.com/en/portal/dashboard">developer portal dashboard</a> select your application and the click on "keys and tokens". Once you are on your project page, select "Generate API Key and Secret" and also select "Access Token and Secret", keep in mind that the last one should be created with read and write permissions, which guarantees that our bot can write tweets for you using the Twitter API. Don't forget to store the keys so you can use it later in our configuration file for Twitter Authentication.</p>

<p>You may want to test your credentials using this python script:</p>

{% highlight python3 %}
#!/usr/bin/python3
import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("[API_KEY]",
    "[API_SECRET_KEY]")
auth.set_access_token("[ACCESS_TOKEN]",
    "[ACCESS_TOKEN_SECRET]")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print("Error during authentication")
    raise e
```

<p>Make sure you replace the square bracket fields with your credentials. Once you're done we can continue with the next step.</p>

<p><b>Create your configuration file to Authenticate our bot</b></p>

{% highlight python3 %}
#!/usr/bin/python3

import tweepy
import os


def create_api():
    consumer_key = os.getenv("API_KEY")
    consumer_secret = os.getenv("API_SECRET_KEY")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except Exception as e:
        print("Error during authentication")
        raise e
    return api
```

<p>Here's an explanation of the authentication script:</p>

<p>The script starts with a shebang <code>#!/usr/bin/python3</code>, which specifies the interpreter to be used to execute the script. In this case, it's set to Python 3.

<p>The script imports the necessary modules, <code>tweepy</code> and <code>os</code>. Alongside of Tweepy, we'll use <code>os</code>, which allows interaction with the operating system, particularly to retrieve environment variables. In this case we need that library because we will store our Twitter keys as environment variables.</P>

<p>The <code>create_api()</code> function is defined. This function is responsible for creating and returning an instance of the Tweepy API, which will be used to interact with the Twitter API.</p>

<p>Inside the <code>create_api()</code> function, the script retrieves several environment variables using <code>os.getenv()</code>. These environment variables are expected to contain the necessary Twitter API credentials: <code>API_KEY</code>, <code>API_SECRET_KEY</code>, <code>ACCESS_TOKEN</code>, and <code>ACCESS_TOKEN_SECRET</code>.</p>

<p>The script uses the credentials obtained from the environment variables to initialize an instance of <code>tweepy.OAuthHandler</code>. This class is responsible for handling the OAuth 1.0a authentication process required by the Twitter API.</p>

<p>The <code>auth.set_access_token()</code> method is called to set the access token and access token secret obtained from the environment variables.</p>

<p>An instance of tweepy.API is created, passing the <code>auth</code> object as an argument. This instance represents the authenticated connection to the Twitter API.</p>

<p>The script then attempts to verify the credentials by calling <code>api.verify_credentials()</code>. If the verification is successful, it prints <code>"Authentication OK"</code>. Otherwise, it catches any exception raised, prints <code>"Error during authentication"</code> and re-raises the exception.</p>

<p>Finally, the created api object is returned from the <code>create_api()</code> function.</p>

<p>In summary, this script defines a function <code>create_api()</code> that creates and returns an authenticated instance of tweepy.API. It retrieves the necessary Twitter API credentials from environment variables, sets up the authentication, and verifies the credentials. This function can be used to establish a connection to the Twitter API for further interactions in your Twitter bot.</p>

<p><b>Create your bot</b></p>
<p>Bot modules: <code>bot_v1.py</code> and <code>split_string.py</code></p>

{% highlight python3 %}
#!/usr/bin/python3
# bot_v1.py
import random

from bots.config import create_api

from datetime import datetime
# import locale
from babel.dates import format_date
from babel.numbers import format_decimal

from utils.split_string import split_string
# Authenticate to Twitter


def tweet_job(api):
    data = '~/tweepy_bot/scrapers/hoy_en_la_historia.txt'
    with open(data, 'r') as filename:
        lines = filename.readlines()

    myline = random.choice(lines)

    # Get the current date
    current_date = datetime.now()

    # Format the date components separately
    day = format_decimal(current_date.day, format='##')
    month = format_date(current_date, format='MMMM', locale='es')

    # Format the date as "month day"
    # Create the formatted date with "de" separator
    formatted_date = f"{day} de {month}"

    # Tweet each line, then wait one minute and tweet another.
    # Note: this design means the bot runs continuously
    myline = myline
    mystr = myline.strip()
    mystr = f"🤖 #HoyEnLaHistoria, {formatted_date}, " + mystr + " [© 2012-2023 Hoyenlahistoria.com]"

    if len(mystr) <= 240:
        original_tweet = api.update_status(status=mystr)
        print(mystr)
    else:
        firstStr, secondStr = split_string(mystr)
        firstStr = firstStr + " [1/2]"
        secondStr = secondStr + " [2/2]"
        original_tweet = api.update_status(status=firstStr)
        api.update_status(status=secondStr,
                          in_reply_to_status_id=original_tweet.id,
                          auto_populate_reply_metadata=True)
        print(f"First tweet: {firstStr}\nsecond tweet: {secondStr}")


def main():
    api = create_api()
    tweet_job(api)


if __name__ == "__main__":
    main()
```

<p>Let's go through the script step by step:</p>

<p>The script imports the <code>random</code> module, which will be used to choose a random line from the file, and the <code>datetime</code> module from the standard library, which will be used to get the current date.</p>

<p>We also imports the <code>create_api()</code> which we created in the previous step, this function is imported from the <code>bots.config</code> module and is responsible for creating an authenticated instance of <code>tweepy.API</code> that connects to the Twitter API.</p>

<p>Aditionally, we import specific functions from the <code>babel.dates</code> and <code>babel.numbers modules</code>. These functions will be used for formatting the date and decimal numbers in a localized manner.</p>

<p>The script also imports the <code>split_string</code>function from the <code>utils.split_string</code> module. This function will be used to split the tweet into multiple parts if its length exceeds Twitter character limit.</p>

<p>The <code>tweet_job(api)</code> function is defined. This function takes the api object (the authenticated instance of <code>tweepy.API</code>) as an argument. Inside the <code>tweet_job()</code> function, the script opens a file named <code>hoy_en_la_historia.txt</code> located at the specified path. It reads all the lines from the file and stores them in the lines list.</p>

<p>The script randomly selects a line from the lines list using <code>random.choice()</code> and assigns it to the <code>myline</code> variable.</p>

<p>We also get the current date using <code>datetime.now()</code> and formats the date components separately. It formats the day as a two-digit decimal number and the month as the full month name in Spanish using the <code>format_decimal()</code> and <code>format_date()</code> functions from the babel library, respectively.</p>

<p>The script creates a formatted date string by combining the day, month, and a custom text. If the length of the tweet string <code>mystr</code> is less than or equal to 240 characters (the Twitter character limit), it directly tweets the <code>mystr</code> using <code>api.update_status()</code> and prints the tweet.</p>

<p>If the length of the tweet string exceeds 240 characters, it splits the tweet using the <code>split_string()</code> function, which splits the string into two parts while considering word boundaries. It adds a marker to indicate the order of the tweets. We'll go through it in the next step.</p>

<p>The script tweets the first part of the split string using <code>api.update_status()</code> and assigns the tweet object to <code>original_tweet</code>. It then tweets the second part as a reply to the original tweet using <code>api.update_status()</code> with the <code>in_reply_to_status_id</code> parameter set to the ID of the original tweet.</p>

<p>Also the <code>main()</code> function is defined, which calls the <code>create_api()</code> function to create an authenticated API instance and passes it to the <code>tweet_job()</code> function.</p>

<p>Finally, we use the entrypoint, which is used to check if the current module is the main module by using the <code>if __name__ == "__main__":</code> condition. If it is, it calls the <code>main()</code> function to start the execution of the script.</p>

<p>In summary, this script defines a function <code>tweet_job()</code> that reads lines from a file, selects a random line, formats the current date, and tweets the content. If the tweet exceeds the character limit, it splits the tweet into multiple parts. The script also defines a <code>main()</code> function that creates an authenticated API instance and calls <code>tweet_job()</code>. When executed as the main module, it sets everything in motion.</p>

<p>Let's checkout the <code>split_string()</code> function</p>
{% highlight python3 %}
#!/usr/bin/env python3

def split_string(string):
    if len(string) > 234:
        # First 240 characters
        first_string = string[:234]
        # Find the last space within the first 240 characters
        last_space_index = first_string.rfind(' ')
        if last_space_index != -1:
            # Truncate to the last space
            first_string = first_string[:last_space_index]
        # Remaining characters
        second_string = string[len(first_string):].strip()
    else:
        first_string = string
        second_string = ""

    return first_string, second_string
```

<p>The <code>split_string()</code> function takes a string as input and splits it into two parts while ensuring that the total length of the resulting strings does not exceed a certain limit. Here's a breakdown of the function's logic:</p>

<p>If the length of the input string is greater than 234 characters (slightly below the Twitter character limit of 240), the function proceeds to split the string. The first 234 characters of the input string are assigned to the variable <code>first_string</code>.</p>

<p>The function searches for the last space within the first 234 characters using the <code>rfind()</code> method. This helps ensure that the split occurs at a word boundary. If a space is found within the first 234 characters, <code>first_string</code> is truncated to the last space, ensuring that it doesn't cut off words. The remaining characters from the input string, after the split point, are assigned to the variable <code>second_string</code>. Any leading or trailing whitespace is stripped using the <code>strip()</code> method. If the length of the input string is less than or equal to 234 characters, the entire input string is assigned to <code>first_string</code>, and <code>second_string</code> is set to an empty string.</P>

<p>Finally, the function returns a <a href="https://www.w3schools.com/python/python_tuples.asp">tuple</a> containing <code>first_string</code> and <code>second_string</code>.</p>

<p>In summary, the <code>split_string()</code> function splits a given string into two parts, with the first part having a maximum length of 234 characters (accounting for the Twitter character limit) while ensuring that the split occurs at a word boundary. It provides a convenient way to split long strings for tweeting purposes, maintaining readability and coherence.</p>

<p>Now let's create our data scraper using bash!</p>

<p><b>Data scraper</b></p>

```
#!/usr/bin/env bash
# Secuence
url=$1
dir="$HOME/estudio/tweepy_bot/scrapers"
rm -rf "$dir"/hoy_en_la_historia.txt
echo $(curl --silent "$url" | htmlq --text | html2text) | tr -s ' ' | sed '/./G' > "$dir"/datos.txt
sed -E 's/([0-9]{3,4} -)/\n\1/g' "$dir"/datos.txt > "$dir"/output.txt
sed -i '/^\s*$/d' "$dir"/output.txt
sed -i '$ s/\./.\n/' "$dir"/output.txt
grep -v -e 'See All' -e 'SHOW' -e 'Efemérides' "$dir"/output.txt | grep -vE '^.{,60}$' > "$dir"/output2.txt
sed 's/ - /, /g' "$dir"/output2.txt > "$dir"/hoy_en_la_historia.txt

# Workspace cleanup
rm -rf "$dir"/output* "$dir"/datos*
```

<p>Here's a brief summary of the functionality of the provided bash script</p>
<p>The script takes a URL as an argument and assigns it to the <code>url</code> variable. It sets the directory path where the data will be stored in the <code>dir</code> variable. The script removes any existing <code>hoy_en_la_historia.txt</code> file in the specified directory. It retrieves data from the specified URL using <code>curl</code>, processes the HTML response using <a href="https://github.com/mgdm/htmlq">htmlq</a> and <a href="https://pypi.org/project/html2text/">html2text</a> (make sure you install first both packages, follow the hyperlinks to see the installation instructions), and stores the result in a temporary file called <code>datos.txt</code>.</p>

<p>The script performs various transformations on the datos.txt file using sed, tr, and grep commands to extract and format the desired data. Let's go through the commands used in the script one by one:</p>

<p><code>url=$1</code>: This command assigns the first argument passed to the script to the variable <code>url</code>. It allows you to provide a URL as an argument when executing the script.</p>

<p><code>dir="$HOME/estudio/tweepy_bot/scrapers"</code>: This command sets the directory path where the data will be stored. It assigns the specified path to the variable <code>dir</code>.</p>

<p><code>rm -rf "$dir"/hoy_en_la_historia.txt</code>: This command removes any existing <code>hoy_en_la_historia.txt</code> file in the specified directory <code>$dir</code>.</p>

<p><code>echo $(curl --silent "$url" | htmlq --text | html2text) | tr -s ' ' | sed '/./G' > "$dir"/datos.txt</code>: This command retrieves the HTML content from the specified URL using <code>curl</code>, processes it using <code>htmlq</code> and <code>html2text</code>, and saves the result in a temporary file called <code>datos.txt</code>. The <code>echo</code> command and subsequent pipeline manipulate the text by removing excessive spaces and adding line breaks.</p>


<p><code>sed -E 's/([0-9]{3,4} -)/\n\1/g' "$dir"/datos.txt > "$dir"/output.txt</code>: <code>([0-9]{3,4} -)</code> is the pattern that matches either a 3-digit or 4-digit sequence followed by a space and a dash. The captured group is then inserted into the replacement string <code>\n\1<code> to add a newline before the matched pattern.</p>

<p><code>sed -i '/^\s*$/d' "$dir"/output.txt</code>: This command is used to delete empty lines in the file. <code>/^\s*$/</code> is a regular expression pattern that matches empty lines. The <code>^</code> represents the start of a line, <code>\s*</code> matches zero or more whitespace characters, and <code>$</code> represents the end of a line. <code>/d</code> is the sed command to delete the matched lines.</p>

    <p><code>sed -i '$ s/\./.\n/' "$dir"/output.txt</code>: <code>$</code> matches the last line of the file. <code>s/\./.\n/</code> finds the first occurrence of a dot <code>\.</code> on the last line and replaces it with the dot followed by a newline <code>.\n</code>.</p>

<p><code>grep -v -e 'See All' -e 'SHOW' -e 'Efemérides' "$dir"/output.txt | grep -vE '^.{,60}$' > "$dir"/output2.txt</code>: This command filters out lines in <code>output3.txt</code> that contain certain keywords (See All, SHOW, Efemérides). It also removes lines that are shorter than or equal to 60 characters. The filtered lines are written to <code>output2.txt</code>.</p>

<p><code>sed 's/ - /, /g' "$dir"/output2.txt > "$dir"/hoy_en_la_historia.txt</code>: This is a substitution command that searches for the pattern "space-dash-space" <code> - </code> and replaces it with a comma and a space <code>, <c/ode>.</p>

<p><code>rm -rf "$dir"/output* "$dir"/datos*</code>: This command removes all temporary files starting with <code>output</code> and <code>datos</code> in the specified directory <code>$dir</code> to clean our workspace.</p>

<p>It saves the final formatted data into the <code>hoy_en_la_historia.txt</code> file, which is the file that we are using the get the data for our bot.</p>

<p>Now let's create the script to call our main bot module from a bash script that will be automated using crontab linux package.</p>

<p><b>Bot runner</b></p>

{% highlight python3 %}
#!/usr/bin/env python3
from bots.bot_v1 import main
import time

maxtries = 8    # 8 * 15 minutes = about 2 hours total of waiting,

for i in range(maxtries):
    try:
        main()
        break
    except:
        time.sleep(900)
        print("fail", i)
```

<p>Here's the script explanation:</p>

<p>The script imports the <code>main</code> function from the <code>bots.bot_v1</code> module Which is the function that we define when created the bot.</p>

<p>The variable <code>maxtries</code> is set to 8, indicating the maximum number of attempts the script will make to execute the <code>main()</code> function. The script enters a loop that iterates <code>maxtries</code> times using the <code>range()</code> function. Within each iteration, the <code>main()</code> function is called. If the execution of the <code>main()</code> function is successful (no exception is raised), the loop is terminated using the <code>break</code> statement, and the script finishes.</p>

<p>If an exception occurs during the execution of the <code>main()</code> function, the script pauses execution for 900 seconds (15 minutes) using the <code>time.sleep()</code> function. After the pause, the loop continues to the next iteration, and the process repeats until either the <code>main()</code> function succeeds or the maximum number of tries is reached. If the maximum number of tries is reached, the script prints <code>"fail"</code> followed by the iteration number <code>i</code> indicating the failed attempt.</p>

<p>In summary, this Python script repeatedly calls the <code>main()</code> function from the <code>bots.bot_v1</code> module with a maximum number of tries. If an exception occurs, it waits for a specific duration before retrying. The script provides a mechanism to handle failures with the cronjob call and ensures that the <code>main()</code> function is executed multiple times within a specified time frame.</p>

<p>We are about to finish, lets check the bash script that we will use to automate our bot using crontab.</p>

<p><b>Cron Tweet script</b></p>

```
# cron_script.sh
#!/usr/bin/env bash
url="https://www.hoyenlahistoria.com/efemerides.php"
cd $HOME/tweepy_bot || exit
./scrapers/scraper.sh $url
python3 bot_runner.py
```

<p><code>url="https://www.hoyenlahistoria.com/efemerides.php"</code>: This line assigns the <a href="https://www.hoyenlahistoria.com/efemerides.php">website url</a> to the variable <code>url</code>. It specifies the website from which the scraper will fetch data.</p>

<p><code>cd $HOME/tweepy_bot || exit</code>: This line changes the current directory to out <code>tweepy_bot</code> project workspace. If the directory change is unsuccessful (for example, if the directory doesn't exist), the script exits.</p>

<p><code>./scrapers/scraper.sh $url</code>: This line executes the shell script <code>scraper.sh</code> located in the scrapers directory. The script takes the value of the <code>url</code> variable as an argument and it will be the script that performs all text file operations that allows us to have a clean file to make out bot tweet for us in readability way.</p>

<p><code>python3 bot_runner.py</code>: This line executes the Python script <code>bot_runner.py</code>. It runs the script responsible for running the bot, which performs the operations based on the data fetched by the scraper.</p>

<p>In summary, this script sets the URL, changes the directory to the appropriate location, executes the scraper script with the specified URL, and then executes the bot runner script to perform operations based on the scraped data.</p>

<p>Finally, let's check our cronjob file.</p>

<p><b>Crontab job</b></p>

<p>In order to automate out bot we'll use a cronjob. The Cron daemon is a built-in Linux utility that runs processes on your system at a scheduled time. Cron reads the crontab (cron tables) for predefined commands and scripts. By using a specific syntax, you can configure a cron job to schedule scripts or other commands to run automatically.</p>

<p>Cron reads the configuration file and the daemon uses a specific syntax to interpret the lines in the crontab configuration. Let's see the syntax to understand the basic components to make it work.</p>

<p><a href="https://phoenixnap.com/kb/set-up-cron-job-linux">Here</a> you can find a detail Cron Jobs in Linux explanation but for the porpuses of our lab, i just to that you keep in mind the file components, now let's check our cron file.</p>

```
API_KEY=[your api key]
API_SECRET_KEY=[your api secret key]
ACCESS_TOKEN=[your access token]
ACCESS_TOKEN_SECRET=[your access token secret]
# m h dom mon dow command
0 6 * * * bash $HOME/tweepy_bot/cron_script.sh
```

<p>To edit this file just type in your terminal <code>crontab -e</code> which will open an editor with the default configuration. Just copy and paste the content at the end of the file. Make sure to replace your keys within the fields.</p>

<p>Let's briefly check the crontab script:</p>

<p>The <code>m h dom mon dow</code> fields represent the minute, hour, day of the month, month, and day of the week, respectively. In this case, <code>0 6 * * *</code> indicates that the specified command should run at 6:00 AM every day. <code>$HOME/tweepy_bot/cron_script.sh</code> is the path to the shell script that contains the necessary commands to run the bot, in our case we call our Cron Tweet script that we created previously.

<p>In summary, the <code>crontab</code> file is configured to execute the cron_script.sh shell script at 6:00 AM every day, which in turn runs the necessary commands to automate the bot.</p>

<p><b>This is how should look our project tree</b></p>
```
~/tweepy_bot
❯ tree
.
├── bot_runner.py
├── bots
│   ├── bot_v1.py
│   └── config.py
├── cron_script.sh
├── scrapers
│   └── scraper.sh
└── utils
    └── split_string.py

4 directorie, 6 files
```

<p>Now we're done with our first twitter bot!</p>

<p><b>Conclusion</b></p>
<p>Creating a Twitter bot using Tweepy and the Twitter API has been a rewarding experience. Through the use of Tweepy's Python library and the authentication credentials provided by the Twitter developer account, I was able to automate the process of tweeting daily. By fetching data from a website, composing tweets, and formatting them appropriately, the bot script fulfilled the requirements of my school program. The implementation of Crontab jobs ensured the bot's automation, allowing for consistent and timely tweets. Overall, this project has not only deepened my understanding of APIs, data scraping, and automation but has also strengthened my skills as a software developer.</p>
