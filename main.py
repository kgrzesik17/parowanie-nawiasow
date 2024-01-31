# Autor: Kacper Grzesik

import os

def parser(file):
    tag = ""
    tags = []
    opened = []
    closed = []


    file = open("ab.html", "r")
    
    for line in file:
        line = line.strip()

        add = 0
        
        for i in line:
            if i == "<":
                add = 1

            if add == 1:
                tag += i

            if i == ">":
                add = 0
                tags.append(tag)
                tag = ""

    for i in tags:
        if i.startswith("</"):
            closed.append(i)
        else:
            opened.append(i)


def isset(variable):
    """
    Sprawdza czy do zmiennej została przypisana wartość.
    """

    try:
        variable
    except NameError:
        variable = None

    if variable is None:
        return 0
    else:
        return 1


def select_file():
    """
    Wybór pliku, dla którego program ma sprawdzić parowanie znaczników.
    """
    file_list = []

    for line in os.listdir(): # przypisuje pliki .html znajdujące się w ścieżce programu do listy
        line = line.lower()

        if line.endswith('.html') or line.endswith('.htm'):
            file_list.append(line)

    while True: # wyświetla wybór dostępnych plików
        selected_file = input(f"Wybierz plik, dla którego chcesz sprawdzić poprawność parowania nawiasów:\n{file_list}\nWpisz \"0\", aby wyjść z programu.\n")
    
        if selected_file == "0":
            input("=" * 33 + "\nProgram autorstwa: Kacper Grzesik\n" + "=" * 33)
            exit()

        if selected_file in file_list:
            return selected_file
        
        else:
            print("\nNie ma takiego pliku.\n")
            

def main():
    while True:
        selected_file = select_file()
    
        if isset(selected_file):
            parser(selected_file)


if __name__ == "__main__":
    main()