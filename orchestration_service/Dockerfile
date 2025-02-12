FROM python:3.11-slim

ENV APP_HOME=/app
ENV PYTHONPATH="${PYTHONPATH}:${APP_HOME}"

WORKDIR $APP_HOME
COPY requirements.txt .

# Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8022

CMD ["python", "orchestrator.py"]
