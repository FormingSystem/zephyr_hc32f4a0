---
id: learning.zephyr-docs.api-source-reference.page-387
title: input_renesas_rx_ctsu.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__renesas__rx__ctsu_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第387章\_input\_renesas\_rx\_ctsu.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/input__renesas__rx__ctsu_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/input__renesas__rx__ctsu_8h.html)。

## 387.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="agroup__renesas__rx__ctsu__interface_html_ga531fdc46f91ffa0b0fdfc787c7a26145"></a>
<a id="astructdevice_html"></a>
<a id="astructrenesas__rx__ctsu__touch__cfg_html"></a>
<a id="astructrenesas__rx__ctsu__touch__cfg_html_aab1ae31d5380ba801401aa5f9e4a7ae0"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_INPUT_INPUT_RENESAS_RX_CTSU_H_
#define ZEPHYR_INCLUDE_INPUT_INPUT_RENESAS_RX_CTSU_H_


#include <rm_touch_qe.h>

#ifdef __cplusplus
extern "C" {
#endif

struct renesas_rx_ctsu_touch_cfg {
        struct st_touch_instance touch_instance;
};

__syscall int renesas_rx_ctsu_group_configure(const struct device *dev,
                                              const struct renesas_rx_ctsu_touch_cfg *cfg);

#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/input_renesas_rx_ctsu.h>


#endif /* ZEPHYR_INCLUDE_INPUT_INPUT_RENESAS_RX_CTSU_H_ */
```

## 387.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 59 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_INPUT_INPUT_RENESAS_RX_CTSU_H_`。

## 387.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/input__renesas__rx__ctsu_8h.html)
- [renesas_rx_ctsu_touch_cfg](../device_power_control_model_reference/P075_renesas_rx_ctsu_touch_cfg_结构体.md)
- [touch_instance](../device_power_control_model_reference/P075_renesas_rx_ctsu_touch_cfg_结构体.md#aab1ae31d5380ba801401aa5f9e4a7ae0)
- [renesas_rx_ctsu_group_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__rx__ctsu__interface.html#ga531fdc46f91ffa0b0fdfc787c7a26145)
- [device](../device_reference/P002_设备对象结构.md)
- [renesas_rx_ctsu_touch_cfg::touch_instance](../device_power_control_model_reference/P075_renesas_rx_ctsu_touch_cfg_结构体.md#aab1ae31d5380ba801401aa5f9e4a7ae0)

---

[上一章](P386_input_renesas_ra_ctsu.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P388_input_touch.h_源码浏览.md)
