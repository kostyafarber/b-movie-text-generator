FROM python:3.8
WORKDIR /app

COPY requirements.txt requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "streamlit", "run", "app/main.py"]

