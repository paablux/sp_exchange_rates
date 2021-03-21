
class FakeRequestInterface():
    def __init__(self):
        pass

    def run_api_symbol(self, symbol):
        if symbol == "EUR":
            fake_data = {"start_at": "2018-01-01", "base": "EUR", "end_at": "2021-01-01","rates": {"2020-11-02": {"CAD": 1.5466, "HKD": 9.0327, "ISK": 163.5, "PHP": 56.407, "DKK": 7.4455, "HUF": 366.24, "CZK": 27.131, "AUD": 1.6533, "RON": 4.8674, "SEK": 10.3625, "IDR": 17064.82, "INR": 86.7555, "BRL": 6.6916, "RUB": 93.745, "HRK": 7.5695, "JPY": 121.93, "THB": 36.249, "CHF": 1.0695, "SGD": 1.5903, "PLN": 4.6018, "BGN": 1.9558, "TRY": 9.8332, "CNY": 7.7962, "NOK": 11.1128, "NZD": 1.7565, "ZAR": 18.8972, "USD": 1.1652, "MXN": 24.7327, "ILS": 3.9681, "GBP": 0.90053, "KRW": 1320.61, "MYR": 4.8443}, "2018-10-09": {"CAD": 1.4861, "HKD": 8.959, "ISK": 132.0, "PHP": 62.027, "DKK": 7.4592, "HUF": 325.29, "CZK": 25.805, "AUD": 1.6203, "RON": 4.6675, "SEK": 10.4445, "IDR": 17486.0, "INR": 85.084, "BRL": 4.3112, "RUB": 76.3635, "HRK": 7.42, "JPY": 129.45, "THB": 37.85, "CHF": 1.1381, "SGD": 1.5859, "PLN": 4.3155, "BGN": 1.9558, "TRY": 7.0183, "CNY": 7.9185, "NOK": 9.4915, "NZD": 1.7784, "ZAR": 17.1823, "USD": 1.1435, "MXN": 21.7228, "ILS": 4.1617, "GBP": 0.8768, "KRW": 1301.02, "MYR": 4.7541}}
        return api_response

def test_extractor()
    extractor = Extract()
    extractor.http_request_interface = FakeRequestInterface
    extractor.run_api_symbol()

