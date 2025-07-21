def risk_assessment():
    print("\nAvaliação de Riscos - InfoSec GRC Toolkit\n")

    risks = []

    while True:
        # Validação para apenas um ativo por vez!
        while True:
            ativo = input("Ativo (ex: banco de dados): ").strip()
            if "," in ativo or " e " in ativo.lower() or "/" in ativo:
                print("Por favor, insira apenas UM ativo por vez.")
            elif ativo == "":
                print("O ativo não pode estar em branco.")
            else:
                break

        ameaca = input("Ameaça (ex: acesso não autorizado): ").strip()
        impacto = input("Impacto (baixo, medio, alto, critico): ").strip().lower()
        probabilidade = input("Probabilidade (baixa, media, alta): ").strip().lower()

        impacto_val = {"baixo": 1, "medio": 2, "medio": 2, "alto": 3, "critico": 4, "critico": 4}.get(impacto, 1)
        probabilidade_val = {"baixa": 1, "media": 2, "media": 2, "alta": 3}.get(probabilidade, 1)

        risco = impacto_val * probabilidade_val

        if risco <= 2:
            nivel = "Baixo"
        elif risco <= 4:
            nivel = "Medio"
        elif risco <= 8:
            nivel = "Alto"
        else:
            nivel = "Critico"

        #  Recomendação com base no ativo/ameaça
        if "acesso" in ameaca.lower():
            controle = "ISO 27001 - A.9 Controle de Acesso"
        elif "dados" in ativo.lower():
            controle = "ISO 27001 - A.18 Proteção de Dados Pessoais"
        else:
            controle = "A definir (conforme análise)"

        risks.append({
            "ativo": ativo,
            "ameaca": ameaca,
            "impacto": impacto,
            "probabilidade": probabilidade,
            "risco": risco,
            "nivel": nivel,
            "controle": controle
        })

        continuar = input("\nDeseja adicionar outro risco? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("\nRelatório de Riscos:")
    for r in risks:
        print(f"- [{r['nivel']}] {r['ativo']} sofre ameaça de {r['ameaca']} → controle sugerido: {r['controle']}")

    return risks
