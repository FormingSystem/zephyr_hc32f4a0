---
id: learning.zephyr-docs.api-source-reference.page-452
title: emul.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lorawan_2emul_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第452章\_emul.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_2emul_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_2emul_8h.html)。

## 452.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="alorawan_2emul_8h_html_a665c46cfe16f6c894e44a3bfbbf235b7"></a>
<a id="alorawan_2emul_8h_html_abedb7884445ac1bb0eb0351a6c413761"></a>
<a id="alorawan_2emul_8h_html_ad3b92479562707f0819696a5de0baa41"></a>
<a id="alorawan_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>

```c
/*
 * Copyright (c) 2024 A Labs GmbH
 * Copyright (c) 2024 tado GmbH
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_LORAWAN_EMUL_H_
#define ZEPHYR_INCLUDE_LORAWAN_EMUL_H_

#include <stdbool.h>
#include <stdint.h>

#include <zephyr/lorawan/lorawan.h>

typedef void (*lorawan_uplink_cb_t)(uint8_t port, uint8_t len, const uint8_t *data);

void lorawan_emul_send_downlink(uint8_t port, bool data_pending, int16_t rssi, int8_t snr,
                                uint8_t len, const uint8_t *data);

void lorawan_emul_register_uplink_callback(lorawan_uplink_cb_t cb);

#endif /* ZEPHYR_INCLUDE_LORAWAN_EMUL_H_ */
```

## 452.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 A Labs GmbH。

版权（Copyright）：© 2024 tado GmbH。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 51 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_LORAWAN_EMUL_H_`。

## 452.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_2emul_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/lorawan/lorawan.h](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_8h.html)
- [lorawan_uplink_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_2emul_8h.html#ad3b92479562707f0819696a5de0baa41)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [lorawan_emul_send_downlink](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_2emul_8h.html#abedb7884445ac1bb0eb0351a6c413761)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [lorawan_emul_register_uplink_callback](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_2emul_8h.html#a665c46cfe16f6c894e44a3bfbbf235b7)
- [lorawan.h](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_8h.html)

---

[上一章](P451_lora.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P453_lorawan.h_源码浏览.md)
