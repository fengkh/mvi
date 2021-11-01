import time


def log_time(func_name):
    with open("D:/_DATA/operation_log.txt", "a+") as f:
        f.write(func_name + str(time.asctime(time.localtime(time.time()))) + "\n")
        f.close()


def log_init():
    with open("D:/_DATA/operation_log.txt", "w") as f:
        f.write("MVI数据处理记录：\n")
        f.close()


def log_show():
    with open("D:/_DATA/operation_log.txt", "r") as f:
        data = f.readlines()
        print("\033[37;42m" + data + "\033[0m")
        f.close()


def log_data(log_info):
    with open("D:/_DATA/operation_log.txt", "a+") as f:
        if isinstance(log_info, list):
            for i in range(len(log_info)):
                f.write("\t\t" + log_info[i] + "\n")
        else:
            f.write("\t\t" + log_info + "\n")
        f.close()
