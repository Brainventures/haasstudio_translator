import pandas as pd
import numpy as np
import os


def pre_translate_file_search(file_name):
    if os.path.isfile(file_name):
        pre_trans_nouns_data = pd.read_excel(file_name, engine='openpyxl')
        return pre_trans_nouns_data


def pre_translate(sentence, file_name, output_lang):
    pre_trans_nouns_data = pre_translate_file_search(file_name)
    if isinstance(pre_trans_nouns_data, type(None)):
        print(f"사전번역 파일이 경로 안에 없습니다. 파일을 현재 경로로 옮겨주세요.\n ---> {os.getcwd()}")
    else:
        if output_lang == 'zh':
            temp_output_lang = 'ch'
        else:
            temp_output_lang = output_lang
        for i in range(len(pre_trans_nouns_data)):
            pre_data = pre_trans_nouns_data[['Noun_KR', f'Noun_{temp_output_lang.upper()}']]
            input_pre_noun = pre_data.iloc[i, 0]
            idx = sentence.find(input_pre_noun)
            if idx != -1:
                if pre_data.iloc[i, 1] is not np.nan:
                    sentence = sentence.replace(
                        sentence[idx:idx+len(input_pre_noun)],
                        pre_data.iloc[i, 1]
                    )
        return sentence