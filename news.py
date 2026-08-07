import feedparser

feeds = {
    "Qiita": "https://qiita.com/popular-items/feed",
    "Zenn": "https://zenn.dev/feed",
    "はてブIT": "https://b.hatena.ne.jp/hotentry/it.rss",
    "GIGAZINE": "https://gigazine.net/news/rss_2.0/",
    "Hacker News": "https://news.ycombinator.com/rss",
    "OpenAI": "https://openai.com/news/rss.xml",
    "Hugging Face": "https://huggingface.co/blog/feed.xml",
    "AWS": "https://aws.amazon.com/jp/blogs/aws/feed/",
    "Azure": "https://azure.microsoft.com/en-us/blog/feed/",
    "Cloudflare": "https://blog.cloudflare.com/rss/",
    "NHK": "https://www3.nhk.or.jp/rss/news/cat0.xml",
    "BBC": "http://feeds.bbci.co.uk/news/world/rss.xml"
}

html = """
<html>
<head>
<meta charset="utf-8">
<title>Tech News</title>
</head>
<body>
<h1>今日の技術ニュース</h1>
"""

for name, url in feeds.items():

    feed = feedparser.parse(url)

    html += f"<h2>{name}</h2><ul>"

    for entry in feed.entries[:5]:

        html += (
            f'<li>{entry.link}</li>'
        )

    html += "</ul>"

html += "</body></html>"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
