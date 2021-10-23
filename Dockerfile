FROM python:3.9

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt --no-cache-dir

CMD ["python", "main.py"]
