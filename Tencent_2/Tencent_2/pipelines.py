import json

class Tencent2Pipeline(object):
    def __init__(self):
        self.f = open("tencent.json","w")
    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.f.write(content)
        return item

    def close_spider(self,spider):
        self.f.close()
