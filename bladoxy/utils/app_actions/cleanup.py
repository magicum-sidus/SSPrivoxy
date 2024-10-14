import bladoxy
import os

import subprocess
import re


def remove_files():
    WORKING_DIRECTORY = os.path.dirname(bladoxy.__file__)

    files_to_remove = [
        os.path.join(WORKING_DIRECTORY, 'modules','shadowsocks_config','shadowsocks.json'),
        os.path.join(WORKING_DIRECTORY, 'modules','shadowsocks_config','shadowsocks.log'),
        os.path.join(WORKING_DIRECTORY, 'modules','shadowsocks_config','shadowsocks.pid'),
        os.path.join(WORKING_DIRECTORY, 'nodes_profiles','all_nodes_info.json'),
        os.path.join(WORKING_DIRECTORY, 'nodes_profiles','name_index_mapping.json'),
        os.path.join(WORKING_DIRECTORY, 'nodes_profiles','nodes_profile.yaml')
    ]

    for file_path in files_to_remove:
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Removed {file_path}")
            else:
                print(f"File {file_path} does not exist")
        except Exception as e:
            print(f"Error removing {file_path}: {e}")




def user_confirmation(prompt):
    """获取用户确认输入 (y/n)"""
    while True:
        reply = input(f"{prompt} (y/n): ").strip().lower()
        if reply in ['y', 'n']:
            return reply == 'y'



def remove_bashrc_section(start_marker, end_marker):
    """从 ~/.bashrc 中删除某个标记的内容"""
    bashrc_path = os.path.expanduser("~/.bashrc")
    if os.path.exists(bashrc_path):
        with open(bashrc_path, 'r') as file:
            bashrc_content = file.read()

        if re.search(f"{start_marker}.*{end_marker}", bashrc_content, re.DOTALL):
            print(f"从 .bashrc 中删除 {start_marker} 和 {end_marker} 之间的内容")
            bashrc_content = re.sub(f"{start_marker}.*?{end_marker}", '', bashrc_content, flags=re.DOTALL)
            with open(bashrc_path, 'w') as file:
                file.write(bashrc_content)
        else:
            print(f"未找到 {start_marker} 标记的环境变量。")
    else:
        print(f"未找到 .bashrc 文件.")

def stop_processes_by_name(process_name):
    """通过进程名停止进程"""
    try:
        result = subprocess.run(['pgrep', '-f', process_name], capture_output=True, text=True)
        pids = result.stdout.strip().split("\n")
        for pid in pids:
            if pid:
                print(f"正在停止进程 {process_name}，PID: {pid}")
                os.kill(int(pid), 9)
    except Exception as e:
        print(f"停止进程 {process_name} 时出现错误: {e}")





def check_marker_in_bashrc(bashrc_path, start_marker):
    """检查 .bashrc 中是否包含指定的标记"""
    try:
        with open(bashrc_path, 'r') as file:
            content = file.read()
        return re.search(re.escape(start_marker), content) is not None
    except FileNotFoundError:
        print(f"未找到文件: {bashrc_path}")
        return False



# def finalize():
#     bashrc_path = os.path.expanduser("~/.bashrc")
#     START_MARKER_BLADOXY = "######## START MY_BLADOXY ########"
#     if check_marker_in_bashrc(bashrc_path, START_MARKER_BLADOXY):
#         # 获取用户确认
#         if user_confirmation("您想要运行 Bladoxy清理程序 吗"):
#             print("正在清理...")
#             # 删除文件
#             remove_files()

#             # 删除 proxy 和 Bladoxy 环境变量
#             START_MARKER_PROXY = "######## START MY_PROXY ########"
#             END_MARKER_PROXY = "######## END MY_PROXY ########"
#             START_MARKER_BLADOXY = "######## START MY_BLADOXY ########"
#             END_MARKER_BLADOXY = "######## END MY_BLADOXY ########"

#             remove_bashrc_section(START_MARKER_PROXY, END_MARKER_PROXY)
#             remove_bashrc_section(START_MARKER_BLADOXY, END_MARKER_BLADOXY)

#             # 停止 'privoxy' 和 'sslocal' 进程
#             stop_processes_by_name('privoxy')
#             stop_processes_by_name('sslocal')

#             print("成功停止进程")

#             print("Bladoxy 清理成功！")
#             print("请执行 source ~/.bashrc 刷新环境变量.")
#         else:
#             print("清理已取消")
#     else:
#         print("请先执行 bladoxy init 进行初始化！")

def finalize():
    # 获取用户确认
    if user_confirmation("您想要运行 Bladoxy清理程序 吗"):
        print("正在清理...")
        # 删除文件
        remove_files()

        # 删除 proxy 和 Bladoxy 环境变量
        START_MARKER_PROXY = "######## START MY_PROXY ########"
        END_MARKER_PROXY = "######## END MY_PROXY ########"
        START_MARKER_BLADOXY = "######## START MY_BLADOXY ########"
        END_MARKER_BLADOXY = "######## END MY_BLADOXY ########"

        remove_bashrc_section(START_MARKER_PROXY, END_MARKER_PROXY)
        remove_bashrc_section(START_MARKER_BLADOXY, END_MARKER_BLADOXY)

        # 停止 'privoxy' 和 'sslocal' 进程
        stop_processes_by_name('privoxy')
        stop_processes_by_name('sslocal')

        print("成功停止进程")

        print("Bladoxy 清理成功！")
        print("请执行 source ~/.bashrc 刷新环境变量.")
    else:
        print("清理已取消")


def finalizeToinit():
    print("正在清理Bladoxy...")
    # 删除文件
    remove_files()

    # 删除 proxy 和 Bladoxy 环境变量
    START_MARKER_PROXY = "######## START MY_PROXY ########"
    END_MARKER_PROXY = "######## END MY_PROXY ########"
    START_MARKER_BLADOXY = "######## START MY_BLADOXY ########"
    END_MARKER_BLADOXY = "######## END MY_BLADOXY ########"

    remove_bashrc_section(START_MARKER_PROXY, END_MARKER_PROXY)
    remove_bashrc_section(START_MARKER_BLADOXY, END_MARKER_BLADOXY)

    # 停止 'privoxy' 和 'sslocal' 进程
    stop_processes_by_name('privoxy')
    stop_processes_by_name('sslocal')

    print("成功停止进程")

    print("Bladoxy 清理成功！")
    print("请执行 source ~/.bashrc 刷新环境变量.")


if __name__ == "__main__":
    finalize()