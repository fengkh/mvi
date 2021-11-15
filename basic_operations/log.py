import time

log_path = "D:\_mvi/log.txt"


def log_time(func_name):
    with open(log_path, "a+") as f:
        f.write(func_name + str(time.asctime(time.localtime(time.time()))) + "\n")
        f.close()
    return time.time()


def log_init():
    with open(log_path, "w") as f:
        f.write("MVI数据处理记录：\n")
        f.close()


def log_show():
    with open(log_path, "r") as f:
        data = f.readlines()
        print('\033[1;31;40m')
        for i in range(len(data)):
            print(data[i])
        f.close()


def log_data(log_info, flag):
    with open(log_path, "a+") as f:
        if isinstance(log_info, list):
            for i in range(len(log_info)):
                f.write(log_info[i] + "; ")
            f.write("\n")
        else:
            if flag == 0:
                f.write("\n\t" + log_info)
            if flag == 1:
                f.write(" " + log_info)
            if flag == -1:
                f.write("\n\t\t" + log_info)
        f.close()


def log_line():
    with open(log_path, "a+") as f:
        f.write("-----------------------------------------------------------------------\n")
        f.close()


def log_speed(start, end, num):
    with open(log_path, "a+") as f:
        f.write("\tTime = " + str(int((end - start) / 60)) + " min, Speed = " + str(
            int((end - start) / num)) + " s/img\n")
        f.close()
