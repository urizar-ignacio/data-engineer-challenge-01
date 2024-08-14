FROM jupyter/base-notebook:x86_64-python-3.11

COPY --chmod=777 ./app /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD jupyter notebook --port 8888 --allow-root --NotebookApp.token=''