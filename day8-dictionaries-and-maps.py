contacts = {}

def printContacts():
    
    try:
      name = input()

      while name:
          if name in contacts:
              print(f"{name}={contacts[name]}")
          else:
              print('Not found')
          name = input()
    except:
        return


def main():
    
    numEntries = int(input().strip())

    for _ in range(numEntries):
        [name, number] = input().strip().split()
        contacts[name] = int(number)

    printContacts()

main()



