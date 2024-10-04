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

	
st.title("[KUBIG 20기 LLM]")

st.subheader('이미지 파일 업로드')
file = st.file_uploader('이미지를 업로드 하세요', type=['jpg', 'jpeg', 'png'])

def save_uploaded_file(directory, file):
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())

if file is not None:
    # 현재 시간으로 파일 이름 지정
    current_time = datetime.now().isoformat().replace(':', '_')
    file.name = current_time + '.jpg'
    
    # 파일 저장
    save_uploaded_file('tmp', file)

    # 이미지 열기
    img = Image.open(file)
    st.image(img)
    
    # 이미지 파일 경로 생성
    file_path = os.path.join('tmp', file.name)

    # OCR API 호출
    def extract_text_from_document(api_key, filename):
        url = "https://api.upstage.ai/v1/document-ai/ocr"
        headers = {"Authorization": f"Bearer {api_key}"}
        files = {"document": open(filename, "rb")}
        response = requests.post(url, headers=headers, files=files)
        return response.json()

    api_key = "up_HMlfm5h1T5Ea4zYWrtzZ1zYRfuzDi"
    ocr_result = extract_text_from_document(api_key, file_path)

    # OCR 텍스트 추출
    def extract_ocr_text(ocr_result):
        ocr_text = " ".join(page['text'] for page in ocr_result['pages'])
        return ocr_text

    # OCR 결과에서 텍스트 추출
    ocr_text = extract_ocr_text(ocr_result)

    st.write(ocr_text)