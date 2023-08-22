# script para criar pastas em qualquer sistema operacional

import os
caminho = os.getcwd() # devolve o diretório onde esta o script que esta sendo interpretado
# o método os.path devolve a string com as caracteristicas com que cada sistema
# operacional utiliza para construir endereços, como por exemplo, o uso de "/" no
# windows e "\" no linux
# o uso do método join() permite criar o caminho correto
# para um diretório em qualquer sistema operacional
caminhPasta = os.path.join(caminho, 'newDirectory')
print(caminhPasta)
pasta = os.makedirs(caminhPasta)
