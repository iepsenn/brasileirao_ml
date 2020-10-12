import streamlit as st
import pandas as pd
import pickle
from xgboost import plot_importance

PREDICTIONS_FILEPATH = 'data/predictions.csv'
PAGE_TITLE = 'Profeta do Brasileirão'
HEADER_TEXT = (
    "Previsões de resultados dos próximos jogos "
    "da séria A do campeonato brasileiro de 2020, onde a "
    "única coisa 100% correta é que terá gol do Galhardo."
)
RESULT_COLUMN = 'Previsões para a rodada {}'
ABOUT_MODEL_TEXT = (
    "Foram utilizados dados dos anos de 2019 e 2020 até "
    "o momento com cerca de 220 features coletadas de "
    "cada jogo, com informações de passes, posse de bola, desarmes, etc."
)
MODEL_FILEPATH = 'data/serial/xgboost_regressor.model'


# @st.cache
def load_data():
    data = pd.read_csv(PREDICTIONS_FILEPATH)
    data = data[data['matchweek'] == data['matchweek'].max()].copy()
    return data


data = load_data()


st.title(PAGE_TITLE)
st.write(HEADER_TEXT)
st.image('imgs/header_image.png', width=800)

st.write('---')
st.header('RESULTADOS')

next_matchweek = data['matchweek'].max()
data[RESULT_COLUMN.format(next_matchweek)] = (
    data['team1'] + ' ' +
    data['score_team1'].astype(str) + ' x ' +
    data['score_team2'].astype(str) + ' ' +
    data['team2']
)
st.table(data[RESULT_COLUMN.format(next_matchweek)])

st.write('---')
st.header('SOBRE OS DADOS E MODELO')
st.write(ABOUT_MODEL_TEXT)

st.write('---')
st.header('QUAIS FEATURES INFLUENCIARAM MAIS O MODELO?')
num_features = st.selectbox(
    'Número de features com mais influencia',
    range(5, 26)
)

with open(MODEL_FILEPATH, 'rb') as serial_model:
    model = pickle.load(serial_model)

ax = plot_importance(model, max_num_features=num_features)
st.pyplot(ax.figure)
