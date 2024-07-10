# Use the official Python image
FROM python:3.9-slim

# Set the working directory inside the Docker image
WORKDIR /app
ENV TRANSFORMERS_CACHE=/app/cache
RUN mkdir -p /app/cache && chmod -R 777 /app/cache

# Copy the requirements file from the host to the Docker image
COPY requirements.txt .
RUN pip install --upgrade pip
# Install dependencies specified in requirements.txt
RUN pip install -r requirements.txt
# Copy all other application files from the host to the Docker image
COPY . .
RUN chmod -R 777 /app

# Expose any necessary ports (if applicable)
EXPOSE 7860

# Command to run the application

CMD python CollatingNews.py && python Huggingface.py && streamlit run FrontEnd.py --server.port 7860 --server.address 0.0.0.0
