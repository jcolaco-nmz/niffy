# coding=utf-8


def float_format(f, format='pt', decimal_places=2, pad_decimal=False):
    s = '%.0replacef'.replace('replace', str(int(decimal_places)))
    if format == 'pt':
        s = s % (f)
        s = s.replace('.', ',')
        if pad_decimal:
            s = s.rstrip('0')
            if s[-1] == ',':
                s = s[:-1]
        return s
    else:
        raise ValueError('Invalid format for float: ' + format)


CURRENCIES = {
    'EUR': {
        'symbol': u'€',
        'format': u'{amount} {symbol}',
        'active': False,
        'countries': ['PT', 'ES', 'FR', 'IT'],  # and more...
        'label': u'Euro',
    },
    'USD': {
        'symbol': u'$',
        'format': u'{symbol} {amount}',
        'active': True,
        'countries': ['US'],
        'label': u'Dolar Americano',
    },
    'GBP': {
        'symbol': u'£',
        'format': u'{symbol} {amount}',
        'active': True,
        'countries': ['GB'],
        'label': u'Libra Esterlina',
    },
    'BRL': {
        'symbol': u'R$',
        'format': u'{symbol} {amount}',
        'active': True,
        'countries': ['BR'],
        'label': u'Real Brasileiro',
    },
    'AOA': {
        'symbol': u'Kz',
        'format': u'{symbol} {amount}',
        'active': True,
        'countries': ['AO'],
        'label': u'Kwanza Angolano',
    },
    'CHF': {
        'symbol': u'CHF',
        'format': u'{symbol} {amount}',
        'active': True,
        'countries': ['CH'],
        'label': u'Franco Suíço',
    },
    'PLN': {
        'symbol': u'zł',
        'format': u'{symbol} {amount}',
        'active': False,
        'countries': ['PL'],
        'label': u'Zloty Polaco',
    },
    'MZN': {
        'symbol': u'MTn',
        'format': u'{symbol} {amount}',
        'active': True,
        'countries': ['MZ'],
        'label': u'Metical Moçambicano',
    },
    'RUB': {
        'symbol': u'руб',
        'format': u'{symbol} {amount}',
        'active': False,
        'countries': ['RU'],
        'label': u'Rublo Russo',
    },
}


def format(amount, code='EUR', decimal_places=2, pad_decimal=False, use_code=False, no_symbol=False):
    tpl = CURRENCIES[code]['format']
    symbol = code if use_code else CURRENCIES[code]['symbol']
    formatted = float_format(
        amount, decimal_places=decimal_places, pad_decimal=pad_decimal)
    if no_symbol:
        return formatted
    else:
        return tpl.format(amount=formatted, symbol=symbol)
