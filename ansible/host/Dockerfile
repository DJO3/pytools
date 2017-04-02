FROM centos:7

RUN yum install -y epel-release && \
yum install -y openssh-clients ansible && \
yum clean all

RUN mkdir -p /root/.ssh 
COPY etc/ssh /root/.ssh 
RUN chmod -R 600 /root/.ssh
