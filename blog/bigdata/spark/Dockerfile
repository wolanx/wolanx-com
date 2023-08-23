FROM apache/spark:python3
LABEL maintainer="wolanx<82540776@qq.com>"

USER root

# add dependence
ADD https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.25/mysql-connector-java-8.0.25.jar /opt/spark/jars
RUN pip install requests

# docker build -t wolanx/spark .
