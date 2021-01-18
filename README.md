# Globex Database Exercise

## Pre-requisites

You will need to have the following tools installed:

- SQL Server Management Studio ([link](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)); and
- Docker ([link](https://www.docker.com/products/docker-desktop)).

Ensure that docker is running on your machine by using `docker -v`.

## First time setup

From command line, in this directory run the startup script appropriate for your shell. (Either `startup.bat` or `startup.sh`).

## Connect to the database

Check that the container is running with `docker ps`, you should see something like the following:

```
CONTAINER ID   IMAGE       COMMAND                  CREATED         STATUS                   PORTS                    NAMES
<SOME_ID>      module-09   "powershell -Command…"   3 minutes ago   Up 3 minutes (healthy)   0.0.0.0:1433->1433/tcp   module-09-container
```

If it isn't, run `docker start module-09-container` to start it. If you stop the container for any reason (e.g. restarting your machine) you'll need to run this command.

Open SQL Server Management Studio and connect with the following details:
Server name: `localhost,1433`
Authentication: `SQL Server Authentication`
Login: `sa`
Password: `Password123!`

Under `Databases` there should be a db called `globex`, with tables populated with data. You can see the tables by expanding `globex` and then the `Tables` folder. Right-click and **Select Top 1000 Rows** for a quick preview of the data in each table.
