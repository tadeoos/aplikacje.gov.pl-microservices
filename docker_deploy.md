Deploy on Docker
================

Services in this repository can be executed inside docker containers.

Docker
------

If you don't have Docker installed go to [docs.docker.com](https://docs.docker.com/) to download the appropriate version for your OS and to start up Docker on your machine (*Get Started* section).


Network
-------

Services communicate over network so when deploing them in containers each container have to be connected to common docker virtual network. This is done by `--network <network_name>` parameter of `docker run` (and `docker service create`) command. Networks are created using `docker network create` command.

Service discovery
-----------------

Services should have ability to discover locations of other services, needed as dependencies. This is acomplished by DNS entries served by docker inside virtual networks. When creating a container use `--name <service_name>` parameter to assign name to newly created service. This name can be resolved by other services connected to the network. It's recommended that hostnames used by service as dependencies can be configured.

Docker compose
--------------

For convenience of deployment this repository includes `docker-compose` configuration.

To run project install `docker-compose` and then execute in root directory of this repository

    docker-compose up

For more info about Docker Compose consult [this guide](https://docs.docker.com/compose/gettingstarted/).

!!! Note for non-Linux users: Since docker runs in Linux VM in order to get proper url for viewing the apps you should find out the url that VM redirects its traffic to. You can easily do this by running

    docker-machine ip $HOST_NAME

Microservices are hosted on the `ip_from_the_last_command:5001`.