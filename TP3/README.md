# TP1
- **Nome**: Miguel Calçado
- **Número de aluno**: `a109361`
- **Foto**:

    <img src="../artifacts/profile.jpg" width="200"> 

- **Email**: `a109361@alunos.uminho.pt`

## Sumário
Geramos um analisador léxico utilizando o script `gen_tokenizer.py` -- disponibilizado pelo Prof. José Carlos Ramalho no notebook `aulaT4.ipynb` -- com a definição de tokens sendo dada pelo arquivo `tokens_def.json`.

A tradução dos tokens dados no enunciado ao ficheiro `json` é relativamente direta, com algumas exceções:
- adicionamos outras palavras reservadas além do `LIMIT` (em particular, `select` e `where`).
- para evitar a captura de palavras reservadas como conceitos, declaramos os tokens dessas palavras antes do token de conceito
- para reconhecer o query de exemplo, declaramos explicitamente os dois-pontos como parte de um conceito (ao invés de somente caráteres alfa-numéricos).

### Exemplo de uso

``` shell
$ python3 gen_tokenizer.py tokens_def.json > tokenizer.py
$ python3 tokenizer.py < example_query 
('NEWLINE', '\n', 1, (31, 32))
('NEWLINE', '\n', 1, (0, 1))
('SELECT', 'select', 1, (0, 6))
('VAR', '?nome', 1, (7, 12))
('VAR', '?desc', 1, (13, 18))
('WHERE', 'where', 1, (19, 24))
('DELIMITADOR', '{', 1, (25, 26))
('NEWLINE', '\n', 1, (26, 27))
('VAR', '?s', 1, (4, 6))
('CONCEITO', 'a', 1, (7, 8))
('CONCEITO', 'dbo:MusicalArtist', 1, (9, 26))
('DELIMITADOR', '.', 1, (26, 27))
('NEWLINE', '\n', 1, (27, 28))
('VAR', '?s', 1, (4, 6))
('CONCEITO', 'foaf:name', 1, (7, 16))
('STRING', '"Chuck Berry"', 1, (17, 30))
('LANG', '@en', 1, (30, 33))
('DELIMITADOR', '.', 1, (34, 35))
('NEWLINE', '\n', 1, (35, 36))
('VAR', '?w', 1, (4, 6))
('CONCEITO', 'dbo:artist', 1, (7, 17))
('VAR', '?s', 1, (18, 20))
('DELIMITADOR', '.', 1, (20, 21))
('NEWLINE', '\n', 1, (21, 22))
('VAR', '?w', 1, (4, 6))
('CONCEITO', 'foaf:name', 1, (7, 16))
('VAR', '?nome', 1, (17, 22))
('DELIMITADOR', '.', 1, (22, 23))
('NEWLINE', '\n', 1, (23, 24))
('VAR', '?w', 1, (4, 6))
('CONCEITO', 'dbo:abstract', 1, (7, 19))
('VAR', '?desc', 1, (20, 25))
('NEWLINE', '\n', 1, (25, 26))
('DELIMITADOR', '}', 1, (0, 1))
('LIMIT', 'LIMIT', 1, (2, 7))
('NUM', '1000', 1, (8, 12))
```

## Ficheiros
* [tpc3.pdf](tpc3.pdf): enunciado do TPC.
* [gen_tokenizer.py](gen_tokenizer.py): script para gerar analisadores léxicos a partir de ficheiros `json` (`aulaT4.ipynb`, pelo Prof. José Carlos Ramalho).
* [tokens_def.json](tokens_def.json): definição dos tokens que servem de base para o analisador léxico.
* [tokenizer.py](tokenizer.py): analisador léxico gerado automaticamente pelo script.
* [example_query](example_query): query dada de exemplo para a linguagem no enunciado.
