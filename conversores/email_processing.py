import pandas as pd
from google.colab import files

# Função para corrigir e-mails
def correct_email(email):
    if pd.isnull(email):
        return email

    # Converter o email para minúsculas para a busca dos domínios e para a substituição
    email = str(email).lower()

    # Lista dos domínios mais comuns para busca
    domains = ['hotmail', 'gmail', 'yahoo', 'bol', 'live', 'uol', 'outlook', 'msn']
    
    # Encontrar onde o domínio começa
    domain_index = -1
    for domain in domains:
        index = email.find(domain)
        if index != -1:
            domain_index = index
            break

    if domain_index != -1:
        email = email[:domain_index] + "@" + email[domain_index:]

    # Corrige os TLDs, certificando-se de que 'com.br' é verificado antes de 'com'
    if 'combr' in email:
        email = email.replace('combr', '.com.br')
    elif 'com' in email:
        email = email.replace('com', '.com')
    if 'br' in email and not '.com.br' in email:
        email = email.replace('br', '.br')

    return email

# Exemplo de uso:
emails = [
    "amarildovrv@hotmailcom",
    "caetanopais@gmailcom",
    "juniorcasimpcombr",
    "patriciagurgel76@hotmailcom",
    # ... outros emails ...
]

# Aplicar a correção em uma lista de e-mails
corrected_emails = [correct_email(email) for email in emails]
print(corrected_emails)

# Para aplicar no DataFrame, seria algo assim:
# df['ColunaEmail'] = df['ColunaEmail'].apply(correct_email)



# Carregar a planilha
uploaded = files.upload()
file_name = next(iter(uploaded))

# Lendo a planilha usando o pandas
df = pd.read_excel(file_name)

# Garanta que 'correct_email' está definida conforme fornecido anteriormente

# Aplicar a correção na coluna 'R' (18ª coluna, pois pandas usa base 0)
df.iloc[:, 17] = df.iloc[:, 17].apply(correct_email)

# Exibindo os e-mails corrigidos
print(df.iloc[:, 17])

# Salvar a planilha corrigida
df.to_excel('planilha_corrigida.xlsx', index=False)

# Fazer o download do arquivo corrigido
files.download('planilha_corrigida.xlsx')