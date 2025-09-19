# 1. ATUALIZE AQUI com os 5 números do último sorteio da Loteria Federal.
#    Exemplo: ['01234', '56789', '98765', '43210', '09182']
resultados_loteria_federal = ['050309','067195','051158','078151','056723'] # Coloque os números aqui

# 2. ATUALIZE AQUI com os números das suas cotas.
#    Exemplo: ['123', '456', '789', '987']
minhas_cotas = ['350','560'] # Coloque suas cotas aqui

# Variável de controle para verificar se já houve um ganhador
vencedor_encontrado = False

# Loop para percorrer cada um dos 5 prêmios da Loteria Federal
for i, premio in enumerate(resultados_loteria_federal):
    # A regra do sorteio é sequencial. Se um prêmio já encontrou um ganhador,
    # não precisa verificar os próximos.
    if vencedor_encontrado:
        break

    print(f"Analisando o {i+1}º prêmio: {premio}")

    # --- Regra 1: Analisar os 3 últimos dígitos ---
    # Pega os 3 últimos caracteres da string do prêmio
    numero_regra_1 = premio[-3:]

    # Verifica se a cota está na sua lista
    if numero_regra_1 in minhas_cotas:
        print(f"Parabéns! Sua cota '{numero_regra_1}' foi sorteada!")
        print(f"Número da Loteria Federal: {premio} (Prêmio {i+1})")
        print("Regra utilizada: Últimos 3 dígitos.")
        vencedor_encontrado = True
        break # Sai do loop principal, pois o ganhador foi encontrado

    # --- Regra 2: Analisar os 3 dígitos do meio ---
    # Pega os caracteres da 2ª a 4ª posição (índices 1 a 3)
    numero_regra_2 = premio[1:4]

    # Verifica se a cota está na sua lista
    if numero_regra_2 in minhas_cotas:
        print(f"Parabéns! Sua cota '{numero_regra_2}' foi sorteada!")
        print(f"Número da Loteria Federal: {premio} (Prêmio {i+1})")
        print("Regra utilizada: Dígitos da 2ª à 4ª posição.")
        vencedor_encontrado = True
        break # Sai do loop principal, pois o ganhador foi encontrado

# Se o loop terminar e não tiver encontrado nenhum ganhador
if not vencedor_encontrado:
    print("\nNenhuma das suas cotas foi sorteada neste concurso. Boa sorte na próxima!")