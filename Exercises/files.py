'''
Example of how to handle files
'''

def main():
    # Open a file for writing and create it if it doesn't exist
    # f = open("textfile.txt","w+")

    # Open the file for appending text to the end
    # f = open("textfile.txt","a")

    # Open the file for read content
    f = open("textfile.txt","r")

    # Write some lines of data to file
    # for i in range(10):
    #     f.write("This is line " + str(i) + "\r\n")

    # Close the file when done
    # f.close()

    # Open the file back up and read the contents
    if f.mode == 'r':
        # contents = f.read()
        fl = f.readlines()
        for l in fl:
            print(l)
        # print(contents)


if __name__ == "__main__":
    main()