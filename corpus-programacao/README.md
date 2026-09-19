# Corpus Universal de Programação — 1.000.000 de exemplos

Este diretório contém um gerador reproduzível para criar localmente o corpus de programação com **1.000.000 de exemplos**.

## Por que o TXT não está versionado diretamente?

O arquivo final tem aproximadamente **374 MB**. O GitHub bloqueia arquivos Git normais acima de 100 MB. Em vez de quebrar o corpus ou depender de Git LFS, este repositório guarda o gerador que recria o TXT completo.

## Uso

```bash
git clone https://github.com/Vinimen58/Scriptfile.git
cd Scriptfile/corpus-programacao
python generate_corpus.py
```

No final será criado:

```
corpus_universal_programacao_1M_exemplos.txt
```

O gerador produz 1.000.000 de registros sintéticos cobrindo múltiplas linguagens, categorias, níveis, restrições e entradas.

## Requisitos

- Python 3.9+
- cerca de 500 MB de espaço livre

Nenhuma biblioteca externa é necessária.
