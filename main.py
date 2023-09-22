import sys # Please don't touch this
sys.path.append('./individual_introductions') # or this 👉👈

# Put all imports below this line
from individual_introductions import shivam_patel
from individual_introductions import andrew_huth
from individual_introductions import manish_kandepalli

def main():
    
    shivam_patel.intro() # call your intro function
    andrew_huth.intro()
    manish_kandepalli.intro()


if __name__ == '__main__':
    main()
