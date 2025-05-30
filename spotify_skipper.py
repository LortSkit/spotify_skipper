import time
import argparse
import pyautogui

screenWidth, screenHeight = pyautogui.size() #til hvor man skal klikke (ik pil)
skiptid = 60 # i sekunder (ik pil)
i = 1        # sangnummer (ik pil)
widthparameter = 38  # pil kun hvis den ikke rammer skip knappen (24 før, nu 38)
heightparameter = 10 # pil kun hvis den rammer over/under knappen (6 før, nu 10)

parser=argparse.ArgumentParser(description="spotify_skippers input parseren. Brug -o til at sætte opstartstiden (ellers 5s) og brug -s til at sætte sangens starttidspunkt (ellers 0s inde i sangen).")


parser.add_argument("-o", type=int)
parser.add_argument("-s", type=int)

args = parser.parse_args()

opstartstid = args.o if not args.o is None else 5

starttidspunkt = args.s if not args.s is None else 0

førstepause = skiptid-starttidspunkt if starttidspunkt <=60 else 0
    

def clickskip():
    pyautogui.click(screenWidth//2+screenWidth//widthparameter, screenHeight - screenHeight//heightparameter)

def clickplay():
    pyautogui.click(screenWidth//2, screenHeight - screenHeight//heightparameter)

def _skip_internal(skiptid):
    global i
    time.sleep(skiptid)
    print(f"Skipper nr. {i}")
    clickskip()
    i+=1

def skipinitial():
    _skip_internal(førstepause)

def skiploop():
    _skip_internal(skiptid)


def skipper(opstartstid, starttidspunkt):
    print(f"Du har {opstartstid} sekunder fra nu til at åbne spotify på fuldskærm, med sangen pauset på {starttidspunkt} sekunder inde i sangen.")

    time.sleep(opstartstid)

    print("Starter nu :)")
    clickplay()

    skipinitial()
    while(True):
        skiploop()


if __name__ == "__main__":

    skipper(opstartstid, starttidspunkt)
