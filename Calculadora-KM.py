import tkinter as tk
from tkinter import ttk

tabela_carros = {
    "Automóvel a gasolina": 12,
    "Automóvel a etanol": 6.9,
    "Automóvel flex a gasolina": 15,
    "Automóvel flex a etanol": 10.4,
    "Automóvel a GNV": 12,
    "Motocicleta a gasolina": 37.2,
    "Motocicleta flex a gasolina": 43.2,
    "Motocicleta flex a etanol": 29.3,
    "Micro-ônibus a diesel": 3.8,
    "Ônibus rodoviário a diesel": 3,
    "Caminhão": 5.1
}

periodos = ["Diária", "Mensal", "Anual"]

combustível = ["Gasolina", "Etanol", "GNV", "Diesel"]

veículos = ["Carro", "Moto", "Caminhão", "Micro-ônibus"]

def calcular_emissao_carbono():
    veiculo = veiculo_combobox.get()
    combustivel_usado = combustivel_combobox.get()
    periodo = periodo_combobox.get()
    km_rodado = int(km_rodado_entry.get())
    tipo_veiculo = tipo_veiculo_combobox.get()

    if periodo == "Diária":
        km_rodado_total = km_rodado * 365
    elif periodo == "Mensal":
        km_rodado_total = km_rodado * 12
    elif periodo == "Anual":
        km_rodado_total = km_rodado * 1
    else:
        resultado_label.config(text="A forma de contagem é inválida!")
        return
    
    if tipo_veiculo in tabela_carros:
        quantidade_combustivel_total = km_rodado_total / tabela_carros[tipo_veiculo]
    else:
        resultado_label.config(text="Esse veículo não está na tabela")
        return

    if combustivel_usado.lower() == "gasolina":
        combustivel_fossil = quantidade_combustivel_total * 0.73
        combustivel_biocombustivel = quantidade_combustivel_total * 0.27

        fator_emissao_fossil_co2 = 2.212
        fator_emissao_biocombustivel_co2 = 1.526

        fator_emissao_fossil_ch4 = 0.0008
        fator_emissao_biocombustivel_ch4 = 0.0002

        fator_emissao_fossil_n2o = 0.00001
        fator_emissao_biocombustivel_n2o = 0.00026
    elif combustivel_usado.lower() == "diesel":
        combustivel_fossil = quantidade_combustivel_total * 0.90
        combustivel_biocombustivel = quantidade_combustivel_total * 0.10

        fator_emissao_fossil_co2 = 2.603
        fator_emissao_biocombustivel_co2 = 2.431

        fator_emissao_fossil_ch4 = 0.0001
        fator_emissao_biocombustivel_ch4 = 0.0003

        fator_emissao_fossil_n2o = 0.00014
        fator_emissao_biocombustivel_n2o = 0.00002
    elif combustivel_usado.lower() == "gnv":
        combustivel_fossil = quantidade_combustivel_total
        combustivel_biocombustivel = 0

        fator_emissao_fossil_co2 = 1.999
        fator_emissao_biocombustivel_co2 = 0

        fator_emissao_fossil_ch4 = 0.0034
        fator_emissao_biocombustivel_ch4 = 0

        fator_emissao_fossil_n2o = 0.00011
        fator_emissao_biocombustivel_n2o = 0
    elif combustivel_usado.lower() == "etanol":
        combustivel_fossil = 0
        combustivel_biocombustivel = quantidade_combustivel_total

        fator_emissao_fossil_co2 = 0
        fator_emissao_biocombustivel_co2 = 1.457

        fator_emissao_fossil_ch4 = 0
        fator_emissao_biocombustivel_ch4 = 0.0004

        fator_emissao_fossil_n2o = 0
        fator_emissao_biocombustivel_n2o = 0.00001
    else:
        resultado_label.config(text="Não temos cálculo para esse tipo de combustível")
        return

    resultado_fossil_co2 = ((combustivel_fossil * fator_emissao_fossil_co2) / 1000) * 1
    resultado_fossil_ch4 = ((combustivel_fossil * fator_emissao_fossil_ch4) / 1000) * 28
    resultado_fossil_n2o = ((combustivel_fossil * fator_emissao_fossil_n2o) / 1000) * 265

    resultado_biocombustivel_co2 = ((combustivel_biocombustivel * fator_emissao_biocombustivel_co2) / 1000) * 1
    resultado_biocombustivel_ch4 = ((combustivel_biocombustivel * fator_emissao_biocombustivel_ch4) / 1000) * 28
    resultado_biocombustivel_n2o = ((combustivel_biocombustivel * fator_emissao_biocombustivel_n2o) / 1000) * 265

    carbono_equivalente = resultado_fossil_co2 + resultado_fossil_ch4 + resultado_fossil_n2o + resultado_biocombustivel_ch4 + resultado_biocombustivel_n2o
    CO2_biogenico = resultado_biocombustivel_ch4 + resultado_biocombustivel_co2 + resultado_biocombustivel_n2o
    comb_fossil = resultado_fossil_co2 + resultado_fossil_ch4 + resultado_fossil_n2o
    carbono = int(carbono_equivalente)
    compensacao = carbono * 7
    emissao_total = carbono_equivalente + CO2_biogenico + comb_fossil

    resultado_label.config(text=f"Emissão total:{emissao_total:.2f} toneladas\nCarbono Equivalente: {carbono_equivalente:.2f} toneladas\nCarbono Biogênico: {CO2_biogenico:.2f} toneladas\nCombustível fóssil: {comb_fossil:.2f} litros\nBiocombustível: {combustivel_biocombustivel:.2f} litros\nÁrvores necessárias para compensar a emissão de CO2:\n{compensacao:.0f}")

