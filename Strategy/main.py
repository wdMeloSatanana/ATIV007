from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Calculadora():
    """
    O Contexto define a interface de interesse aos clientes.
    """

    def __init__(self, operation: ElementIteration) -> None:
        """
        Normalmente, o Contexto aceita uma estratégia no construtor, mas 
        também fornece um setter para mudá-lo em tempo de execução.
        """

        self._operation = operation

    @property
    def operation(self) -> ElementIteration:
        """
        O contexto mantém uma referência para um dos objetos de estrategia sem saber
        a classe concreta. Deverá trabalhar com todas através da interface Strategy.
        """

        return self._operation

    @operation.setter
    def operation(self, operation: ElementIteration) -> None:
        """
        Normalmente, o contexto permite alterar o objeto Strategy em tempo de execução.
        """

        self._operation = operation

    def evaluateData(self) -> None:
        """
        O contexto realiza o trabalho o enviando para o objeto Strategy em vez de implementar
        variações do algoritmo em si.
        """

        # ...

        print("Contexto: Realizando a operação matemática (não sei qual)")
        result = self._operation.execute((1, 2, 3, 4, 5))
        print(result)

        # ...


class ElementIteration(ABC):
    """
    Esta interface declara operações comuns a todas variações do mesmo algoritmo.
    O contexto usa esta interface para chamar o algoritmo definido nas Contrete
    Strategies/Estratégias Concretas.
    """

    @abstractmethod
    def execute(self, data: List):
        pass


"""
Contrete Strategies/Estratégias Concretas implementam o algoritmo seguindo a 
interface, tornando substituíveis. 
"""


class Summatiom(ElementIteration):
    def execute(self, data: List) -> int:
        return sum(data)


class Product(ElementIteration):
    def execute(self, data: List) -> int:
        x =1 
        for i in data:
            x = x * i 
        return x


if __name__ == "__main__":
    # O código do cliente seleciona uma estratégia e envia para o contexto.
    context = Calculadora(Summatiom())
    print("Cliente: Strategy está como operação de somatório")
    context.evaluateData()

    print()
    print()
    
   
    print("Cliente: Strategy está como operação de produtório")
    context.operation = Product()
    context.evaluateData()
