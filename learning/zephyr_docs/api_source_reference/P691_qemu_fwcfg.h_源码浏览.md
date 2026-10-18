---
id: learning.zephyr-docs.api-source-reference.page-691
title: qemu_fwcfg.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/qemu__fwcfg_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第691章\_qemu\_fwcfg.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/qemu__fwcfg_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/qemu__fwcfg_8h.html)。

## 691.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__qemu__fwcfg__interface_html_ga118812a7348407f9e487c5f55e825ba2"></a>
<a id="agroup__qemu__fwcfg__interface_html_gaab1f00f9d5d9df199b9d35fbb6aa2f64"></a>
<a id="agroup__qemu__fwcfg__interface_html_gabfbe0c933d36f47b1e54c0e95c981eae"></a>
<a id="agroup__qemu__fwcfg__interface_html_gac3b30171a9b46599efa30324d44b58a8"></a>
<a id="agroup__qemu__fwcfg__interface_html_gae48557d89be4df85a9308c9a0c8b4454"></a>
<a id="aselect_8h_html_a7ffa34f8c9a12e7fd43f5ef65bf889fa"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Maximilian Zimmermann
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_QEMU_FWCFG_QEMU_FWCFG_H_
#define ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_QEMU_FWCFG_QEMU_FWCFG_H_


#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include <zephyr/device.h>
#include <zephyr/sys/util.h>

#define FW_CFG_SIGNATURE 0x0000
#define FW_CFG_ID        0x0001
#define FW_CFG_FILE_DIR  0x0019

#define FW_CFG_ID_F_TRADITIONAL BIT(0)
#define FW_CFG_ID_F_DMA         BIT(1)

int qemu_fwcfg_read_item(const struct device *dev, uint16_t key, void *buf, size_t len);

int qemu_fwcfg_write_item(const struct device *dev, uint16_t key, const void *buf, size_t len);

int qemu_fwcfg_get_features(const struct device *dev, uint32_t *features);

int qemu_fwcfg_find_file(const struct device *dev, const char *file, uint16_t *select,
                         uint32_t *size);

bool qemu_fwcfg_dma_supported(const struct device *dev);


#endif /* ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_QEMU_FWCFG_QEMU_FWCFG_H_ */
```

## 691.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Maximilian Zimmermann。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 113 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_QEMU_FWCFG_QEMU_FWCFG_H_`。

## 691.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/qemu__fwcfg_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [qemu_fwcfg_read_item](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html#ga118812a7348407f9e487c5f55e825ba2)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [qemu_fwcfg_write_item](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html#gae48557d89be4df85a9308c9a0c8b4454)
- [qemu_fwcfg_get_features](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html#gac3b30171a9b46599efa30324d44b58a8)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [qemu_fwcfg_find_file](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html#gabfbe0c933d36f47b1e54c0e95c981eae)
- [select](https://docs.zephyrproject.org/latest/doxygen/html/select_8h.html#a7ffa34f8c9a12e7fd43f5ef65bf889fa)
- [qemu_fwcfg_dma_supported](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html#gaab1f00f9d5d9df199b9d35fbb6aa2f64)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P690_qdec_stm32.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P692_quicklogic-eos-s3-pinctrl.h_源码浏览.md)
