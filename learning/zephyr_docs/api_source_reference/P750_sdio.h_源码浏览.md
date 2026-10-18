---
id: learning.zephyr-docs.api-source-reference.page-750
title: sdio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第750章\_sdio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h.html)。

## 750.1\_原始可见代码（Source Code）

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
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="adevice_8h_html"></a>
<a id="asd_8h_html"></a>
<a id="asd__spec_8h_html_a3a542344967c5c1912bde216559e7cd6"></a>
<a id="asdhc_8h_html"></a>
<a id="asdio_8h_html_a2ac93072041651597b9027156706f0d0"></a>
<a id="asdio_8h_html_a341c846c55adf512a4c3397f38d4bbf9"></a>
<a id="asdio_8h_html_a417829a0558b236465b70ff637a7ca38"></a>
<a id="asdio_8h_html_a55bd42c4d41643444890227ee6cbbfc5"></a>
<a id="asdio_8h_html_a5beb64599a265b117a42858e8087ae4a"></a>
<a id="asdio_8h_html_a68f75f10ea65cef4bc650b6e2ec4001d"></a>
<a id="asdio_8h_html_a8cf3af67ef909dd93cdfec29250d76c6"></a>
<a id="asdio_8h_html_a8fbc927607a156abc4c47bc551f72b11"></a>
<a id="asdio_8h_html_a9bfb4970e28830151d2a293475b98435"></a>
<a id="asdio_8h_html_aa3e60d2c643cd054af56cb44d193074b"></a>
<a id="asdio_8h_html_aae010680d9035116f503d7ddc1cf8590"></a>
<a id="asdio_8h_html_ab7ec658d92672acfa36d073191d0369f"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructsd__card_html"></a>
<a id="astructsdio__func_html"></a>

```c
/*
 * Copyright 2023 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_SD_SDIO_H_
#define ZEPHYR_INCLUDE_SD_SDIO_H_

#include <zephyr/device.h>
#include <zephyr/drivers/sdhc.h>
#include <zephyr/sd/sd.h>

#ifdef __cplusplus
extern "C" {
#endif

int sdio_init_func(struct sd_card *card, struct sdio_func *func,
                   enum sdio_func_num num);

int sdio_enable_func(struct sdio_func *func);

int sdio_set_block_size(struct sdio_func *func, uint16_t bsize);

int sdio_read_byte(struct sdio_func *func, uint32_t reg, uint8_t *val);

int sdio_write_byte(struct sdio_func *func, uint32_t reg, uint8_t write_val);

int sdio_rw_byte(struct sdio_func *func, uint32_t reg, uint8_t write_val,
                 uint8_t *read_val);

int sdio_read_fifo(struct sdio_func *func, uint32_t reg, uint8_t *data,
                   uint32_t len);

int sdio_write_fifo(struct sdio_func *func, uint32_t reg, uint8_t *data,
                    uint32_t len);

int sdio_read_blocks_fifo(struct sdio_func *func, uint32_t reg, uint8_t *data,
                          uint32_t blocks);

int sdio_write_blocks_fifo(struct sdio_func *func, uint32_t reg, uint8_t *data,
                           uint32_t blocks);

int sdio_read_addr(struct sdio_func *func, uint32_t reg, uint8_t *data,
                   uint32_t len);

int sdio_write_addr(struct sdio_func *func, uint32_t reg, uint8_t *data,
                    uint32_t len);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SD_SDMMC_H_ */
```

## 750.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 212 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SD_SDMMC_H_`。

## 750.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/sdhc.h](../peripheral_bus_storage_header_reference/P025_zephyr__drivers__sdhc.h_头文件参考.md)
- [zephyr/sd/sd.h](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md)
- [sdio_init_func](https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h.html#aae010680d9035116f503d7ddc1cf8590)
- [sd_card](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md)
- [sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)
- [sdio_func_num](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a3a542344967c5c1912bde216559e7cd6)
- [sdio_enable_func](https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h.html#aa3e60d2c643cd054af56cb44d193074b)
- [sdio_set_block_size](https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h.html#a417829a0558b236465b70ff637a7ca38)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [sdio_read_byte](https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h.html#a2ac93072041651597b9027156706f0d0)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sdio_write_byte](https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h.html#a9bfb4970e28830151d2a293475b98435)
- [sdio_rw_byte](https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h.html#a8fbc927607a156abc4c47bc551f72b11)
- [sdio_read_fifo](https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h.html#a8cf3af67ef909dd93cdfec29250d76c6)
- [sdio_write_fifo](https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h.html#a5beb64599a265b117a42858e8087ae4a)
- [sdio_read_blocks_fifo](https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h.html#ab7ec658d92672acfa36d073191d0369f)
- [sdio_write_blocks_fifo](https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h.html#a68f75f10ea65cef4bc650b6e2ec4001d)
- [sdio_read_addr](https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h.html#a341c846c55adf512a4c3397f38d4bbf9)
- [sdio_write_addr](https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h.html#a55bd42c4d41643444890227ee6cbbfc5)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [sd.h](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md)
- [sdhc.h](../peripheral_bus_storage_header_reference/P025_zephyr__drivers__sdhc.h_头文件参考.md)

---

[上一章](P749_scg_k4.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P751_sdmmc.h_源码浏览.md)
