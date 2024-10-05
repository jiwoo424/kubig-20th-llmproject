from setuptools import setup, find_packages

setup(
    name='kubig-20th-llmproject',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # 필요한 패키지들을 여기에 나열하세요.
        'streamlit==1.39.0',
        'pandas==2.2.3',
        'numpy',
        'datetime==5.5',
        'pillow==10.0.0',
        'requests',
        'flask==2.2.2',
        'werkzeug==2.2.3',
        'langchain-upstage==0.3.0',
        'langchain-core==0.3.0',
        'langchain',
        'pydantic>=2.7.4,<3.0.0',
        'faiss-cpu',
        'scikit-learn',
    ],
)
