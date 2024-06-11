import streamlit as st
import requests as req
import pandas as pd

def get(url):
    return req.get(url).json()

input_dict = {}

with st.sidebar:
    response = get('http://127.0.0.1:8000/secoes/')
    options = [item['cd_secao'] for item in response]

    secao = st.selectbox('Seção', options=options, key='secao', index=None, placeholder="Selecione uma seção")
    input_dict['secao'] = secao

    if secao is None:
        st.session_state.clear()
    else:
        if 'secao' in st.session_state and st.session_state.secao:
            divisoes = get(f'http://127.0.0.1:8000/secoes/{st.session_state.secao}/divisoes/')
            divisao_options = [item['cd_divisao'] for item in divisoes]
            divisao = st.selectbox('Divisão', options=divisao_options, key='divisao', index=None, placeholder="Selecione uma divisão")
            input_dict['divisao'] = divisao

            if divisao is None:
                for key in list(st.session_state.keys()):
                    if key != 'secao':
                        del st.session_state[key]
            else:
                if 'divisao' in st.session_state and st.session_state.divisao:
                    grupos = get(f'http://127.0.0.1:8000/divisoes/{st.session_state.divisao}/grupos/')
                    grupo_options = [item['cd_grupo'] for item in grupos]
                    grupo = st.selectbox('Grupo', options=grupo_options, key='grupo', index=None, placeholder="Selecione um grupo")
                    input_dict['grupo'] = grupo

                    if grupo is None:
                        for key in list(st.session_state.keys()):
                            if key not in ['secao', 'divisao']:
                                del st.session_state[key]
                    else:
                        if 'grupo' in st.session_state and st.session_state.grupo:
                            classes = get(f'http://127.0.0.1:8000/grupos/{st.session_state.grupo}/classes/')
                            classe_options = [item['cd_classe'] for item in classes]
                            classe = st.selectbox('Classe', options=classe_options, key='classe', index=None, placeholder="Selecione uma classe")
                            input_dict['classe'] = classe

                            if classe is None:
                                for key in list(st.session_state.keys()):
                                    if key not in ['secao', 'divisao', 'grupo']:
                                        del st.session_state[key]
                            else:
                                if 'classe' in st.session_state and st.session_state.classe:
                                    subclasses = get(f'http://127.0.0.1:8000/classes/{st.session_state.classe}/subclasses/')
                                    subclass_options = [item['cd_subclasse'] for item in subclasses]
                                    subclass = st.selectbox('Subclasse', options=subclass_options, key='subclass', index=None, placeholder="Selecione uma subclasse")
                                    input_dict['subclasse'] = subclass

    if st.button('Imprimir valores'):
        query = ''
        for key, value in input_dict.items():
            if value:
                query += f'{key}={value}&'
        else:
            try:
                response = req.get(f'http://127.0.0.1:8000/arrecadacoes/?{query[:-1]}').json()
                df = pd.DataFrame(response)
                st.session_state['df'] = df
            except:
                st.session_state['df'] = None
                st.write('Erro ao buscar dados')

if 'df' in st.session_state and st.session_state['df'] is not None:                
    with st.chat_message('user'):
        message = ''
        if st.session_state['df']['cd_subclasse'].nunique() == 1:
            message += f"\nSubclasse: {st.session_state['df']['cd_subclasse'].unique().item()}\n"
        else:
            message += f"\nSubclasses atendidas: {st.session_state['df']['cd_subclasse'].nunique()}\n"
            
        message += f"\nMédia de arrecadação: R$ {st.session_state['df']['vl_arrecadacao'].mean():,.2f}\n"
        message += f"\nMaior de arrecadação: R$ {st.session_state['df']['vl_arrecadacao'].max():,.2f}\n"
        message += f"\nMenor de arrecadação: R$ {st.session_state['df']['vl_arrecadacao'].min():,.2f}\n"
        message += f"\nTotal de arrecadação: R$ {st.session_state['df']['vl_arrecadacao'].sum():,.2f}\n"
        st.write(message)
        with st.expander('Visualizar planilha'):
            st.write(st.session_state['df'])