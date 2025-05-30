import time
import argparse
import pyautogui

screenWidth, screenHeight = pyautogui.size() #til hvor man skal klikke (ik pil)
skiptid = 60 # i sekunder (ik pil)
i = 1        # sangnummer (ik pil)

parser=argparse.ArgumentParser(description="spotify_skippers input parseren. Brug -o til at sætte opstartstiden (ellers 10s) og brug -s til at sætte sangens starttidspunkt (ellers 0s inde i sangen).")


parser.add_argument("-o", type=int)
parser.add_argument("-s", type=int)

args = parser.parse_args()

opstartstid = args.o if not args.o is None else 10

starttidspunkt = args.s if not args.s is None else 0

førstepause = skiptid-starttidspunkt if starttidspunkt <=60 else 0
    

def skiploop():
    global i
    time.sleep(skiptid)
    print(f"Skipper nr. {i}")
    pyautogui.click(screenWidth//2+screenWidth//24, screenHeight - screenHeight//6)
    i+=1

def skipper(opstartstid, starttidspunkt):
    global i
    global førstepause
    print(f"Du har {opstartstid} sekunder fra nu til at åbne spotify på fuldskærm, med sangen pauset på {starttidspunkt} sekunder inde i sangen.")

    time.sleep(opstartstid)

    print("Starter nu :)")
    pyautogui.click(screenWidth//2, screenHeight - screenHeight//6)

    time.sleep(førstepause)
    print(f"Skipper nr. {i}")
    pyautogui.click(screenWidth//2+screenWidth//24, screenHeight - screenHeight//6)
    i+=1
    while(True):
        time.sleep(skiptid)
        print(f"Skipper nr. {i}")
        pyautogui.click(screenWidth//2+screenWidth//24, screenHeight - screenHeight//6)
        i+=1


if __name__ == "__main__":

    skipper(opstartstid, starttidspunkt)
