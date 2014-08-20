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
#print command

def check_path(path):
    return os.path.exists(path)

if command[0] == 'ls':
    try:
        if command[1] == '-l':
            """ls -l (path)"""
            """owner group others hardlinks owner group size month day time filename"""
            try:
                path = command[2]
                if os.path.exists(path):   
                    dir_list = os.listdir(path)
                    for i in xrange(len(dir_list)):
                        dir_list[i] = path + '/' + dir_list[i]
                else:
                    raise IOError("specified directory doesnt exist")
            except IndexError:
                dir_list = os.listdir(os.getcwd())
                for i in xrange(len(dir_list)):
                    dir_list[i] = os.getcwd() + '/' + dir_list[i]
            for file in dir_list:
                st = os.stat(file)
                details = ''
                if os.path.isdir(file):
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
                details += ' ' + str(st.st_nlink).rjust(2) + ' ' + pwd.getpwuid(st.st_uid).pw_name.ljust(4) + ' ' + grp.getgrgid(st.st_gid).gr_name.ljust(4)
                details += ' ' + str(st.st_size).rjust(6) + ' ' + time.strftime("%B %d %H:%M", time.gmtime(st.st_mtime)).ljust(18)
                details += ' ' + file.split('/')[-1]
                print details
        else:
            raise
    except:
        """ls (path)"""
        try:
            path = command[1]
            if os.path.exists(path):
                dir_list = os.listdir(path)
            else:
                raise IOError("specified directory doesnt exist")
        except IndexError:
            dir_list = os.listdir(os.getcwd())
        #col_width = max(len(file) for file in dir_list) + 2 
        for file in dir_list:
            print file
            # print string.ljust(file,col_width),

elif command[0] == 'cp':
    pass
