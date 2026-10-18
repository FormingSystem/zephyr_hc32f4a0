---
id: learning.zephyr-docs.api-file-interface-reference.page-55
title: zephyr__dt-bindings__gpio__stm32-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_zephyr\_\_dt-bindings\_\_gpio\_\_stm32-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stm32-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 55.1\_宏定义（Macros）

<a id="r_ga9a05f736e9ee915f591a65a7f6d382d3"></a>

```c
#define STM32_GPIO_WKUP (1 << 8)
```

相关声明：[STM32_GPIO_WKUP](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html#ga9a05f736e9ee915f591a65a7f6d382d3)。

配置 GPIO 引脚，使系统能够在断电状态（Poweroff）后通过该引脚上电。

<a id="r_gaa8d19f48bfea73193ff35c06a6894df6"></a>

```c
#define STM32_GPIO_LOW_SPEED (0x0 << STM32_GPIO_SPEED_SHIFT)
```

相关声明：[STM32_GPIO_LOW_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html#gaa8d19f48bfea73193ff35c06a6894df6)。

将 GPIO 引脚输出速度（output speed）配置为低速。

<a id="r_gaee4f9eb7cb958d4a55d13029658bdff3"></a>

```c
#define STM32_GPIO_MEDIUM_SPEED (0x1 << STM32_GPIO_SPEED_SHIFT)
```

相关声明：[STM32_GPIO_MEDIUM_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html#gaee4f9eb7cb958d4a55d13029658bdff3)。

将 GPIO 引脚输出速度配置为中速。

<a id="r_gac91d2b48bc764131896ebb3b0436dac1"></a>

```c
#define STM32_GPIO_HIGH_SPEED (0x2 << STM32_GPIO_SPEED_SHIFT)
```

相关声明：[STM32_GPIO_HIGH_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html#gac91d2b48bc764131896ebb3b0436dac1)。

将 GPIO 引脚输出速度配置为高速。

<a id="r_gaeff690b8406b0ed24f97bbe8ab4bf31e"></a>

```c
#define STM32_GPIO_VERY_HIGH_SPEED (0x3 << STM32_GPIO_SPEED_SHIFT)
```

相关声明：[STM32_GPIO_VERY_HIGH_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html#gaeff690b8406b0ed24f97bbe8ab4bf31e)。

将 GPIO 引脚输出速度配置为超高速。


## 55.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P826_stm32-gpio.h_源码浏览.md)
- [STM32_GPIO_WKUP](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html#ga9a05f736e9ee915f591a65a7f6d382d3)
- [STM32_GPIO_LOW_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html#gaa8d19f48bfea73193ff35c06a6894df6)
- [STM32_GPIO_MEDIUM_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html#gaee4f9eb7cb958d4a55d13029658bdff3)
- [STM32_GPIO_HIGH_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html#gac91d2b48bc764131896ebb3b0436dac1)
- [STM32_GPIO_VERY_HIGH_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html#gaeff690b8406b0ed24f97bbe8ab4bf31e)

---

[上一章](P054_zephyr__net__ssh__client.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P056_____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__common.h_文件参考.md)
