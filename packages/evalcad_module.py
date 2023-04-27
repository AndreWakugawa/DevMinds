def evalcad():
    import os, sys, csv # Puxa imports da main
    import pandas as pd # Importa o pandas 
    filename = 'login_data.csv' # Nome do arquivo
    target_dir = 'data_sample/' # Diretório relativo
    csv_path = os.path.join(target_dir, filename) # Seleciona diretório
    csv_path2 = os.path.join(target_dir,'aval_data.csv') # Concatena o diretório e nome do aval_data.csv

# Lê os arquivos .csv em forma de dataframe
    df_original = pd.read_csv(csv_path, encoding='utf-8') 
    df_destino = pd.read_csv(csv_path2, encoding='utf-8')

# Seleciona apenas a coluna id e nome do login_data.csv e cria um novo dataframe somente com os dados filtrados
    colunas_desejadas = ['id', 'nome'] 
    df_selecionado = df_original[colunas_desejadas].tail(1)

    df_concatenado = pd.concat([df_selecionado,df_destino],ignore_index=True) #Aqui o novo dataframe filtrado é concatenado junto com a aval_data.csv

    df_concatenado.to_csv(csv_path2, index=False, encoding='utf-8') #Nesse momento, todo o arquivo aval_data.csv é substituido por um novo aval_data.csv com os novos dados dentro.