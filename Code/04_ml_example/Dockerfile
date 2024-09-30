FROM python:3.8-slim-buster

COPY email_classification.py /

RUN pip install --no-cache-dir scikit-learn

CMD [ "python", "./email.py" ]
