FROM python:3.9-slim
WORKDIR /app

COPY . .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


EXPOSE 7860
ENTRYPOINT [ "python" ]
CMD [ "ChatWhiz.py" ]