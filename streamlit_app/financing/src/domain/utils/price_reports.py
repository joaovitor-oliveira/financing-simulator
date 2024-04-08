from financing.src.domain.price_method import PriceMethod


class PriceReport():
    @staticmethod
    def simple_report(total_amount: float, installments: int, rate: float) -> dict:
        price = PriceMethod(total_amount, installments, round(rate / 100, 4))
        total_value = round(price.calculate_total_value(), 2)
        emr = round(price.calculate_effective_monthly_rate() * 1000, 2)
        tec = round(price.calculate_total_effective_cost(), 2)

        return [
            "Totais",
            f"R$ {total_value:.2f}",
            f"R$ {tec:.2f}",
            f"R$ {total_amount:.2f}",
            f"Juros efetivos: {emr:.2f} %",
        ]

    def complete_report(total_amount: float, installments: int, rate: float) -> dict:
        rate = round(rate / 100, 4)
        price = PriceMethod(total_amount, installments, rate)
        monthly_payment = round(price.calculate_monthly_payment(), 2)
        outstanding_balance = round(total_amount, 2)

        report = [
            [
                "0",
                "R$ 0.00",
                "R$ 0.00",
                "R$ 0.00",
                f"R$ {outstanding_balance:.2f}"
            ]
        ]

        for month in range(installments):
            monthly_interest = round(round(outstanding_balance, 2) * rate, 2)
            amortization = round(monthly_payment - monthly_interest, 2)
            outstanding_balance = round(max(0, outstanding_balance - amortization), 2)
            report.append([
                f"{month + 1}",
                f"R$ {round(monthly_payment, 2):.2f}",
                f"R$ {round(monthly_interest, 2):.2f}",
                f"R$ {round(amortization, 2):.2f}",
                f"R$ {round(outstanding_balance, 2):.2f}"
            ])

        return report
