---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-27
title: zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzg-common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzg-common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_renesas\_\_pinctrl-rzg-common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzg-common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RZ/G (RZ/G3S)的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

查看此文件的源码。

<a id="details"></a>

Renesas RZ/G (RZ/G3S)的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 27.1\_宏定义（Macros）

<a id="r_ga02f280ee325bc9e66e5566f8d6f3feec"></a>

```c
#define RZG_PINMUX(port, pin, func)
```

相关声明：[RZG_PINMUX](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#ga02f280ee325bc9e66e5566f8d6f3feec)。

创建包含端口／引脚／功能信息（Port / Pin / Function Information）的编码值（Encoded Value）。

<a id="r_gabe4747778068dd33b142d7a891ca901e"></a>

```c
#define RZG_FILTER_SET(filnum, filclksel)
```

相关声明：[RZG_FILTER_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#gabe4747778068dd33b142d7a891ca901e)。

将滤波级数（Filter Stage Count）和时钟选择（Clock Selection）编码为一个配置值。

<a id="define-members-0"></a>

### Renesas RZ/G 数字噪声滤波选项（Digital Noise Filter Options）

设置滤波级数（Filter Stages，`FILNUM`）和采样时钟分频器（Sampling Clock Divider，`FILCLKSEL`）。

<a id="r_ga410e1db2102a72b3222f3f87e9191b36"></a>

```c
#define RZG_FILNUM_4_STAGE 0
```

相关声明：[RZG_FILNUM_4_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#ga410e1db2102a72b3222f3f87e9191b36)。

`FILNUM`：4 级滤波器（4-stage Filter）。

<a id="r_ga7ec85695dd35462b15784cf869e2ecdd"></a>

```c
#define RZG_FILNUM_8_STAGE 1
```

相关声明：[RZG_FILNUM_8_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#ga7ec85695dd35462b15784cf869e2ecdd)。

`FILNUM`：8 级滤波器（8-stage Filter）。

<a id="r_ga7fb5e17c2033f7de03440445de58497d"></a>

```c
#define RZG_FILNUM_12_STAGE 2
```

相关声明：[RZG_FILNUM_12_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#ga7fb5e17c2033f7de03440445de58497d)。

`FILNUM`：12 级滤波器（12-stage Filter）。

<a id="r_ga4c3d0f96e45fcff456391291544c2d7e"></a>

```c
#define RZG_FILNUM_16_STAGE 3
```

相关声明：[RZG_FILNUM_16_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#ga4c3d0f96e45fcff456391291544c2d7e)。

`FILNUM`：16 级滤波器（16-stage Filter）。

<a id="r_gaebf11f5c29f9d62a4bc6076430f5af74"></a>

```c
#define RZG_FILCLKSEL_NOT_DIV 0
```

相关声明：[RZG_FILCLKSEL_NOT_DIV](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#gaebf11f5c29f9d62a4bc6076430f5af74)。

`FILCLKSEL`：不分频（No Division）。

<a id="r_ga6fc19ace82becb78720423edd9a80f03"></a>

```c
#define RZG_FILCLKSEL_DIV_9000 1
```

相关声明：[RZG_FILCLKSEL_DIV_9000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#ga6fc19ace82becb78720423edd9a80f03)。

`FILCLKSEL`：9000 分频（Divided by 9000）。

<a id="r_ga82fe6b7f1ba59ab812683890fa2f0e7c"></a>

```c
#define RZG_FILCLKSEL_DIV_18000 2
```

相关声明：[RZG_FILCLKSEL_DIV_18000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#ga82fe6b7f1ba59ab812683890fa2f0e7c)。

`FILCLKSEL`：18000 分频（Divided by 18000）。

<a id="r_gacecffc879cdcd14232b7cc2714e46e8f"></a>

```c
#define RZG_FILCLKSEL_DIV_36000 3
```

相关声明：[RZG_FILCLKSEL_DIV_36000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#gacecffc879cdcd14232b7cc2714e46e8f)。

`FILCLKSEL`：36000 分频（Divided by 36000）。


## 27.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_pin_register_fields_reference/P003_pinctrl-rzg-common.h_源码浏览.md)
- [RZG_PINMUX](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#ga02f280ee325bc9e66e5566f8d6f3feec)
- [RZG_FILTER_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#gabe4747778068dd33b142d7a891ca901e)
- [RZG_FILNUM_4_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#ga410e1db2102a72b3222f3f87e9191b36)
- [RZG_FILNUM_8_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#ga7ec85695dd35462b15784cf869e2ecdd)
- [RZG_FILNUM_12_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#ga7fb5e17c2033f7de03440445de58497d)
- [RZG_FILNUM_16_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#ga4c3d0f96e45fcff456391291544c2d7e)
- [RZG_FILCLKSEL_NOT_DIV](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#gaebf11f5c29f9d62a4bc6076430f5af74)
- [RZG_FILCLKSEL_DIV_9000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#ga6fc19ace82becb78720423edd9a80f03)
- [RZG_FILCLKSEL_DIV_18000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#ga82fe6b7f1ba59ab812683890fa2f0e7c)
- [RZG_FILCLKSEL_DIV_36000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html#gacecffc879cdcd14232b7cc2714e46e8f)

<a id="header-details"></a>

---

[上一章](P026_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rza3m.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P028_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzv-common.h_文件参考.md)
