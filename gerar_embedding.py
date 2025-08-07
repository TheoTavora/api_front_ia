"""
from sentence_transformers import SentenceTransformer
import json
# Aqui um vetor chamado "faq" referente as perguntas-base, que será transformado em JSON.
with open('base_faq_raw.json', 'r', encoding='utf-8') as f:
    faq = json.load(f)

# Modelo leve e gratuito: all-MiniLM-L6-v2
modelo = SentenceTransformer('all-MiniLM-L6-v2')

# Extrai apenas as perguntas para gerar embeddings
perguntas = [item['pergunta'] for item in faq]

# Gera os embeddings
vetores = modelo.encode(perguntas).tolist()

# Junta pergunta, resposta e embedding
faq_completo = []
for i, item in enumerate(faq):
    faq_completo.append({
        "pergunta": item['pergunta'],
        "resposta": item['resposta'],
        "embedding": vetores[i]
    })

# Salva tudo no base_faq.json final
with open('base_faq.json', 'w', encoding='utf-8') as f:
    json.dump(faq_completo, f, ensure_ascii=False, indent=2)

print("base_faq.json gerado com sucesso!")
"""

from sentence_transformers import SentenceTransformer
import json

# Modelo leve e gratuito: all-MiniLM-L6-v2
modelo = SentenceTransformer('all-MiniLM-L6-v2')

