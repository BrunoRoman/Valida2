FROM python:3.7

COPY . /Arquivos

WORKDIR /Arquivos

RUN pip install -r requirements.txt

RUN chmod +x /Arquivos/start.sh

CMD ["./start.sh"]

