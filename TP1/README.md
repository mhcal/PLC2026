# TP1
- **Nome**: Miguel Calçado
- **Número de aluno**: `a109361`
- **Foto**:

    <img src="../artifacts/profile.jpg" width="200"> 

- **Email**: `a109361@alunos.uminho.pt`

## Resumo
**Q**: Expressão regular que aceite strings binárias que não contenham substring "011".
**A**: `1*(0+1?)*`

- `1*`: faz o fecho de Kleene no caractere `1`, i.e. aceita uma quantidade arbitrária (possivelmente nula) de repetições de `1`. O autómato equivalente só sai deste estado quando encontrar a primeira ocorrência de `0`.
- `(0+1?)*`: especifica que a seguir podemos ter um número não negativo de ocorrências de `0`, seguidos de *no máximo uma possível* ocorrência de `1`, tornando impossível a inserção de um segundo `1`.

## Ficheiros
[tp1.py](tp1.py) contém um script para testar o regex contra inputs de utilizador.
