from dotenv import dotenv_values

def main():
   my_secret = dotenv_values(".env")
   print(my_secret)

if __name__ == "__main__":
   main()

