from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()

    queue.enqueue({"nome_do_arquivo": "1.txt", "qtd_linhas": 3})
    queue.enqueue({"nome_do_arquivo": "2.txt", "qtd_linhas": 25})
    queue.enqueue({"nome_do_arquivo": "3.txt", "qtd_linhas": 9})

    assert queue.dequeue() == {"nome_do_arquivo": "1.txt", "qtd_linhas": 3}
    assert queue.dequeue() == {"nome_do_arquivo": "2.txt", "qtd_linhas": 25}

    assert len(queue) == 1

    queue2 = PriorityQueue()

    queue2.enqueue({"nome_do_arquivo": "1.txt", "qtd_linhas": 6})
    queue2.enqueue({"nome_do_arquivo": "2.txt", "qtd_linhas": 3})

    queue2.search(0) == {"nome_do_arquivo": "2.txt", "qtd_linhas": 3}

    queue3 = PriorityQueue()

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue3.search(4)

    with pytest.raises(IndexError, match="pop from empty list"):
        queue3.dequeue()

    queue4 = PriorityQueue()

    queue4.enqueue({"nome_do_arquivo": "1.txt", "qtd_linhas": 1})
    queue4.enqueue({"nome_do_arquivo": "2.txt", "qtd_linhas": 6})
    queue4.enqueue({"nome_do_arquivo": "3.txt", "qtd_linhas": 2})
    queue4.enqueue({"nome_do_arquivo": "4.txt", "qtd_linhas": 7})
    queue4.enqueue({"nome_do_arquivo": "5.txt", "qtd_linhas": 3})
    queue4.enqueue({"nome_do_arquivo": "6.txt", "qtd_linhas": 8})

    assert queue4.search(5) == {"nome_do_arquivo": "2.txt", "qtd_linhas": 8}
    assert queue4.search(4) == {"nome_do_arquivo": "4.txt", "qtd_linhas": 7}
    assert queue4.search(0) == {"nome_do_arquivo": "1.txt", "qtd_linhas": 1}
