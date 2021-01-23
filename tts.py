import sys
import pyttsx3

def main():
    tts = pyttsx3.init()
    if(len(sys.argv)<2):
        stdin = True
    else:
        for i in sys.argv:
            if(i=='-h'):
                print("Usage: python tts.py [filename]")
                exit()
        stdin = False
    if(stdin):
        while(1):
            sInput = input()
            tts.say(sInput)
            tts.runAndWait()
    else:
        with open(sys.argv[1], 'r') as f:
            fInput = f.readlines()
            for i in fInput:
                tts.say(i)
                tts.runAndWait()
    tts.stop()

if __name__ == '__main__':
    main()
