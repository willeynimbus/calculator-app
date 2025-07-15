FROM python:3.9-slim
     WORKDIR /app
     COPY . .
     RUN pip install --no-cache-dir unittest2
     CMD ["python", "calculator.py"]