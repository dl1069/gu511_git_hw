# set your parent image to be from the `ubuntu` repository and with the
# `20.04` tag
# --------------- #
sudo docker pull ubuntu:20.04
# --------------- #

# copy the contents of the current directory into the root directory (/)
# --------------- #
COPY . / 
# --------------- #

# use `apt-get update` to update the index of packages in your docker container
# --------------- #
RUN apt-get update
# --------------- #

# use `apt-get` to install the `curl` and `ca-certificates` packages. you need
# to use the -y flag to automatically answer "yes" to all apt-get's questions
# --------------- #
RUN apt-get install -y curl ca-certificates

# --------------- #

# define an environment variable `MYVAR` with default value `l33t`
# --------------- #
ENV MYVAR l33t
# --------------- #

# set the default launch command to invoke our shell script using `bash`
# that is, `bash gu511_download.sh`. remember that `docker` won't know what to
# do with that full command with a space in it...
# --------------- #
#COPY bash gu511_download.sh /usr/bin/bash gu511_download.sh
RUN chmod +x /usr/bin/bash gu511_download.sh
CMD ["bash gu511_download.sh"]
# --------------- #
