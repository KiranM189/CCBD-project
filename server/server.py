import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from socket import *

def scrape_articles():
  webPage = requests.get(TARGET_URL)
  print(webPage)
  soup = BeautifulSoup(webPage.content, 'html.parser')
  for data in soup(['style', 'script']):
    data.decompose()
  words = ' '.join(soup.stripped_strings)
  wordList = words.split(' ')
  data = [[TARGET_URL, words, len(wordList)]]
  df = pd.DataFrame(data, columns=['URL', 'Data', 'Count'])
  return df

def save_to_csv(data, filename="shared-data/scraped_articles.csv"):
  directory = filename.split('/')[0]
  if(os.path.exists(filename)):
    data.to_csv(filename, mode='a', index=False, header=False)
  else:
    os.makedirs(directory, exist_ok=True)
    data.to_csv(filename, mode='a', index=False, header=['URL', 'Data', 'Count'])

def get_data(link, filename="shared-data/scraped_articles.csv"):
    """
    Return data from CSV file with count of words
    Using the link as key return variable "count" as the count of words 
    """
    df = pd.read_csv(filename)
    link_df=df[df['URL']==link]
    if link_df.empty:
        print("No data")
        return None
    count = link_df.iloc[0]['Count']
    ans=str(count)
    Message="The count of words in the URL is "+ans
    connectionSocket.send(Message.encode())
    connectionSocket.close()
    return count
  
if __name__ == "__main__":
  serverPort = 12000
  serverSocket = socket(AF_INET,SOCK_STREAM)
  serverSocket.bind(("",serverPort))
  serverSocket.listen(1)
  print("The server is ready to receive")
  while True:
    connectionSocket, addr = serverSocket.accept()
    URL = connectionSocket.recv(1024).decode()
    # Replace with the target URL you want to scrape
    TARGET_URL = URL
    if(TARGET_URL!=""):
      break
  scraped_data = scrape_articles()
  save_to_csv(scraped_data)
  print("Data scraped and saved to scraped_articles.csv. Word count is ", get_data(TARGET_URL))
