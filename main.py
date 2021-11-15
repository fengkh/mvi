import basic_operations.log as log
import functions.prediction as pred
import functions.preprocessing as proc

if __name__ == '__main__':
    log.log_data("完整流程测试-2", 1)
    proc.compress("D:\_mvi\_ndpi", "D:\_mvi\_ndpi_", 8, 8)
    # ori_path和des_path应为存文件的文件夹路径，并非文件路路径
    proc.normalize_size("D:\_mvi\_ndpi_", "D:\_mvi\_size", 10240)
    proc.crop("D:\_mvi\_size", "D:\_mvi\_crop", 1024)
    start = log.log_time("prediction")
    pred.get_100_predict("D:\_mvi\_crop")
    end = log.log_time("prediction complete")
    log.log_speed(start, end, 1)
    proc.stitch("D:\_mvi\_crop", "D:\_mvi\_stitch")
    # end = log.log_time()
    # log.log_speed(start, end, 1)
