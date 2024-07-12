import requests
import re
import json

def re_domain(url):
    pattern_domain = r"https?://([^/]+)"
    match = re.search(pattern_domain, url)
    if match:
        domain = match.group(1)
        return domain
    else:
        return None

url = "https://ww0.lanzout.com/i2nzH245c6hc"  
password = "8888"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
}

response = requests.get(url, headers=headers)
url_pattern = re.compile(r"url\s*:\s*'(/ajaxm\.php\?file=\d+)'")
url_match = url_pattern.search(response.text).group(1)
skdklds_pattern = re.compile(r"var\s+skdklds\s*=\s*'([^']*)';")
skdklds_match = skdklds_pattern.search(response.text).group(1)

print(url_match, skdklds_match)

data = {
    'action': 'downprocess',
    'sign': skdklds_match,
    'p': password,
}
headers = {
    "Referer": url,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
}
response2 = requests.post(f"https://{re_domain(url)}{url_match}", headers=headers, data=data)
data = json.loads(response2.text)
dom = data['dom']
url = data['url']
full_url = dom + "/file/" + url

def download_file(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"文件已下载到: {filename}")
    else:
        print("下载失败，状态码：", response.status_code)

#重定向后的URL
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Microsoft Edge\";v=\"122\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "down_ip=1"
}
response3 = requests.get(full_url, headers=headers, allow_redirects=False)
redirect_url = response3.headers['Location']

