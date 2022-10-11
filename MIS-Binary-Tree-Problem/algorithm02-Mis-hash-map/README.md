## Prova de Corretude e Exemplos de Execução

### Algoritmo Recursivo 2 - MIS com HasMap

#### Justificação de Corretude


Para provar a corretude do algoritmo podemos usar a seguinte método de indução para pecorrer a árvore e calcular o MIS:

Assim, queremos provar que P(n) = "FindMISSize(root, d)" retorna a quantidade de elementos do Conjunto Independente Máximo, para qualquer tamanho da árvore.

Caso Base: Se a quantidade de nós na arvore for igual a 0, ou seja, a raiz da árvore é nula, temos que por conta do condional ele retornará 0. Logo, P(0) vale.

Considere algum n > 0
Hipótese: P(k) vale, para 0 <= K < n.

Dado que, o algoritmo recebe uma árvore que contém sub-árvores, ou seja, com a quantidade de nós > 0, ademais, depois da verificação é nulo, diferentemente do algoritmo anterior, temos também, que passar por uma verificação se o nó atual está contido no map, se não, será possível fazer a chamada recursiva para os filhos da direita e da esquerda do nó atual, caso sejam nulos o primeiro condicional retornará 0 voltará e retrocederá na pilha de chamadas até a instância que invocou as chamadas, caso contrário, farará com que a váriavel excluir recebe um valor > 0. Ainda assim, caso não forem nulos, chamará recursivamente até o último nó que contém nós nulos, quando chegar nesse caso será possível incrementar o valor da variável incluir², para assim, demonstrar que esse é um nó independente. Ademais, 


