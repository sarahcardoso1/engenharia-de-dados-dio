def analise_vendas(vendas):
    
    total_vendas = sum(vendas)
    media_vendas = (sum(vendas)/len(vendas))
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
   
    entrada_dividida = entrada.split(',')
    analise_vendas = map(int, entrada_dividida)
    vendas = list(analise_vendas)
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))