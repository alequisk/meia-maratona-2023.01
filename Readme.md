# Problemas da MEIA MARATONA 2023 - DESPEDIDA DAS AULAS
---

- [x] [1257](https://www.beecrowd.com.br/judge/pt/problems/view/1257) Array Hash
- [x] [1310](https://www.beecrowd.com.br/judge/pt/problems/view/1310) Lucro
- [x] [1449](https://www.beecrowd.com.br/judge/pt/problems/view/1459) Foco
- [x] [1514](https://www.beecrowd.com.br/judge/pt/problems/view/1514) Competição
- [ ] [1756](https://www.beecrowd.com.br/judge/pt/problems/view/1756) Algoritmo Genético
- [x] [2482](https://www.beecrowd.com.br/judge/pt/problems/view/2482) Etiquetas de Noel
- [x] [2520](https://www.beecrowd.com.br/judge/pt/problems/view/2520) O Último Analógimôn
- [x] [2544](https://www.beecrowd.com.br/judge/pt/problems/view/2544) Kage Bunshin no Jutsu
- [x] [2867](https://www.beecrowd.com.br/judge/pt/problems/view/2867) Dígitos
- [x] [2884](https://www.beecrowd.com.br/judge/pt/problems/view/2884) Interruptores

## Dígitos

Nivel: **Fácil**

Nesse problema você pode resolver de duas maneiras:
  - Utilizar a linguagem python para fazer e exponenciação e fazer a contagem dos dígitos transformando o resultando em string;
  - Usar de conceitos matemáticos onde o número de dígitos podem ser representados a partir da fórmula: $\floor(m * log_{10}(n)) + 1$.

## Kage Bunshin no Jutsu

Nivel: **Fácil**

Apenas precisamos simular o processo de multiplicar a partir de 1 (o original) enquanto o número de indivíduos são menores que o número de clones da questão. É fácil notar que esse problema é uma progressão geométrica com razão 1/2.

## Array Hash

Nível: **Fácil**
Conteúdo: Laços de repetição.

Nesse problema você pode apenas usar os índices dos laços de repetição para realizar a contagem do hash.

## Lucro

Nível: **Fácil/Médio**
Conteúdo: Laços de repetição, força bruta

Para resolver você pode simular todos as sequências de dias inicialmente pelo dia 1, depois pelo dia 2 e assim por diante, sempre adicionando o valor arrecadado no dia menos o valor da receita da prefeitura. 

## O Último Analógimôn

Nível: **Fácil**

Você pode notar que o menor caminho sempre será ir o número de casas que representa a diferença de cada um dos eixos, ou seja, a diferença de casas que estão nas coordenadas x do ash com x do pokemon e analogamente as coordenadas em y.

## Etiquetas de Noel

Nível: **Fácil**
Conhecimento prévio: Dicionários / Mapas

Você pode adicionar cada idioma em um mapa/dicionário com sua respectiva mensagem e mostrar acessando sua chave, sem necessidade de pesquisar esse valor em algum tipo de vetor.

## Interruptores

Nível: **Médio/Difícil**
Conhecimento prévio: Operações bitwise

Para resolver esse problema você precisará executar as verificações de troca de estado das lampadas de maneira rápida. Para que isso seja possível podemos nos aproveitar de operações bitwise com número das lampadas que serão trocadas de estado. Nesse caso iremos utilizar a operação "OR" (ou) para que sejam setadas os valores que serão trocados, e a operação "XOR" (ou exclusivo) para que seja executado a troca de estado das lâmpadas. É possível perceber também que para que consigamos determinar se ele vai ou não desligar todas as lâmpadas será necessário efetuar todas a sequência de interruptores duas vezes, uma vez que pode ocorrer de antes de apagar uma lâmpada na sequência ele acabara de acender outra que estava apagada e apenas será possivel apagá-la quando retornar ao início da sequência.

Outros tipos de soluções como simular da mesma forma que vem no problema e trocar o estado sobre um array de estados lâmpadas também será válido.