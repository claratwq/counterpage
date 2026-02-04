# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install required packages
RUN pip install --no-cache-dir gradio

# Copy all files into container
COPY . .

# Expose port 7860 (HF Spaces standard)
EXPOSE 7860

# Run the Gradio app
CMD ["python", "app.py"]
