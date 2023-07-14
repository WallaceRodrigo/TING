from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    txt_importer_return = txt_importer(path_file)

    process_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer_return),
        "linhas_do_arquivo": txt_importer_return,
    }

    for i in range(len(instance)):
        if (
            instance.search(i)["nome_do_arquivo"]
            == process_dict["nome_do_arquivo"]
        ):
            return None

    instance.enqueue(process_dict)
    return print(process_dict, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
