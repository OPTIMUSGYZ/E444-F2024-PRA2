FROM python:3.10
WORKDIR /usr/local/flasky

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5012

ENV PYTHONDONTWRITEBYTECODE=1
ENV FLASK_APP=hello.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

CMD ["flask", "run", "--host=0.0.0.0"]