# Relatório — Lucas Rafael Barbosa (3503)

Relatório do projeto, preenchido na sua branch. Cada marco acrescenta a sua seção. Responda com as suas palavras e com
os números da sua execução; cada resposta cabe em até 6 linhas, além das tabelas.

## Marco 1

### Ambiente

<!-- Cole aqui a saída de `which python` e da Etapa 0 do `python marco1.py`. -->

### R1 — Expressões regulares

<!-- Uma string que re.match aceita e re.fullmatch rejeita com o padrão de tag; consequência para valida_tag. -->

### R2 — Linhas inválidas

<!-- Por que ler_log devolve as linhas descartadas; uma situação real em que descartar em silêncio esconderia um problema. -->

### R3 — Late binding

<!-- Por que errados["PT102"](4095) dá 409,5 e por que a sua criar_conversores não tem o problema. -->

### R4 — Escala nominal

<!-- Hipótese para a diferença da Etapa 2(f) e onde, no código da base, está a explicação. -->

### R5 — Previsão × medição (Etapa 3)

Previsões registradas no commit: 16ceca0

| Grandeza | Previsão | Medido |
| --- | --- | --- |
| Memória da lista / memória do `uint16` | 18 | |
| Tempo do laço / tempo vetorizado | 30 | |
| Tempo da compreensão / tempo do laço | 0,8 | |

<!-- Explique a maior diferença entre previsão e medição; por que uint16 * 20 dá 16364; que dtype você escolheria para contagens e para kPa. -->

### R6 — Tipos da SerieTemporal (Etapa 4d)

| Expressão | Tipo previsto | Tipo observado |
| --- | --- | --- |
| `s + s` | SerieTemporal | |
| `s[1:]` | Serie Temporal | |
| `s * 2` | Serie Temporal | |
| `s.sum()` | float64 | |
| `s[0]` | float64 | |

<!-- Explique o resultado que mais surpreendeu você. -->

### R7 — Issue #4

Quando fazíamos media_movel(30) ao invés de 571 = 600 - 30 + 1 valores, obtíamos só 570. Os testes TesteMediaMovelRegressão (principalmente teste_tamanho_600_janela_30) davam erro. Isso acontecia porque a soma acumulada estava começando do índice 0, e não no valor 0, então acumulada[janela:] - acumulada[:-janela] perde a primeira janela. Então, foi colocado um 0 no começo e retorno como SerieTemporal. Os testes estavam pegando porque estavam conferindo só tipos, erros, sem ver o tamanho dos intervalos. Um caso legal é que a janela igual a 1 deve ser do tamanho da série, e é coberto pelo teste teste_janela_igual_ao_tamanho.
