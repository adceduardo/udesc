def compress(uncompressed):
    # Inicializa o dicionário com caracteres ASCII (0-255)
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    
    if w:
        result.append(dictionary[w])
    return result


def decompress(compressed):
    
    from io import StringIO

   
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}

    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
           
            entry = w + w[0]
        else:
            raise ValueError(f'Código inválido: {k}')

        result.write(entry)

       
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result.getvalue()

texto_original = "TOBEORNOTTOBEORTOBEORNOT"
compactado = compress(texto_original)
descompactado = decompress(compactado.copy())

print(f"Original:    {texto_original}")
print(f"Compactado:  {compactado}")
print(f"Descompactado: {descompactado}")
print(f"Sucesso: {texto_original == descompactado}")
