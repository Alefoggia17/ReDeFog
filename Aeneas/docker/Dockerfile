#########################################################################################################################
# CSC4006 - Research And Development Project
# Developed by: Jonathan McChesney (MEng Computer Games Development)
# Queen's University Belfast
#
# Component: Dockerfile
#
# Purpose: This Dockerfile determines the linux server (ubuntu:18.04) and declarse the execute.sh script as a CMD Compose,
#			file - instantiating an entrypoint for the script using the /scripts folder. The relevant dependencies are installed
#			and the ubuntu service is updated etc. Wget and git are installed to allow for repository management and pulling
#			the relevant urls. Boto3 is installed to allow for integration with an S3 instance. The git repository is initialised,
#			added and configured to pull only the relevant application sub folder. This allows a specific version of the application
#			to be pulled and built consistently. Depending on the applications bespoke requirements the debian environment arguement
#			is set to remove interactivity during the build the process, this is to ensure automated deployment.
#
#########################################################################################################################

FROM ubuntu:22.04
COPY execute.sh scripts/execute.sh

WORKDIR /root

RUN \
	apt-get update && apt-get install -y \
	autoconf \
	build-essential \
	libtool \
	time \
	bc \
	python3 \
	python3-pip \
	git

RUN \
	apt-get install -y \
	wget 
	
RUN \
	python3 -m pip install boto3	
	
RUN \
	cd Aeneas/aeneas && \
	bash install_dependencies.sh && \
	pip install -r requirements.txt && \
	python3 setup.py build_ext --inplace
	
# defaults command
CMD ["scripts/execute.sh"]
