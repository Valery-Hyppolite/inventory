
FROM python:3.9.6-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

LABEL maintainer="InventoryDjangoApp"

WORKDIR /app
#RUN python -m env /opt/env
COPY requirements.txt requirements.txt
COPY entrypoint.sh entrypoint.sh
# RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000

#CREATE A VIRTUAL ENV, INTALL REQUIREMENT.TXT, UPDATE PIP PACKAGE, NSTALL THE PAKCAGES FOR POSTGRSQL DRIVER AND DELETE DOES PACKAGE THAT ARE NO LONGER NEEDED AFTER INSTALATION

RUN  python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r requirements.txt
    #chmod +x entrypoint.sh
    #useradd -m -s /bin/bash myapp
    
ENV PATH="entrypoint.sh:/py/bin:$PATH"
# #USER app
CMD ["sh", "entrypoint.sh"]


# python -m venv /py && \
#     /py/bin/pip install --upgrade pip && \
#     apk add --update --no-cache postgresql-client && \
#     apk add --update --no-cache --virtual .tmp-deps \
#         build-base postgresql-dev musl-dev && \
#     /py/bin/pip install -r requirements.txt \
#     apk del .tmp-deps
#     #useradd -m -s /bin/bash myapp