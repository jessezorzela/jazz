class NodoArvore:

def init(self, chave=None, esquerda=None, direita=None):

self.chave = chave
self.esquerda = esquerda
self.direita = direita
def repr(self):

return '%s <- %s -> %s' % (self.esquerda and
self.esquerda.chave,
self.chave,
self.direita and
self.direita.chave)
# Vejamos como criar nodos de uma árvore usando o código acima.

raiz = NodoArvore(3)
raiz.esquerda = NodoArvore(5)
raiz.direita = NodoArvore(1)
print("Árvore: ", raiz)
raiz = NodoArvore(40)
raiz.esquerda = NodoArvore(20)
raiz.direita = NodoArvore(60)
raiz.direita.esquerda = NodoArvore(50)
raiz.direita.direita = NodoArvore(70)
raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita = NodoArvore(30)
def em_ordem(raiz):


if not raiz:
return
# Visita filho da esquerda.
em_ordem(raiz.esquerda)
# Visita nodo corrente.
print(raiz.chave),
# Visita filho da direita.
em_ordem(raiz.direita)
def insere(raiz, nodo):


"""Insere um nodo em uma árvore binária depesquisa."""
# Nodo deve ser inserido na raiz.
if raiz is None:
raiz = nodo
# Nodo deve ser inserido na subárvore direita.
elif raiz.chave < nodo.chave:
if raiz.direita is None:
raiz.direita = nodo

else:
insere(raiz.direita, nodo)
# Nodo deve ser inserido na subárvore esquerda.
else:
if raiz.esquerda is None:
raiz.esquerda = nodo

else:
insere(raiz.esquerda, nodo)
raiz = NodoArvore(40)
for chave in [20, 60, 50, 70, 10, 30]:
nodo = NodoArvore(chave)
insere(raiz, nodo)
# Imprime o caminhamento em ordem da árvore.
em_ordem(raiz)
raiz = NodoArvore(40)
for chave in [20, 60, 50, 70, 10, 30]:
nodo = NodoArvore(chave)
insere(raiz, nodo)
# Procura por valores na árvore.
for chave in [-50, 10, 30, 70, 100]:
resultado = busca(raiz, chave)
if resultado:
print("Busca pela chave {}:
      Sucesso!".format(chave))
else:
print("Busca pela chave {}:
      Falha!".format(chave))
