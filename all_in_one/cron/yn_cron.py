from all_in_one import model
from all_in_one.cron.scraper import extract_news
import datetime

def add_news():
    news = extract_news()
    for info in news:
        url = info['url']
        result = model.News.objects(url__exact=url)
        if len(result) == 0:
            model.News(url=url, title=info['title']).save()


if __name__ == '__main__':
    print("start")
    print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    add_news()
    print("end")
