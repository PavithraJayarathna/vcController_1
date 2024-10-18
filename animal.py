import sys

def cat():
    print("Hello cat")

def default():
    print("cattt")

def main ():
    if sys.argv[1] =="cat":
        cat()

    else:
        default()


if __name__ == '__main__':
    main()

