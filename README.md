# Installation

## Step 1 - Install python

To run this program you must first [install python](https://www.python.org/downloads/). It will most likely placed python in `C:\Python***`, where `***` is the version number (if python 3.13 is installed, then it's in the folder `C:\Python313`, for example.)

## Step 2 - Add Python to the PATH

Open a terminal and type the following command:

```
python --version
```

If it displays a version, you're ready to go to step 3. If you instead get an error, then you need to [add python to your PATH](https://stackoverflow.com/questions/4621255/how-do-i-run-a-python-program-in-the-command-prompt-in-windows-7). The instructions are as follows:

- Press the windows key and type "environment" (or "miljø" in Danish), and press enter
- In the window that opened, press the bottom-right button "Environment Variables..." ("Miljøvariabler...").
- In the bottom table labelled "System variables" ("Systemvariabler"), find the variable named "Path". Click on it and press the "Edit..." ("Rediger...") button.
- Press "New" ("Ny") and type `C:\Python***` (make sure it's the right name!)
- Press ok on everything
- Open a new terminal again (has to be new), and retype `python --version` to see that it works.

## Step 3 - Install dependencies

Now we need the pyautogui package to allow for the program to use your mouse to click. To download that package, type the following command into a terminal:

```
pip install pyautogui
```

Once that's done, you're ready to run the program

# How to run spotify_skipper

If you haven't already, clone this repository (you only need the `spotify_skipper.py` file). Open a terminal with the python file inside. You can run the program by typing the following command:

```
py .\spotify_skipper.py -o 5 -s 0
```

You will see the following message displayed:

```
Du har 5 sekunder fra nu til at åbne spotify på fuldskærm, med sangen pauset på 0 sekunder inde i sangen.
```

If you are starting in the middle of the song, simply type `-s 23` to make sure it knows that you're 23 seconds into the first song (for example). If you don't wanna wait 5 seconds until the program start, simply type `-o 2` to only wait 2 seconds instead. Capiche?

## Troubleshooting - It's clicking in the wrong places!

If the program doesn't quite hit the buttons, then open the `spotify_skipper.py` file and look at lines 8-9:

```
widthparameter = 38  # pil kun hvis den ikke rammer skip knappen (24 før, nu 38)
heightparameter = 10 # pil kun hvis den rammer over/under knappen (6 før, nu 10)
```

Make the the widthparameter a bigger number, if you want it to go more towards the middle of the screen (go left).

Make the heightparameter bigger, if you want to move it down the screen.

And vice versa for both.
