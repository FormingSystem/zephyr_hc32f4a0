---
id: learning.zephyr-docs.api-source-configuration-reference.page-49
title: lwm2m_path.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__path_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_lwm2m\_path.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__path_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__path_8h.html)。

## 49.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00021"></a>
<a id="foldopen00045"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>

```c
/*
 * Copyright (c) 2020 Endian Technologies AB
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_LWM2M_PATH_H_
#define ZEPHYR_INCLUDE_NET_LWM2M_PATH_H_


#define LWM2M_PATH(...) \
        LWM2M_PATH_MACRO(__VA_ARGS__, LWM2M_PATH4, LWM2M_PATH3, \
                         LWM2M_PATH2, LWM2M_PATH1)(__VA_ARGS__)


/* Internal helper macros for the LWM2M_PATH macro */
#define LWM2M_PATH_VA_NUM_ARGS(...) \
        LWM2M_PATH_VA_NUM_ARGS_IMPL(__VA_ARGS__, 5, 4, 3, 2, 1)
#define LWM2M_PATH_VA_NUM_ARGS_IMPL(_1, _2, _3, _4, N, ...) N

#define LWM2M_PATH1(_x) #_x
#define LWM2M_PATH2(_x, _y) #_x "/" #_y
#define LWM2M_PATH3(_x, _y, _z) #_x "/" #_y "/" #_z
#define LWM2M_PATH4(_a, _x, _y, _z) #_a "/" #_x "/" #_y "/" #_z

#define LWM2M_PATH_MACRO(_1, _2, _3, _4, NAME, ...) NAME

#define LWM2M_OBJ(...) \
        GET_OBJ_MACRO(__VA_ARGS__, LWM2M_OBJ4, LWM2M_OBJ3, LWM2M_OBJ2, LWM2M_OBJ1)(__VA_ARGS__)

/* Internal helper macros for the LWM2M_OBJ macro */
#define GET_OBJ_MACRO(_1, _2, _3, _4, NAME, ...) NAME
#define LWM2M_OBJ1(oi) (struct lwm2m_obj_path) {.obj_id = oi, .level = 1}
#define LWM2M_OBJ2(oi, oii) (struct lwm2m_obj_path) {.obj_id = oi, .obj_inst_id = oii, .level = 2}
#define LWM2M_OBJ3(oi, oii, ri) (struct lwm2m_obj_path) \
        {.obj_id = oi, .obj_inst_id = oii, .res_id = ri, .level = 3}
#define LWM2M_OBJ4(oi, oii, ri, rii) (struct lwm2m_obj_path) \
        {.obj_id = oi, .obj_inst_id = oii, .res_id = ri, .res_inst_id = rii, .level = 4}


#endif /* ZEPHYR_INCLUDE_NET_LWM2M_PATH_H_ */
```

## 49.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Endian Technologies AB。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 51 行

供 `LWM2M_PATH` 宏使用的内部辅助宏。

### 注释 3：原第 87 行

供 `LWM2M_OBJ` 宏使用的内部辅助宏。

### 注释 4：原第 99 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_LWM2M_PATH_H_`。

## 49.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__path_8h.html)

---

[上一章](P048_time.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P050_math.h_源码浏览.md)
