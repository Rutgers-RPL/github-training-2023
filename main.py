import sys # Please don't touch this
sys.path.append('./individual_introductions') # or this 👉👈

# Put all imports below this line
from individual_introductions import shivam_patel # import the file containing your individual introduction blurb
from individual_introductions import andrew_huth
from individual_introductions import spenser_butrym 

def main():
    
    shivam_patel.intro() # call your intro function
    andrew_huth.intro()
    spenser_butrym.intro()

if __name__ == '__main__':
    main()
