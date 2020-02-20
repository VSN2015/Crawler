# Crawler
Đang lấy ảnh từ website ok 

Python 3.5

settings.py # trỏ đường dẫn ảnh về máy
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
# ITEM_PIPELINES = {'tutorial.pipelines.TutorialPipeline': 1}
IMAGES_STORE = '/home/vansang/Desktop/images'
