---
id: learning.zephyr-docs.api-file-supplement-reference.page-114
title: zephyr__drivers__clock_control__smartbond_clock_control.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smartbond__clock__control_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第114章\_zephyr\_\_drivers\_\_clock\_control\_\_smartbond\_clock\_control.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/smartbond__clock__control_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas SmartBond设备的时钟控制定义（Clock Control Definitions）。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/clock_control.h>
```

查看此文件的源码。

Renesas SmartBond设备的时钟控制定义（Clock Control Definitions）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 114.1\_枚举（Enumerations）

<a id="r_ga951aa7e2fb999ade4f6c404ce9570a83"></a>

```c
enum smartbond_clock { SMARTBOND_CLK_NONE , SMARTBOND_CLK_RC32K , SMARTBOND_CLK_RCX , SMARTBOND_CLK_XTAL32K , SMARTBOND_CLK_RC32M , SMARTBOND_CLK_XTAL32M , SMARTBOND_CLK_PLL96M , SMARTBOND_CLK_USB , SMARTBOND_CLK_DIVN_32M , SMARTBOND_CLK_HCLK , SMARTBOND_CLK_LP_CLK , SMARTBOND_CLK_SYS_CLK }
```

相关声明：[smartbond_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#ga951aa7e2fb999ade4f6c404ce9570a83)、[SMARTBOND_CLK_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83a89ea767c0399e9325736b661b7c5d298)、[SMARTBOND_CLK_RC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83a16fb9df64c8f3921272f0fe93f9ed6c7)、[SMARTBOND_CLK_RCX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83aa4fb1618d90efc7580dd3f89e7ef9036)、[SMARTBOND_CLK_XTAL32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83ae1a24769cf389312fbf1554cc4404c99)、[SMARTBOND_CLK_RC32M](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83a683e5cf10c55857edb78c547dd02a7e3)、[SMARTBOND_CLK_XTAL32M](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83a372e528a85ba9f8a7c2c1b90c54f77ab)、[SMARTBOND_CLK_PLL96M](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83a1ac03107185f01fbcd9f12733a1d89b3)、[SMARTBOND_CLK_USB](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83a556a67233b4c5f4a43bdc483b0548bbb)、[SMARTBOND_CLK_DIVN_32M](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83a21bab67b1cf51a9784fbcdea997134fe)、[SMARTBOND_CLK_HCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83afde13daa39fdbe4048ba2f1459027258)、[SMARTBOND_CLK_LP_CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83a6abb5210f065753cbfa1fbd74d7562a7)、[SMARTBOND_CLK_SYS_CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83ad10e9e43712650502a7f92479071c297)。

SmartBond 振荡器（Oscillators）和时钟（Clocks）。


## 114.2\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/clock_control.h](../timer_reference/P096_时钟控制完整头文件.md)
- [查看此文件的源码。](../api_source_reference/P793_smartbond_clock_control.h_源码浏览.md)
- [smartbond_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#ga951aa7e2fb999ade4f6c404ce9570a83)
- [SMARTBOND_CLK_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83a89ea767c0399e9325736b661b7c5d298)
- [SMARTBOND_CLK_RC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83a16fb9df64c8f3921272f0fe93f9ed6c7)
- [SMARTBOND_CLK_RCX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83aa4fb1618d90efc7580dd3f89e7ef9036)
- [SMARTBOND_CLK_XTAL32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83ae1a24769cf389312fbf1554cc4404c99)
- [SMARTBOND_CLK_RC32M](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83a683e5cf10c55857edb78c547dd02a7e3)
- [SMARTBOND_CLK_XTAL32M](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83a372e528a85ba9f8a7c2c1b90c54f77ab)
- [SMARTBOND_CLK_PLL96M](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83a1ac03107185f01fbcd9f12733a1d89b3)
- [SMARTBOND_CLK_USB](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83a556a67233b4c5f4a43bdc483b0548bbb)
- [SMARTBOND_CLK_DIVN_32M](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83a21bab67b1cf51a9784fbcdea997134fe)
- [SMARTBOND_CLK_HCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83afde13daa39fdbe4048ba2f1459027258)
- [SMARTBOND_CLK_LP_CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83a6abb5210f065753cbfa1fbd74d7562a7)
- [SMARTBOND_CLK_SYS_CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__smartbond.html#gga951aa7e2fb999ade4f6c404ce9570a83ad10e9e43712650502a7f92479071c297)

<a id="header-details"></a>

---

[上一章](P113_zephyr__sip_svc__sip_svc_controller.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P115_zephyr__net__sntp_server.h_文件参考.md)
