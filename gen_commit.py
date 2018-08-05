# coding: utf-8
import os
import warnings

ROO_DIR = '/Users/robert/Documents/code/AliyunSVideo-product_v3.6.5'

KEY_WORD = 'COMMIT_ID'
VERSION_FILE_NAME = 'version.h'
LOG_FILE = 'log.txt'

dir_list = \
    {
        'alivc_framework': 'sources/native/modules/alivc_framework',
        # 'src': 'sources/native/src',
        # 'android': 'sources/android'
    }


output_list = {}

def write_version_file():
    print 'will be add in the furture...'

def add_commit_to_file(commit_id):
    b_update_commit_id = False
    if not os.path.exists(VERSION_FILE_NAME):
        write_version_file()

    try:
        input_file = open(VERSION_FILE_NAME, 'r')
        file_content_list = input_file.readlines()
        input_file.close()
    except:
        raise IOError("line {} is not exit !".format(VERSION_FILE_NAME))

    for i, line in enumerate(file_content_list):
        print 'i = {}, line = {}'.format(i, line)
        if KEY_WORD in line:
            index = line.find(KEY_WORD)
            file_content_list[i] = line.replace(line[index+len(KEY_WORD):], '   ' + commit_id)
            b_update_commit_id = True
            break

    if b_update_commit_id == False:
        warnings.warn("{} is not be update.".format(VERSION_FILE_NAME))

    output_file = open(VERSION_FILE_NAME, 'w')
    output_file.writelines(file_content_list)
    output_file.close()


def get_commit():
    print 'cqd, pwd = {}'.format(os.getcwd())
    cmd = 'git log -n 1 > ' + LOG_FILE
    os.system(cmd)

    commit_id_find = ''

    try:
        file_log = open(LOG_FILE, 'r')
        file_log_contents_list = file_log.readlines()
        file_log.close()
    except:
        raise IOError("line {} open failed !".format(LOG_FILE))

    for i, line in enumerate(file_log_contents_list):
        if 'commit' in line:
            commit_id_find = line.split(' ')[-1]
            break

    if commit_id_find == '':
        raise TypeError("commit id is found")
    else:
        return commit_id_find.strip()

def generate_version_file():
    for key, dir in dir_list.items():
        sub_dir = ROO_DIR + '/' + dir
        os.chdir(sub_dir)

        commit_id = get_commit()
        add_commit_to_file(commit_id)


def test():
    print "CQD, dir = {}".format(ROO_DIR)
    os.chdir(ROO_DIR)
    generate_version_file()


if __name__ == '__main__':
    test()
