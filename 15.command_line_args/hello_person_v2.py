import argparse

def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo"
    }
    msg =f'{greetings[lang] } {name} !!'
    print (msg)
if __name__== '__main__':
#Creating a Parser: Create an ArgumentParser object, which
# will hold all the information necessary to parse the
# command-line arguments.
    parser = argparse.ArgumentParser(
        description="Procides persoanal greeting!!"
    )

    #Adding Arguments: Add arguments to the parser using 
    #add_argument() method.
    parser.add_argument(
        "-n","--name", metavar="name",
        required = True, help="The name of the person to Greet"
    )
    parser.add_argument(
        "-l","--lang", metavar="language",
        required = True, choices=['English', 'Spanish', 'German'], help="In the language of the greeting"
    )

    #here -n and --name both represents arguemnt called name 
    #for which we are going to get input from the command-line.like :
    #     py hello_person.py -n venkat
    #In this case you must specify value for name in cmd when running the program.


    #Parsing Arguments: Parse the command-line arguments using the parse_args() method.
    args= parser.parse_args()

    hello(args.name, args.lang)