FROM python:3.12-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirement.txt

ENV PYTHONPATH=.

CMD ["python", "apps/user_app/app.py"]