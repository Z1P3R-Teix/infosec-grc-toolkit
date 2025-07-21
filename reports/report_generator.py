def gerar_relatorio(maturidade_resultado, riscos):
    with open("relatorio_grc.md", "w", encoding="utf-8") as f:
        f.write("# Relatório GRC - InfoSec Toolkit\n\n")

        # Avaliação de Maturidade
        f.write("## Avaliação de Maturidade (ISO 27001)\n")
        f.write(f"- Média geral: {maturidade_resultado['media']:.2f} / 5\n")

        if maturidade_resultado["pontos_fracos"]:
            f.write("- Pontos fracos:\n")
            for p in maturidade_resultado["pontos_fracos"]:
                titulo = p.split('\n')[0] 
                f.write(f"  - {titulo}\n")
        else:
            f.write("- Nenhum ponto fraco identificado.\n")

        f.write("\n---\n\n")

        # Avaliação de Riscos
        f.write("## Avaliação de Riscos\n\n")

      
        ativo_width = 15
        ameaca_width = 30
        nivel_width = 10
        controle_width = 35

       
        f.write(
            f"| {'Ativo'.ljust(ativo_width)} | "
            f"{'Ameaça'.ljust(ameaca_width)} | "
            f"{'Nível'.ljust(nivel_width)} | "
            f"{'Controle Sugerido'.ljust(controle_width)} |\n"
        )
        f.write(
            f"|{'-'*ativo_width}|{'-'*ameaca_width}|{'-'*nivel_width}|{'-'*controle_width}|\n"
        )

        
        for r in riscos:
            ativo = r.get("ativo", "N/A").ljust(ativo_width)
            ameaca = r.get("ameaca", "N/A").ljust(ameaca_width)
            nivel = r.get("nivel", "N/A").ljust(nivel_width)
            controle = r.get("controle", "A definir (conforme análise)").ljust(controle_width)
            f.write(f"| {ativo} | {ameaca} | {nivel} | {controle} |\n")

        f.write("\n---\n\n")

        # Recomendações
        f.write("## Recomendação\n")
        f.write("- Reforçar os pontos fracos identificados na maturidade\n")
        f.write("- Tratar os riscos de nível Alto e Crítico com prioridade\n")

    print("\nRelatório gerado com sucesso: relatorio_grc.md")
