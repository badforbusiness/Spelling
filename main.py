import csv
import vlc
import time
import random
from gtts import gTTS

with open('timetotal.csv', newline='') as f:
    reader = csv.reader(f)
    totaltime = list(reader)
f.close()

tTime = 0

for times in totaltime:
    tTime = tTime + int(times[1])

word = ("you have this much minecraft time:" + str(tTime) + "  Minutes,  " + "how many minutes would you like to earn" )
tts = gTTS(text=word, lang='en')
tts.save("interim.mp3")
p = vlc.MediaPlayer("interim.mp3")
p.play()
time.sleep(8)
p.stop()









number = int(input("number:"))


# open persistant list
with open('list.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
f.close()
#print(data)


sample_list = random.sample(data, k= number)
#print(sample_list)



for line in sample_list:

    line[2] = str(int(line[2]) + 1)

    currentword = line[1]

    x = 0
    while x < 3:
        # get word from list and play
        word = ("Spell    , " + currentword)
        tts = gTTS(text=word, lang='en')
        tts.save("interim.mp3")
        p = vlc.MediaPlayer("interim.mp3")
        p.play()
        time.sleep(2)
        p.stop()


        # get the input
        text = input("Please spell:")  # Python 3

        #test
        if text==currentword:
            line[3] = str(int(line[3]) + 1)
            print ("correct")
            x = 3
        else: x = x + 1




# save the result
with open('list.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerows(data)

word = ("you have earned" + str(number) + "minutes of minecraft time")
tts = gTTS(text=word, lang='en')
tts.save("interim.mp3")
p = vlc.MediaPlayer("interim.mp3")
p.play()
time.sleep(3)
p.stop()


with open('timetotal.csv', 'w', newline='') as f:
    write = csv.writer(f)
    totaltime.append([time.gmtime() , number])
    write.writerows(totaltime)


s = vlc.MediaPlayer("spon.mp3")
s.play()
time.sleep(50)
s.stop()