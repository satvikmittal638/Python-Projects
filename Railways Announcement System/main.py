import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
    """
    Makes the mp3 of the text given
    :param text:text to convert to speech
    :param filename:file into which the text will be converted
    :return:
    """
    myTxt = str(text)
    language = "hi"
    gTTS(text=myTxt, lang=language, slow=True).save(filename)


def mergeAudios(audiosList):
    """
    Merges the audio files using pyDub
    It appends all the audio files to an empty AudioSegment using a for loop
    :return:pyDub audio segment
    """
    combined_audios = AudioSegment.empty()
    for audio in audiosList:
        combined_audios += combined_audios.from_mp3(audio)
    return combined_audios


def generateSkeleton():
    """
    Generates required cropped portion of the hindidi audio announcement
    :return:
    """
    audio = AudioSegment.from_mp3("railway.mp3")

    # 1 - कृपया ध्यान दीजिये
    start = 88000
    end = 90200
    audio_processed = audio[start:end]
    audio_processed.export("1_hindi.mp3")

    # 2 - (place)

    # 3 -  से चलकर
    start = 91000
    end = 92200
    audio_processed = audio[start:end]
    audio_processed.export("3_hindi.mp3")

    # 4 - (via place)

    # 5 - के रास्ते
    start = 94000
    end = 95000
    audio_processed = audio[start:end]
    audio_processed.export("5_hindi.mp3")

    # 6 - (destination place)

    # 7 - को जाने वाली गाडी संख्या
    start = 96000
    end = 98900
    audio_processed = audio[start:end]
    audio_processed.export("7_hindi.mp3")

    # 8 - (number and name)

    # 9 - कुछ ही समय में प्लेटफार्म संख्या
    start = 105500
    end = 108200
    audio_processed = audio[start:end]
    audio_processed.export("9_hindi.mp3")

    # 10 - (number)

    # 11 - पर आ रही है
    start = 109000
    end = 112250
    audio_processed = audio[start:end]
    audio_processed.export("11_hindi.mp3")


def generateAnnouncement(excelFile):
    """
    Generates the announcement after reading the required parameters from the item file
    :param excelFile: the path to the item file which would be read using pandas
    :return:
    """
    excel = pd.read_excel(excelFile)
    print(excel)

    # individual announcement are made row wise
    for index, item in excel.iterrows():
        # 2 - from
        textToSpeech(item['from'], '2_hindi.mp3')

        # 4 - via
        textToSpeech(item['via'], '4_hindi.mp3')

        # 6 - to
        textToSpeech(item['to'], '6_hindi.mp3')

        # 8 - Train no. and name
        textToSpeech(f"{item['train_no']} {item['train_name']}", '8_hindi.mp3')

        # 10 - platform no.
        textToSpeech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1, 12)]
        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{index + 1}_hindi.mp3", format="mp3")


if __name__ == '__main__':
    print("Generating skeleton..")
    generateSkeleton()
    print("Skeleton generated")
    print("Generating announcement")
    generateAnnouncement("announce_hindi.xlsx")
    print("Announcement generated successfully")
