---
id: learning.zephyr-docs.api-update-memory-topic-reference.page-3
title: 瑞萨（Renesas）SmartBond
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_瑞萨（Renesas）SmartBond

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 3.1\_文件（Files）

<a id="r_smartbond_5Fclock_5Fcontrol_2Eh"></a>

```c
file smartbond_clock_control.h
```

相关声明：[smartbond_clock_control.h](../api_file_supplement_reference/P114_zephyr__drivers__clock_control__smartbond_clock_control.h_文件参考.md)。

Renesas SmartBond设备的时钟控制定义（Clock Control Definitions）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.2\_枚举（Enumerations）

<a id="r_ga951aa7e2fb999ade4f6c404ce9570a83"></a>

```c
enum smartbond_clock { SMARTBOND_CLK_NONE , SMARTBOND_CLK_RC32K , SMARTBOND_CLK_RCX , SMARTBOND_CLK_XTAL32K , SMARTBOND_CLK_RC32M , SMARTBOND_CLK_XTAL32M , SMARTBOND_CLK_PLL96M , SMARTBOND_CLK_USB , SMARTBOND_CLK_DIVN_32M , SMARTBOND_CLK_HCLK , SMARTBOND_CLK_LP_CLK , SMARTBOND_CLK_SYS_CLK }
```

相关声明：[smartbond_clock](#ga951aa7e2fb999ade4f6c404ce9570a83)、[SMARTBOND_CLK_NONE](#gga951aa7e2fb999ade4f6c404ce9570a83a89ea767c0399e9325736b661b7c5d298)、[SMARTBOND_CLK_RC32K](#gga951aa7e2fb999ade4f6c404ce9570a83a16fb9df64c8f3921272f0fe93f9ed6c7)、[SMARTBOND_CLK_RCX](#gga951aa7e2fb999ade4f6c404ce9570a83aa4fb1618d90efc7580dd3f89e7ef9036)、[SMARTBOND_CLK_XTAL32K](#gga951aa7e2fb999ade4f6c404ce9570a83ae1a24769cf389312fbf1554cc4404c99)、[SMARTBOND_CLK_RC32M](#gga951aa7e2fb999ade4f6c404ce9570a83a683e5cf10c55857edb78c547dd02a7e3)、[SMARTBOND_CLK_XTAL32M](#gga951aa7e2fb999ade4f6c404ce9570a83a372e528a85ba9f8a7c2c1b90c54f77ab)、[SMARTBOND_CLK_PLL96M](#gga951aa7e2fb999ade4f6c404ce9570a83a1ac03107185f01fbcd9f12733a1d89b3)、[SMARTBOND_CLK_USB](#gga951aa7e2fb999ade4f6c404ce9570a83a556a67233b4c5f4a43bdc483b0548bbb)、[SMARTBOND_CLK_DIVN_32M](#gga951aa7e2fb999ade4f6c404ce9570a83a21bab67b1cf51a9784fbcdea997134fe)、[SMARTBOND_CLK_HCLK](#gga951aa7e2fb999ade4f6c404ce9570a83afde13daa39fdbe4048ba2f1459027258)、[SMARTBOND_CLK_LP_CLK](#gga951aa7e2fb999ade4f6c404ce9570a83a6abb5210f065753cbfa1fbd74d7562a7)、[SMARTBOND_CLK_SYS_CLK](#gga951aa7e2fb999ade4f6c404ce9570a83ad10e9e43712650502a7f92479071c297)。

SmartBond 振荡器（Oscillators）和时钟（Clocks）。

## 3.3\_详细说明（Detailed Documentation）

<a id="ga951aa7e2fb999ade4f6c404ce9570a83"></a>

### `smartbond_clock`

```c
enum smartbond_clock
```

```c
#include <zephyr/drivers/clock_control/smartbond_clock_control.h>
```

SmartBond 振荡器（Oscillators）和时钟（Clocks）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SMARTBOND_CLK_NONE` | 不代表时钟，仅用于错误情况（Error Case）。 |
| `SMARTBOND_CLK_RC32K` | 32 kHz RC 振荡器（Oscillator）。 |
| `SMARTBOND_CLK_RCX` | RCX 低功耗振荡器（Low-power Oscillator）。 |
| `SMARTBOND_CLK_XTAL32K` | 32 kHz 晶体振荡器（Crystal Oscillator）。 |
| `SMARTBOND_CLK_RC32M` | 32 MHz RC 振荡器（Oscillator）。 |
| `SMARTBOND_CLK_XTAL32M` | 32 MHz 晶体振荡器（Crystal Oscillator）。 |
| `SMARTBOND_CLK_PLL96M` | 96 MHz 锁相环（PLL）。 |
| `SMARTBOND_CLK_USB` | USB 时钟（Clock）。 |
| `SMARTBOND_CLK_DIVN_32M` | 分频后的 32 MHz 时钟（Divided Clock）。 |
| `SMARTBOND_CLK_HCLK` | 高级高性能总线（AHB）时钟。 |
| `SMARTBOND_CLK_LP_CLK` | 低功耗时钟（Low-power Clock）。 |
| `SMARTBOND_CLK_SYS_CLK` | 系统时钟（System Clock）。 |


## 3.4\_原页交叉引用（Cross References）

- [smartbond_clock_control.h](../api_file_supplement_reference/P114_zephyr__drivers__clock_control__smartbond_clock_control.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga951aa7e2fb999ade4f6c404ce9570a83a89ea767c0399e9325736b661b7c5d298"></a>
<a id="gga951aa7e2fb999ade4f6c404ce9570a83a16fb9df64c8f3921272f0fe93f9ed6c7"></a>
<a id="gga951aa7e2fb999ade4f6c404ce9570a83aa4fb1618d90efc7580dd3f89e7ef9036"></a>
<a id="gga951aa7e2fb999ade4f6c404ce9570a83ae1a24769cf389312fbf1554cc4404c99"></a>
<a id="gga951aa7e2fb999ade4f6c404ce9570a83a683e5cf10c55857edb78c547dd02a7e3"></a>
<a id="gga951aa7e2fb999ade4f6c404ce9570a83a372e528a85ba9f8a7c2c1b90c54f77ab"></a>
<a id="gga951aa7e2fb999ade4f6c404ce9570a83a1ac03107185f01fbcd9f12733a1d89b3"></a>
<a id="gga951aa7e2fb999ade4f6c404ce9570a83a556a67233b4c5f4a43bdc483b0548bbb"></a>
<a id="gga951aa7e2fb999ade4f6c404ce9570a83a21bab67b1cf51a9784fbcdea997134fe"></a>
<a id="gga951aa7e2fb999ade4f6c404ce9570a83afde13daa39fdbe4048ba2f1459027258"></a>
<a id="gga951aa7e2fb999ade4f6c404ce9570a83a6abb5210f065753cbfa1fbd74d7562a7"></a>
<a id="gga951aa7e2fb999ade4f6c404ce9570a83ad10e9e43712650502a7f92479071c297"></a>

---

[上一章](P002_大型组成数据客户端模型（Large Composition Data Client model）.md) · [返回大纲](大纲.md) · [下一章](P004_连接管理器连接性批量 API（Connectivity Bulk API）.md)
