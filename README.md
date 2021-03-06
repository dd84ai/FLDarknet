# FLDarkNet
Website for [Freeancer Discovery community](https://discoverygc.com/forums) \
The main purpose to provide info about in game stuff, and game server side information \
 \
we can describe it in short words as \
Online flstat \
but with server side info (static and dynamic) \
for more info look for [Future plans](https://github.com/dd84ai/fldarknet/blob/main/README.md#philosophy) section below

![image](https://user-images.githubusercontent.com/20555918/113764510-402a8c80-9745-11eb-9365-25a3b67b8212.png)

# Tech stack
* Python 3.8.6
* Django 3.1.7
* Docker
* Jinja2
* Bootstrap
* Javascript

# Contributing
## Installing instruction

### Linux Ubuntu

```
apt-get update
apt-get -y install python3.8 python3-pip python3-venv
apt-get -y install git
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

# Deployment

- install docker
- python scripts.py dock deploy

# Testing
make sure to run this before submitting your work

- python scripts.py test full # makes sure nothing falls apart

for a more detailed information you can run next sequence:

- python scripts.py test pylint
- python scripts.py test flake
- python scripts.py test unit
- python scripts.py test cover

# Running

- python scripts.py run
```
Options:
  -d, --debug            enables debug
  -f, --folder TEXT      sets path to freelancer folder for parsing in
                         background, default='dark_copy'

  -t, --timeout INTEGER  sets timeout between parsing loops
  --help                 Show this message and exit.
```

# Notes
Author works in Visual Studio code \
All types of modes to launch the server can be quickly launched from its "run" interface \
[.vscode/.launch](https://github.com/dd84ai/fldarknet/blob/main/.vscode/launch.json) has settings for that \

# Code organizations
* Prefer English over your native language in comments and commit messages.
* If your code can be unit-tested, add unit tests.
* Run unit testing when you start working and before making any commit
* Run pylint checker and fix all new errors, which were not in the last not your commit
* fix errors appeared in workflow if they appeared (after commit or opened pull request) \
![image](https://user-images.githubusercontent.com/20555918/113766107-43267c80-9747-11eb-8945-9d6bed920ad6.png)
* Name your commits according to [Convetional Commits 1.0 style](https://www.conventionalcommits.org/en/v1.0.0/)
* The cardinal rule for creating good commits is to ensure there is only one logical change per commit / read [Structural split of changes](https://wiki.openstack.org/wiki/GitCommitMessages#Structural_split_of_changes)
* (Optonally, but highly preffered) [Issues](https://github.com/dd84ai/fldarknet/issues) are created in order to gather information before you can submit Pull Request of your work
* For further inspirations in syle and code organizations, author looks [here](https://github.com/f213/education-backend) and [here](https://searx.github.io/searx/dev/contribution_guide.html#documentation)
* Add yourself to [AUTHORS.rst](https://github.com/dd84ai/fldarknet/blob/main/AUTHORS.rst)

# Submitting pull requests
Explain:
* What it brings  # human-like description
* Features        # if necessary links to relative commits or issues 
* Fixes           # if necessary links to relative commits or issues
* API             # if necessary mention any added new flags / commands
* Notes           # if necessary

# Future plans
* Parsing data for more tables from Universe folder
* Parsing data from FLhook configs \
For example: About mining bonuses, server side prices, tech compatilibities, cloak/jump stats. \
We aim to replace tutorials maintained by players
* Adding dynamic data from [FLHook](https://github.com/DiscoveryGC/FLHook), [My flhook fork](https://github.com/dd84ai/FLHook) by json'ifications. \
For example: which player bases have available ores for sale (or equipment). 
* Making custom front interface to render main tables, and its sub table based on chosen row in main one (inspired by [FLstat](https://discoverygc.com/forums/showthread.php?tid=115254&pid=1524529#pid1524529))

# Philosophy
* Easy installation and deployments: The project is highly probably going to be dockerized for easiest effort to be used by any Linux Server administrator. Preferably we are going to make some sort of automated deploying system.
* Full automatization: Every extracted data should be fully automated, the app should parse the data and launch in its working state without any human-changable data to maintain it.
* Speed: We can make relatively long operations during server start, but during client usage everything should be as fast as possible. Minimalistic GUI interface will be prefered. SQL queries should be as fast as possible too.

# Contacts
* Email: dd84ai+fldarknet@gmail.com
* Discord: Darkwind#7896 at [fldarknet server](https://discord.gg/KTUcZyv98q)
* Discovery: [Private messages](https://discoverygc.com/forums/member.php?action=profile)
