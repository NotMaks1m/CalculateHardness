from math import pi

result = None
result_hb = None
result_hr = None
result_hk = None

def brinel() -> float:

    in_range_brinel_load = lambda x: 1 <= x <= 3000
    in_range_bribel_dia_ind = lambda x: x in [1, 2.5, 5, 10]

    load = float(input("Введите используемую нагрузку в кгс. F = "))

    while not in_range_brinel_load(load):
        load = float(input("Введите введите корректное значение нагрузки F (1..3000) в мм. F = "))

    diameter_ind = float(input("Введите диаметр индентора в мм. D = "))

    while not in_range_bribel_dia_ind(diameter_ind):
        diameter_ind = float(input("Введите корректный диаметр индентора в мм. D = "))

    in_range_diameter_imprint = lambda x: 0.24 * diameter_ind <= x <= 0.4 * diameter_ind

    diameter_imprint = float(input("Введите диаметр в мм. d = "))

    while not in_range_diameter_imprint(diameter_imprint):
        diameter_imprint = float(input("Введенный вами диаметр не корректен. Введите корректное значение в мм. d = "))


    hb = float(2 * load) / (pi * diameter_ind * (diameter_ind - (diameter_ind ** 2 - diameter_imprint ** 2) ** (1/2)))

    return hb

def rokvel() -> float:
    data_scales = lambda x: x in ["A", "B", "C"]
    constanta = 0.0

    scale = input("Введите использованную шкалу, где: А, B или C. Scale = ")
    while not data_scales(scale):
        scale = input("Введенная шкала не корретктна, введите шкалу повторно, где: А, B или C. Scale = ")

    height = float(input("Введите глубину отпечатка - "))

    if scale == "A" or scale == "C":
        constanta = 100.0

    elif scale == "B":
        constanta = 130.0


    hr = constanta - height / 0.002

    return hr

def vikers() -> float:

    load = float(input("Введите приложенную нагрузку - "))
    d1 = float(input("Введите величину первой диагонали - "))
    d2 = float(input("Введите величину второй диагонали - "))

    medium_diag = (d1 + d2) / 2

    hv = 0.1891 * (load / (pow(medium_diag, 2)))

    return hv

metods_data =lambda x : x in ["HB", "HR", "HV"]
method = input("Введите используемый метод определения твердости (HB, HR, HV) - ")

while not metods_data(method):
    method = input("Введенный вами метод не корректен. Введите повторно(HB, HR, HV) - ")

if method == "HB":
    result_hb = brinel()

    # HB -> HR
    if 200 <= result_hb <= 620:
        result_hr = 0.116 * result_hb - 13.2
    else:
        result_hr = None

    # HB -> HK
    if result_hb < 300:
        result_hk = result_hb
    elif 300 <= result_hb <= 650:
        result_hk = result_hb + 0.000012 * result_hb**2
    else:
        result_hk = None


elif method == "HR":
    result_hr = rokvel()

    # HR -> HB и HK
    if 20 < result_hr < 67:
        result_hb = (
            -102.84
            + 11.158 * result_hr
            - 0.05804 * result_hr**2
        )
        result_hk = (
            -140.94
            + 12.297 * result_hr
            - 0.05286 * result_hr**2
        )
    else:
        result_hb = None
        result_hk = None


elif method == "HV":
    result_hv = vikers()

    # HV -> HB
    if 300 <= result_hv <= 600:
        result_hb = (
            0.93 * result_hv
            + 0.00007 * result_hv**2
        )
    else:
        result_hb = None

    # HV -> HR
    if 240 <= result_hv <= 900:
        result_hr = (
            -0.00000009 * result_hv**3
            + 0.000104 * result_hv**2
            + 0.0385 * result_hv
            - 12
        )
    else:
        result_hr = None


print(f"Значение твердости по Бринеллю - {result_hb}")
print(f"Значение твердости по Роквеллу - {result_hr}")
print(f"Значение твердости по Виккерсу - {result_hk}")