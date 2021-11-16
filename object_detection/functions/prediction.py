from PIL import Image, ImageDraw, ImageFont

import object_detection.api.baidu_api as bpi
import system_operation.file as fop
import system_operation.log as log


def get_one_predict(ori_path):
    json = bpi.predict(ori_path)
    if len(json['results']) is not 0:
        print(json)
        for i in range(len(json['results'])):
            img = Image.open(ori_path)
            results = json['results']
            height = results[i]['location']['height']
            left = results[i]['location']['left']
            top = results[i]['location']['top']
            width = results[i]['location']['width']
            left_top = (left, top)
            left_down = (left, top + height)
            right_top = (left + width, top)
            right_down = (left + width, top + height)
            area = width * height
            if area < 1024 * 1024 * 2 / 3:
                draw = ImageDraw.Draw(img)
                ttfront = ImageFont.truetype('simhei.ttf', 70)  # 字体大小
                draw.text((left, top), str(round(results[i]['score'], 2)), fill=(0, 25, 25), font=ttfront)
                draw.line(left_top + left_down, fill=128, width=10)
                draw.line(left_top + right_top, fill=128, width=10)
                draw.line(right_top + right_down, fill=128, width=10)
                draw.line(right_down + left_down, fill=128, width=10)
            img.save(ori_path)


def get_100_predict(ori_path):
    log.log_line()
    start = log.log_time("\tprediction:")
    file_paths = fop.get_dir_file(ori_path)
    num = len(file_paths) * 100
    log.log_data("Total numbers:" + num, 0)
    for i in range(len(file_paths)):
        files = fop.get_files_ab_path(file_paths[i])
        for j in range(len(files)):
            get_one_predict(files[j])
    end = log.log_time("\n\tprediction complete:")
    log.log_speed(start, end, num)
    log.log_line()
