---
id: learning.zephyr-docs.api-file-network-device-reference.page-26
title: zephyr__dt-bindings__pinctrl__renesas__pinctrl-rcar-common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rcar-common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_renesas\_\_pinctrl-rcar-common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rcar-common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas R-Car的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

查看此文件的源码。

<a id="details"></a>

Renesas R-Car的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 26.1\_宏定义（Macros）

<a id="r_gadbde593c77123c64c2f63e4e8f508ccb"></a>

```c
#define IPSR(bank, shift, func)
```

相关声明：[IPSR](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#gadbde593c77123c64c2f63e4e8f508ccb)。

构造 IPSR 属性条目（Property Entry）的辅助宏，仅适用于 Gen3/4。

<a id="r_ga840b9b9f9f5513088896bbb960724d8f"></a>

```c
#define RCAR_GP_PIN(bank, pin)
```

相关声明：[RCAR_GP_PIN](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#ga840b9b9f9f5513088896bbb960724d8f)。

编码具备 GPIO 能力的引脚的辅助宏。

<a id="r_ga6e8b18f9578375cb325e9e5b204b6c66"></a>

```c
#define RCAR_NOGP_PIN(pin)
```

相关声明：[RCAR_NOGP_PIN](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#ga6e8b18f9578375cb325e9e5b204b6c66)。

编码不具备 GPIO 能力的引脚的辅助宏。

<a id="r_ga0d4d66df6e1565e2d9f3cfdca9aa5362"></a>

```c
#define IPnSR(bank, reg, shift, func)
```

相关声明：[IPnSR](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#ga0d4d66df6e1565e2d9f3cfdca9aa5362)。

为 Gen4 片上系统（SoC）构造 IPSR 属性条目的辅助宏。

<a id="r_ga66425dcd41fb8297e87a13d2c597d1b5"></a>

```c
#define IPSR_DUMMY IPnSR(0x1f, 7, 0x1f, 0xf)
```

相关声明：[IPSR_DUMMY](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#ga66425dcd41fb8297e87a13d2c597d1b5)、[IPnSR](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#ga0d4d66df6e1565e2d9f3cfdca9aa5362)。

为引脚定义占位 IPSR 标志（Dummy IPSR Flag）的宏。

<a id="r_ga5109d4c9a0f6625194c2e4d940805be7"></a>

```c
#define RCAR_ALTSEL_FUNC(group, pin, func)
```

相关声明：[RCAR_ALTSEL_FUNC](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#ga5109d4c9a0f6625194c2e4d940805be7)、[group](../posix_system_model_reference/P003_group_结构体.md)。

构造 ALTSEL 属性条目（Property Entry）的辅助宏，仅适用于 Gen5。

<a id="define-members-0"></a>

### R-Car 引脚输入输出电压电平（I/O Voltage Levels）

<a id="r_ga866ef498674c60a51c56decc15421e25"></a>

```c
#define PIN_VOLTAGE_NONE 0
```

相关声明：[PIN_VOLTAGE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#ga866ef498674c60a51c56decc15421e25)。

不选择输入输出电压（I/O Voltage）。

<a id="r_gaeb4cb1a9f61be2a30c5b11bec746b839"></a>

```c
#define PIN_VOLTAGE_1P8V 1
```

相关声明：[PIN_VOLTAGE_1P8V](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#gaeb4cb1a9f61be2a30c5b11bec746b839)。

1.8 V 输入输出电压（I/O Voltage）。

<a id="r_gacc995ebea352dc5bf5042e29cd1e15d0"></a>

```c
#define PIN_VOLTAGE_3P3V 2
```

相关声明：[PIN_VOLTAGE_3P3V](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#gacc995ebea352dc5bf5042e29cd1e15d0)。

3.3 V 输入输出电压（I/O Voltage）。


## 26.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P143_pinctrl-rcar-common.h_源码浏览.md)
- [IPSR](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#gadbde593c77123c64c2f63e4e8f508ccb)
- [RCAR_GP_PIN](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#ga840b9b9f9f5513088896bbb960724d8f)
- [RCAR_NOGP_PIN](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#ga6e8b18f9578375cb325e9e5b204b6c66)
- [IPnSR](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#ga0d4d66df6e1565e2d9f3cfdca9aa5362)
- [IPSR_DUMMY](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#ga66425dcd41fb8297e87a13d2c597d1b5)
- [RCAR_ALTSEL_FUNC](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#ga5109d4c9a0f6625194c2e4d940805be7)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [PIN_VOLTAGE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#ga866ef498674c60a51c56decc15421e25)
- [PIN_VOLTAGE_1P8V](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#gaeb4cb1a9f61be2a30c5b11bec746b839)
- [PIN_VOLTAGE_3P3V](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rcar.html#gacc995ebea352dc5bf5042e29cd1e15d0)

<a id="header-details"></a>

---

[上一章](P025_zephyr__mpipe__utils__mpipe_player.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P027_zephyr__drivers__firmware__scmi__power.h_文件参考.md)
