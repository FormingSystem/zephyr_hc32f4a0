---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-25
title: zephyr__dt-bindings__pinctrl__renesas__pinctrl-rza-common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rza-common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_renesas\_\_pinctrl-rza-common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rza-common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RZ/A的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

查看此文件的源码。

<a id="details"></a>

Renesas RZ/A的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 25.1\_宏定义（Macros）

<a id="r_gaad0f3d9e2b289afca587d9897ad35210"></a>

```c
#define RZA_PINMUX(port, pin, func)
```

相关声明：[RZA_PINMUX](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#gaad0f3d9e2b289afca587d9897ad35210)。

创建包含端口／引脚／功能信息（Port / Pin / Function Information）的编码值（Encoded Value）。

<a id="r_gacb3f592d302bb7ee67914ade80a3fb44"></a>

```c
#define RZA_FILTER_SET(filnum, filclksel)
```

相关声明：[RZA_FILTER_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#gacb3f592d302bb7ee67914ade80a3fb44)。

将滤波级数（Filter Stage Count）和时钟选择（Clock Selection）编码为一个配置值。

<a id="define-members-0"></a>

### Renesas RZ/A 数字噪声滤波选项（Digital Noise Filter Options）

设置滤波级数（Filter Stages，`FILNUM`）和采样时钟分频器（Sampling Clock Divider，`FILCLKSEL`）。

<a id="r_gae2fb4f96b6b50ad80a433780e422db2f"></a>

```c
#define RZA_FILNUM_4_STAGE 0
```

相关声明：[RZA_FILNUM_4_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#gae2fb4f96b6b50ad80a433780e422db2f)。

`FILNUM`：4 级滤波器（4-stage Filter）。

<a id="r_ga9e4ed308e81c23c7d70a70f3708b3392"></a>

```c
#define RZA_FILNUM_8_STAGE 1
```

相关声明：[RZA_FILNUM_8_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#ga9e4ed308e81c23c7d70a70f3708b3392)。

`FILNUM`：8 级滤波器（8-stage Filter）。

<a id="r_ga6d57d4270438ff5b6cc72111e6d03562"></a>

```c
#define RZA_FILNUM_12_STAGE 2
```

相关声明：[RZA_FILNUM_12_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#ga6d57d4270438ff5b6cc72111e6d03562)。

`FILNUM`：12 级滤波器（12-stage Filter）。

<a id="r_ga9a82059d12af7f931f051a304113735e"></a>

```c
#define RZA_FILNUM_16_STAGE 3
```

相关声明：[RZA_FILNUM_16_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#ga9a82059d12af7f931f051a304113735e)。

`FILNUM`：16 级滤波器（16-stage Filter）。

<a id="r_gab5bb0119588fa51a96489d03a62c4b83"></a>

```c
#define RZA_FILCLKSEL_NOT_DIV 0
```

相关声明：[RZA_FILCLKSEL_NOT_DIV](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#gab5bb0119588fa51a96489d03a62c4b83)。

`FILCLKSEL`：不分频（No Division）。

<a id="r_ga6d987d1bb9a03f28abf5980f0a45ceb4"></a>

```c
#define RZA_FILCLKSEL_DIV_9000 1
```

相关声明：[RZA_FILCLKSEL_DIV_9000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#ga6d987d1bb9a03f28abf5980f0a45ceb4)。

`FILCLKSEL`：9000 分频（Divided by 9000）。

<a id="r_ga9fe6a4f870d9260c13f055245b3d22cb"></a>

```c
#define RZA_FILCLKSEL_DIV_18000 2
```

相关声明：[RZA_FILCLKSEL_DIV_18000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#ga9fe6a4f870d9260c13f055245b3d22cb)。

`FILCLKSEL`：18000 分频（Divided by 18000）。

<a id="r_ga24aeabb3038f110c9d4a76df150987ef"></a>

```c
#define RZA_FILCLKSEL_DIV_36000 3
```

相关声明：[RZA_FILCLKSEL_DIV_36000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#ga24aeabb3038f110c9d4a76df150987ef)。

`FILCLKSEL`：36000 分频（Divided by 36000）。


## 25.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_pin_register_fields_reference/P002_pinctrl-rza-common.h_源码浏览.md)
- [RZA_PINMUX](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#gaad0f3d9e2b289afca587d9897ad35210)
- [RZA_FILTER_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#gacb3f592d302bb7ee67914ade80a3fb44)
- [RZA_FILNUM_4_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#gae2fb4f96b6b50ad80a433780e422db2f)
- [RZA_FILNUM_8_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#ga9e4ed308e81c23c7d70a70f3708b3392)
- [RZA_FILNUM_12_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#ga6d57d4270438ff5b6cc72111e6d03562)
- [RZA_FILNUM_16_STAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#ga9a82059d12af7f931f051a304113735e)
- [RZA_FILCLKSEL_NOT_DIV](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#gab5bb0119588fa51a96489d03a62c4b83)
- [RZA_FILCLKSEL_DIV_9000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#ga6d987d1bb9a03f28abf5980f0a45ceb4)
- [RZA_FILCLKSEL_DIV_18000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#ga9fe6a4f870d9260c13f055245b3d22cb)
- [RZA_FILCLKSEL_DIV_36000](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html#ga24aeabb3038f110c9d4a76df150987ef)

<a id="header-details"></a>

---

[上一章](P024_zephyr__drivers__sensor__paj7620.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P026_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rza3m.h_文件参考.md)
