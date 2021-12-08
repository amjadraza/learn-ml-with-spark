FROM jupyter/pyspark-notebook


COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

#COPY ./notebooks ./notebooks

#CMD ["uvicorn", "file_processor.API.main:app", "--host", "0.0.0.0", "--port", "8000"]
