endereco = "Rua Lydio Fernandes da Costa, 71, Palmeiras, Suzano, SP, 08625-325"

import re

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)
if busca:
  cep = busca.group()
  print(cep)