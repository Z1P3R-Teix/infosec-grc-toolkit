#  InfoSec GRC Toolkit

Uma ferramenta simples de linha de comando para realizar:

- Avaliação de Maturidade baseada na **ISO 27001**
- Avaliação de Riscos (Impacto × Probabilidade)
- Sugestões automáticas de controles mitigadores
- Geração de relatório em **Markdown (.md)**


---

##  Funcionalidades

- Avaliação de Maturidade baseada na ISO 27001  
- Avaliação de Riscos com cálculo de nível (baixo a crítico)  
- Sugestão de controles com base na ameaça/ativo  
- Geração automática de relatório Markdown  
- Projeto leve e modular, rodando direto no terminal  

---

## Tecnologias Usadas

- Python **3.8+**
- Estrutura modular (`maturity_assessment`, `risk_assessment`, `reports`)
- CLI via terminal
- Markdown para relatórios
- Baseado em frameworks **ISO 27001** e **NIST CSF** (não oficial)

---

## Como usar

1. **Clone o repositório**

```bash
git clone https://github.com/Z1P3R-Teix/grc-toolkit.git
cd grc-toolkit
```

2. **Execute o Script**
``` python main.py ```

## Exemplo de Relatório Gerado
  ### Avaliação de Maturidade (ISO 27001)
  - Média geral: 3.00 / 5
  - Nenhum ponto fraco identificado.
  
  ### Avaliação de Riscos
  | Ativo           | Ameaça                | Nível | Controle Sugerido                          |
  |-----------------|-----------------------|-------|--------------------------------------------|
  | Banco de Dados  | Acesso não autorizado | Alto  | A definir (conforme análise)               |
  
  ### Recomendação
  - Reforçar os pontos fracos identificados na maturidade
  - Tratar os riscos de nível Alto e Crítico com prioridade



