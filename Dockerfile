#FROM python:3.11
FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip uninstall -y opencv-python
RUN pip install opencv-python-headless

EXPOSE 8080
o
CMD ["gunicorn", "controller:app", "-b", "8080"]
