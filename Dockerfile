FROM python:3.10-slim

COPY . /home/Snells-Law_Calculator/
WORKDIR /home/Snells-Law_Calculator

RUN apt update && \
    apt install -y --no-install-recommends \
        libgl1 \
        libfontconfig1 \
        shared-mime-info \
        libdbus-1-3 \
        libxcb-image0 \
        libxcb-keysyms1 \
        libxcb-shape0 \
        libxcb-randr0 \
        libxcb-xinerama0 \
        libxcb-icccm4 \
        libxkbcommon-x11-0 \
        libxcb-render-util0 && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "main.py" ]
