from claptcha import Claptcha
import os
import numpy as np
import cv2

def generateCaptcha(outdir, font, num_captchas=200):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alphabets = alphabets.upper()
    
    try:
        os.mkdir(outdir)
    except:
        "Directory already present, saving captcha to the directory."
    
    # Select one alphabet if indicator 1 else number
    for i in range(num_captchas):
        char_num_ind = list(np.random.randint(0, 2, 4))
        text = ""
        for ind in char_num_ind:
            if ind == 1:
                loc = np.random.randint(0, 26, 1)
                text = text + alphabets[np.random.randint(0, 26, 1)[0]]
            else:
                text = text + str(np.random.randint(0, 10, 1)[0])
        
        c = Claptcha(text, font)
        text, image = c.image
        image.save(outdir + "/" + text + ".png")
    
    print(f"{num_captchas} {outdir} CAPTCHAs generated.")

def mainProcess(outdir_train, num_captchas_train,
                outdir_val, num_captchas_val,
                outdir_test, num_captchas_test,
                font="CartographCF-Bold.otf"):

    generateCaptcha(outdir_train, font, num_captchas_train)
    generateCaptcha(outdir_val, font, num_captchas_val)
    generateCaptcha(outdir_test, font, num_captchas_test)
    
if __name__ == "__main__":
    mainProcess("train", 100,
                "val", 100,
                "test", 100)
    
    print("Process Complete. CAPTCHAs generated.")