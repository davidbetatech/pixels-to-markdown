import os
import time
import datetime
import json

date = [{}]
path = ""


def createDir():
    path = os.getcwd() + "/test"
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)
    return path


def betterName(p):
    year = p['date'][0:4]
    month = p['date'][5:7]
    day = p['date'][8:10]
    return (month + '-' + day + '-' + year)


def modTime(p, filename):
    year = p['date'][:4]
    month = p['date'][5:7]
    day = p['date'][8:10]
    hour = 0
    minute = 0
    second = 0
    date = datetime.datetime(year=int(year), month=int(
        month), day=int(day), hour=hour, minute=minute, second=second)
    modTime = time.mktime(date.timetuple())
    os.utime(filename, (modTime, modTime))
    return


def mood(i):
    tag = ""
    if(i == 1):
        tag = "worst"
    elif(i == 2):
        tag = 'bad'
    elif(i == 3):
        tag = 'okay'
    elif(i == 4):
        tag = 'good'
    elif(i == 5):
        tag = "best"
    return tag


def writeEmotions(emotions, f):
    emotions.sort()
    f.write('## Emotions: \n')
    for e in emotions:
        f.write('- ' + e + '\n')
    return


def noteCreator(p, path):
    name = betterName(p)
    filename = path + '/' + name + '.md'
    f = open(filename, "w+")
    m = p['mood']
    moods = mood(m)
    modTime(p, filename)
    f.write('# ' + name + '\n')
    f.write('## Mood: ' + moods + '\n---\n')
    f.write(p['notes'] + '\n' + '\n---\n')
    # f.write('Emotions: ' + str(p[
    #     'emotions'
    # ]))
    writeEmotions(p['emotions'], f)
    f.close()
    return


with open('untitled.txt',  'r', encoding='utf8', errors='ignore') as json_file:
    data = json.load(json_file)
    path = createDir()
    for p in data:
        noteCreator(p, path)
