# Build Stage
FROM bcapuano/atheris:2.1.1-python3.10
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y git

ADD . /src
WORKDIR /src
RUN python3 -m pip install .
RUN git fetch --recurse-submodules

CMD ["/src/mayhem/fuzz_cal.py"]
