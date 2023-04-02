FROM ubuntu:latest

RUN apt-get update -y\
	&& apt-get install -y git\
	g++\
	clang

RUN echo "===> Cloning calculator..."\
	&& cd /tmp \
	&& git clone https://github.com/Scen4ri0/calc.git

RUN echo "===> Compiling calculator..."\
	&& cd /tmp/calc \
	&& g++ -o calculator calc.cpp

CMD echo "Running calculator"\
	&& cd /tmp/calc \
	&& ./calculator
