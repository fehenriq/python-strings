url = "https://docs.google.com/spreadsheets/d/10UD_32t2ExF4IT3tThE3YyxW25jaGhjWctGcSVqfI2g/edit#gid=182409236"
indice_start = url.find("d/")
indice_end = url.find("/edit")
url_id = url[indice_start + 2:indice_end]

print(url_id)