janela = tk.Tk()
janela.title("Calculadora de Emissão de Carbono - quilômetros")
janela.geometry("700x900") 
janela.configure(background="lavender blush")

space0_label = tk.Label(janela, background="lavender blush", text="")
space0_label.pack()

bemvindo_label =tk.Label(janela, font= "arial", height=2, background="lavender blush", text="Seja bem-vindo a nossa calculadora de emissões de carbono!")
bemvindo_label.pack()

veiculo_label = tk.Label(janela, font= "arial", height=2, background="lavender blush", text="Selecione o tipo de veículo:")
veiculo_label.pack()
veiculo_combobox = ttk.Combobox(janela, values=veículos, width=50)
veiculo_combobox.pack()

space2_label = tk.Label(janela, background="lavender blush", text="")
space2_label.pack()

combustivel_label = tk.Label(janela, font= "arial", height=2, background="lavender blush", text="Selecione o tipo de combustível:")
combustivel_label.pack()
combustivel_combobox = ttk.Combobox(janela, values=combustível, width=50)
combustivel_combobox.pack()

space3_label = tk.Label(janela, background="lavender blush", text="")
space3_label.pack()

periodo_label = tk.Label(janela, font= "arial", height=2, background="lavender blush", text="Como deseja informar a quantidade de km:")
periodo_label.pack()
periodo_combobox = ttk.Combobox(janela, values=periodos, width=50)
periodo_combobox.pack()

space4_label = tk.Label(janela, background="lavender blush", text="")
space4_label.pack()

km_rodado_label = tk.Label(janela, font= "arial", height=2, background="lavender blush", text="Digite a quantidade de Km rodados:")
km_rodado_label.pack()
km_rodado_entry = tk.Entry(janela, relief="solid", border=0.5)
km_rodado_entry.pack()

space5_label = tk.Label(janela, background="lavender blush", text="")
space5_label.pack()

tipo_veiculo_label = tk.Label(janela, font= "arial", height=2, background="lavender blush", text="Qual dos itens abaixo se enquadra melhor com o seu veículo:")
tipo_veiculo_label.pack()
tipo_veiculo_combobox = ttk.Combobox(janela, width=50, values=list(tabela_carros.keys()))
tipo_veiculo_combobox.pack()

space6_label = tk.Label(janela, background="lavender blush", text="")
space6_label.pack()

calcular_button = tk.Button(janela, font= "arial", height=1, width=20, background="black", foreground="white", text="Calcular", command=calcular_emissao_carbono)
calcular_button.pack()

space7_label = tk.Label(janela, background="lavender blush", text="")
space7_label.pack()

resultado_label = tk.Label(janela, background="lavender blush", font= "arial", height=7, text="")
resultado_label.pack()

janela.mainloop()