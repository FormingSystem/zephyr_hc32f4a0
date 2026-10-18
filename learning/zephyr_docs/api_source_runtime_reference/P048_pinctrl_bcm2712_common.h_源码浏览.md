---
id: learning.zephyr-docs.api-source-runtime-reference.page-48
title: pinctrl_bcm2712_common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__bcm2712__common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_pinctrl\_bcm2712\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__bcm2712__common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__bcm2712__common_8h.html)。

## 48.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="abcm2712-pinctrl_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>

```c
/*
 * Copyright (c) 2025 TOKITA Hiroshi
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_BCM2712_COMMON_H_
#define ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_BCM2712_COMMON_H_

#include <stdint.h>
#include <zephyr/dt-bindings/pinctrl/bcm2712-pinctrl.h>


/* Initialize one BCM2712 pinctrl entry from a devicetree property item. */
#define BRCM_BCM2712_PINCTRL_STATE_PIN_INIT(node_id, prop, idx)                                    \
        {                                                                                          \
                .unused = 0,                                                                       \
        }

/* Per-pin configuration container for BCM2712 pinctrl state data. */
struct brcm_bcm2712_pinctrl_pinconfig {
        uint8_t unused;
};

/* Apply one BCM2712 pin configuration entry. */
int brcm_bcm2712_pinctrl_configure_pin(const struct brcm_bcm2712_pinctrl_pinconfig *pin);


#endif /* ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_BCM2712_COMMON_H_ */
```

## 48.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 TOKITA Hiroshi。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 22 行

根据一个设备树属性项初始化一个 BCM2712 引脚控制（Pinctrl）条目。

### 注释 3：原第 28 行

BCM2712 引脚控制状态数据中逐引脚的配置容器（Per-pin configuration container）。

### 注释 4：原第 33 行

应用一个 BCM2712 引脚配置条目。

### 注释 5：原第 40 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_BCM2712_COMMON_H_`。

## 48.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__bcm2712__common_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/dt-bindings/pinctrl/bcm2712-pinctrl.h](https://docs.zephyrproject.org/latest/doxygen/html/bcm2712-pinctrl_8h.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bcm2712-pinctrl.h](https://docs.zephyrproject.org/latest/doxygen/html/bcm2712-pinctrl_8h.html)

---

[上一章](P047_parser_state.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P049_pinctrl_rp1_common.h_源码浏览.md)
