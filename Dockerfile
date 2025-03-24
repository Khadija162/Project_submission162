# Dockerfile
FROM python:3.10-slim
#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10
# Install Python dependencies

# Set working directory
WORKDIR /app

COPY . /app 
# Copy all project files
#COPY . /requirement.txt /app/requirement.txt


RUN python -m pip install -r requirement.txt

#COPY . /app /app

# Expose FastAPI port
#EXPOSE 8000

# Default command: run FastAPI app
#
CMD ["python", "run.py"]

#CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
