import os
import sys
import pandas as pd
import logging


# save logs
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("./get_text_info_log.txt")
streamHandler = logging.StreamHandler()
logger.addHandler(file_handler)
logger.addHandler(streamHandler)


def text_data_information(file):
    count = 0
    spaces = 0
    char_count = 0
    word_count = 0
    word_count_without = 0

    for line_count, line in enumerate(file):
        count = line_count + 1

        spaces += line.count(' ')

        word_count += len(line.split(" "))

        split_line = line.split(" ")
        without = [word for word in split_line if word != '\n']
        word_count_without += len((without))

        char_count += line.__len__()

    df = pd.DataFrame({'문장수': count, '공백수': spaces, '단어수-공백포함': word_count, \
                       '단어수-공백제외': word_count_without, '글자수': char_count},
                      index=['{}'.format(file.name[7:])])

    return df

def all_text_data_information():
    listdir=os.listdir('./data/')
    all_information=pd.DataFrame()
    information_list=[]

    for list in listdir:
        try :
            logger.info('open file : {}'.format(list))
            file = open("./data/{}".format(list))
            information = text_data_information(file)

        except :
            logger.info('ERROR : failed at opening a file : {}'.format(list))

        information_list.append(information)
        logger.info('close file : {}'.format(list))
        file.close()

    all_information=pd.concat(information_list,ignore_index=False)
    all_information.to_excel('./test_data_information.xlsx')
    logger.info('Finished! Text data information is saved in ./test_data_information.xlsx')

all_text_data_information()