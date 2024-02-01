# Autor: Kacper Grzesik

import os

def parser(file):
    """
    Sprawdza praowanie pliku.
    """
    tag = ""
    tags = []
    opened = []
    closed = []
    opened_temp = []
    closed_temp = []
    voids = []


    voids_file = open("void_elements.txt", "r") # plik zawierające puste znaczniki

    for line in voids_file:
        line = line.strip()

        voids.append(line)
        
    file = open(file, "r")
    
    for line in file:
        line = line.strip()

        add = 0
        
        for i in line:
            if i == "<":
                add = 1

            if add == 1:
                tag += i

            if i == ">" or i == " ":
                add = 0
                tags.append(tag)
                tag = ""

    for i in tags: # dodawanie tagów do listy (w tym pomocniczej)
        if i.startswith("</"):
            closed.append(i[2:-1:])
            closed_temp.append(i[2:-1:])
        else:
            opened.append(i[1:-1:])
            opened_temp.append(i[1:-1:])

    for i in opened_temp: # usuwanie sparowanych tagów
        if i in closed_temp:
            closed.remove(i)

    for i in closed_temp:
        if i in opened_temp:
            opened.remove(i)

    opened_temp = opened
    closed_temp = closed
    opened = []
    closed = []

    for i in opened_temp: # filtrowanie dopuszczalnych pustych znaczników
        if i.lower() in voids:
            opened_temp.remove(i)
            
    for i in closed_temp:
        if i.lower() in voids:
            closed_temp.remove(i)

    opened_temp = filter(None, opened_temp)

    for i in opened_temp: # dodawnie znaczników (dla wyglądu)
        i = "<" + i + ">"
        opened.append(i)

    for i in closed_temp:
        i = "</" + i + ">"
        closed.append(i)
    
    if not opened and not closed:
        print("\nPlik został poprawnie sparowany.\n")
    else:
        print("\nPlik nie został poprawnie sparowany.")
        print(f"Otwarte znaczniki, które nie zostały zamknięte: {opened}")
        print(f"Zamknięte znaczniki, które niezostały otwarte: {closed}\n")

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