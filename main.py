import json
import os
from datetime import datetime, timezone
from url_analyzer import analyze_url


def save_log(entry, filename='logs.json'):
    history_list = []
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                history_list = json.load(f)
        except json.JSONDecodeError:
            history_list = []

    history_list.append(entry)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(history_list, f, ensure_ascii=False, indent=4)


def main():
    print('=' * 30)
    print('🛡️ URL Safety Checker')
    print('=' * 30)

    while True:
        url = input('Введите URL (или exit для выхода): ').strip()

        if url.lower() in ['exit', 'quit', 'выход']:
            print('До свидания!')
            break
        if not url:
            print('Адрес не должен быть пустым')
            continue

        print(f'\nАнализ безопасности ссылки: {url}')
        check = analyze_url(url)
        print(check)

        logs = {
            'url': url,
            'time': datetime.now().astimezone().isoformat(),
            'check': check,
        }
        save_log(logs)
        print(f"💾 Запись добавлена в logs.json")


if __name__ == '__main__':
    main()