---
id: learning.zephyr-docs.rtio-headers-reference.page-6
title: RTIO设备头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/iodev_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_RTIO设备头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/iodev_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P005_RTIO设备头文件参考.md)和[公共API](../rtio_core_reference/P001_RTIO公共接口.md)。

## 6.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00034"></a>
<a id="foldopen00049"></a>
<a id="foldopen00067"></a>
<a id="astructrtio__iodev__api_html"></a>
<a id="astructrtio__iodev__api_html_a6cd795906753535571ec1ecc0e0c430c"></a>
<a id="astructrtio__iodev__sqe_html"></a>
<a id="astructrtio__iodev_html"></a>
<a id="astructrtio__iodev_html_a6dfedbfb58356e0647e5c20632656977"></a>
<a id="astructrtio__iodev_html_af0f3a27fe8dea2161c9a73cb838bdeec"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * SPDX-FileCopyrightText: Copyright (c) 2022 Intel Corporation
<a id="l00003"></a> * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
<a id="l00004"></a> * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
<a id="l00005"></a> *
<a id="l00006"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00007"></a> */
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>#ifndef ZEPHYR_INCLUDE_RTIO_IODEV_H_
<a id="l00016"></a>#define ZEPHYR_INCLUDE_RTIO_IODEV_H_
<a id="l00017"></a>
<a id="l00018"></a>#ifdef __cplusplus
<a id="l00019"></a>extern "C" {
<a id="l00020"></a>#endif
<a id="l00021"></a>
<a id="l00026"></a>
<a id="l00028"></a>struct rtio_iodev_sqe;
<a id="l00030"></a>
<a id="l00034"></a>struct rtio_iodev_api {
<a id="l00043"></a>        void (*submit)(struct rtio_iodev_sqe *iodev_sqe);
<a id="l00044"></a>};
<a id="l00045"></a>
<a id="l00049"></a>struct rtio_iodev {
<a id="l00051"></a>        const struct rtio_iodev_api *api;
<a id="l00052"></a>
<a id="l00054"></a>        void *data;
<a id="l00055"></a>};
<a id="l00056"></a>
<a id="l00057"></a>/* Do not try and reformat the macros */
<a id="l00058"></a>/* clang-format off */
<a id="l00059"></a>
<a id="l00067"></a>#define RTIO_IODEV_DEFINE(name, iodev_api, iodev_data)          \
<a id="l00068"></a>        STRUCT_SECTION_ITERABLE(rtio_iodev, name) = {           \
<a id="l00069"></a>                .api = (iodev_api),                             \
<a id="l00070"></a>                .data = (iodev_data),                           \
<a id="l00071"></a>        }
<a id="l00072"></a>
<a id="l00073"></a>/* clang-format on */
<a id="l00074"></a>
<a id="l00078"></a>
<a id="l00079"></a>#ifdef __cplusplus
<a id="l00080"></a>}
<a id="l00081"></a>#endif
<a id="l00082"></a>
<a id="l00083"></a>#endif /* ZEPHYR_INCLUDE_RTIO_IODEV_H_ */
</code></pre>

## 6.2\_可见注释译文（Comments）

1. 版权属于Intel Corporation（2022年）以及Infineon Technologies AG或其关联公司（2026年）；保留全部权利，许可证为Apache-2.0。原始SPDX记录完整保留。

2. 不要尝试重新格式化这些宏。

3. 关闭clang-format自动格式化。

4. 恢复clang-format自动格式化。

5. 头文件保护宏`ZEPHYR_INCLUDE_RTIO_IODEV_H_`结束。

## 6.3\_原页符号提示（Symbol Descriptions）

### `rtio_iodev_api`

RTIO输入输出设备应实现的API。

定义位置（Definition）：iodev.h:34。

符号定位：[rtio_iodev_api](../rtio_model_reference/P004_RTIO设备函数表.md)。

### `rtio_iodev_api::submit`

```c
void(* submit)(struct rtio_iodev_sqe *iodev_sqe)
```

向IODEV提交一个待处理的条目。

定义位置（Definition）：iodev.h:43。

符号定位：[rtio_iodev_api::submit](../rtio_model_reference/P004_RTIO设备函数表.md#a6cd795906753535571ec1ecc0e0c430c)。

### `rtio_iodev_sqe`

输入输出设备提交队列条目（I/O Device Submission Queue Entry）。

定义位置（Definition）：sqe.h:403。

符号定位：[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

### `rtio_iodev`

具有请求提交函数表（Function Table）的输入输出设备（I/O Device）。

定义位置（Definition）：iodev.h:49。

符号定位：[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)。

### `rtio_iodev::api`

```c
const struct rtio_iodev_api * api
```

函数指针表（Function Pointer Table）。

定义位置（Definition）：iodev.h:51。

符号定位：[rtio_iodev::api](../rtio_model_reference/P003_RTIO输入输出设备.md#a6dfedbfb58356e0647e5c20632656977)。

### `rtio_iodev::data`

```c
void * data
```

与此IODEV关联的数据。

定义位置（Definition）：iodev.h:54。

符号定位：[rtio_iodev::data](../rtio_model_reference/P003_RTIO输入输出设备.md#af0f3a27fe8dea2161c9a73cb838bdeec)。

## 6.4\_源码跟踪译注

> 译注——IODEV提供api函数表与不透明data指针；RTIO_IODEV_DEFINE宏把它们静态保存到可迭代段（Iterable Section）中的对象，不深复制数据，也不启动硬件。data应按具体适配层要求指向有效对象，它不是固定类型的通用外设地址。

> 译注——IODEV是RTIO提交目标，不是Zephyr struct device的类型别名。执行器调用api->submit，驱动通常排队或启动硬件后尽快返回，再通过rtio_iodev_sqe_ok／err报告完成。void返回类型没有提供同步的操作结果。

> 译注——函数表及数据的生命周期必须覆盖异步请求，用户空间还需拥有相关IODEV访问权限。更多约定见[设备函数表](../rtio_model_reference/P004_RTIO设备函数表.md)和[核心接口](../rtio_core_reference/P001_RTIO公共接口.md)。

头文件相对定位：[include/zephyr/rtio/iodev.h](../../../include/zephyr/rtio/iodev.h)，关联实现／接口：[subsys/rtio/rtio_executor.c](../../../subsys/rtio/rtio_executor.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/rtio/iodev.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/rtio_executor.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 6.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P005_RTIO设备头文件参考.md)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [rtio_iodev_api](../rtio_model_reference/P004_RTIO设备函数表.md)
- [submit](../rtio_model_reference/P004_RTIO设备函数表.md#a6cd795906753535571ec1ecc0e0c430c)
- [rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)
- [api](../rtio_model_reference/P003_RTIO输入输出设备.md#a6dfedbfb58356e0647e5c20632656977)
- [data](../rtio_model_reference/P003_RTIO输入输出设备.md#af0f3a27fe8dea2161c9a73cb838bdeec)

---

[上一章](P005_RTIO设备头文件参考.md) · [返回大纲](大纲.md)