# Aqui um vetor chamado "faq" referente as perguntas-base, que será transformado em JSON.
faq = [
  {
    "pergunta": "Quais cidades vocês atendem?",
    "resposta": "Atendemos na região metropolitana de Porto Alegre: Novo Hamburgo, Estância Velha, São Leopoldo, Nova Hartz, Esteio, Sapucaia do Sul, Canoas, Cachoeirinha, Gravataí, Porto Alegre, Viamão, Alvorada e Guaíba."
  },
  {
    "pergunta": "Vocês têm casa em Porto Alegre?",
    "resposta": "Dependendo da zona. Na Zona Sul sim. Na Zona Norte indicamos Alvorada ou Gravataí. Na Zona Leste, indicamos Viamão."
  },
  {
    "pergunta": "Tem opção de casa nessa região?",
    "resposta": "Verificamos no mapa da Movese. Se não tiver casa próxima, oferecemos apartamento como alternativa mais viável pelo Minha Casa Minha Vida."
  },
  {
    "pergunta": "Quero casa, não apartamento.",
    "resposta": "NOME DO CLIENTE, aqui eu quero ser muito transparente contigo. Realmente, hoje não há opções de casas próximas à região que você deseja... (seguir com explicação do playbook)."
  },
  {
    "pergunta": "Quais imóveis estão disponíveis?",
    "resposta": "Para garantir que eu te envie opções dentro da tua realidade financeira, você pode me dizer aproximadamente qual é a tua renda mensal familiar hoje?"
  },
  {
    "pergunta": "Tem imóvel 100% financiado?",
    "resposta": "Sim, dentro do programa Minha Casa Minha Vida, dependendo da sua renda e aprovação na análise de crédito."
  },
  {
    "pergunta": "Tem opções sem entrada?",
    "resposta": "Verificamos a viabilidade durante a análise de crédito. Alguns imóveis permitem entrada facilitada ou subsídio que cobre parte dela."
  },
  {
    "pergunta": "Tem imóvel com garagem?",
    "resposta": "Sim. Assim que souber sua renda e localização desejada, envio opções com esse diferencial."
  },
  {
    "pergunta": "Vocês têm planta ou fotos do imóvel?",
    "resposta": "Encontrei uma excelente opção pra você que se encaixa dentro da tua renda e do que você está procurando. Dá uma olhada com calma nesse empreendimento aqui: ENVIAR MATERIAL."
  },
  {
    "pergunta": "Esse imóvel é pelo Minha Casa Minha Vida?",
    "resposta": "Sim, trabalhamos com imóveis dentro do programa."
  },
  {
    "pergunta": "Qual o valor do imóvel?",
    "resposta": "Pra garantir que eu te envie opções que caibam no seu orçamento, você pode me dizer sua renda mensal?"
  },
  {
    "pergunta": "Preciso dar entrada?",
    "resposta": "Se for o primeiro imóvel e sua renda for compatível, é possível conseguir 100% financiado. Se não for o primeiro, pode precisar de entrada."
  },
  {
    "pergunta": "Qual valor mínimo de entrada?",
    "resposta": "Se não for o primeiro imóvel, geralmente é necessário pelo menos R$ 10.000,00 de entrada."
  },
  {
    "pergunta": "Qual o valor da parcela?",
    "resposta": "Depende da sua renda. Após simulação, conseguimos estimar o valor das parcelas com mais precisão."
  },
  {
    "pergunta": "O imóvel é financiado pela Caixa?",
    "resposta": "Sim, trabalhamos com financiamento pela Caixa Econômica."
  },
  {
    "pergunta": "Posso usar o FGTS?",
    "resposta": "Sim, é possível usar o FGTS para entrada ou amortização, dentro das regras da Caixa."
  },
  {
    "pergunta": "Qual a taxa de juros?",
    "resposta": "Variável conforme o perfil e programa, mas dentro das condições do Minha Casa Minha Vida são as menores do mercado."
  },
  {
    "pergunta": "Qual o prazo do financiamento?",
    "resposta": "Até 35 anos, dependendo da idade e aprovação da Caixa."
  },
  {
    "pergunta": "Tenho score baixo, posso financiar?",
    "resposta": "Verificamos na análise de crédito. Existem casos de aprovação mesmo com score baixo, especialmente se for o primeiro imóvel."
  },
  {
    "pergunta": "Já fui reprovado, posso tentar de novo?",
    "resposta": "Você chegou a entender o motivo da sua reprovação? O corretor explicou exatamente o que faltou ou o que precisa ajustar?"
  },
  {
    "pergunta": "Quais documentos preciso enviar?",
    "resposta": "Apenas 3: RG ou CNH, comprovante de residência e comprovante de renda."
  },
  {
    "pergunta": "Como sei se fui aprovado?",
    "resposta": "Após envio dos documentos, o retorno da análise sai em até 48h úteis."
  },
  {
    "pergunta": "Tem custo para fazer a análise?",
    "resposta": "Não. A análise de crédito é gratuita."
  },
  {
    "pergunta": "Com nome sujo posso financiar?",
    "resposta": "Depende do valor e tipo da restrição. Dívidas menores que R$ 1.000,00 ainda permitem análise."
  },
  {
    "pergunta": "Como assino a MO?",
    "resposta": "Você pode assinar pelo aplicativo gov.br. Vou te mandar um tutorial rapidinho pra isso."
  },
  {
    "pergunta": "Não tenho comprovante de renda, posso financiar?",
    "resposta": "Verificamos outras formas de comprovação. Precisa ser analisado caso a caso."
  },
  {
    "pergunta": "Já tenho um imóvel, posso financiar outro?",
    "resposta": "Se estiver no nome e com escritura registrada, não. Caso contrário, pode ter direito ao programa."
  },
  {
    "pergunta": "Quanto tempo demora para aprovar?",
    "resposta": "Aproximadamente 48h úteis após envio completo da documentação."
  },
  {
    "pergunta": "Preciso abrir conta na Caixa?",
    "resposta": "Em alguns casos sim, especialmente se o motivo de reprovação anterior foi rating mínimo."
  },
  {
    "pergunta": "Tenho dívida com desconto, posso financiar?",
    "resposta": "Se fez acordo, precisa aguardar até 90 dias para sair do BACEN. Você lembra quando foi que fez o acordo com essa instituição financeira?"
  }
]

# Gera os embeddings
for item in faq:
    embedding = modelo.encode(item["pergunta"]).tolist()  # converte para lista nativa do Python
    item["embedding"] = embedding

# Salva no JSON, UTF-8
with open("base_faq.json", "w", encoding="utf-8") as f:
    json.dump(faq, f, ensure_ascii=False, indent=2)

print("base_faq.json gerado com sucesso!")
