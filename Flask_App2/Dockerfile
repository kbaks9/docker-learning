FROM python:3.8-slim
WORKDIR /myapp
COPY . .
RUN pip install flask redis
EXPOSE 5000
CMD ["python","myapp2.py"]