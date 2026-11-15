---
id: learning.zephyr-docs.api-file-service-interface-reference.page-42
title: zephyr__drivers__misc__pio_rpi_pico__pio_rpi_pico.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pio__rpi__pico_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_zephyr\_\_drivers\_\_misc\_\_pio\_rpi\_pico\_\_pio\_rpi\_pico.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pio__rpi__pico_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Raspberry Pi Pico可编程输入输出（PIO）驱动的头文件。

<a id="details"></a>

```c
#include <zephyr/devicetree/gpio.h>
#include <hardware/pio.h>
```

查看此文件的源码。

Raspberry Pi Pico可编程输入输出（PIO）驱动的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 42.1\_宏定义（Macros）

<a id="r_ga744449bb6c1a409a9d8677c66667ea9b"></a>

```c
#define RPI_PICO_PIO_DEFINE_PROGRAM(name, wrap_target, wrap, ...)
```

相关声明：[RPI_PICO_PIO_DEFINE_PROGRAM](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#ga744449bb6c1a409a9d8677c66667ea9b)。

定义可编程输入输出（PIO）程序的辅助宏（Utility Macro）。

<a id="r_ga0d74a21471e301563224d4673ca1a738"></a>

```c
#define RPI_PICO_PIO_GET_WRAP_TARGET(name)
```

相关声明：[RPI_PICO_PIO_GET_WRAP_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#ga0d74a21471e301563224d4673ca1a738)。

获取程序回绕目标（Wrap Target）的辅助宏（Utility Macro）。

<a id="r_ga5cc3f015332a73cba6141e94b8fbe67e"></a>

```c
#define RPI_PICO_PIO_GET_WRAP(name)
```

相关声明：[RPI_PICO_PIO_GET_WRAP](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#ga5cc3f015332a73cba6141e94b8fbe67e)。

获取程序回绕源（Wrap Source）的辅助宏（Utility Macro）。

<a id="r_ga989341427ba2e681aba5c4d702d91927"></a>

```c
#define RPI_PICO_PIO_GET_PROGRAM(name)
```

相关声明：[RPI_PICO_PIO_GET_PROGRAM](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#ga989341427ba2e681aba5c4d702d91927)。

获取 PIO 程序指针的辅助宏（Utility Macro）。

<a id="r_ga482acc1e13f4b6ef96f55a2c9e3b7a07"></a>

```c
#define DT_RPI_PICO_PIO_PIN_BY_NAME(node_id, p_name, p_idx, g_name, g_idx)
```

相关声明：[DT_RPI_PICO_PIO_PIN_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#ga482acc1e13f4b6ef96f55a2c9e3b7a07)。

根据引脚控制（Pinctrl）／组名称和索引获取引脚编号。

<a id="r_gaa3620b14a4d34eed3302048d58a86893"></a>

```c
#define DT_INST_RPI_PICO_PIO_PIN_BY_NAME(inst, p_name, p_idx, g_name, g_idx)
```

相关声明：[DT_INST_RPI_PICO_PIO_PIN_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#gaa3620b14a4d34eed3302048d58a86893)。

根据引脚控制（Pinctrl）／组名称和索引获取引脚编号。

<a id="r_gad2aef23ab08361004bba9209f9e612c1"></a>

```c
#define DT_INST_PIO_PIN_BY_NAME(inst, name)
```

相关声明：[DT_INST_PIO_PIN_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#gad2aef23ab08361004bba9209f9e612c1)。

根据引脚名称获取引脚编号（Pin Number）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 42.2\_函数（Functions）

<a id="r_gad9607572a90350fc3c6cf818e3efa99a"></a>

```c
static PIO pio_rpi_pico_get_pio (const struct device *dev)
```

相关声明：[pio_rpi_pico_get_pio](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#gad9607572a90350fc3c6cf818e3efa99a)、[device](../device_reference/P002_设备对象结构.md)。

获取可编程输入输出（PIO）对象。

<a id="r_gac3c70836b493b3fd535ea073c1f7d55b"></a>

```c
int pio_rpi_pico_allocate_sm (const struct device *dev, size_t *sm)
```

相关声明：[pio_rpi_pico_allocate_sm](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#gac3c70836b493b3fd535ea073c1f7d55b)、[device](../device_reference/P002_设备对象结构.md)。

分配状态机（State Machine）。


## 42.3\_原页交叉引用（Cross References）

- [zephyr/devicetree/gpio.h](../dt_peripheral_reference/P002_GPIO设备树头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P660_pio_rpi_pico.h_源码浏览.md)
- [RPI_PICO_PIO_DEFINE_PROGRAM](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#ga744449bb6c1a409a9d8677c66667ea9b)
- [RPI_PICO_PIO_GET_WRAP_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#ga0d74a21471e301563224d4673ca1a738)
- [RPI_PICO_PIO_GET_WRAP](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#ga5cc3f015332a73cba6141e94b8fbe67e)
- [RPI_PICO_PIO_GET_PROGRAM](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#ga989341427ba2e681aba5c4d702d91927)
- [DT_RPI_PICO_PIO_PIN_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#ga482acc1e13f4b6ef96f55a2c9e3b7a07)
- [DT_INST_RPI_PICO_PIO_PIN_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#gaa3620b14a4d34eed3302048d58a86893)
- [DT_INST_PIO_PIN_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#gad2aef23ab08361004bba9209f9e612c1)
- [pio_rpi_pico_get_pio](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#gad9607572a90350fc3c6cf818e3efa99a)
- [device](../device_reference/P002_设备对象结构.md)
- [pio_rpi_pico_allocate_sm](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#gac3c70836b493b3fd535ea073c1f7d55b)

<a id="header-details"></a>

---

[上一章](P041_zephyr__dt-bindings__gpio__nordic-npm13xx-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P043_zephyr__drivers__pwm__max2221x.h_文件参考.md)
