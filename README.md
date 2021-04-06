# FLDarkNet
Website for Freeancer Discovery community located at https://discoverygc.com/forums
The main purpose to provide info about in game stuff, and game server side information

![image](https://user-images.githubusercontent.com/20555918/113764510-402a8c80-9745-11eb-9365-25a3b67b8212.png)


# Contributing
## Installing instruction

### Windows:

```
install python 3.8 or higher #author prefers 3.8.6 because uses Windows 7
python -m venv venv          #to create virtual venv folder
venv\Scripts\active
pip install -r requirements.txt

set FREELANCER_FOLDER=dark_copy        #Freelancer files folder in this reposity, but you can set path to real freelancer Folder
set DARK_PARSE=true                    #Flag to parse files
set DARK_SAVE=true                     #flag to save as db dump
python manage.py runserver
```

### Linux Ubuntu

```
apt-get update
apt-get -y install python3.8 python3-pip python3-venv
apt-get -y install git
python3 -m venv venv
source venv/bin/activate


pip install -r requirements.txt
export FREELANCER_FOLDER=dark_copy        #Freelancer files folder in this reposity, but you can set path to real freelancer Folder
export DARK_PARSE=true                    #Flag to parse files
export DARK_SAVE=true                     #flag to save as db dump
python manage.py runserver
```

# Unit testing
### light unit test testing from db dump without parsing
```
export DARK_PARSE=true
python manage.py test
```

### full unit testing with parsing from Freelancer saved copy
```
export FREELANCER_FOLDER=dark_copy
export DARK_PARSE=true //flag to parse
export DARK_SAVE=true //flag to save as db dump
python manage.py runserver
```

# Stastic code checkers
We use pylint with its plugin for django \
instructions to run in different OS below 
### Windows 
```
scripts\fldarknet_pylint.bat
```

### Linux
```
pylint --load-plugins pylint_django --django-settings-module="fldarknet.settings" --disable=django-not-configured fldarknet main ship commodities
```

# Available flags

```
FREELANCER_FOLDER=Freelancer    #set path to freelancer folder, default 'Freelancer'
DARK_PARSE=false                #set true to data by parsing freelancer folder (FREELANCER_FOLDER flag should be active)
DARK_SAVE=false                 #set true to save parsed data to database dump after parsing finish (requires active DARK_PARSE flag)
DARL_LOAD=false                 #set true to load data from database dump (dump.json file in root) (other flags should be not active)
DARK_COPY=false                 #set true to refresh data in dark_copy folder, if extracted data from another Freelancer folder (DARK_PARSE should be active)
```

# Notes
Author works in Visual Studio code \
All types of modes to launch the server can be quickly launched from its "run" interface \
[.vscode/.launch](https://github.com/dd84ai/fldarknet/blob/main/.vscode/launch.json) has settings for that \

# Code organizations
* Prefer English over your native language in comments and commit messages.
* If your code can be unit-tested, add unit tests.
* Run light and full unit testing when you start working and before making any commit
* Run pylint checker and fix all new errors, [which were not there before](https://github.com/dd84ai/fldarknet/runs/2263439228?check_suite_focus=true)
* Name your commits according to [Convetional Commits 1.0 style](https://www.conventionalcommits.org/en/v1.0.0/)
* The cardinal rule for creating good commits is to ensure there is only one logical change per commit / read [Structural split of changes](https://wiki.openstack.org/wiki/GitCommitMessages#Structural_split_of_changes)
* For further inspirations in syle and code organizations, author looks [here](https://github.com/f213/education-backend) and [here](https://searx.github.io/searx/dev/contribution_guide.html#documentation)

# Submitting pull requests
Explain:
* What it brings  # human-like description
* Features        # if necessary links to relative commits or issues 
* Fixes           # if necessary links to relative commits or issues
* API             # if necessary mention any added new flags / commands
* Notes           # if necessary

# Future plans
* Parsing data for more tables from Universe folder
* Parsing data from FLhook configs
* Adding dynamic data from [FLHook](https://github.com/DiscoveryGC/FLHook) by json'ifications. For exampple: which player bases sell ores. [My flhook fork](https://github.com/dd84ai/FLHook)
* Making custom front interface to render main tables, and its sub table based on chosen row in main one (inspired by [FLstat](https://discoverygc.com/forums/showthread.php?tid=115254&pid=1524529#pid1524529))
