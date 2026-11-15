---
id: learning.zephyr-docs.api-source-supplement-reference.page-38
title: cy8cmbr3xxx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cy8cmbr3xxx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_cy8cmbr3xxx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cy8cmbr3xxx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/cy8cmbr3xxx_8h.html)。

## 38.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="agroup__cy8cmbr3xxx__interface_html_ga0d8534cc7dc74a6b17cf30ecb4ac1bfd"></a>
<a id="agroup__cy8cmbr3xxx__interface_html_ga26da2ccc3ff92bc2c29021f66f184448"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructcy8cmbr3xxx__config__data_html"></a>
<a id="astructcy8cmbr3xxx__config__data_html_aadacd16ce180b86d1c80c8e56b5dc4da"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2025 Basalte bv
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_INPUT_CY8CMBR3XXX_H_
#define ZEPHYR_INCLUDE_INPUT_CY8CMBR3XXX_H_


#include <zephyr/types.h>

#define CY8CMBR3XXX_EZ_CLICK_CONFIG_SIZE 128

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

struct cy8cmbr3xxx_config_data {
        uint8_t data[CY8CMBR3XXX_EZ_CLICK_CONFIG_SIZE];
};

int cy8cmbr3xxx_configure(const struct device *dev,
                          const struct cy8cmbr3xxx_config_data *config_data);

#ifdef __cplusplus
}
#endif /* __cplusplus */


#endif /* ZEPHYR_INCLUDE_INPUT_CY8CMBR3XXX_H_ */
```

## 38.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Basalte bv。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 31 行

条件编译标记：`__cplusplus`。

### 注释 3：原第 55 行

条件编译标记：`__cplusplus`。

### 注释 4：原第 59 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_INPUT_CY8CMBR3XXX_H_`。

## 38.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/cy8cmbr3xxx_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [cy8cmbr3xxx_config_data](../sensor_navigation_model_reference/P007_cy8cmbr3xxx_config_data_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../sensor_navigation_model_reference/P007_cy8cmbr3xxx_config_data_结构体.md#aadacd16ce180b86d1c80c8e56b5dc4da)
- [CY8CMBR3XXX_EZ_CLICK_CONFIG_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__cy8cmbr3xxx__interface.html#ga0d8534cc7dc74a6b17cf30ecb4ac1bfd)
- [cy8cmbr3xxx_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__cy8cmbr3xxx__interface.html#ga26da2ccc3ff92bc2c29021f66f184448)
- [device](../device_reference/P002_设备对象结构.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [cy8cmbr3xxx_config_data::data](../sensor_navigation_model_reference/P007_cy8cmbr3xxx_config_data_结构体.md#aadacd16ce180b86d1c80c8e56b5dc4da)

---

[上一章](P037_cs40l5x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P039_dfu_cli.h_源码浏览.md)
