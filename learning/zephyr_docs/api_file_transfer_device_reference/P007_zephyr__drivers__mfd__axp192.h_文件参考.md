---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-7
title: zephyr__drivers__mfd__axp192.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2axp192_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_mfd\_\_axp192.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2axp192_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stddef.h>
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="r_a61d7d88bead4733fedcbfb70f8ada464"></a>

```c
#define AXP192_GPIO_FUNC_VALID(func)
```

相关声明：[AXP192_GPIO_FUNC_VALID](#a61d7d88bead4733fedcbfb70f8ada464)。

检查给定的 GPIO 功能值（Function Value）是否有效。

<a id="r_a0df71981c80a3c46e168287c39df88ee"></a>

```c
#define AXP192_GPIO_MAX_NUM 6U
```

相关声明：[AXP192_GPIO_MAX_NUM](#a0df71981c80a3c46e168287c39df88ee)。

AXP192 电源管理集成电路（PMIC）支持的 GPIO 数量上限。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.2\_枚举（Enumerations）

<a id="r_ac92e5fa77591e02e49570d1a1c38e249"></a>

```c
enum axp192_gpio_func { AXP192_GPIO_FUNC_INPUT = BIT(0) , AXP192_GPIO_FUNC_OUTPUT_OD = BIT(1) , AXP192_GPIO_FUNC_OUTPUT_LOW = BIT(2) , AXP192_GPIO_FUNC_LDO = BIT(3) , AXP192_GPIO_FUNC_ADC = BIT(4) , AXP192_GPIO_FUNC_PWM = BIT(5) , AXP192_GPIO_FUNC_FLOAT = BIT(6) , AXP192_GPIO_FUNC_CHARGE_CTL = BIT(7) , AXP192_GPIO_FUNC_INVALID }
```

相关声明：[axp192_gpio_func](#ac92e5fa77591e02e49570d1a1c38e249)、[AXP192_GPIO_FUNC_INPUT](#ac92e5fa77591e02e49570d1a1c38e249ab8eee3f4b6ce22594b90d7e49e4927df)、[AXP192_GPIO_FUNC_OUTPUT_OD](#ac92e5fa77591e02e49570d1a1c38e249af1c2244571c0a3b12c0ae94c583c1a4b)、[AXP192_GPIO_FUNC_OUTPUT_LOW](#ac92e5fa77591e02e49570d1a1c38e249a8d006f1e4284057f5b952b236729c5f5)、[AXP192_GPIO_FUNC_LDO](#ac92e5fa77591e02e49570d1a1c38e249ae9f961ad84c38f3315e3cdb25ede9328)、[AXP192_GPIO_FUNC_ADC](#ac92e5fa77591e02e49570d1a1c38e249ab3a2622cccb9ec1cdf22ddd5ac75ae6a)、[AXP192_GPIO_FUNC_PWM](#ac92e5fa77591e02e49570d1a1c38e249a2634f857f19e03ab8337780025c25579)、[AXP192_GPIO_FUNC_FLOAT](#ac92e5fa77591e02e49570d1a1c38e249a69c1f986672389305a3000b83a12417f)、[AXP192_GPIO_FUNC_CHARGE_CTL](#ac92e5fa77591e02e49570d1a1c38e249a5955f43848da067d9134790f9fe1c240)、[AXP192_GPIO_FUNC_INVALID](#ac92e5fa77591e02e49570d1a1c38e249ad16e246ca71f2e865cccf1b4ad2f9286)。

GPIO 功能类型（Function Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="r_ga61c3f46791f4efa08ee45fc85dc32c81"></a>

```c
int mfd_axp192_gpio_func_ctrl (const struct device *dev, const struct device *client_dev, uint8_t gpio, enum axp192_gpio_func func)
```

相关声明：[mfd_axp192_gpio_func_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__axp192.html#ga61c3f46791f4efa08ee45fc85dc32c81)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[axp192_gpio_func](#ac92e5fa77591e02e49570d1a1c38e249)。

请求将 GPIO 引脚（Pin）配置为指定功能（Function）。

<a id="r_ga29db6e44c801fecfa1df2d9da93c2e0b"></a>

```c
int mfd_axp192_gpio_func_get (const struct device *dev, uint8_t gpio, enum axp192_gpio_func *func)
```

相关声明：[mfd_axp192_gpio_func_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__axp192.html#ga29db6e44c801fecfa1df2d9da93c2e0b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[axp192_gpio_func](#ac92e5fa77591e02e49570d1a1c38e249)。

读取指定 GPIO 引脚（Pin）的当前配置（Configuration）。

<a id="r_ga8db91c44adbf8ca6f727e2deb0aa96dd"></a>

```c
int mfd_axp192_gpio_pd_ctrl (const struct device *dev, uint8_t gpio, bool enable)
```

相关声明：[mfd_axp192_gpio_pd_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__axp192.html#ga8db91c44adbf8ca6f727e2deb0aa96dd)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用指定 GPIO 引脚（Pin）的下拉（Pull-down）。

<a id="r_gabdacd1e10bacf9f0393beb65327eaeea"></a>

```c
int mfd_axp192_gpio_pd_get (const struct device *dev, uint8_t gpio, bool *enabled)
```

相关声明：[mfd_axp192_gpio_pd_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__axp192.html#gabdacd1e10bacf9f0393beb65327eaeea)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

读取指定 GPIO 的当前下拉配置（Pull-down Configuration）。

<a id="r_gaa12241d0655122f05da06dc506d2a5c0"></a>

```c
int mfd_axp192_gpio_read_port (const struct device *dev, uint8_t *value)
```

相关声明：[mfd_axp192_gpio_read_port](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__axp192.html#gaa12241d0655122f05da06dc506d2a5c0)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 GPIO 端口（Port）。

<a id="r_ga7570c8657918c15c71fddca264bce10e"></a>

```c
int mfd_axp192_gpio_write_port (const struct device *dev, uint8_t value, uint8_t mask)
```

相关声明：[mfd_axp192_gpio_write_port](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__axp192.html#ga7570c8657918c15c71fddca264bce10e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入 GPIO 端口（Port）。

## 7.4\_详细说明（Detailed Documentation）

<a id="a61d7d88bead4733fedcbfb70f8ada464"></a>

### `AXP192_GPIO_FUNC_VALID`

```c
#define AXP192_GPIO_FUNC_VALID ( func)
```

展开值（Value）：

```c
(func < AXP192_GPIO_FUNC_INVALID)
```

检查给定的 GPIO 功能值（Function Value）是否有效。

<a id="a0df71981c80a3c46e168287c39df88ee"></a>

### `AXP192_GPIO_MAX_NUM`

```c
#define AXP192_GPIO_MAX_NUM 6U
```

AXP192 电源管理集成电路（PMIC）支持的 GPIO 数量上限。

<a id="ac92e5fa77591e02e49570d1a1c38e249"></a>

### `axp192_gpio_func`

```c
enum axp192_gpio_func
```

GPIO 功能类型（Function Type）。

每个 GPIO 只能配置一种功能（Function）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `AXP192_GPIO_FUNC_INPUT` |  |
| `AXP192_GPIO_FUNC_OUTPUT_OD` |  |
| `AXP192_GPIO_FUNC_OUTPUT_LOW` |  |
| `AXP192_GPIO_FUNC_LDO` |  |
| `AXP192_GPIO_FUNC_ADC` |  |
| `AXP192_GPIO_FUNC_PWM` |  |
| `AXP192_GPIO_FUNC_FLOAT` |  |
| `AXP192_GPIO_FUNC_CHARGE_CTL` |  |
| `AXP192_GPIO_FUNC_INVALID` |  |


## 7.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P160_axp192.h_源码浏览.md)
- [mfd_axp192_gpio_func_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__axp192.html#ga61c3f46791f4efa08ee45fc85dc32c81)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mfd_axp192_gpio_func_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__axp192.html#ga29db6e44c801fecfa1df2d9da93c2e0b)
- [mfd_axp192_gpio_pd_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__axp192.html#ga8db91c44adbf8ca6f727e2deb0aa96dd)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [mfd_axp192_gpio_pd_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__axp192.html#gabdacd1e10bacf9f0393beb65327eaeea)
- [mfd_axp192_gpio_read_port](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__axp192.html#gaa12241d0655122f05da06dc506d2a5c0)
- [mfd_axp192_gpio_write_port](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__axp192.html#ga7570c8657918c15c71fddca264bce10e)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="adrivers_2mfd_2axp192_8h_html_ac92e5fa77591e02e49570d1a1c38e249ad16e246ca71f2e865cccf1b4ad2f9286"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ac92e5fa77591e02e49570d1a1c38e249ab8eee3f4b6ce22594b90d7e49e4927df"></a>
<a id="ac92e5fa77591e02e49570d1a1c38e249af1c2244571c0a3b12c0ae94c583c1a4b"></a>
<a id="ac92e5fa77591e02e49570d1a1c38e249a8d006f1e4284057f5b952b236729c5f5"></a>
<a id="ac92e5fa77591e02e49570d1a1c38e249ae9f961ad84c38f3315e3cdb25ede9328"></a>
<a id="ac92e5fa77591e02e49570d1a1c38e249ab3a2622cccb9ec1cdf22ddd5ac75ae6a"></a>
<a id="ac92e5fa77591e02e49570d1a1c38e249a2634f857f19e03ab8337780025c25579"></a>
<a id="ac92e5fa77591e02e49570d1a1c38e249a69c1f986672389305a3000b83a12417f"></a>
<a id="ac92e5fa77591e02e49570d1a1c38e249a5955f43848da067d9134790f9fe1c240"></a>
<a id="ac92e5fa77591e02e49570d1a1c38e249ad16e246ca71f2e865cccf1b4ad2f9286"></a>

---

[上一章](P006_zephyr__drivers__firmware__scmi__pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__drivers__mfd__npm13xx.h_文件参考.md)
