FROM centos:8

ADD snippet/mongodb-org-4.2.repo /etc/yum.repos.d/
RUN dnf -y install mongodb-org
