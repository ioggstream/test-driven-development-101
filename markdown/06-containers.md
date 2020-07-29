---

# Container Intermezzo

----

## Goals

- basic docker usage

- describing environments with docker-compose

- run commands with docker

---

# Containers

Containerization is a lightweight virtualization technology that
provides a vm-like user experience using processes.

Docker is a container implementation and a platform for developers
and sysadmins to develop, ship, and run applications.

You can see a container like a virtual machine.

For more information on container, see www.docker.com

---

# Docker in practice

The docker command simulates a separate linux machine.

The following command creates a new linux container that has its own
filesystem and ip address.

```bash
# the --rm flag removes athe container at exit
docker run --rm -ti busybox  
```

Exercise:

- list the running processes with `ps -ef`, note that by default
  the busybox image ran a shell as the first process
- use `ip -4 -o a` to show the container ip address
- use `hostname` to show the container hostname
- `exit` the container 

---

## Containers



```
$ docker create  # creates a container but does not start it.
$ docker run     # creates and starts a container.
$ docker stop    # stops it.
$ docker start   # will start it again.
$ docker restart # restarts a container.
$ docker rm      # deletes a container.
$ docker kill    # sends a SIGKILL to a container.
$ docker attach  # will connect to a running container.
$ docker wait    # blocks until container stops.
$ docker exec    # executes a command in a running container.
```

----

inspecting containers

```
$ docker ps      # shows running containers.
$ docker inspect # information on a container (incl. IP address).
$ docker logs    # gets logs from container.
$ docker events  # gets events from container.
$ docker port    # shows public facing port of container.
$ docker top     # shows running processes in container.
$ docker diff    # shows changed files in container's FS.
$ docker stats   # shows metrics, memory, cpu, filsystem
```




---

# Pre-built images

Docker Hub is a public store where you can download containers with packaged
software name Images.

```bash
# Let's search ubuntu images
docker search ubuntu
```

----

Now run an ubuntu machine

```bash
docker run --rm -ti ubuntu
```

Exercise:

- check that `python3` is not installed
- install it with `apt-get update && apt-get -y install python3`
- run `python3 --version`

----

Docker Hub provides many pre-built images, including python, java, maven
and much more: we can usually skip installing software and reuse prebuilt
images.

``bash
docker run --rm -ti python
``  

Exercise:

- check that you're showing the python prompt `>>>`
- test the python interpreter with `print("Ciao")`
- `exit()`

----

## Commands for interacting with images


```
$ docker images  # shows all images.
$ docker import  # creates an image from a tarball.
$ docker build   # creates image from Dockerfile.
$ docker commit  # creates image from a container.
$ docker rmi     # removes an image.
$ docker history # list changes of an image.
```

----

## Dockerfile

You can create new images modifying existing ones using a Dockerfile.

```
FROM debian:7.8
MAINTAINER Piuma "piuma@piumalab.org"
RUN apt-get update && apt-get -y install apache2
EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
```

---

# Using docker with maven

To test the `maven` image we need a project


```bash
# clone a simple maven project from github
git clone https://github.com/junit-team/junit5-workshop
cd junit5-workshop
```

Now, let's build it using a docker container, isolating the build from our
 computer environment.
 
----

We will pass some more parameters to docker now:
 - `-v` maps a local directory to the container 
 - `-w` sets the current working directory
 

```bash
# Everything you see is happening in the container :)
docker run --rm -v $PWD:/code -w /code maven mvn test
```

----

Using containers we can build and run  software without installing on our
 machine a complete environment, and without breaking our laptop libraries!
 
We can also recreate legacy environments.

---

## Docker Compose

Docker-compose provides a convenient way to run one or more containers in a
 coordinate way, eg an application and a server.
 
Let's try a simple one with a python server and a python client.




 