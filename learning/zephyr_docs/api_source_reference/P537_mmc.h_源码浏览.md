---
id: learning.zephyr-docs.api-source-reference.page-537
title: mmc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mmc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第537章\_mmc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mmc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mmc_8h.html)。

## 537.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="ammc_8h_html_a2dd835a0e88299400cd1b4e1533a7b4b"></a>
<a id="ammc_8h_html_aa890ebd312875906583d56ddb1a03560"></a>
<a id="ammc_8h_html_acc996d4fba8673401816a7b41707b96f"></a>
<a id="asd_8h_html"></a>
<a id="asdhc_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructsd__card_html"></a>

```c
/*
 * Copyright 2022 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_SD_MMC_H_
#define ZEPHYR_INCLUDE_SD_MMC_H_

#include <zephyr/device.h>
#include <zephyr/drivers/sdhc.h>
#include <zephyr/sd/sd.h>

#ifdef __cplusplus
extern "C" {
#endif

int mmc_write_blocks(struct sd_card *card, const uint8_t *wbuf,
        uint32_t start_block, uint32_t num_blocks);

int mmc_read_blocks(struct sd_card *card, uint8_t *rbuf,
        uint32_t start_block, uint32_t num_blocks);

int mmc_ioctl(struct sd_card *card, uint8_t cmd, void *buf);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SD_MMC_H_ */
```

## 537.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 76 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SD_MMC_H_`。

## 537.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mmc_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/sdhc.h](../peripheral_bus_storage_header_reference/P025_zephyr__drivers__sdhc.h_头文件参考.md)
- [zephyr/sd/sd.h](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md)
- [mmc_write_blocks](https://docs.zephyrproject.org/latest/doxygen/html/mmc_8h.html#acc996d4fba8673401816a7b41707b96f)
- [sd_card](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mmc_read_blocks](https://docs.zephyrproject.org/latest/doxygen/html/mmc_8h.html#aa890ebd312875906583d56ddb1a03560)
- [mmc_ioctl](https://docs.zephyrproject.org/latest/doxygen/html/mmc_8h.html#a2dd835a0e88299400cd1b4e1533a7b4b)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [sd.h](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md)
- [sdhc.h](../peripheral_bus_storage_header_reference/P025_zephyr__drivers__sdhc.h_头文件参考.md)

---

[上一章](P536_mmc56x3.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P538_tty.h_源码浏览.md)
