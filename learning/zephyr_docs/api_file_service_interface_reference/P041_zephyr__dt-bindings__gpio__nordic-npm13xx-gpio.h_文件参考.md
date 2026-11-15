---
id: learning.zephyr-docs.api-file-service-interface-reference.page-41
title: zephyr__dt-bindings__gpio__nordic-npm13xx-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nordic-npm13xx-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_zephyr\_\_dt-bindings\_\_gpio\_\_nordic-npm13xx-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nordic-npm13xx-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 41.1\_宏定义（Macros）

<a id="define-members-0"></a>

### nPM13xx GPIO 驱动能力标志（Drive Strength Flags）。

nPM13xx GPIO 驱动能力标志（Drive Strength Flags）。

<a id="r_ga6a747e318dbdecb394e6c97055cf7d3b"></a>

```c
#define NPM13XX_GPIO_DRIVE_1MA (0U << 8U)
```

相关声明：[NPM13XX_GPIO_DRIVE_1MA](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga6a747e318dbdecb394e6c97055cf7d3b)。

1 mA 驱动能力（Drive）。

<a id="r_ga29c65d6c81acd6c6474a8d5463d30312"></a>

```c
#define NPM13XX_GPIO_DRIVE_6MA (1U << 8U)
```

相关声明：[NPM13XX_GPIO_DRIVE_6MA](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga29c65d6c81acd6c6474a8d5463d30312)。

6 mA 驱动能力（Drive）。

<a id="define-members-1"></a>

### nPM13xx GPIO 去抖标志（Debounce Flags）。

nPM13xx GPIO 去抖标志（Debounce Flags）。

<a id="r_ga94b628f01bd35ef5a8c4be5810853d8a"></a>

```c
#define NPM13XX_GPIO_DEBOUNCE_OFF (0U << 9U)
```

相关声明：[NPM13XX_GPIO_DEBOUNCE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga94b628f01bd35ef5a8c4be5810853d8a)。

普通驱动（Normal Drive）。

<a id="r_ga37203fc635db945392c25ba5eddb42ad"></a>

```c
#define NPM13XX_GPIO_DEBOUNCE_ON (1U << 9U)
```

相关声明：[NPM13XX_GPIO_DEBOUNCE_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga37203fc635db945392c25ba5eddb42ad)。

高驱动（High Drive）。

<a id="define-members-2"></a>

### nPM13xx GPIO 看门狗复位标志（Watchdog Reset Flags）。

nPM13xx GPIO 看门狗复位标志（Watchdog Reset Flags）。

<a id="r_ga7e835aa905fce6b9bd88f6c113ad8fbd"></a>

```c
#define NPM13XX_GPIO_WDT_RESET_OFF (0U << 10U)
```

相关声明：[NPM13XX_GPIO_WDT_RESET_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga7e835aa905fce6b9bd88f6c113ad8fbd)。

关闭（Off）。

<a id="r_gac17073bd2d8bda878c0cf7307276efcb"></a>

```c
#define NPM13XX_GPIO_WDT_RESET_ON (1U << 10U)
```

相关声明：[NPM13XX_GPIO_WDT_RESET_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#gac17073bd2d8bda878c0cf7307276efcb)。

开启（On）。

<a id="define-members-3"></a>

### nPM13xx GPIO 掉电预警标志（Power Loss Warning Flags）。

nPM13xx GPIO 掉电预警标志（Power Loss Warning Flags）。

<a id="r_ga8aa4cab9a6961ca60a14e1cae448376e"></a>

```c
#define NPM13XX_GPIO_PWRLOSSWARN_OFF (0U << 11U)
```

相关声明：[NPM13XX_GPIO_PWRLOSSWARN_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga8aa4cab9a6961ca60a14e1cae448376e)。

关闭（Off）。

<a id="r_gae774196d9a4258da3d849899de5b744b"></a>

```c
#define NPM13XX_GPIO_PWRLOSSWARN_ON (1U << 11U)
```

相关声明：[NPM13XX_GPIO_PWRLOSSWARN_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#gae774196d9a4258da3d849899de5b744b)。

开启（On）。


## 41.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P582_nordic-npm13xx-gpio.h_源码浏览.md)
- [NPM13XX_GPIO_DRIVE_1MA](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga6a747e318dbdecb394e6c97055cf7d3b)
- [NPM13XX_GPIO_DRIVE_6MA](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga29c65d6c81acd6c6474a8d5463d30312)
- [NPM13XX_GPIO_DEBOUNCE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga94b628f01bd35ef5a8c4be5810853d8a)
- [NPM13XX_GPIO_DEBOUNCE_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga37203fc635db945392c25ba5eddb42ad)
- [NPM13XX_GPIO_WDT_RESET_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga7e835aa905fce6b9bd88f6c113ad8fbd)
- [NPM13XX_GPIO_WDT_RESET_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#gac17073bd2d8bda878c0cf7307276efcb)
- [NPM13XX_GPIO_PWRLOSSWARN_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga8aa4cab9a6961ca60a14e1cae448376e)
- [NPM13XX_GPIO_PWRLOSSWARN_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#gae774196d9a4258da3d849899de5b744b)

---

[上一章](P040_zephyr__mpipe__mpipe_buffer.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P042_zephyr__drivers__misc__pio_rpi_pico__pio_rpi_pico.h_文件参考.md)
