FROM ubuntu:latest

ENV JAVA_HOME="/usr/lib/jvm/java-1.11.0-openjdk-amd64" \
    SPARK_HOME="/opt/spark" \
    PYSPARK_PYTHON="/usr/bin/python3" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_NO_INTERACTION=1 \
    PROJECT_PATH="/opt/code"

ENV PATH="$POETRY_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$JAVA_HOME/bin:$PATH"

RUN mkdir $POETRY_HOME

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y curl build-essential python3 python3-pip python-is-python3 openjdk-11-jdk scala git \
    --no-install-recommends

WORKDIR /opt
RUN curl -sSL https://dlcdn.apache.org/spark/spark-3.3.1/spark-3.3.1-bin-hadoop3.tgz -o spark.tgz
RUN tar -xzf spark.tgz
RUN mv spark-3.3.1-bin-hadoop3 spark
RUN spark-shell --packages org.apache.spark:spark-hadoop-cloud_2.13:3.3.1

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=$POETRY_HOME python3 -

WORKDIR $PROJECT_PATH
COPY pyproject.toml ./
COPY ./src src/

RUN poetry install --no-root --only main

WORKDIR $PROJECT_PATH/src
CMD ["poetry", "run", "uvicorn", "back.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
EXPOSE 4040