"""Part B My Commands"""
import sys
import os
import stat
import pwd
import grp
import shutil
import time
import string

def check_path(command, pos):
    """Returns path if it exists or error or False if it is not specified"""
    try:
        path = command[pos]
        if os.path.exists(path):
            return path
        else:
            print "specified directory doesnt exist"
            sys.exit(0)
    except IndexError:
        path = False
        return path

def check_src(command, pos):
    try:
        src = command[pos]
        return src
    except:
        print "%s: missing file operand" % command[0]
        sys.exit(0)

def check_dest(command, pos):
    try:
        dest = command[pos]
        return dest
    except:
        print "%s: missing destination file operand" % command[0]
        sys.exit(0)

def check_option(command, pos):
    try:
        option = command[pos]
    except IndexError:
        option = False
    return option

def list_files(command, startpath):
    try:
        if not os.path.isdir(startpath):
            raise
        pre = '#--------------------'
        post = '-------------------#'
        i = 0 
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 2 *(level)
            i += 1
            if indent:
                print '{}{}'.format(indent, '|')
            print '{}{} Folder name: {}/{}'.format(indent, pre, os.path.basename(root), post)
            subindent = ' ' * 2 *(level + 1)
            if not dirs and not files:
                print '\n{}{}'.format(subindent*5, '(EMPTY FOLDER)')
            for f in files:
                print '{}{}'.format(subindent, '|')
                try:
                    path = os.path.join(root, f)
                    if os.path.exists(path):
                        complete_path = path
                except:
                    complete_path = os.path.join(os.getcwd(), path)
                st = os.stat(complete_path)
                details = f + str(st.st_size).rjust(6) + ' bytes ' + time.strftime("%B %d %H:%M", time.gmtime(st.st_mtime)).ljust(16)
                #print '{}#-{}'.format(subindent, f)
                print '{}#-{}'.format(subindent, details)
    except:
        print "%s: directory does not exist" % command[0]
        sys.exit(0)

def file_details(command, path, root=None):
    """Returns file details in ls -l format"""
    try:
        try:
            if os.path.exists(path):
                complete_path = path
        except:
            try:
                path = os.path.join(root, path)
                if os.path.exists(path):
                    complete_path = path
                else:
                    complete_path = os.path.join(os.getcwd(), path)
            except:
                print "Invalid path specified"
                sys.exit(0)
        st = os.stat(complete_path)
        details = ''
        if os.path.isdir(complete_path):
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
        #improve the following spaghetti code
        details += ' ' + str(st.st_nlink).rjust(2) + ' ' + pwd.getpwuid(st.st_uid).pw_name.ljust(4) + ' ' + grp.getgrgid(st.st_gid).gr_name.ljust(4)
        details += ' ' + str(st.st_size).rjust(6) + ' ' + time.strftime("%B %d %H:%M", time.gmtime(st.st_mtime)).ljust(18)
        details += ' ' + path.split('/')[-1]
        return details
    except:
        print "Path does not exist"

def main():
    try:
        command = raw_input().strip()
        command = command.split()
    except:
        print "Enter correct command"
        sys.exit(0)
    if command[0] == 'ls':
        """ls command"""
        try:
            if command[1] == '-l':
                """ls -l (path)"""
                """owner group others hardlinks owner group size month day time filename"""
                try:
                    path = command[2]
                    try:
                        if os.path.exists(path):
                            dir_list = os.listdir(path)
                            for i in xrange(len(dir_list)):
                                dir_list[i] = os.path.join(path, dir_list[i])
                    except:
                        print "%s: specified directory doesnt exist" % command[0]
                        sys.exit(0)
                except IndexError:
                    dir_list = os.listdir(os.getcwd())
                    for i in xrange(len(dir_list)):
                        dir_list[i] = os.path.join(os.getcwd(), dir_list[i])
                for file in dir_list:
                    details = file_details(command, file)
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
                    print "%s: specified directory doesnt exist" % command[0]
                    sys.exit(0)
            except IndexError:
                dir_list = os.listdir(os.getcwd())
            #col_width = max(len(file) for file in dir_list) + 2 
            for file in dir_list:
                print file
                # print string.ljust(file,col_width),

    elif command[0] == 'cp':
        """cp command"""
        option = check_option(command, 1)
        if option == '-r':
            src = check_src(command, 2)
            dest = check_dest(command, 3)
            shutil.copytree(src, dest)
        elif not option:
            print "%s: missing file operand" % command[0]
            sys.exit(0)
        else:
            src = check_src(command, 1)
            if os.path.isdir(src):
                print "cp: omitting directory %s" % src
                sys.exit(0)
            dest = check_dest(command, 2)
            shutil.copy(src, dest)

    elif command[0] == 'mv':
        """move and rename"""
        src = check_src(command, 1)
        dest = check_dest(command, 2)
        try:
            shutil.move(src, dest)
        except shutil.Error as e:
            print "mv: %s" % e

    elif command[0] == 'rm':
        """rm command"""
        option = check_option(command, 1)
        if option == '-r':
            src = check_src(command, 2)
            shutil.rmtree(src)
        elif not option:
            print "%s: missing file operand" % command[0]
        else:
            src = check_src(command, 1)
            try:
                os.remove(src)
            except OSError:
                print "%s: cannot remove '%s': Is a directory" % (command[0],command[1])
                sys.exit(0)

    elif command[0] == 'dirstr':
        """dirstr command"""
        try:
            startpath = command[1]
        except:
            startpath = os.getcwd()
        list_files(command, startpath)

    #Bonus commands
    elif command[0] == 'pwd':
        print os.getcwd()

    elif command[0] == 'mkdir':
        try:
            d = command[1]
            if not os.path.exists(d):
                os.makedirs(d)
            else:
                print "%s: cannot create directory '%s': File exists" % (command[0],d)
        except IndexError:
            print "%s: missing operand" % command[0]

if __name__ == '__main__':
    main()