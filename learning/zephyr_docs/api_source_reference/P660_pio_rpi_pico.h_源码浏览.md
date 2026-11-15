---
id: learning.zephyr-docs.api-source-reference.page-660
title: pio_rpi_pico.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pio__rpi__pico_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第660章\_pio\_rpi\_pico.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pio__rpi__pico_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pio__rpi__pico_8h.html)。

## 660.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="foldopen00117"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="foldopen00133"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="foldopen00142"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="foldopen00151"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="adevicetree_2gpio_8h_html"></a>
<a id="agroup__pio__rpi__pico__interface_html_gac3c70836b493b3fd535ea073c1f7d55b"></a>
<a id="agroup__pio__rpi__pico__interface_html_gad9607572a90350fc3c6cf818e3efa99a"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_aca2d801eb15996cf1c74dc65cfa651fc"></a>

```c
/*
 * Copyright (c) 2023 Tokita, Hiroshi <tokita.hiroshi@fujitsu.com>
 * Copyright (c) 2023 Yonatan Schachter
 * Copyright (c) 2023 Ionut Pavel <iocapa@iocapa.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MISC_PIO_RPI_PICO_PIO_RPI_PICO_H_
#define ZEPHYR_INCLUDE_DRIVERS_MISC_PIO_RPI_PICO_PIO_RPI_PICO_H_


#include <zephyr/devicetree/gpio.h>

#include <hardware/pio.h>

#define RPI_PICO_PIO_DEFINE_PROGRAM(name, wrap_target, wrap, ...)       \
        static const uint32_t name ## _wrap_target = wrap_target;       \
        static const uint32_t name ## _wrap = wrap;                     \
        static const uint16_t name ## _program_instructions[] = {       \
                __VA_ARGS__                                             \
        };                                                              \
        static const struct pio_program name ## _program = {            \
                .instructions = name ## _program_instructions,          \
                .length = ARRAY_SIZE(name ## _program_instructions),    \
                .origin = -1,                                           \
        }

#define RPI_PICO_PIO_GET_WRAP_TARGET(name) name ## _wrap_target

#define RPI_PICO_PIO_GET_WRAP(name) name ## _wrap

#define RPI_PICO_PIO_GET_PROGRAM(name) &name ## _program

#define DT_RPI_PICO_PIO_PIN_BY_NAME(node_id, p_name, p_idx, g_name, g_idx)                      \
        RP2_GET_PIN_NUM(DT_PROP_BY_IDX(                                                         \
                DT_CHILD(DT_PINCTRL_BY_NAME(node_id, p_name, p_idx), g_name), pinmux, g_idx))

#define DT_INST_RPI_PICO_PIO_PIN_BY_NAME(inst, p_name, p_idx, g_name, g_idx)                    \
        DT_RPI_PICO_PIO_PIN_BY_NAME(DT_DRV_INST(inst), p_name, p_idx, g_name, g_idx)

#define DT_INST_PIO_PIN_BY_NAME(inst, name) \
        DT_PIO_PIN_BY_NAME(DT_DRV_INST(inst), name)

static inline PIO pio_rpi_pico_get_pio(const struct device *dev)
{
        return *(PIO *)(dev->config);
}

int pio_rpi_pico_allocate_sm(const struct device *dev, size_t *sm);


#endif /* ZEPHYR_INCLUDE_DRIVERS_MISC_PIO_RPI_PICO_PIO_RPI_PICO_H_ */
```

## 660.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Tokita, Hiroshi <tokita.hiroshi@fujitsu.com>。

版权（Copyright）：© 2023 Yonatan Schachter。

版权（Copyright）：© 2023 Ionut Pavel <iocapa@iocapa.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 170 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MISC_PIO_RPI_PICO_PIO_RPI_PICO_H_`。

## 660.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pio__rpi__pico_8h.html)
- [zephyr/devicetree/gpio.h](../dt_peripheral_reference/P001_GPIO设备树头文件参考.md)
- [pio_rpi_pico_get_pio](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#gad9607572a90350fc3c6cf818e3efa99a)
- [device](../device_reference/P002_设备对象结构.md)
- [config](../device_reference/P002_设备对象结构.md#aca2d801eb15996cf1c74dc65cfa651fc)
- [pio_rpi_pico_allocate_sm](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html#gac3c70836b493b3fd535ea073c1f7d55b)
- [gpio.h](../dt_peripheral_reference/P001_GPIO设备树头文件参考.md)
- [device::config](../device_reference/P002_设备对象结构.md#aca2d801eb15996cf1c74dc65cfa651fc)

---

[上一章](P659_pinctrl_soc_sam_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P661_pipelink.h_源码浏览.md)
