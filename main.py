import sys # Please don't touch this
sys.path.append('./individual_introductions') # or this 👉👈

# Put all imports below this line
from individual_introductions import shivam_patel # import the file containing your individual introduction blurb
from individual_introductions import andrew_huth
from individual_introductions import jason_merchan
from individual_introductions import aj_lipiarski


def main():
    
    shivam_patel.intro() # call your intro function
    andrew_huth.intro()
    jason_merchan.intro()
    aj_lipiarski.intro()


if __name__ == '__main__':
    main()
