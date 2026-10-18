---
id: learning.zephyr-docs.api-file-system-power-reference.page-10
title: zephyr__dt-bindings__sensor__lis2dh.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2lis2dh_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_dt-bindings\_\_sensor\_\_lis2dh.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2lis2dh_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST LIS2DH 3-axis accelerometer的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the ST LIS2DH 3-axis accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="define-members-0"></a>

### GPIO 中断配置（Interrupt Configuration）

设备树属性（Devicetree Properties）`int1-gpio-config` 和 `int2-gpio-config` 的取值。

<a id="r_ga673dad0efc816668086fc88983c13cbb"></a>

```c
#define LIS2DH_DT_GPIO_INT_EDGE_BOTH 0
```

相关声明：[LIS2DH_DT_GPIO_INT_EDGE_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga673dad0efc816668086fc88983c13cbb)。

在信号的两个边沿（Both Signal Edges）均触发。

<a id="r_gafbf7948886682093cbc8034720bbabd5"></a>

```c
#define LIS2DH_DT_GPIO_INT_EDGE_RISING 1
```

相关声明：[LIS2DH_DT_GPIO_INT_EDGE_RISING](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#gafbf7948886682093cbc8034720bbabd5)。

在上升沿（Rising Edge）触发。

<a id="r_ga61b4f2c56b4bc253148340c52b1dca74"></a>

```c
#define LIS2DH_DT_GPIO_INT_EDGE_FALLING 2
```

相关声明：[LIS2DH_DT_GPIO_INT_EDGE_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga61b4f2c56b4bc253148340c52b1dca74)。

在下降沿（Falling Edge）触发。

<a id="r_ga044d5fee79faaafcb2ed0363cce9329c"></a>

```c
#define LIS2DH_DT_GPIO_INT_LEVEL_HIGH 3
```

相关声明：[LIS2DH_DT_GPIO_INT_LEVEL_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga044d5fee79faaafcb2ed0363cce9329c)。

在信号为高电平（High）时触发。

<a id="r_ga06837f6473ace3107383e076903fde19"></a>

```c
#define LIS2DH_DT_GPIO_INT_LEVEL_LOW 4
```

相关声明：[LIS2DH_DT_GPIO_INT_LEVEL_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga06837f6473ace3107383e076903fde19)。

在信号为低电平（Low）时触发。

<a id="define-members-1"></a>

### 任意运动检测模式（Any-motion Detection Mode）

设备树属性（Devicetree Property）`anym-mode` 的取值。

<a id="r_ga97fdffadeb9f76118134e9c1bc1e1fb5"></a>

```c
#define LIS2DH_DT_ANYM_OR_COMBINATION 0
```

相关声明：[LIS2DH_DT_ANYM_OR_COMBINATION](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga97fdffadeb9f76118134e9c1bc1e1fb5)。

对已启用轴进行逻辑或组合（OR Combination）。

<a id="r_ga236b804ce12742583a07dd7e342467a3"></a>

```c
#define LIS2DH_DT_ANYM_6D_MOVEMENT 1
```

相关声明：[LIS2DH_DT_ANYM_6D_MOVEMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga236b804ce12742583a07dd7e342467a3)。

六方向运动识别（6-direction Movement Recognition）。

<a id="r_gaddcd38964fcc1d465fa6d5b4a09ee47a"></a>

```c
#define LIS2DH_DT_ANYM_AND_COMBINATION 2
```

相关声明：[LIS2DH_DT_ANYM_AND_COMBINATION](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#gaddcd38964fcc1d465fa6d5b4a09ee47a)。

对已启用轴进行逻辑与组合（AND Combination）。

<a id="r_ga78a545b550b5ec39729cf283afb676ae"></a>

```c
#define LIS2DH_DT_ANYM_6D_POSITION 3
```

相关声明：[LIS2DH_DT_ANYM_6D_POSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga78a545b550b5ec39729cf283afb676ae)。

六方向位置识别（6-direction Position Recognition）。


## 10.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P206_lis2dh.h_源码浏览.md)
- [LIS2DH_DT_GPIO_INT_EDGE_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga673dad0efc816668086fc88983c13cbb)
- [LIS2DH_DT_GPIO_INT_EDGE_RISING](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#gafbf7948886682093cbc8034720bbabd5)
- [LIS2DH_DT_GPIO_INT_EDGE_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga61b4f2c56b4bc253148340c52b1dca74)
- [LIS2DH_DT_GPIO_INT_LEVEL_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga044d5fee79faaafcb2ed0363cce9329c)
- [LIS2DH_DT_GPIO_INT_LEVEL_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga06837f6473ace3107383e076903fde19)
- [LIS2DH_DT_ANYM_OR_COMBINATION](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga97fdffadeb9f76118134e9c1bc1e1fb5)
- [LIS2DH_DT_ANYM_6D_MOVEMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga236b804ce12742583a07dd7e342467a3)
- [LIS2DH_DT_ANYM_AND_COMBINATION](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#gaddcd38964fcc1d465fa6d5b4a09ee47a)
- [LIS2DH_DT_ANYM_6D_POSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga78a545b550b5ec39729cf283afb676ae)

<a id="header-details"></a>

---

[上一章](P009_zephyr__dt-bindings__sensor__icm4268x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__dt-bindings__gpio__espressif-esp32-gpio.h_文件参考.md)
