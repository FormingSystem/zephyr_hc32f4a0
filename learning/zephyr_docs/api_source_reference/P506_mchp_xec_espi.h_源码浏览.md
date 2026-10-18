---
id: learning.zephyr-docs.api-source-reference.page-506
title: mchp_xec_espi.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__xec__espi_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第506章\_mchp\_xec\_espi.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__xec__espi_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__xec__espi_8h.html)。

## 506.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="aespi_8h_html"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2026 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef INCLUDE_ZEPHYR_DRIVERS_ESPI_MCHP_XEC_ESPI_H_
#define INCLUDE_ZEPHYR_DRIVERS_ESPI_MCHP_XEC_ESPI_H_

#include <zephyr/drivers/espi.h>

#ifdef CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX

#define MCHP_XEC_MAX_MAILBOX_INDEX 32

#define MCHP_XEC_ESPI_PERIPHERAL_MAILBOX 0x100U

enum mchp_xec_espi_pc_mbox_cmd_id {
        MCHP_XEC_ESPI_PC_MBOX_CMD_ID_HOST_TO_EC = 0,
        MCHP_XEC_ESPI_PC_MBOX_CMD_ID_EC_TO_HOST,
        MCHP_XEC_ESPI_PC_MBOX_CMD_ID_SMI_SRC,
        MCHP_XEC_ESPI_PC_MBOX_CMD_ID_SMI_MASK,
        MCHP_XEC_ESPI_PC_MBOX_CMD_ID_MAX,
};

enum mchp_xec_espi_pc_mbox_isrc {
        MCHP_XEC_ESPI_PC_MBOX_ISRC_EC = 0,
        MCHP_XEC_ESPI_PC_MBOX_ISRC_SIRQ,
        MCHP_XEC_ESPI_PC_MBOX_ISRC_SIRQ_SMI,
        MCHP_XEC_ESPI_PC_MBOX_ISRC_MAX,
};

int mchp_xec_espi_pc_mailbox_get(const struct device *dev, uint8_t mbox_idx, uint8_t num_mboxes,
                                 uint8_t *dest);

int mchp_xec_espi_pc_mailbox_set(const struct device *dev, uint8_t mbox_idx, uint8_t num_mboxes,
                                 const uint8_t *src);

int mchp_xec_espi_pc_mailbox_get_all(const struct device *dev, uint32_t *dest);

int mchp_xec_espi_pc_mailbox_set_all(const struct device *dev, const uint32_t *src);

int mchp_xec_espi_pc_mailbox_cmd(const struct device *dev, enum mchp_xec_espi_pc_mbox_cmd_id cmd_id,
                                 uint8_t cmd);

int mchp_xec_espi_pc_mailbox_ictrl(const struct device *dev, enum mchp_xec_espi_pc_mbox_isrc id,
                                   uint8_t enable);

#endif /* CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX */

#endif /* INCLUDE_ZEPHYR_DRIVERS_ESPI_MCHP_XEC_ESPI_H_ */
```

## 506.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 119 行

条件编译配置（Configuration）标记：`CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX`。

### 注释 3：原第 121 行

头文件保护宏（Header guard）标记：`INCLUDE_ZEPHYR_DRIVERS_ESPI_MCHP_XEC_ESPI_H_`。

## 506.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__xec__espi_8h.html)
- [zephyr/drivers/espi.h](../peripheral_bus_storage_header_reference/P004_zephyr__drivers__espi.h_头文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [espi.h](../peripheral_bus_storage_header_reference/P004_zephyr__drivers__espi.h_头文件参考.md)

---

[上一章](P505_mchp_sam_pmc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P507_mchp_xec_pcr.h_源码浏览.md)
