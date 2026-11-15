---
id: learning.zephyr-docs.api-source-reference.page-450
title: loopback_disk.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/loopback__disk_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第450章\_loopback\_disk.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/loopback__disk_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/loopback__disk_8h.html)。

## 450.1\_原始可见代码（Source Code）

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
<a id="l00011"></a>
<a id="l00012"></a>
<a id="foldopen00016"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="adisk_8h_html"></a>
<a id="afs__interface_8h_html"></a>
<a id="aloopback__disk_8h_html_a17a5f2ad1706fd7c3a8dcdbda2753b9c"></a>
<a id="aloopback__disk_8h_html_af3dca356272ee28c2865592d73d2563d"></a>
<a id="astructdisk__info_html"></a>
<a id="astructfs__file__t_html"></a>
<a id="astructloopback__disk__access_html"></a>
<a id="astructloopback__disk__access_html_a3e71921671d406734dd0125e3478abc2"></a>
<a id="astructloopback__disk__access_html_a958b6ae459ade33487c01fa5e60c31b3"></a>
<a id="astructloopback__disk__access_html_ae290129bd48f42de5acd28876af95c3e"></a>
<a id="astructloopback__disk__access_html_ae34d1252cb853510aef1c173bb540fb2"></a>

```c
/*
 * Copyright (c) 2023 Embedded Solutions GmbH
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_LOOPBACK_DISK_ACCESS_H_
#define ZEPHYR_INCLUDE_DRIVERS_LOOPBACK_DISK_ACCESS_H_

#include <zephyr/drivers/disk.h>
#include <zephyr/fs/fs_interface.h>

struct loopback_disk_access {
        struct disk_info info;
        const char *file_path;
        struct fs_file_t file;
        size_t num_sectors;
};

int loopback_disk_access_register(struct loopback_disk_access *ctx, const char *file_path,
                                  const char *disk_access_name);

int loopback_disk_access_unregister(struct loopback_disk_access *ctx);

#endif /* ZEPHYR_INCLUDE_DRIVERS_LOOPBACK_DISK_ACCESS_H_ */
```

## 450.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Embedded Solutions GmbH。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 57 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_LOOPBACK_DISK_ACCESS_H_`。

## 450.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/loopback__disk_8h.html)
- [zephyr/drivers/disk.h](../peripheral_bus_storage_header_reference/P003_zephyr__drivers__disk.h_头文件参考.md)
- [zephyr/fs/fs_interface.h](../storage/P078_文件系统接口头文件.md)
- [loopback_disk_access](../network_service_model_reference/P029_loopback_disk_access_结构体.md)
- [disk_info](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md)
- [info](../network_service_model_reference/P029_loopback_disk_access_结构体.md#a958b6ae459ade33487c01fa5e60c31b3)
- [file_path](../network_service_model_reference/P029_loopback_disk_access_结构体.md#ae34d1252cb853510aef1c173bb540fb2)
- [fs_file_t](../storage/P038_文件系统文件对象.md)
- [file](../network_service_model_reference/P029_loopback_disk_access_结构体.md#ae290129bd48f42de5acd28876af95c3e)
- [num_sectors](../network_service_model_reference/P029_loopback_disk_access_结构体.md#a3e71921671d406734dd0125e3478abc2)
- [loopback_disk_access_register](https://docs.zephyrproject.org/latest/doxygen/html/loopback__disk_8h.html#a17a5f2ad1706fd7c3a8dcdbda2753b9c)
- [loopback_disk_access_unregister](https://docs.zephyrproject.org/latest/doxygen/html/loopback__disk_8h.html#af3dca356272ee28c2865592d73d2563d)
- [disk.h](../peripheral_bus_storage_header_reference/P003_zephyr__drivers__disk.h_头文件参考.md)
- [fs_interface.h](../storage/P078_文件系统接口头文件.md)
- [loopback_disk_access::num_sectors](../network_service_model_reference/P029_loopback_disk_access_结构体.md#a3e71921671d406734dd0125e3478abc2)
- [loopback_disk_access::info](../network_service_model_reference/P029_loopback_disk_access_结构体.md#a958b6ae459ade33487c01fa5e60c31b3)
- [loopback_disk_access::file](../network_service_model_reference/P029_loopback_disk_access_结构体.md#ae290129bd48f42de5acd28876af95c3e)
- [loopback_disk_access::file_path](../network_service_model_reference/P029_loopback_disk_access_结构体.md#ae34d1252cb853510aef1c173bb540fb2)

---

[上一章](P449_loopback.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P451_lora.h_源码浏览.md)
