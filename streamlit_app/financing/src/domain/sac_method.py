from financing.src.domain.financing_method_interface import FinancingMethod


class SacMethod(FinancingMethod):

    def __init__(self, pv: float, n: int, i: float) -> None:
        '''
        A instance of SAC financing method.

        Args:
            pv (float): The total financing value.
            n (int): The number of payments.
            i (float): The nominal yearly interest rate.
        '''
        self.__pv = pv
        self.__n = n
        self.__i = i

    def calculate_amortization(self) -> float:
        '''
        Calculate the monthly amortization.

        Returns:
            float: The monthly amortization amount.
        '''
        pv = self.__pv
        n = self.__n

        amortization = pv / n
        return amortization

    def calculate_monthly_payment(self, m: int) -> float:
        '''
        Calculate the monthly payment for a given month.

        Args:
            m (int): The month for which to calculate the payment.

        Returns:
            float: The monthly payment amount for the given month.
        '''
        pv = self.__pv
        im = self.calculate_effective_monthly_rate()
        amortization = self.calculate_amortization()

        pmt = amortization + (pv - (amortization * (m - 1))) * im
        return pmt

    def calculate_total_effective_cost(self) -> float:
        '''
        Calculate the total effective cost.

        Returns:
            float: The total effective cost.
        '''
        pmt_total = sum(self.calculate_monthly_payment(m) for m in range(1, self.__n + 1))
        return pmt_total - self.__pv

    def calculate_effective_monthly_rate(self) -> float:
        '''
        Calculate the effective monthly rate.

        Returns:
            float: The effective monthly rate.
        '''
        i = self.__i

        im = (1 + i) ** (1 / 12) - 1
        return im

    def calculate_total_value(self) -> float:
        '''
        Calculate the total value of financing.

        Returns:
            float: The total value of financing.
        '''
        pv = self.__pv
        cet = self.calculate_total_effective_cost()

        total_value = pv + cet
        return total_value
