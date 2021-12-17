"""
번역 파이프라인 : 문장 입력 -> 사전 번역 -> 문장 번역
"""

from pretrans import pre_translate
import torch
import streamlit as st
from kobart import get_kobart_tokenizer
from transformers.models.bart import BartForConditionalGeneration

# 개체명 사전 번역 표
ARCHITECTURE_TRANSLATION = 'architecture_translation.xlsx'


@st.cache
def load_model():
    en_model = BartForConditionalGeneration.from_pretrained('./kr_en_translate')
    ja_model = BartForConditionalGeneration.from_pretrained('./kr_ja_translate')
    zh_model = BartForConditionalGeneration.from_pretrained('./kr_zh_translate')
    # tokenizer = get_kobart_tokenizer()
    return {'en': en_model, 'ja': ja_model, 'zh': zh_model}

model_dict = load_model()
tokenizer = get_kobart_tokenizer()
st.title("번역 테스트")

option = st.selectbox('번역할 언어 선택', ('영어', '일본어', '중국어'))
st.write('선택한 언어 :', option)

text = st.text_area("한글 문장 입력:")

st.markdown("### 입력한 한글 문장")
st.write(text)
if text:
    text = text.replace('\n', '')
    st.markdown("### 사전 번역 결과")
    if option == '영어':
        sentence = pre_translate(text, ARCHITECTURE_TRANSLATION, 'en')
        choice_lang = 'en'
    elif option == '일본어':
        sentence = pre_translate(text, ARCHITECTURE_TRANSLATION, 'ja')
        choice_lang = 'ja'
    elif option == '중국어':
        sentence = pre_translate(text, ARCHITECTURE_TRANSLATION, 'zh')
        choice_lang = 'zh'
    # 문제점 발견 : pre trans data에 김중업과 김중업건축박물관이 같이 있어 상단에 위치한 김중업에서 먼저 search가 중단됨
    st.write(sentence)
    st.markdown("### 번역 결과")
    

    with st.spinner('processing..'):    
        input_ids = tokenizer.encode(sentence)
        input_ids = torch.tensor(input_ids)
        input_ids = input_ids.unsqueeze(0)
        output = model_dict[choice_lang].generate(input_ids, eos_token_id=1, max_length=512, num_beams=26, no_repeat_ngram_size=3)
        output = tokenizer.decode(output[0], skip_special_tokens=True)
        
        output_sentence = []
        for idx, word in enumerate(output):
            try:
                if word == output[idx + 1][:len(word)]:
                    continue
                else:
                    output_sentence.append(word)
            except:
                output_sentence.append(word)
                
    st.write(output_sentence)
