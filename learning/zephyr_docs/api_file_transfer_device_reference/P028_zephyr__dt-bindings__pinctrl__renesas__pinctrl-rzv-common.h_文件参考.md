---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-28
title: zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzv-common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzv-common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_renesas\_\_pinctrl-rzv-common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzv-common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RZ/V的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

查看此文件的源码。

<a id="details"></a>

Renesas RZ/V的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 28.1\_宏定义（Macros）

<a id="r_gace27a9fee40fcee657b3aff941b3ac6b"></a>

```c
#define RZV_PINMUX(port, pin, func)
```

相关声明：[RZV_PINMUX](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#gace27a9fee40fcee657b3aff941b3ac6b)。

创建包含端口／引脚／功能信息（Port / Pin / Function Information）的编码值（Encoded Value）。

<a id="r_ga038292c08044da9e82019e7aa73abf1c"></a>

```c
#define RZV_FILTER_SET(filnum, filclksel)
```

相关声明：[RZV_FILTER_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#ga038292c08044da9e82019e7aa73abf1c)。

将滤波级数（Filter Stage Count）和时钟选择（Clock Selection）编码为一个配置值。

<a id="define-members-0"></a>

### Renesas RZ/V 数字噪声滤波选项（Digital Noise Filter Options）

设置滤波级数（Filter Stages，`FILNUM`）和采样时钟分频器（Sampling Clock Divider，`FILCLKSEL`）。

<a id="r_ga474313de5067232584bb66a293cceef1"></a>

```c
#define RZV_FILNUM_4_STAGE 0
```

相关声明：[RZV_FILNUM_4_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#ga474313de5067232584bb66a293cceef1)。

`FILNUM`：4 级滤波器（4-stage Filter）。

<a id="r_gab51d90be14e4d81c38c4cfa620270b64"></a>

```c
#define RZV_FILNUM_8_STAGE 1
```

相关声明：[RZV_FILNUM_8_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#gab51d90be14e4d81c38c4cfa620270b64)。

`FILNUM`：8 级滤波器（8-stage Filter）。

<a id="r_gab3b284fd4bd5a16a2ea1d83116832cd2"></a>

```c
#define RZV_FILNUM_12_STAGE 2
```

相关声明：[RZV_FILNUM_12_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#gab3b284fd4bd5a16a2ea1d83116832cd2)。

`FILNUM`：12 级滤波器（12-stage Filter）。

<a id="r_ga12034f75c3817d20962999b9040caca6"></a>

```c
#define RZV_FILNUM_16_STAGE 3
```

相关声明：[RZV_FILNUM_16_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#ga12034f75c3817d20962999b9040caca6)。

`FILNUM`：16 级滤波器（16-stage Filter）。

<a id="r_gabac8582aa87640663955060639507ade"></a>

```c
#define RZV_FILCLKSEL_NOT_DIV 0
```

相关声明：[RZV_FILCLKSEL_NOT_DIV](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#gabac8582aa87640663955060639507ade)。

`FILCLKSEL`：不分频（No Division）。

<a id="r_ga43a5dfaf850006746e679e73a414e446"></a>

```c
#define RZV_FILCLKSEL_DIV_9000 1
```

相关声明：[RZV_FILCLKSEL_DIV_9000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#ga43a5dfaf850006746e679e73a414e446)。

`FILCLKSEL`：9000 分频（Divided by 9000）。

<a id="r_gad1e144b7c5bf2d735a74f4bf84a58561"></a>

```c
#define RZV_FILCLKSEL_DIV_18000 2
```

相关声明：[RZV_FILCLKSEL_DIV_18000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#gad1e144b7c5bf2d735a74f4bf84a58561)。

`FILCLKSEL`：18000 分频（Divided by 18000）。

<a id="r_ga5cb812371774b2162d5b6f71d3422c19"></a>

```c
#define RZV_FILCLKSEL_DIV_36000 3
```

相关声明：[RZV_FILCLKSEL_DIV_36000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#ga5cb812371774b2162d5b6f71d3422c19)。

`FILCLKSEL`：36000 分频（Divided by 36000）。


## 28.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_workqueue_pin_control_reference/P005_pinctrl-rzv-common.h_源码浏览.md)
- [RZV_PINMUX](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#gace27a9fee40fcee657b3aff941b3ac6b)
- [RZV_FILTER_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#ga038292c08044da9e82019e7aa73abf1c)
- [RZV_FILNUM_4_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#ga474313de5067232584bb66a293cceef1)
- [RZV_FILNUM_8_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#gab51d90be14e4d81c38c4cfa620270b64)
- [RZV_FILNUM_12_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#gab3b284fd4bd5a16a2ea1d83116832cd2)
- [RZV_FILNUM_16_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#ga12034f75c3817d20962999b9040caca6)
- [RZV_FILCLKSEL_NOT_DIV](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#gabac8582aa87640663955060639507ade)
- [RZV_FILCLKSEL_DIV_9000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#ga43a5dfaf850006746e679e73a414e446)
- [RZV_FILCLKSEL_DIV_18000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#gad1e144b7c5bf2d735a74f4bf84a58561)
- [RZV_FILCLKSEL_DIV_36000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html#ga5cb812371774b2162d5b6f71d3422c19)

<a id="header-details"></a>

---

[上一章](P027_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzg-common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P029_zephyr__drivers__pinctrl__pinctrl_rcar_x5h_common.h_文件参考.md)
