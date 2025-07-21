def run_assessment():
    print("\n--- Avaliação de Maturidade ISO 27001 ---\n")

    perguntas = [
        "1. O nível de implementação de controles de acesso na organização é:\n   1 - Inexistente\n   2 - Inicial (não formalizado)\n   3 - Parcialmente implementado\n   4 - Bem implementado, mas sem revisão contínua\n   5 - Totalmente implementado, documentado e auditado regularmente",
        "2. O nível de gestão de incidentes de segurança da informação é:\n   1 - Inexistente\n   2 - Ad hoc\n   3 - Procedimentos definidos mas não aplicados consistentemente\n   4 - Procedimentos aplicados com monitoramento\n   5 - Processos totalmente implementados com revisão contínua",
        "3. O nível de conscientização sobre segurança da informação entre os colaboradores é:\n   1 - Nulo\n   2 - Baixo\n   3 - Médio\n   4 - Alto\n   5 - Excelente, com treinamentos regulares e campanhas ativas",
        "4. O grau de controle sobre acesso físico a áreas sensíveis é:\n   1 - Inexistente\n   2 - Parcial\n   3 - Implementado sem monitoramento\n   4 - Monitorado e controlado\n   5 - Com auditorias regulares e revisão de acessos",
        "5. A frequência e eficácia das auditorias internas de segurança da informação é:\n   1 - Nunca realizadas\n   2 - Ocasionalmente\n   3 - Regulares mas superficiais\n   4 - Regulares com revisão de ações corretivas\n   5 - Parte integrante da melhoria contínua"
    ]

    respostas = []

    for pergunta in perguntas:
        while True:
            try:
                print("\n" + pergunta)
                resposta = int(input("Sua resposta (1 a 5): "))
                if resposta < 1 or resposta > 5:
                    raise ValueError
                respostas.append((pergunta, resposta)) 
                break
            except ValueError:
                print("⚠️  Entrada inválida. Por favor, insira um número de 1 a 5.")

    media = sum([nota for _, nota in respostas]) / len(respostas)
    print(f"\nMédia de Maturidade: {media:.2f}")

    if media < 2:
        print("Recomendação: Implementar urgentemente controles básicos de segurança.")
    elif media < 3.5:
        print("Recomendação: Melhorar processos e implementar políticas mais robustas.")
    elif media < 4.5:
        print("Recomendação: Consolidar e revisar práticas existentes.")
    else:
        print("Recomendação: Manter e auditar continuamente os controles de segurança.")

    return respostas
