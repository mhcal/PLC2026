# TP1
- **Nome**: Miguel Calçado
- **Número de aluno**: `a109361`
- **Foto**:

    <img src="../artifacts/profile.jpg" width="200"> 

- **Email**: `a109361@alunos.uminho.pt`

## Sumário
A função `markdown_to_html` no ficheiro [tp2.py](tp2.py) faz a conversão de todos os elementos descritos no enunciado do TPC2. É importante notar que, ao utilizar a função `sub` repetidas vezes numa mesma string, a ordem em que as substituições são feitas importa. No contexto deste exercício, por exemplo, os elementos **bold** devem ser capturados antes dos elementos *itálicos*; por via de regra, quando dois patterns coincidem lexicograficamente em certos pontos, o que tem menor abrangência (ou seja, o que é mais específico) deve ser executado primeiro.

Com o uso de um boilerplate, o programa [tp2.py](tp2.py) converte ficheiros `.md` que utilizem apenas dos elementos descritos no enunciado do TPC2 em um ficheiro `.html` (que pode ser lido por browsers). O programa aceita como parâmetro (opcional) o path do ficheiro `.md` a ser convertido; por defeito, o programa utiliza o ficheiro [foo.md](foo.md) (gerado completamente, à exceção do coelho, no site [https://jaspervdj.be/lorem-markdownum/](https://jaspervdj.be/lorem-markdownum/)).

### Exemplo de uso

``` shell
python3 tp2.py foo.md
```

## Ficheiros
* [tp2.py](tp2.py): programa que converte (um subset de) ficheiros `.md` em `.html`.
* [foo.md](foo.md): exemplo de ficheiro `.md`.
* [coelho.jpg](../artifacts/coelho.jpg): coelho.

