---
id: learning.zephyr-docs.api-source-reference.page-135
title: disk_access.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/disk__access_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第135章\_disk\_access.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/disk__access_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/disk__access_8h.html)。

## 135.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00024"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="adisk_8h_html"></a>
<a id="agroup__disk__access__interface_html_ga152d85821d73644fea7ffde27b7c953c"></a>
<a id="agroup__disk__access__interface_html_ga5152825bf2a70902e65dbc596a944a1b"></a>
<a id="agroup__disk__access__interface_html_gaa0495600320a71ea9e861fcf19da7184"></a>
<a id="agroup__disk__access__interface_html_gab666eac293bae609ee600ebb2b105373"></a>
<a id="agroup__disk__access__interface_html_gaba3fead8c0ce65945b440bf824fd4144"></a>
<a id="agroup__disk__access__interface_html_gac5348a854fe68a607672118c91346133"></a>
<a id="agroup__disk__access__interface_html_gafb8528762248a3dcbe7e4d0a9ee31890"></a>
<a id="agroup__disk__access__interface_html_ggab666eac293bae609ee600ebb2b105373ab78aa619814300a71ef45643e3d01ab6"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_STORAGE_DISK_ACCESS_H_
#define ZEPHYR_INCLUDE_STORAGE_DISK_ACCESS_H_



#include <zephyr/drivers/disk.h>

#ifdef __cplusplus
extern "C" {
#endif

int disk_access_init(const char *pdrv);

int disk_access_status(const char *pdrv);

int disk_access_read(const char *pdrv, uint8_t *data_buf,
                     uint32_t start_sector, uint32_t num_sector);

int disk_access_write(const char *pdrv, const uint8_t *data_buf,
                      uint32_t start_sector, uint32_t num_sector);

enum disk_access_erase_type {
        DISK_ACCESS_ERASE_PHYSICAL = 0,
};

int disk_access_erase(const char *pdrv, uint32_t start_sector, uint32_t num_sector,
                      enum disk_access_erase_type erase_type);

int disk_access_ioctl(const char *pdrv, uint8_t cmd, void *buff);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_STORAGE_DISK_ACCESS_H_ */
```

## 135.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 144 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_STORAGE_DISK_ACCESS_H_`。

## 135.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/disk__access_8h.html)
- [zephyr/drivers/disk.h](../peripheral_bus_storage_header_reference/P003_zephyr__drivers__disk.h_头文件参考.md)
- [disk_access_init](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gaba3fead8c0ce65945b440bf824fd4144)
- [disk_access_status](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gac5348a854fe68a607672118c91346133)
- [disk_access_read](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#ga5152825bf2a70902e65dbc596a944a1b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [disk_access_write](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gaa0495600320a71ea9e861fcf19da7184)
- [disk_access_erase_type](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gab666eac293bae609ee600ebb2b105373)
- [DISK_ACCESS_ERASE_PHYSICAL](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#ggab666eac293bae609ee600ebb2b105373ab78aa619814300a71ef45643e3d01ab6)
- [disk_access_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gafb8528762248a3dcbe7e4d0a9ee31890)
- [disk_access_ioctl](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#ga152d85821d73644fea7ffde27b7c953c)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [disk.h](../peripheral_bus_storage_header_reference/P003_zephyr__drivers__disk.h_头文件参考.md)

---

[上一章](P134_dis.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P136_sf32lb.h_源码浏览.md)
