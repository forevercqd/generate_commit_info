# coding: utf-8
import os
import warnings

ROO_DIR = '/Users/robert/Documents/code/AliyunSVideo-product_v3.6.5'

VERSION_FILE_NAME = 'version.h'
dir_list = \
    {
        'alivc_framework': 'sources/native/modules/alivc_framework',
        # 'src': 'sources/native/src',
        # 'android': 'sources/android'
    }
key_word = 'COMMIT_ID'

output_list = {}

def write_version_file():
    print 'will be add in the furture...'

def add_commit_to_file():
    b_update_commit_id = False
    if not os.path.exists(VERSION_FILE_NAME):
        write_version_file()

    try:
        input_file = open(VERSION_FILE_NAME, 'r')
        file_content_list = input_file.readlines()
        input_file.close()
    except:
        raise IOError("line {} is not exit !".format(VERSION_FILE_NAME))

    for i, value in enumerate(file_content_list):
        print 'i = {}, value = {}'.format(i, value)
        if key_word in value:
            index = value.find(key_word)
            file_content_list[i] = value.replace(value[index+len(key_word):],' 123')
            b_update_commit_id = True

    if b_update_commit_id == False
        warnings.warn("{} is not be update.".format(VERSION_FILE_NAME))

    output_file = open(VERSION_FILE_NAME, 'w')
    output_file.writelines(file_content_list)
    output_file.close()




def get_commit():
    for key, dir in dir_list.items():
        sub_dir = ROO_DIR + '/' + dir
        os.chdir(sub_dir)
        os.system('git log -n 1 > log.txt')
        add_commit_to_file()


def test():
    print "CQD, dir = {}".format(ROO_DIR)
    os.chdir(ROO_DIR)
    get_commit()


if __name__ == '__main__':
    test()
