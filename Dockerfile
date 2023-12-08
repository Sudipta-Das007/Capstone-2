FROM  python:alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV ML_ENDPOINT=http://172.17.0.2:5000
EXPOSE 8088
CMD python app.py
