# Project

-> To create a client and a server
-> Server: 
    - Scrape Data from TARGET_URL in server.py file and save it csv file
    - Count the number of words present in saved data
    - Share the data (csv file) to client (using volume mount)
-> Client: 
    - Client reads data from shared-data of server using mount in only read-only fashion
    - Note: Client should not be able to modify the csv file and only read it

# Commands and Tasks:

### Task1 : Build the client image, no changes required in client side EXCEPT for Task5 (below)

1. in client folder
docker build -t client-image .

### Task2 : Complete the DockerFile before building the image, Fill the <complete> parts in DockerFile
2. in server folder
docker build -t server-image .

### Task3 : Complete the required functions in server.py file
3. in server folder
docker run -ti --name server-container -v shared-data:/app/shared-data/ server-image

### Task4 : Run the right `docker run` commmand to read data from the server container, should be able to ONLY read the data from the volume
4. in client folder: The below command is not correct, do the required change based on Task4
docker run -ti --name client-container --volumes-from server-container client-image


## Not mandatory task 
### Task5: Establish a socket connection between client and server such that client can send the TARGET_URL to server
### Note: Feel free to create the required functions for this task in both server.py file and client.py file
