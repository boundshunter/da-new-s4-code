#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: su
# 动态导入
# 动态加载
import importlib
func = importlib.import_module('lib.aa')
print(func)
obj = func.ccc()
print(obj.name)