"""Part B My Commands"""

import os
import stat
import pwd
import grp
import time
import string

"""ls command"""

command = raw_input()
command = command.split(' ')

def check_path(path):
    return os.path.exists(path)

if command[0] == 'ls':
    if command[1] == '-l':
        """owner group others  owner group size month day time filename"""
        if command[2]:
            try:
                check_path(command[2])
            except:
            dir_list = os.listdir(command[2])

        else:
            dir_list = os.listdir(os.getcwd())
        for file in dir_list:
            filepath = os.getcwd() + '/' + file
            st = os.stat(filepath)
            details = ''
            if os.path.isdir(filepath):
                details += 'd'
            else:
                details += '-'
            if bool(st.st_mode & stat.S_IRUSR):
                details += 'r'
            else:
                details += '-'
            if bool(st.st_mode & stat.S_IWUSR):
                details += 'w'
            else:
                details += '-'
            if bool(st.st_mode & stat.S_IXUSR):
                details += 'x'
            else:
                details += '-'
            if bool(st.st_mode & stat.S_IRGRP):
                details += 'r'
            else:
                details += '-'
            if bool(st.st_mode & stat.S_IWGRP):
                details += 'w'
            else:
                details += '-'
            if bool(st.st_mode & stat.S_IXGRP):
                details += 'x'
            else:
                details += '-'
            if bool(st.st_mode & stat.S_IROTH):
                details += 'r'
            else:
                details += '-'
            if bool(st.st_mode & stat.S_IWOTH):
                details += 'w'
            else:
                details += '-'
            if bool(st.st_mode & stat.S_IXOTH):
                details += 'x'
            else:
                details += '-'
            details += ' ' + str(st.st_nlink) + ' ' + pwd.getpwuid(st.st_uid).pw_name + ' ' + grp.getgrgid(st.st_gid).gr_name
            details += ' ' + str(st.st_size).rjust(6) + ' ' + time.strftime("%B %d %H:%M", time.gmtime(st.st_mtime)) + ' ' + file
            print details
    else:
        dir_list = os.listdir(os.getcwd())
        # dir_list = os.listdir(command[1])
        col_width = max(len(file) for file in dir_list) + 2 
        for file in dir_list:
            print file
            # print string.ljust(file,col_width),

elif command[0] == 'cp':
    pass
