import client

if __name__ == "__main__":
   cl = client.AOTYSession()
   print(cl.request('get', "").text)
