import sys # Please don't touch this
sys.path.append('./individual_introductions') # or this 👉👈

# Put all imports below this line
from individual_introductions import shivam_patel # import the file containing your individual introduction blurb
from individual_introductions import andrew_huth
from individual_introductions import daniel_li


def main():
    
    shivam_patel.intro() # call your intro function
    andrew_huth.intro()
    daniel_li.intro()


if __name__ == '__main__':
    main()
