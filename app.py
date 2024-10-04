import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import os
from PIL import Image
import requests
from flask import Flask, request, jsonify
import re
from langchain_upstage import ChatUpstage
from langchain_core.messages import HumanMessage




	
st.title("[KUBIG 20기 LLM] 전세사기")


def save_uploaded_file(directory, file) :
    # 1. 디렉토리가 있는지 확인하여, 없으면 먼저, 디렉토리부터 만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)

    # 2. 디렉토리가 있으니, 파일을 저장한다.
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())

    # 3. 파일 저장이 성공했으니, 화면에 성공했다고 보여주면서 리턴
    return st.success('{} 에 {} 파일이 저장되었습니다.'.format(directory, file.name))


st.subheader('이미지 파일 업로드')

file = st.file_uploader('이미지를 업로드 하세요', type=['jpg','jpeg','png'])

if file is not None :
        current_time = datetime.now()
        print(current_time.isoformat().replace(':','_') )
        current_time = current_time.isoformat().replace(':','_')
        print( current_time + '.jpg' )

        file.name = current_time + '.jpg'

            # 바꾼파일명으로, 파일을 서버에 저장한다.
        save_uploaded_file('tmp', file)


            # 파일을 웹 화면에 나오게.
        img = Image.open(file)
        st.image(img)
        
        
def extract_text_from_document(api_key, filename):
    url = "https://api.upstage.ai/v1/document-ai/ocr"
    headers = {"Authorization": f"Bearer {api_key}"}
    files = {"document": open(filename, "rb")}
    response = requests.post(url, headers=headers, files=files)
    return response.json()

api_key = "up_HMlfm5h1T5Ea4zYWrtzZ1zYRfuzDi"
ocr_result = extract_text_from_document(api_key, img)

def extract_ocr_text(ocr_result):
    # ocr_result의 'pages' 필드에서 각 페이지의 'text' 필드만 추출
    ocr_text = " ".join(page['text'] for page in ocr_result['pages'])
    return ocr_text

# ocr_text 추출
ocr_text = extract_ocr_text(ocr_result)



st.write(ocr_text)
