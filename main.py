import sys # Please don't touch this
sys.path.append('./individual_introductions') # or this 👉👈

# Put all imports below this line
from individual_introductions import shivam_patel # import the file containing your individual introduction blurb

def main():
    
    shivam_patel.intro() # call your intro function


if __name__ == '__main__':
    main()
