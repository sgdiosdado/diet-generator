FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /dietgenerator
WORKDIR /dietgenerator
COPY requirements.txt /dietgenerator/
RUN pip install -r requirements.txt
COPY . /dietgenerator/
