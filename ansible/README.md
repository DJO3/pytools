# Requirements
1. [Docker Community Edition](https://www.docker.com/community-edition)
    * Tested on macOS Sierra 10.12.4
    * Docker CE Version 17.03.1-ce-mac5 (16048)

# Getting Started
1. `git clone https://github.com/DJO3/pytools.git`
2. `cd pytools/ansible`
3. `docker-compose build`
4. `docker-compose up -d`

# Example Commands
1. Enter ansible container
    * `docker exec -it ansible bash`
2. Ping all hosts
    * `ansible all -m ping`
3. Execute command on all hosts
    * `ansible all -a "/bin/echo hello"`
4. Ping hosts in a group
    * `ansible containers -m ping`
