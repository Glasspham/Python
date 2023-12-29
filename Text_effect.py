from time import sleep

def animatedText(text, time=0.1):
    length = len(text)
    step = -1
    while True:
        step *= -1
        a, b =(length - 1, length) if step == 1 else (2, -1)
        for i in range(length - a, b, step):
            bwText = ""
            for j in range(length):
                bwText += ("\033[1;7m" + text[j] + "\033[0m") if i == j else text[j]
            print(bwText, end="\r")
            sleep(time)

animatedText("Hello world")
