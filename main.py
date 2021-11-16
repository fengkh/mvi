import object_detection.functions.prediction as pred
import object_detection.functions.preprocessing as proc
import system_operation.log as log


# 从病理切片到预测出结果的完整流程操作
def object_detection():
    # ori_path和des_path应为存文件的文件夹路径，并非文件路路径
    log.log_data("Object detection with Baidu-API", 1)
    proc.compress("D:\_mvi\_ndpi", "D:\_mvi\_ndpi_", 8, 8)
    proc.normalize_size("D:\_mvi\_ndpi_", "D:\_mvi\_size", 10240)
    proc.crop("D:\_mvi\_size", "D:\_mvi\_crop", 1024)
    pred.get_100_predict("D:\_mvi\_crop")
    proc.stitch("D:\_mvi\_crop", "D:\_mvi\_results")


if __name__ == '__main__':
    object_detection()
