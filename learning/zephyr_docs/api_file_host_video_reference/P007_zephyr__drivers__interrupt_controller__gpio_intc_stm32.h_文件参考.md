---
id: learning.zephyr-docs.api-file-host-video-reference.page-7
title: zephyr__drivers__interrupt_controller__gpio_intc_stm32.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_gpio\_intc\_stm32.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/types.h>
#include <zephyr/drivers/gpio.h>
```

查看此文件的源码。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.1\_类型定义（Typedefs）

<a id="r_a52c69f3ce04242217e00981c1315a374"></a>

```c
typedef uint32_t stm32_gpio_irq_line_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[stm32_gpio_irq_line_t](#a52c69f3ce04242217e00981c1315a374)。

STM32 微控制器（MCU）的通用输入输出中断控制器（GPIO Interrupt Controller）API。

<a id="r_a69ad9c575223c813f484423e56200560"></a>

```c
typedef void(* stm32_gpio_irq_cb_t) (gpio_port_pins_t pin, void *user)
```

相关声明：[stm32_gpio_irq_cb_t](#a69ad9c575223c813f484423e56200560)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

GPIO 中断回调函数签名（Interrupt Callback Signature）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.2\_枚举（Enumerations）

<a id="r_a8f9c3db22937ebe4382215227c410b61"></a>

```c
enum stm32_gpio_irq_trigger { STM32_GPIO_IRQ_TRIG_NONE = 0x0 , STM32_GPIO_IRQ_TRIG_RISING = 0x1 , STM32_GPIO_IRQ_TRIG_FALLING = 0x2 , STM32_GPIO_IRQ_TRIG_BOTH = 0x3 , STM32_GPIO_IRQ_TRIG_HIGH_LEVEL = 0x4 , STM32_GPIO_IRQ_TRIG_LOW_LEVEL = 0x5 }
```

相关声明：[stm32_gpio_irq_trigger](#a8f9c3db22937ebe4382215227c410b61)、[STM32_GPIO_IRQ_TRIG_NONE](#a8f9c3db22937ebe4382215227c410b61adb4cda594aec45886263f14968e6b3d2)、[STM32_GPIO_IRQ_TRIG_RISING](#a8f9c3db22937ebe4382215227c410b61a601ac25a6a83f5a01dc8ce8bb8f547ae)、[STM32_GPIO_IRQ_TRIG_FALLING](#a8f9c3db22937ebe4382215227c410b61a2d20b462dad9d074ce7bb1479d3066c9)、[STM32_GPIO_IRQ_TRIG_BOTH](#a8f9c3db22937ebe4382215227c410b61a46af906f79e53b4301c50292840bd301)、[STM32_GPIO_IRQ_TRIG_HIGH_LEVEL](#a8f9c3db22937ebe4382215227c410b61a961343f06deca1a4ae9288b81e167048)、[STM32_GPIO_IRQ_TRIG_LOW_LEVEL](#a8f9c3db22937ebe4382215227c410b61a2a13de1280bfac5e1cb484db56843e2c)。

GPIO 中断触发标志（Interrupt Trigger Flags）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="r_a03badd2828ca67e3f8adadc75fec2bd2"></a>

```c
stm32_gpio_irq_line_t stm32_gpio_intc_get_pin_irq_line (uint32_t port, gpio_pin_t pin)
```

相关声明：[stm32_gpio_irq_line_t](#a52c69f3ce04242217e00981c1315a374)、[stm32_gpio_intc_get_pin_irq_line](#a03badd2828ca67e3f8adadc75fec2bd2)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)。

获取 GPIO 端口 `port` 上指定引脚对应的 GPIO 中断线值（Interrupt Line Value）。

<a id="r_ad1c9359de9847ebd2670987302c48f8d"></a>

```c
void stm32_gpio_intc_enable_line (stm32_gpio_irq_line_t line)
```

相关声明：[stm32_gpio_intc_enable_line](#ad1c9359de9847ebd2670987302c48f8d)、[stm32_gpio_irq_line_t](#a52c69f3ce04242217e00981c1315a374)。

使能指定中断线（Line）的 GPIO 中断。

<a id="r_a0bb3bd355218c41e9173f061f46ec997"></a>

```c
void stm32_gpio_intc_disable_line (stm32_gpio_irq_line_t line)
```

相关声明：[stm32_gpio_intc_disable_line](#a0bb3bd355218c41e9173f061f46ec997)、[stm32_gpio_irq_line_t](#a52c69f3ce04242217e00981c1315a374)。

禁用指定中断线（Line）的 GPIO 中断。

<a id="r_a23b9ea466101b4367232237ab5a9a42f"></a>

```c
void stm32_gpio_intc_select_line_trigger (stm32_gpio_irq_line_t line, uint32_t trg)
```

相关声明：[stm32_gpio_intc_select_line_trigger](#a23b9ea466101b4367232237ab5a9a42f)、[stm32_gpio_irq_line_t](#a52c69f3ce04242217e00981c1315a374)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为指定 GPIO 中断线选择触发方式（Trigger）。

<a id="r_a4a750e87f445487c517f24a0266f6a4b"></a>

```c
int stm32_gpio_intc_set_irq_callback (stm32_gpio_irq_line_t line, stm32_gpio_irq_cb_t cb, void *user)
```

相关声明：[stm32_gpio_intc_set_irq_callback](#a4a750e87f445487c517f24a0266f6a4b)、[stm32_gpio_irq_line_t](#a52c69f3ce04242217e00981c1315a374)、[stm32_gpio_irq_cb_t](#a69ad9c575223c813f484423e56200560)。

设置在指定 GPIO 中断线发生中断时调用的回调（Callback）。

<a id="r_a21b0c2213fbcdf179c8b4bdb29561863"></a>

```c
void stm32_gpio_intc_remove_irq_callback (stm32_gpio_irq_line_t line)
```

相关声明：[stm32_gpio_intc_remove_irq_callback](#a21b0c2213fbcdf179c8b4bdb29561863)、[stm32_gpio_irq_line_t](#a52c69f3ce04242217e00981c1315a374)。

移除指定外部中断线（EXTI Line）的中断回调。

## 7.4\_详细说明（Detailed Documentation）

<a id="a69ad9c575223c813f484423e56200560"></a>

### `stm32_gpio_irq_cb_t`

```c
typedef void(* stm32_gpio_irq_cb_t) (gpio_port_pins_t pin, void *user)
```

GPIO 中断回调函数签名（Interrupt Callback Signature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pin` | 发生中断的 GPIO 引脚（Pin）。 |
| `user` | 提供给 `stm32_gpio_intc_set_irq_callback` 的数据。 |

**说明（Note）**：注意：此回调在中断服务例程上下文（ISR Context）中调用。

<a id="a52c69f3ce04242217e00981c1315a374"></a>

### `stm32_gpio_irq_line_t`

```c
typedef uint32_t stm32_gpio_irq_line_t
```

STM32 微控制器（MCU）的通用输入输出中断控制器（GPIO Interrupt Controller）API。

此 API 用于与 STM32 微控制器的 GPIO 中断控制器（Interrupt Controller）交互。

表示 GPIO 中断线的不透明类型（Opaque Type）。

<a id="a8f9c3db22937ebe4382215227c410b61"></a>

### `stm32_gpio_irq_trigger`

```c
enum stm32_gpio_irq_trigger
```

GPIO 中断触发标志（Interrupt Trigger Flags）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `STM32_GPIO_IRQ_TRIG_NONE` |  |
| `STM32_GPIO_IRQ_TRIG_RISING` |  |
| `STM32_GPIO_IRQ_TRIG_FALLING` |  |
| `STM32_GPIO_IRQ_TRIG_BOTH` |  |
| `STM32_GPIO_IRQ_TRIG_HIGH_LEVEL` |  |
| `STM32_GPIO_IRQ_TRIG_LOW_LEVEL` |  |

<a id="a0bb3bd355218c41e9173f061f46ec997"></a>

### `stm32_gpio_intc_disable_line()`

```c
void stm32_gpio_intc_disable_line ( stm32_gpio_irq_line_t line)
```

禁用指定中断线（Line）的 GPIO 中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `line` | GPIO 中断线（Interrupt Line）。 |

<a id="ad1c9359de9847ebd2670987302c48f8d"></a>

### `stm32_gpio_intc_enable_line()`

```c
void stm32_gpio_intc_enable_line ( stm32_gpio_irq_line_t line)
```

使能指定中断线（Line）的 GPIO 中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `line` | GPIO 中断线（Interrupt Line）。 |

<a id="a03badd2828ca67e3f8adadc75fec2bd2"></a>

### `stm32_gpio_intc_get_pin_irq_line()`

```c
stm32_gpio_irq_line_t stm32_gpio_intc_get_pin_irq_line ( uint32_t port, gpio_pin_t pin )
```

获取 GPIO 端口 `port` 上指定引脚对应的 GPIO 中断线值（Interrupt Line Value）。

<a id="a21b0c2213fbcdf179c8b4bdb29561863"></a>

### `stm32_gpio_intc_remove_irq_callback()`

```c
void stm32_gpio_intc_remove_irq_callback ( stm32_gpio_irq_line_t line)
```

移除指定外部中断线（EXTI Line）的中断回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `line` | 外部中断线（EXTI Interrupt Line）。 |

<a id="a23b9ea466101b4367232237ab5a9a42f"></a>

### `stm32_gpio_intc_select_line_trigger()`

```c
void stm32_gpio_intc_select_line_trigger ( stm32_gpio_irq_line_t line, uint32_t trg )
```

为指定 GPIO 中断线选择触发方式（Trigger）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `line` | GPIO 中断线（Interrupt Line）。 |
| `trg` | 中断触发方式（Interrupt Trigger），参见 `stm32_gpio_irq_trigger`。 |

<a id="a4a750e87f445487c517f24a0266f6a4b"></a>

### `stm32_gpio_intc_set_irq_callback()`

```c
int stm32_gpio_intc_set_irq_callback ( stm32_gpio_irq_line_t line, stm32_gpio_irq_cb_t cb, void * user )
```

设置在指定 GPIO 中断线发生中断时调用的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `line` | GPIO 中断线（Interrupt Line）。 |
| `cb` | 中断回调函数（Interrupt Callback Function）。 |
| `user` | 供回调使用的自定义用户数据（Custom User Data）。 |

**返回（Returns）**：返回值：成功返回 0；若 `line` 已设置回调则返回 `-EBUSY`。


## 7.5\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [查看此文件的源码。](../api_source_network_reference/P007_gpio_intc_stm32.h_源码浏览.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)
- [gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a8f9c3db22937ebe4382215227c410b61adb4cda594aec45886263f14968e6b3d2"></a>
<a id="a8f9c3db22937ebe4382215227c410b61a601ac25a6a83f5a01dc8ce8bb8f547ae"></a>
<a id="a8f9c3db22937ebe4382215227c410b61a2d20b462dad9d074ce7bb1479d3066c9"></a>
<a id="a8f9c3db22937ebe4382215227c410b61a46af906f79e53b4301c50292840bd301"></a>
<a id="a8f9c3db22937ebe4382215227c410b61a961343f06deca1a4ae9288b81e167048"></a>
<a id="a8f9c3db22937ebe4382215227c410b61a2a13de1280bfac5e1cb484db56843e2c"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_zephyr__mgmt__ec_host_cmd__ec_host_cmd.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__drivers__interrupt_controller__intel_vtd.h_文件参考.md)
