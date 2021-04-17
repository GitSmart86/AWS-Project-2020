# Docker

-   Docker is a stand alone product, but it is often used as an addon to Github to extend what can be stored remotely off of local computers.
-   GitHub stores the portable source code, and Docker holds a portable venv and GitHub's code.
-   Docker contains 3 things:
    1. DockerFile
    2. docker-compose.yml
    3. Docker.exe software which also adds cmd prompt inputs

#

1.  DockerFile

    -   The Verb File.
    -   This file runs everytime a Docker/GitHub poject is built.
    -   It reproducts the terminal cmds of a human.
    -   In this lab, it sets up:
        -   a venv (virtual environment),
        -   clones a git repo,
        -   installs that given repo's requiements.txt,
        -   syncs its DB (python ./manage.py migrate),
        -   and starts the Django server.

#

2.  docker-compose.yml

    -   The Spec. Sheet File
    -   This file contains any configurations or services of the docker project.
    -   NOTE: Since docker is a virtual environment, it also can reroute its incoming child service ports to whatever outgoing ports the docker wants to serve to clients.
    -   In this lab, the .yml contains:
        -   a Postgres DB
        -   a Django server
            -   NOTE: since django depends on a DB, the django service within the .yml contains a "depends_on: - \'postgres' " clause.

#

3.  Docker.exe
    -   The Admin program for docker instances. (localhost:8000/admin for django)
    -   Includes terminal cmds under _Docker ..._
    -   Terminal cmds:
        1. `Docker images` lists all local Docker projects (named images).
        2. `Docker rmi -f var(image_id)` deletes input image_id from pc.
        3. `Docker build var(directory) -t var(name)` builds or creates a new Dock_Proj.
            - _directory_ can be "." which means "current directory".
        4. `Docker-compose up` starts Docker instance.
            - cmd prompt automatically detects which project to start, IF you correctly _cd_ into the given Dock_Proj's dir.
            - This vanilla cmd with automatically build the Dock_Proj. upon first execution.
            - To rebuild/refresh a Dock_Proj, do `Docker-compose up --build`
