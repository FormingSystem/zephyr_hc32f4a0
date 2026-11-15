---
id: learning.zephyr-docs.flash-reference.page-22
title: EEPROM公共头文件源码
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/eeprom_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_EEPROM公共头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/eeprom_8h_source.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。原网页省略了用于生成接口文档的部分注释，因此原行号会跳跃；这里的“全部可见代码”不等于包含所有文档注释的原始文件。接口说明、参数与返回值见[对应头文件参考](P021_EEPROM公共头文件参考.md)及[本册大纲](大纲.md)。

## 22.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00043"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__eeprom__interface__backend_html_gaa12f5fdb02e73a608d5fdf128b14b4be"></a>
<a id="agroup__eeprom__interface__backend_html_gabbf1d1f66944f2297c68686a7db080ac"></a>
<a id="agroup__eeprom__interface__backend_html_gaee46582bce50cf50cc0293d006ca2ba8"></a>
<a id="agroup__eeprom__interface_html_ga1973e8982de88f53e49154dc73461e56"></a>
<a id="agroup__eeprom__interface_html_ga27a1f50af8916f9291dad4a63796a707"></a>
<a id="agroup__eeprom__interface_html_ga92b92c8fb721f1b94038a20443d46e52"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructeeprom__driver__api_html"></a>
<a id="astructeeprom__driver__api_html_a821724b35926882a1a732f1fb541b965"></a>
<a id="astructeeprom__driver__api_html_a82ef001ad60f95fabb37235a40974854"></a>
<a id="astructeeprom__driver__api_html_ade546770dc302ecb149a8631bbf5b5cb"></a>

```c
/*
 * Copyright (c) 2019 Vestas Wind Systems A/S
 *
 * Heavily based on drivers/flash.h which is:
 * Copyright (c) 2017 Nordic Semiconductor ASA
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_EEPROM_H_
#define ZEPHYR_INCLUDE_DRIVERS_EEPROM_H_


#include <zephyr/types.h>
#include <stddef.h>
#include <sys/types.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif


typedef int (*eeprom_api_read)(const struct device *dev, off_t offset,
                               void *data,
                               size_t len);

typedef int (*eeprom_api_write)(const struct device *dev, off_t offset,
                                const void *data, size_t len);

typedef size_t (*eeprom_api_size)(const struct device *dev);

__subsystem struct eeprom_driver_api {
        eeprom_api_read read;
        eeprom_api_write write;
        eeprom_api_size size;
};


__syscall int eeprom_read(const struct device *dev, off_t offset, void *data,
                          size_t len);

static inline int z_impl_eeprom_read(const struct device *dev, off_t offset,
                                     void *data, size_t len)
{
        return DEVICE_API_GET(eeprom, dev)->read(dev, offset, data, len);
}

__syscall int eeprom_write(const struct device *dev, off_t offset,
                           const void *data,
                           size_t len);

static inline int z_impl_eeprom_write(const struct device *dev, off_t offset,
                                      const void *data, size_t len)
{
        return DEVICE_API_GET(eeprom, dev)->write(dev, offset, data, len);
}

__syscall size_t eeprom_get_size(const struct device *dev);

static inline size_t z_impl_eeprom_get_size(const struct device *dev)
{
        return DEVICE_API_GET(eeprom, dev)->size(dev);
}

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/eeprom.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_EEPROM_H_ */
```

## 22.2\_可见注释译文（Comments）

1. 版权为2019年Vestas Wind Systems A/S；本文件大量基于drivers/flash.h，后者版权为2017年Nordic Semiconductor ASA及2016年Intel Corporation。许可证为Apache-2.0，全部署名原样保留。

2. 结束ZEPHYR_INCLUDE_DRIVERS_EEPROM_H_头文件包含保护（Header Include Guard）。

## 22.3\_源码跟踪译注

> 译注——系统调用转发：read、write、size三个驱动函数指针由eeprom_driver_api保存。公共系统调用（System Call）的z_impl_eeprom_*实现只取操作表并转发，不在这些内联包装中检查缓冲区或设备范围。实际参数和返回值语义见[EEPROM接口](../hardware/P040_EEPROM接口参考.md)。

仓库相对定位：[include/zephyr/drivers/eeprom.h](../../../include/zephyr/drivers/eeprom.h)；本次核对的[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/eeprom.h)摘要见[来源记录](../SOURCES.md)。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致；不能把这种一致性推广到以后滚动更新的main。

本批未构建、烧录、擦写或实板运行；代码阅读和文档核验不代表硬件操作通过。

## 22.4\_原页交叉引用（Cross References）

- [查看此文件参考说明](P021_EEPROM公共头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [eeprom_api_read](../hardware/P049_EEPROM驱动后端接口.md#gaa12f5fdb02e73a608d5fdf128b14b4be)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [eeprom_api_write](../hardware/P049_EEPROM驱动后端接口.md#gaee46582bce50cf50cc0293d006ca2ba8)
- [eeprom_api_size](../hardware/P049_EEPROM驱动后端接口.md#gabbf1d1f66944f2297c68686a7db080ac)
- [eeprom_driver_api](../hardware/P054_EEPROM驱动操作结构.md)
- [read](../hardware/P054_EEPROM驱动操作结构.md#a821724b35926882a1a732f1fb541b965)
- [write](../hardware/P054_EEPROM驱动操作结构.md#ade546770dc302ecb149a8631bbf5b5cb)
- [size](../hardware/P054_EEPROM驱动操作结构.md#a82ef001ad60f95fabb37235a40974854)
- [eeprom_read](../hardware/P040_EEPROM接口参考.md#ga92b92c8fb721f1b94038a20443d46e52)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [eeprom_write](../hardware/P040_EEPROM接口参考.md#ga1973e8982de88f53e49154dc73461e56)
- [eeprom_get_size](../hardware/P040_EEPROM接口参考.md#ga27a1f50af8916f9291dad4a63796a707)

---

[上一章](P021_EEPROM公共头文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_伪EEPROM头文件参考.md)
