# serieA_prophet

Os resultados futuros no futebol é sempre algo difícil de estimar, pois existem muitos fatores que influenciam no resultado, sendo algum deles até pessoais de cada jogador ou questões extra campo dos clubes em geral. Esse repositório tenta utilizar alguma variáveis extraídas durante os jogos anteriores para tentar prever os próximos resultados.

## Variáveis Utilizadas
Foram utilizadas cerca de 220 features extraídas dos jogos, como as estatísticas de passes, finalizações, faltas, desarmes, etc. As features extraídas foram utilizadas usando o cálculo da média dos últimos 3 jogos, metodologia que é utilizada para prever os jogos futuros, onde não será possível acessar o valor dessas variáveis (elas não existem ainda).

## Modelo
Foi utilizado o modelo de regressão XGBoost com os parâmetros padrão e sem nenhum tipo de seleção de features.

## TODO
- Utilizar busca de parâmetros para o modelo;
- Utilizar algum método de seleção de feature (possivelmente [RFE](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html));
- Mexer na estrutura da página.


**A única certeza é que terá gol de Thiago Galhardo.**