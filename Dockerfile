FROM python:3.7-alpine3.10

COPY api.py ./app/api.py
RUN pip install flask flask_restful
WORKDIR /app
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["api.py"]
