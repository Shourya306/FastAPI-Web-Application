FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install -r requirement.txt

EXPOSE 4000

CMD ["python","app.py"]