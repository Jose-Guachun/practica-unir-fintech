"""
License: Apache
Organization: UNIR
"""

import os
import sys
from collections import Counter

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))

def translate_messages_to_english():
    messages = {
        "file_argument": "The file must be specified as the first argument",
        "duplicates_argument": "The second argument indicates whether duplicates should be removed",
        "reading_file": "The words will be read from the file",
        "file_not_found": "The file does not exist",
        "total_words": "Total words",
    }
    return messages

def remove_duplicates_from_list(items):
    return list(set(items))

def filter_words_by_length(words, min_length=1):
    """
    Filtra las palabras de una lista según una longitud mínima.

    Args:
        words (list): Lista de palabras.
        min_length (int): Longitud mínima de las palabras a incluir.

    Returns:
        list: Lista de palabras que cumplen con la longitud mínima.
    """
    if not isinstance(words, list):
        raise RuntimeError(f"Se esperaba una lista, pero se recibió {type(words)}")
    return [word for word in words if len(word) >= min_length]

def count_words(items):
    """Cuenta cuántas palabras hay en la lista."""
    return len(items)

def count_words_with_counter(items):
    """Cuenta cuántas palabras hay en la lista."""
    if not isinstance(items, list):
        raise RuntimeError(f"No puede contar las palabras en {type(items)}")
    return Counter(items)


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)
    else:
        duplicate_count = count_words_with_counter(word_list)
        print(f"Palabras duplicadas: {duplicate_count}")
        for word, count in duplicate_count.items():
            if count > 1:
                print(f"{word}: {count} veces")

    total_words = count_words(word_list)
    print(f"Total de palabras: {total_words}")


    print(sort_list(word_list))