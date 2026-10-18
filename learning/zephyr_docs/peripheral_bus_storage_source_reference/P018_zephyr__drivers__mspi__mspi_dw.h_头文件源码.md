---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-18
title: zephyr__drivers__mspi__mspi_dw.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mspi__dw_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr__drivers__mspi__mspi_dw.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mspi__dw_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P018_zephyr__drivers__mspi__mspi_dw.h_头文件参考.md)。

## 18.1\_原始可见代码（Source Code）

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
<a id="l00013"></a>
<a id="foldopen00018"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructmspi__dw__timing__cfg_html"></a>
<a id="astructmspi__dw__timing__cfg_html_a2614dad76fd70ee93e0442b0f45a72ee"></a>

```c
/*
 * Copyright (c) 2025 Tenstorrent AI ULC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_MSPI_DW_H_
#define ZEPHYR_INCLUDE_DRIVERS_MSPI_DW_H_

#ifdef __cplusplus
extern "C" {
#endif

struct mspi_dw_timing_cfg {
        uint32_t rx_sample_dly; /* RX sample delay, written to RX_SAMPLE_DLY register */
};

/* Configure RX_SAMPLE_DLY register for MSPI DW SSI */
#define MSPI_DW_RX_TIMING_CFG BIT(0)

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_MSPI_DW_H_ */
```

## 18.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Tenstorrent AI ULC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 19 行

接收采样延迟（RX sample delay），写入 `RX_SAMPLE_DLY` 寄存器。

### 注释 3：原第 22 行

为 MSPI DW SSI 配置 `RX_SAMPLE_DLY` 寄存器。

### 注释 4：原第 29 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MSPI_DW_H_`。

## 18.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P018_zephyr__drivers__mspi__mspi_dw.h_头文件参考.md)
- [mspi_dw_timing_cfg](../peripheral_bus_storage_model_reference/P044_mspi_dw_timing_cfg_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [rx_sample_dly](../peripheral_bus_storage_model_reference/P044_mspi_dw_timing_cfg_结构体.md#a2614dad76fd70ee93e0442b0f45a72ee)
- [mspi_dw_timing_cfg::rx_sample_dly](../peripheral_bus_storage_model_reference/P044_mspi_dw_timing_cfg_结构体.md#a2614dad76fd70ee93e0442b0f45a72ee)

---

[上一章](P017_zephyr__drivers__mspi.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__drivers__mux.h_头文件源码.md)
