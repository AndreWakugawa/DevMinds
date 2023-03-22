# IMPORTS PRÓPRIOS
import config

# IMPORTS TERCEIROS
import pandas

# LÊ A TABELA DA CONFIG.PY
table1 = pandas.read_csv(config.tabela_DIR, sep=',')

print(table1)