FROM python:3.8-slim as Build
WORKDIR /app
COPY . .
RUN pip install flask redis
EXPOSE 5002
CMD ["python", "myapp.py"]