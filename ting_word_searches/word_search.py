def exists_word(word, instance):
    result = []

    for i in range(len(instance)):
        file_name = instance.search(i)["nome_do_arquivo"]
        lines = instance.search(i)["linhas_do_arquivo"]
        occurrences = []

        for line_index, line in enumerate(lines):
            if word.lower() in line.lower():
                occurrences.append({"linha": line_index + 1})

        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": occurrences,
                }
            )

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
