FROM python:3.13.2-alpine
WORKDIR /home/sepehr/DevOps/Roshan_Tasks/web_app 
ENV FLASK_APP=web_app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run", "--debug"]
