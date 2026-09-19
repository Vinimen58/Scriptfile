# Corpus Universal de Programação — 1M exemplos

Este repositório contém um gerador determinístico de corpus sintético para estudo e pré-treinamento de modelos de IA especializados em código.

## Gerar o TXT completo

Requer Python 3.9+.

```bash
git clone https://github.com/Vinimen58/Scriptfile.git
cd Scriptfile
python corpus_generator.py
```

O comando cria:

```
corpus_universal_programacao_1M_exemplos.txt
```

com **1.000.000 de registros sintéticos**.

Para testar com um corpus pequeno:

```bash
python corpus_generator.py --examples 10000 --output teste.txt
```

## Observação

O TXT completo é grande demais para ser armazenado como arquivo comum no GitHub sem Git LFS. Por isso o repositório contém o gerador, que reconstrói o corpus localmente sem dependências externas.

O corpus sintético não substitui código real devidamente licenciado, documentação oficial, testes executáveis e validação automática para treinamento sério de modelos.
