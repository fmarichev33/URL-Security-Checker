from urllib.parse import urlparse
import ipaddress


def analyze_url(url: str):
    risks = []
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    host = parsed_url.hostname

    # Правило 1: наличие @ в домене
    if '@' in parsed_url.netloc:
        risks.append('Подозрительно: обнаружен символ @ в доменной части. Возможна маскировка хоста')
    # Правило 2: использование IP-адреса
    if host:
        try:
            ipaddress.ip_address(host)
            risks.append('Вместо доменного имени используется IP-адрес')
        except ValueError:
            pass
    #Правило 3: большая длина адреса
    if len(url) > 75:
        risks.append('Слишком большая длина адреса')
    # Правило 4: наличие подозрительных слов
    sus_words = ['login', 'secure', 'verify',
                 'update', 'account', 'banking']
    for word in sus_words:
        if word in url.lower():
            risks.append(f'Обнаружено подозрительное ключевое слово: {word}')
            break
    if len(risks) > 0:
        return risks
    else:
        return "✅ Ссылка безопасна"