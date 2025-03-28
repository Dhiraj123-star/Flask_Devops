# Stage 1: Build dependencies
FROM python:3.13-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt --target /app/packages

# Stage 2: Create final lightweight image
FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /app/packages /usr/local/lib/python3.13/site-packages
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
