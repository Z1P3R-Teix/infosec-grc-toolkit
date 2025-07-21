from maturity_assessment.iso_27001 import run_assessment
from risk_assessment.risk_matrix import risk_assessment
from reports.report_generator import gerar_relatorio

def main():
    print("Infosec GRC Toolkit - Avaliação")
    
    maturidade = run_assessment()
    riscos = risk_assessment()

    resultado_maturidade = {
        "media": sum([s for _, s in maturidade]) / len(maturidade),
        "pontos_fracos": [q for q, s in maturidade if s < 3]
    }
    print("DEBUG - Conteúdo de riscos:", riscos)

    gerar_relatorio(resultado_maturidade, riscos)

if __name__ == "__main__":
    main()
