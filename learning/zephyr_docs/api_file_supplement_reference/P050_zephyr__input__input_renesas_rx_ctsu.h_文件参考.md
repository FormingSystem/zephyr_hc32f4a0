---
id: learning.zephyr-docs.api-file-supplement-reference.page-50
title: zephyr__input__input_renesas_rx_ctsu.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__renesas__rx__ctsu_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_zephyr\_\_input\_\_input\_renesas\_rx\_ctsu.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/input__renesas__rx__ctsu_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RX电容触摸感应单元（CTSU）输入驱动的头文件。

<a id="details"></a>

```c
#include <rm_touch_qe.h>
#include <zephyr/syscalls/input_renesas_rx_ctsu.h>
```

查看此文件的源码。

Renesas RX电容触摸感应单元（CTSU）输入驱动的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 50.1\_数据结构（Data Structures）

<a id="r_renesas_5Frx_5Fctsu_5Ftouch_5Fcfg"></a>

```c
struct renesas_rx_ctsu_touch_cfg
```

相关声明：[renesas_rx_ctsu_touch_cfg](../device_power_control_model_reference/P075_renesas_rx_ctsu_touch_cfg_结构体.md)。

Renesas RX电容触摸感应单元（CTSU）设备的配置数据。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 50.2\_函数（Functions）

<a id="r_ga531fdc46f91ffa0b0fdfc787c7a26145"></a>

```c
int renesas_rx_ctsu_group_configure (const struct device *dev, const struct renesas_rx_ctsu_touch_cfg *cfg)
```

相关声明：[renesas_rx_ctsu_group_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__rx__ctsu__interface.html#ga531fdc46f91ffa0b0fdfc787c7a26145)、[device](../device_reference/P002_设备对象结构.md)、[renesas_rx_ctsu_touch_cfg](../device_power_control_model_reference/P075_renesas_rx_ctsu_touch_cfg_结构体.md)。

使用 Renesas QE 电容触摸工作流（QE for Capacitive Touch Workflow）生成的配置，配置电容触摸感应单元组设备（CTSU Group Device）。


## 50.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P387_input_renesas_rx_ctsu.h_源码浏览.md)
- [renesas_rx_ctsu_touch_cfg](../device_power_control_model_reference/P075_renesas_rx_ctsu_touch_cfg_结构体.md)
- [renesas_rx_ctsu_group_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__rx__ctsu__interface.html#ga531fdc46f91ffa0b0fdfc787c7a26145)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>

---

[上一章](P049_zephyr__input__input_renesas_ra_ctsu.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P051_zephyr__bluetooth__services__nus__inst.h_文件参考.md)
