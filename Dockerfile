FROM python:3.8

WORKDIR /renamer-otaku-v2

COPY . /renamer-otaku-v2/
RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD python3 main.py
