# Base image
FROM python:3.11-slim

# Prevent Python from buffering logs
ENV PYTHONUNBUFFERED=1

# Streamlit uses this port on Cloud Run
ENV PORT=8080

# Set working directory
WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy dependency files first (better Docker cache)
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy the rest of the project
COPY . .

# Expose Cloud Run port
EXPOSE 8080

# Start Streamlit
CMD ["uv", "run", "streamlit", "run", "app/Home.py", "--server.port=8080", "--server.address=0.0.0.0"]