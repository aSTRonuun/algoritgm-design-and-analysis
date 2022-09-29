## Prova de Corretude e Exemplos de Execução

### Algoritmo Recursivo 1 - MIS

#### Justificação de Corretude

Para provar a corretude do algoritmo podemos usar a seguinte método de indução para pecorrer a árvore e calcular o MIS:

Assim, queremos provar que P(n) = "FindMISSize(root)" retorna a quantidade de elementos do Conjunto Independente Máximo, para qualquer tamanho da árvore.

Caso Base: Se a quantidade de nós na arvore for igual a 0, ou seja, a raiz da árvore é nula, temos que por conta do condional ele retornará 0. Logo, P(0) vale.

Considere algum n > 0
Hipótese: P(k) vale, para 0 <= K < n.

Quando o algoritmo recebe uma árvore que contém sub-árvores, ou seja, com a quantidade de nós > 0, ele faz uma chamada recursiva passando o filho direito e filho esquedo do nó atual, caso sejam nulos o primeiro condional retornará 0 e voltará e retrocederá na pilha de chamadas até o caso base, apartir daí, farará com que a várivel excluir receba um valor >= 0. Caso não sejem nulos, chamará recursivamente até o último nó que contém nós nulos, quando chegar nessa caso será possível incrementar o valor da varível incluir, para demonstrar que esse é um nó válido, depois vai ser verificado se os filhos da direita e da esquerda atual são nulos, se não forem nulos, irá ser possível incrementar o valor chamando recursivamente os netos da esquerda e da direita do nó atual, se ouver netos não nulos, irá retornar valores > 0, incrementendando, assim, a variável incluir. Desse modo, passado todas as chamadas recursivas, o valor de incluir e excluir são comparados a fim de retornar o valor máximo e assim, podemos provar que o algoritmo tem execução finita e retorna a quantidade de elementos e, portanto, P(n) vale nesse caso.


