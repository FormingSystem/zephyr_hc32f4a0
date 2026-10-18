---
id: learning.zephyr-docs.api-extension-topic-reference.page-8
title: 树莓派 Pico（Raspberry Pi Pico）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__rpi__pico.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_树莓派 Pico（Raspberry Pi Pico）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__rpi__pico.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 8.1\_文件（Files）

<a id="r_clock_5Fcontrol_5Frpi_5Fpico_2Eh"></a>

```c
file clock_control_rpi_pico.h
```

相关声明：[clock_control_rpi_pico.h](../api_file_supplement_reference/P018_zephyr__drivers__clock_control__clock_control_rpi_pico.h_文件参考.md)。

Raspberry Pi Pico设备的时钟控制定义（Clock Control Definitions）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.2\_函数（Functions）

<a id="r_ga1c14aa77af4ca5a6cb24929a09c4ec30"></a>

```c
int clock_control_rpi_pico_reconfigure (const struct device *dev)
```

相关声明：[clock_control_rpi_pico_reconfigure](#ga1c14aa77af4ca5a6cb24929a09c4ec30)、[device](../device_reference/P002_设备对象结构.md)。

重新应用设备树（Devicetree）声明的外部晶体振荡器／锁相环／时钟拓扑（XOSC / PLL / Clock Topology）。

## 8.3\_详细说明（Detailed Documentation）

<a id="ga1c14aa77af4ca5a6cb24929a09c4ec30"></a>

### `clock_control_rpi_pico_reconfigure()`

```c
int clock_control_rpi_pico_reconfigure ( const struct device * dev)
```

```c
#include <zephyr/drivers/clock_control/clock_control_rpi_pico.h>
```

重新应用设备树（Devicetree）声明的外部晶体振荡器／锁相环／时钟拓扑（XOSC / PLL / Clock Topology）。

当低功耗模式（Low-Power Mode）重置时钟后，用于恢复时钟（Clocks），例如 RP2350 的 `SUSPEND_TO_RAM` 模式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 时钟控制器设备（Clock-Controller Device）。 |

返回（Returns）：成功时为 0；若某个时钟无法配置，则为 `-EINVAL`。


## 8.4\_原页交叉引用（Cross References）

- [clock_control_rpi_pico.h](../api_file_supplement_reference/P018_zephyr__drivers__clock_control__clock_control_rpi_pico.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_瑞萨（Renesas）R-Car.md) · [返回大纲](大纲.md) · [下一章](P009_CY8CMBR3xxx API主题.md)
