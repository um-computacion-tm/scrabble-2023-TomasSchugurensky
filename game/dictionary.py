from pyrae import dle


class DictionaryConnectionError(Exception):
    ...
class InvalidWordException(Exception):
    ...

dle.set_log_level(log_level='CRITICAL')

def dict_validate_word(word):
    word = str(word)
    try:
        search = dle.search_by_word(word=word)
        if search is None:
            raise InvalidWordException(f"La '{word}' no existe en el diccionario")
        return search.meta_description != 'Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'
    except Exception as e:
        raise DictionaryConnectionError("Hubo problemas al conectarse a la API") from e