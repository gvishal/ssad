"""Part B My Commands"""
import sys
import os
import stat
import pwd
import grp
import shutil
import time
import string

"""ls command"""

command = raw_input().strip()
command = command.split(' ')
# print command

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

def move(src, dst):
    """This code has been taken from shutil.py and modified for my use.
    Recursively move a file or directory to another location. This is
    similar to the Unix "mv" command.

    If the destination is a directory or a symlink to a directory, the source
    is moved inside the directory. The destination path "must not" already
    exist.

    If the destination already exists but is not a directory, it may be
    overwritten depending on os.rename() semantics.

    If the destination is on our current filesystem, then rename() is used.
    Otherwise, src is copied to the destination and then removed.
    A lot more could be done here...  A look at a mv.c shows a lot of
    the issues this implementation glosses over.

    """
    real_dst = dst
    if os.path.isdir(dst):
        if _samefile(src, dst):
            # We might be on a case insensitive filesystem,
            # perform the rename anyway.
            os.rename(src, dst)
            return

        real_dst = os.path.join(dst, _basename(src))
        if os.path.exists(real_dst):
            raise Error, "Destination path '%s' already exists" % real_dst
    try:
        os.rename(src, real_dst)
    except OSError:
        if os.path.isdir(src):
            if _destinsrc(src, dst):
                raise Error, "Cannot move a directory '%s' into itself '%s'." % (src, dst)
            copytree(src, real_dst, symlinks=True)
            rmtree(src)
        else:
            copy2(src, real_dst)
            os.unlink(src)

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
    option = check_option(command, 1)
    if option == '-r':
        src = check_src(command, 2)
        shutil.rmtree(src)
    elif not option:
        print "%s: missing file operand" % command[0]
    else:
        src = check_src(command, 1)
        if os.path.isdir(src):
            print "%s: cannot remove %s: Is a directory" % (command[0],command[1])
            sys.exit(0)
        os.remove(src)

elif command[0] == 'dirstr':
    pass