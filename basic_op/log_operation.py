import time


def log_time(func_name):
    with open("D:/_DATA/operation_log.txt", "a+") as f:
        f.write(func_name + str(time.asctime(time.localtime(time.time()))) + "\n")
        f.close()
    return time.time()


def log_init():
    with open("D:/_DATA/operation_log.txt", "w") as f:
        f.write("MVI数据处理记录：\n")
        f.close()


def log_show():
    with open("D:/_DATA/operation_log.txt", "r") as f:
        data = f.readlines()
        print('\033[1;31;40m')
        for i in range(len(data)):
            print(data[i])
        f.close()


def log_data(log_info):
    with open("D:/_DATA/operation_log.txt", "a+") as f:
        f.write("\t\t")
        if isinstance(log_info, list):
            for i in range(len(log_info)):
                f.write(log_info[i] + "; ")
            f.write("\n")
        else:
            f.write(log_info + "\n")
        f.close()


def log_line():
    with open("D:/_DATA/operation_log.txt", "a+") as f:
        f.write("-----------------------------------------------------------------------\n")
        f.close()


def log_speed(start, end, num):
    with open("D:/_DATA/operation_log.txt", "a+") as f:
        f.write("\tTime = " + str(int((end - start) / 60)) + " min, Speed = " + str(
            int((end - start) / num)) + " s/img\n")
        f.close()
