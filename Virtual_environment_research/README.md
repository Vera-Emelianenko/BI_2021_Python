OS system to run the script: WSL1 Ubuntu-20.04 in Windows Terminal 1.11.2921.0 in Microsoft Windows [Version 10.0.19043.1288] (Windows 10 Home Version 21H1). 

All the requirements for the script are listed in requirements.py, one library per line. 

At any step, you can check that pain.py works (or not) by typing 

```
python3.9 pain.py
```

To run the script from wsl1 in Microsoft Windows [Version 10.0.19043.1288]: 

1. First, get python 3.9, since pain.py contains "|" operator for dictionaries that is only supported for python 3.9 
The instruction to install python 3.9 can be found at https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-9-0-on-ubuntu-18-04-lts/

I used the following commands from the fish shell in wsl (all command run from the same folder which contained pain.py): 

```
bash # I use this since I have fish shell by default 
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
apt-get update
apt list | grep python3.9 # Verify the updated Python packages list  
sudo apt-get install python3.9
sudo apt install python3.9-distutils
python3.9  # verify that you have python 3.9 now 
>>> exit() # exit python 
```

Now we are all set with python and we can create virtual environment for pain! 

2. Setting virtual environment
```
python3.9 -m pip install --upgrade pip setuptools virtualenv
python3.9 -m virtualenv pain
source pain/bin/activate
```

If you activated the environment right, you should see the environment name in brachets. In my case, it looks like this: 

```
$ source pain/bin/activate
(pain)
```

3. Install dependencies: 

```
python3.9 -m pip install kivy[base] kivy_examples
python3.9 -m pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
python3.9 -m pip install --upgrade bs4
python3.9 -m pip install --upgrade Bio
python3.9 -m pip install --upgrade aiohttp
python3.9 -m pip install --upgrade pandas
python3.9 -m pip install --upgrade scipy
python3.9 -m pip install scanpy # in my case, reopening terminal was needed to install scanpy 
python3.9 -m pip install opencv-python
python3.9 -m pip install lxml
```

4. Getting graphical interface for wsl 

All the necessary libraries seem to be installed, but the script required graphical interface which is not a part of wsl by default. 

Instruction to install simple wsl graphical interface can be found here: https://medium.com/@dhanar.santika/installing-wsl-with-gui-using-vcxsrv-6f307e96fac0

In short: 
1) Go to https://sourceforge.net/projects/vcxsrv/, download the program and install it on Windows (by executing .exe file)
2) Choose One Large Window, Start No Client, check the "Disable access control" option. You should see big black window appear. 

Now, return to wsl command line and install xfce4. 

```
sudo apt-get install xfce4
cd ~
nano .bashrc
```
Now, as a last line of the opened file, write `export DISPLAY=:0.0`

Exit wsl and run it again (I do `bash` and `source pain/bin/activate` again to enter the same env). To check that  xfce4 works, try running

```
startxfce4
```
If the black screen changes to sort of 'Desktop', you are good to go! 

5. Checking pain.py

Now you can load pain.py. Go to the directory with pain.py, make sure you are in the same env where you installed all the dependencies (`source pain/bin/activate`). Run 

```
python3.9 pain.py
```
You should see the window with the text "Ура, всё работает!"