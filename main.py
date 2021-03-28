#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2021/3/28 5:48 下午
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : 1.py

import os
import json
import shutil


class BiVideo:
    def __init__(self, _path):
        self.path = _path
        self.title = ''

    def change(self, _path):
        """
        修改视频文件名
        1.获取新的视频文件名
        2.修改视频文件名
        :param _path: 子目录路径
        :return:
        """
        g = os.walk(_path)
        for path, dir_list, file_list in g:
            new_file_path = ''
            for file_name in file_list:
                file_path = os.path.join(path, file_name)
                if file_name.endswith('.info'):
                    new_file_name = self.get_new_name(file_path)
                    new_file_path = os.path.join(path, new_file_name)
                else:
                    continue

            for file_name in file_list:
                old_file_path = os.path.join(path, file_name)
                if file_name.endswith('.mp4'):
                    print(old_file_path)
                    print(new_file_path)
                    os.rename(old_file_path, new_file_path)
                else:
                    continue

    def get_new_name(self, path):
        """
        获取视频文件名
        :param path: info 文件的路径
        :return:
        """
        with open(path, encoding='utf8') as f:
            d = f.read()
        d = json.loads(d)
        name = d['PartName'] + '.mp4'
        if '/' in name:
            l1 = name.split('/')
            name = l1[-1]

        if self.title == '':
            self.title = d['Title']
            if '/' in self.title:
                l2 = name.split('/')
                self.title = l2[-1]
        return name

    def move(self, p):
        """
        将视频文件移动至上级目录
        :param p:
        :return:
        """
        g = os.walk(p)
        for path, dir_list, file_list in g:
            for file_name in file_list:
                if file_name.endswith('.mp4'):
                    file_path = os.path.join(path, file_name)
                    print('    file_path: ', file_path)
                    print('         path: ', path)
                    dir_path = os.path.abspath(os.path.dirname(path))
                    print('     dir_path: ', dir_path)
                    new_file_path = os.path.join(dir_path, file_name)
                    print('new_file_path: ', new_file_path)
                    shutil.move(file_path, new_file_path)

    def delete(self, p):
        """
        删除没用的文件和目录：.xml文件、.info文件、子目录
        （视频文件移动到上级目录之后，再删除没用的文件，最后再删除子目录）
        :param p: 子目录路径
        :return:
        """
        g = os.walk(p)
        for path, dir_list, file_list in g:
            for file_name in file_list:
                file_path = os.path.join(path, file_name)
                print(file_path)
                os.remove(file_path)
        os.removedirs(p)

    def rename(self):
        """
        修改视频目录名称
        :return:
        """
        p_dir = os.path.dirname(self.path)
        new_dir = os.path.join(p_dir, self.title)
        os.rename(self.path, new_dir)

    def run(self):
        """
        操作前请做好备份！！！
        操作前请做好备份！！！
        操作前请做好备份！！！
        遍历每个子目录执行下面操作：
        1.修改视频文件名
        2.将视频文件移动到上级目录
        3.删除无用的文件
        最后执行修改视频目录名称操作（顺序很重要）
        :param p:
        :return:
        """
        g = os.walk(self.path)
        for path, dir_list, file_list in g:
            dir_list.sort()
            for file_name in file_list:
                file_path = os.path.join(path, file_name)
                if file_name.endswith('.jpg') or file_name.endswith('.dvi'):
                    print('delete: ', file_path)
                    os.remove(file_path)

            for dir in dir_list:
                dir_path = os.path.join(path, dir)
                print(dir_path)

                self.change(dir_path)
                self.move(dir_path)
                self.delete(dir_path)

        self.rename()


if __name__ == '__main__':
    p = '/Users/mac/Movies/SpringCloud Netflix从入门到精通教程/415138740'
    b = BiVideo(p)
    b.run()
