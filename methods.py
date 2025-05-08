def adjust_price(price_in_euro):
    if price_in_euro < 20:
        price_in_euro *= 2.2
    elif 20 <= price_in_euro < 30:
        price_in_euro *= 2.0
    elif 30 <= price_in_euro < 50:
        price_in_euro *= 1.7
    elif 50 <= price_in_euro < 60:
        price_in_euro *= 1.6
    elif 60 <= price_in_euro < 70:
        price_in_euro *= 1.5
    else:
        price_in_euro *= 1.4

    return price_in_euro

def clean_and_filter_sizes_and_prices(sizes, prices):
    filtered_data = {}
    for size, price in zip(sizes, prices):
        if "Duftset" in size:
            continue

        if "ml" in size:
            size_value = size.split("ml")[0].strip()  # Извлекаем числовое значение
            size_cleaned = f"Объём:{size_value} мл"
        elif "stk" in size.lower():
            # Приводим к нижнему регистру для проверки, а затем используем оригинальную строку для split
            size_value = size.split("Stk")[0].strip()  # Извлекаем числовое значение
            size_cleaned = f"Объём:{size_value} шт"
        elif "g" in size:
            size_value = size.split("g")[0].strip()
            size_cleaned = f"Объём:{size_value} г"
        elif "Augen Make-up Set" in size:
            size_value = size.split("Augen Make-up Set")[0].strip()
            size_cleaned = f"Объём:{size_value} Набор для макияжа глаз"
        else:
            size_cleaned = size

        try:
            price = float(price)
        except ValueError:
            continue

        if size_cleaned not in filtered_data or price > filtered_data[size_cleaned]:
            filtered_data[size_cleaned] = price

    filtered_sizes = list(filtered_data.keys())
    filtered_prices = list(filtered_data.values())

    return filtered_sizes, filtered_prices

def process_brand_type(brand_type):
    translation_map = {
        "FLÜSSIGE FOUNDATION": "Тональная основа",
        "Lipgloss": "Блеск для губ",
        "Нighlighter": "Хайлайтер",
        "Wimpernserum": "Сыворотка для ресниц",
        "Concealer": "Консилер",
        "Flüssige Foundation": "Тональная основа",
        "Rouge": "Румяна",
        "Mascara": "Тушь для ресниц",
        "Gesichtscreme": "Крем для лица",
        "Cushion Foundation": "Тональная основа-кушон",
        "Stick Foundation": "Тональный стик",
        "Augenbrauenfarbe": "Краска для бровей",
        "Lidschatten": "Тени для век",
        "CC Cream": "СС-крем",
        "Lippenstift": "Помада",
        "Lippenbalsam": "Бальзам для губ",
        "Puderperlen": "Пудра",
        "Augenmake-up Entferner": "Средство для снятия макияжа с глаз",
        "Loser Puder": "Рассыпчатая пудра",
        "Creme Foundation": "Тональный крем",
        "Kompaktpuder": "Компактная пудра",
        "Fixing Spray": "Фиксирующий спрей",
        "Reinigungsöl": "Гидрофильное масло",
        "Reinigungsschaum": "Очищающая пенка для умывания",
        "Getönte Gesichtscreme": "Тональный крем для лица",
        "Fixierpuder": "Фиксирующая пудра",
        "Reinigungsgel": "Очищающий гель для умывания",
        "Kompakt Foundation": "Компактная основа",
        "Augenbrauenstift": "Карандаш для бровей",
        "Make-up Palette": "Палитра для макияжа",
        "Augen Make-up Set": "Набор для макияжа глаз",
        "Lippenöl": "Масло для губ",
        "Augenbrauengel": "Гель для бровей",
        "Lippenstift Hülle": "Футляр для помады",
        "Reinigungsmilch": "Очищающее молочко",
        "BB Cream": "ВВ-крем",
        "LOSER PUDER MIT NATÜRLICHEM FINISH": "Рассыпчатая пудра с натуральным финишем",
        "Primer": "Праймер",
        "Bronzingpuder": "Бронзирующая пудра",
        "Eyeliner": "Подводка для глаз",
        "Cremerouge": "Кремовые румяна",
        "Puder": "Пудра",
        "NAGELLACK – FARBE UND GLANZ MIT LANGEM HALT": "Лак для ногтей – стойкий цвет и блеск",
        "Bronzer": "Бронзер",
    }
    return translation_map.get(brand_type, "")