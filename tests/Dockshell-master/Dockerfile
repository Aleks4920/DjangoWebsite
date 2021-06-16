FROM node:8.11.3-slim

RUN apt-get update \
    && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common \
    python \
    build-essential \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - \
    && add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/debian \
    $(lsb_release -cs) stable" \
    && apt-get update \
    && apt-get install -y docker-ce=18.06.0~ce~3-0~debian

COPY . /var/www/dockshell
RUN cd /var/www/dockshell && npm install

EXPOSE 8100
WORKDIR /root/
ENTRYPOINT ["node"]
CMD ["/var/www/dockshell/app.js", "-p", "8100"]
