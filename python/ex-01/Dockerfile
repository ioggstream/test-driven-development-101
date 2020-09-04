#
# This is an example Dockerfile which loads an ubuntu:20.04 image
#  and then install on it python3-pip.
#
FROM ubuntu:20.04
RUN apt-get -dy update && \
	apt-get install -y python3-pip && \
	apt-get clean
