import re
import requests

def get_suggestion_words(keyword):
    url = f"https://www.baidu.com/su?wd={keyword}"

    response = requests.get(url)
    if response.status_code == 200:
        match = re.search(r's:\s*\[([^\]]+)\]', response.text)
        if match:
            suggestions = match.group(1)
            return suggestions

    return None

# 测试示例

