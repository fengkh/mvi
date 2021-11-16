import system_operation.log as log
import object_detection.functions.prediction as pred
import object_detection.functions.preprocessing as proc

if __name__ == '__main__':
    log.log_data("完整流程测试-2", 1)
    # proc.compress("D:\_mvi\_ndpi", "D:\_mvi\_ndpi_", 8, 8)
    # ori_path和des_path应为存文件的文件夹路径，并非文件路路径
    # proc.normalize_size("D:\_mvi\_ndpi_", "D:\_mvi\_size", 10240)
    proc.crop("D:\_mvi\_ndpi", "D:\_mvi\_crop", 1024)
    pred.get_100_predict("D:\_mvi\_crop")
    proc.stitch("D:\_mvi\_crop", "D:\_mvi\_stitch")
