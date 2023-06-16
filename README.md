# PDF Divider

Este é um script em Python para dividir um arquivo PDF em vários arquivos PDF de uma única página.

## Pré-requisitos

Certifique-se de ter o Python instalado em seu sistema. Além disso, instale a biblioteca PyPDF2 executando o seguinte comando:

```
pip install PyPDF2
```

## Como Usar

1. Faça o download ou clone este repositório em sua máquina.
2. Coloque os arquivos PDF que você deseja dividir na pasta "data" localizada no diretório do script.
3. Execute o script `script.py`.
4. Os arquivos PDF serão divididos em páginas individuais e salvos na pasta "out" localizada no diretório do script.
5. Cada página será salva em um arquivo PDF separado com o seguinte formato de nome: "nome_arquivo_numero_da_pagina.pdf". Por exemplo, se o arquivo original for "documento.pdf" e tiver 3 páginas, os arquivos divididos serão nomeados como "documento_1.pdf", "documento_2.pdf" e "documento_3.pdf".

## Notas

- Certifique-se de ter permissões de leitura na pasta "data" para acessar os arquivos PDF.
- Certifique-se de ter permissões de escrita na pasta "out" para salvar os arquivos PDF divididos.
- Certifique-se de que os arquivos na pasta "data" sejam arquivos PDF válidos.
- Certifique-se de que a biblioteca PyPDF2 esteja instalada corretamente antes de executar o script.

## Autor

* Thiago da Silveira Gentil