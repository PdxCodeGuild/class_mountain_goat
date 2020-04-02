

# Setup

This document contains an overview for the software setup for the course. Please try to get as much done as possible before the course starts, but we'll also go over the setup on the first day of class to ensure everyone's up to speed.

We'll be using [Zoom](https://zoom.us/) to hold class online, I'll post a link to each day's meeting on Slack. Students are required to have their video on the majority of the time to ensure they're engaged, but if you're concerned about privacy you can set a "virtual background" by clicking the arrow next to the video icon and selecting "choose virtual background". You can find some free backgrounds [here](https://www.shutterstock.com/discover/free-virtual-backgrounds). You're also welcome to mute yourself if you're not talking to cut down on background noise. Zoom also allows people to share their screens.

## 1 Pick a CLI

CLI stands for 'command-line interface', and it was the only way to use a computer before the development of GUIs 'graphical user interface'. It's still used to perform many computer operations that go 'under the hood'.

#### Opening the CLI

In OS X, the default CLI is called `Terminal`, which you can find by typing `terminal` in search, or under `Finder -> Applications -> Utilities`.

In Windows, the default CLI is `cmd`, which you can find by typing `cmd` in search, or pressing `Windows+R`, typing `cmd`, and hitting `enter`. This will work for executing python, but there's no color differentiation, and some commands like `ls` and `rm` won't work in `cmd`. A much better CLI is [Cmder](http://cmder.net/). Another option for Windows is [Powershell](https://msdn.microsoft.com/en-us/powershell/scripting/setup/installing-windows-powershell).

In Linux, you can open a terminal with `Ctrl + Alt + T`.

Visual Studio Code also has a terminal built in, which you can access with `ctrl+j` or using the main menu `Terminal -> New Terminal`.

#### Common CLI Commands

- `pwd` displays the path of the current directory
- `ls` lists the contents of the current directory
- `cd <directoryname>` change directory
    - `cd ..` will bring you into the parent directory
    - `cd` alone will return you to your 'home' directory
- `mkdir <foldername>` create a new folder 
- `rmdir <foldername>` removes a folder
- `rm <filename>` removes a file
- `mv filename1 filename2` moves or renames a file
- `cp filename1 filename2` copies a file
- `up-arrow` will bring up the last command entered
- `tab` will attempt to autocomplete whatever you're typing
    - try `cd D` + `tab` + `tab`
- `ctrl+c` kill currently running process

## 2 Install the latest version of [Python (3.8.2)](https://www.python.org/downloads/)

Python is a programming language, and we'll be using the python interpreter in order to run our code. We'll write our source code in text files with the extension `.py` and run the code by running `python file.py` in our terminals. You can find more info in the [official docs](https://docs.python.org/3/using/cmdline.html).


- `python` start the interactive interpreter
- `python <file>` execute the python source code in the given file
- `python --help` print out all command-line options
- `python --version` show which version of python you're using

If you're on windows be sure to select "add python to path" when installing. You can check whether the installation was successful by running `python --version` or `python3 --version`.

## 2 Install [Git](https://git-scm.com/downloads) and make a [GitHub](https://github.com/) account

Git is a version control system, it keeps tracks of changes to files to allow developers to undo changes and collaborate on projects. You can check whether the installation was successful by running `git` in a terminal which should show a list of commands.

GitHub is a hosting service for Git repositories. Our class will have a repository hosted there we'll collaborate on. It also serves as a programmer's portfolio, potential employers can see your activity and code you commit, so make sure you commit changes regularly and only commit clean, working code.

## 3 Install [Visual Studio Code](https://code.visualstudio.com/)

Visual Studio Code is a source code editor we'll be using. It includes many helpful features that will make editing code easier. You're also welcome to check out [Atom](https://atom.io/) or [PyCharm](https://www.jetbrains.com/pycharm/).

## 4 Install [Slack](https://slack.com/)

Slack is an instant messaging service we'll use to communicate. If you send me an email `matthew@pdxcodeguild.com` I can send you an invite to PDX Code Guild's Slack. You can use Slack in a browser, but it can also be installed as a desktop and mobile app.

- Desktop: [Windows](https://slack.com/downloads/windows), [Mac](https://slack.com/downloads/mac), [Linux](https://slack.com/downloads/linux)
- Mobile: [Android](https://slack.com/downloads/android), [iOS](https://slack.com/downloads/ios)
