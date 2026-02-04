FROM python:3.11-slim

WORKDIR /app

RUN pip install flask

# Copy the rest of the app
COPY . .

EXPOSE 7860

CMD ["python", "app.py"]
