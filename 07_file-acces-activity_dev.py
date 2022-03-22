file =open("device.txt", "a")
while True:
            newItem = input("Enter device name: ")
            if newItem == 'exit':
                print("ALL DONE!")
                break
            file.write(newItem +"\n")
file.close( )