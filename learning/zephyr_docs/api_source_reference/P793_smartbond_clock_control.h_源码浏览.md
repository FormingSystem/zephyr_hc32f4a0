---
id: learning.zephyr-docs.api-source-reference.page-793
title: smartbond_clock_control.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smartbond__clock__control_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第793章\_smartbond\_clock\_control.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/smartbond__clock__control_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/smartbond__clock__control_8h.html)。

## 793.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="aclock__control_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__clock__control__smartbond_html_ga951aa7e2fb999ade4f6c404ce9570a83"></a>
<a id="agroup__clock__control__smartbond_html_gga951aa7e2fb999ade4f6c404ce9570a83a16fb9df64c8f3921272f0fe93f9ed6c7"></a>
<a id="agroup__clock__control__smartbond_html_gga951aa7e2fb999ade4f6c404ce9570a83a1ac03107185f01fbcd9f12733a1d89b3"></a>
<a id="agroup__clock__control__smartbond_html_gga951aa7e2fb999ade4f6c404ce9570a83a21bab67b1cf51a9784fbcdea997134fe"></a>
<a id="agroup__clock__control__smartbond_html_gga951aa7e2fb999ade4f6c404ce9570a83a372e528a85ba9f8a7c2c1b90c54f77ab"></a>
<a id="agroup__clock__control__smartbond_html_gga951aa7e2fb999ade4f6c404ce9570a83a556a67233b4c5f4a43bdc483b0548bbb"></a>
<a id="agroup__clock__control__smartbond_html_gga951aa7e2fb999ade4f6c404ce9570a83a683e5cf10c55857edb78c547dd02a7e3"></a>
<a id="agroup__clock__control__smartbond_html_gga951aa7e2fb999ade4f6c404ce9570a83a6abb5210f065753cbfa1fbd74d7562a7"></a>
<a id="agroup__clock__control__smartbond_html_gga951aa7e2fb999ade4f6c404ce9570a83a89ea767c0399e9325736b661b7c5d298"></a>
<a id="agroup__clock__control__smartbond_html_gga951aa7e2fb999ade4f6c404ce9570a83aa4fb1618d90efc7580dd3f89e7ef9036"></a>
<a id="agroup__clock__control__smartbond_html_gga951aa7e2fb999ade4f6c404ce9570a83ad10e9e43712650502a7f92479071c297"></a>
<a id="agroup__clock__control__smartbond_html_gga951aa7e2fb999ade4f6c404ce9570a83ae1a24769cf389312fbf1554cc4404c99"></a>
<a id="agroup__clock__control__smartbond_html_gga951aa7e2fb999ade4f6c404ce9570a83afde13daa39fdbe4048ba2f1459027258"></a>

```c
/*
 * Copyright (c) 2023 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_SMARTBOND_CLOCK_CONTROL_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_SMARTBOND_CLOCK_CONTROL_H_

#include <zephyr/device.h>
#include <zephyr/drivers/clock_control.h>


#ifdef __cplusplus
extern "C" {
#endif

enum smartbond_clock {
        SMARTBOND_CLK_NONE,
        SMARTBOND_CLK_RC32K,
        SMARTBOND_CLK_RCX,
        SMARTBOND_CLK_XTAL32K,
        SMARTBOND_CLK_RC32M,
        SMARTBOND_CLK_XTAL32M,
        SMARTBOND_CLK_PLL96M,
        SMARTBOND_CLK_USB,
        SMARTBOND_CLK_DIVN_32M,
        SMARTBOND_CLK_HCLK,
        SMARTBOND_CLK_LP_CLK,
        SMARTBOND_CLK_SYS_CLK,
};


int z_smartbond_select_sys_clk(enum smartbond_clock sys_clk);

int z_smartbond_select_lp_clk(enum smartbond_clock lp_clk);


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_SMARTBOND_CLOCK_CONTROL_H_ */
```

## 793.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 71 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_SMARTBOND_CLOCK_CONTROL_H_`。

## 793.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/smartbond__clock__control_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
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
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)

---

[上一章](P792_smartbond-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P794_smp_bt.h_源码浏览.md)
