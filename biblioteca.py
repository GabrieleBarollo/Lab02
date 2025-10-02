from  operator import itemgetter
def carica_da_file(file_path):
    """Carica i libri dal file"""
    # TODO
    try:
        input_file = open(file_path, "r")
        tab = []
        for line in input_file:
            l1 = []
            data_list = line.split(",")
            for data in data_list:
                data = data.rstrip()
                l1.append(data)
            tab.append(l1)

        input_file.close()
        return tab
    except FileNotFoundError:
        return None



def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    # TODO
    try:
        file = open(file_path, "a")
        check = True
        n = 0
        while check and n < len(biblioteca):
            if titolo == biblioteca[n][0]:
                check = False
            else:
                n = n+1

        if check:
            l2 = []
            l2.append(titolo)
            l2.append(autore)
            l2.append(anno)
            l2.append(pagine)
            l2.append(sezione)
            biblioteca.append(l2)
            for i in range(len(l2)):
                if i == (len(l2)-1):
                    file.write(str(l2[i]))
                else:
                    parola = str(l2[i]) + ","
                    file.write(parola)

        else:
            print("Il libro è già inserito all'interno della biblioteca")

        file.close()

        return check
    except Exception:
        return None



def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO
    try:
        control = False
        for line in biblioteca:
            if titolo == line[0]:
                result = line[0] + "," + " " + line[1] + "," + " " + line[2] + "," + " " + line[3] + "," + " " + line[4]
                control = True
        if not control:
            result = None

        return result

    except Exception:
        return None


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    try:
        data_tab_provv = []
        for dataline in biblioteca:
            if str(sezione) in dataline:
                data_tab_provv.append(dataline)

        tab_ord = sorted(data_tab_provv, key = itemgetter(0))
        list_titles = []
        for line in tab_ord:
            list_titles.append(line[0])
        return list_titles

    except Exception:
        return None


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    print("Il tuo file è stato scaricato correttamente")
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

