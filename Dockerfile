FROM python:3.10-slim

WORKDIR /home/Snells-Law_Calculator

COPY . /home/Snells-Law_Calculator/

RUN apt update && \
    apt install python3-pyqt5 -y && \
    pip3 install -r requirements.txt

CMD [ "python3", "main.py" ]
