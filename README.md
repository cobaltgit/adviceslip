# A simple client for Tom Kiss' Advice Slip API that doubles as a command line application

## Installation

```bash
# PyPi install
$ python3.8 -m pip install adviceslip # Python 3.8 or higher is required
# Git install
$ python3.8 -m pip install git+https://github.com/cobaltgit/adviceslip
```

## Example usage

### In a Python program

```py
import adviceslip

with adviceslip.Client() as client: # automatically close client using context manager
    random_slip = client.random() # get a random slip

    slip_id = 12
    slip_from_id = client.slip_from_id(slip_id) # get a slip from an ID

    search = client.search("good") # returns a search object, which contains an iterator of slip objects

print(random_slip.id) # print the ID of the random slip

print(slip_from_id.advice) # print the advice from a slip

print(f"Total results from search: {search.total_results}") # print the amount of results from a search object
for slip in search: # iterate over the search object
    print(f"#{slip.id}: {slip.date} - {slip.advice}") # print the ID, date and advice of each slip
```

### Command Line

To utilise the command line application, you'll need to install the cli extra  
```bash
$ pip install adviceslip[cli]
```

```bash
$ adviceslip --id 12 # Get a slip from a specific ID
Always block trolls.

$ adviceslip --random # Get a random slip
Eliminate the unnecessary.

$ adviceslip --search good # Search for slips using a given query
#92: You can have too much of a good thing. - 2016-08-09
#95: Good advice is something a man gives when he is too old to set a bad example. - 2016-09-15
#120: A nod is as good as a wink to a blind horse. - 2016-12-11
#122: You spend half your life asleep or in bed. It's worth spending money on a good mattress, decent pillows and a comfy duvet. - 2016-05-25
#174: Be a good lover. - 2014-06-03
#176: Good things come to those who wait. - 2017-02-04
#179: Never regret. If it's good, it's wonderful. If it's bad, it's experience. - 2016-12-03
#180: Never regret. If it's good, it's wonderful. If it's bad, it's experience. - 2015-06-24
#215: Once you find a really good friend don't do anything that could mess up your friendship. - 2016-03-01
```

## Development

Feel free to contribute to the library! Here's some simple instructions to get you set up and ready!  

* First, you'll need to fork the repository and clone it to a directory on your computer with Git.

```bash
$ git clone https://github.com/username/adviceslip.git # replace username with your GitHub username
```

* Next, install the development dependencies for testing and development purposes. Use the following commands

```bash
$ poetry install
$ poetry run pre-commit install # installs the pre-commit hook for code formatting and linting
```

#### Testing

Before you PR any changes, please test your code
Testing can be done across all compatible Python versions with a simple Tox command that runs `pytest` on your code!

```bash
$ poetry run tox
```
