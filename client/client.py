# No changes required here EXCEPT FOR TASK 5
"""
This is the client which reads from "shared-data/scraped_articles.csv" present in server.py file
"shared-data/scraped_articles.csv" is mounted from server container
"""
import pandas as pd
from socket import *

serverName = "172.17.0.2"  
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

URL = input("Input the URL:")
clientSocket.send(URL.encode()) 
clientSocket.close()

df = pd.read_csv("shared-data/scraped_articles.csv")
print(df)
