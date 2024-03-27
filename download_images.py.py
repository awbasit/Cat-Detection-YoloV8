from simple_image_download import simple_image_download as simp

response = simp.simple_image_download
keyword = ["cats"]

for kw in keyword:
    response().download(kw, 200)