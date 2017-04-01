FROM centos:7

RUN yum install -y openssh-server && yum clean all

RUN /usr/bin/ssh-keygen -A
