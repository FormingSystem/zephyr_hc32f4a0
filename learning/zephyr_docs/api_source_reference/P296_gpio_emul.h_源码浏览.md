---
id: learning.zephyr-docs.api-source-reference.page-296
title: gpio_emul.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__emul_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第296章\_gpio\_emul.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gpio__emul_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gpio__emul_8h.html)。

## 296.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00046"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00070"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00088"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="foldopen00115"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="foldopen00139"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="foldopen00172"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="agroup__gpio__emul_html_ga3962e337bc22e532f2c181724621fcf8"></a>
<a id="agroup__gpio__emul_html_ga5fdc3ebb295074bb5befeaaa75f05da0"></a>
<a id="agroup__gpio__emul_html_ga781faaeb7570b8cc1095ebe99c3efdf9"></a>
<a id="agroup__gpio__emul_html_ga86bd5ff4f557e4d520a4f760fb74cdd5"></a>
<a id="agroup__gpio__emul_html_gaa62613aa6eb442d2c4e436893316124f"></a>
<a id="agroup__gpio__emul_html_gaa6e4c5c2c53d421e9635c0a977172205"></a>
<a id="agroup__gpio__emul_html_gaa7eae6a0f85d0f0fb6a8aa41329f4709"></a>
<a id="agroup__gpio__emul_html_gab937159126e992126de136f6b1523191"></a>
<a id="agroup__gpio__interface_html_ga38179eb7a46a743c12cfac28f347fb34"></a>
<a id="agroup__gpio__interface_html_ga5f5cb5e7dae6d58e072bb450af029d2e"></a>
<a id="agroup__gpio__interface_html_ga7f40ed51f14fd8000e9b52ab347b273f"></a>
<a id="agroup__gpio__interface_html_gabcebe24c93486896e1dfc2459ec25693"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astructdevice_html"></a>
<a id="astructgpio__dt__spec_html"></a>
<a id="astructgpio__dt__spec_html_a5d617d47e2f568c7a4402a8f5a40ed4f"></a>
<a id="astructgpio__dt__spec_html_ad7e6fbb0cba0be94a47d4f2add056c84"></a>

```c
/*
 * Copyright (c) 2020 Friedt Professional Engineering Services, Inc
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_EMUL_H_
#define ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_EMUL_H_

#include <zephyr/types.h>
#include <zephyr/drivers/gpio.h>

#ifdef __cplusplus
extern "C" {
#endif


int gpio_emul_input_set_masked(const struct device *port, gpio_port_pins_t pins,
                              gpio_port_value_t values);

static inline int gpio_emul_input_set(const struct device *port, gpio_pin_t pin,
                                     int value)
{
        return gpio_emul_input_set_masked(port, BIT(pin), value ? BIT(pin) : 0);
}

static inline int gpio_emul_input_set_dt(const struct gpio_dt_spec *spec, int value)
{
        return gpio_emul_input_set(spec->port, spec->pin, value);
}

int gpio_emul_output_get_masked(const struct device *port, gpio_port_pins_t pins,
                               gpio_port_value_t *values);

static inline int gpio_emul_output_get(const struct device *port, gpio_pin_t pin)
{
        int ret;
        gpio_port_value_t values;

        ret = gpio_emul_output_get_masked(port, BIT(pin), &values);
        if (ret == 0) {
                ret = (values & BIT(pin)) ? 1 : 0;
        }

        return ret;
}

static inline int gpio_emul_output_get_dt(const struct gpio_dt_spec *spec)
{
        return gpio_emul_output_get(spec->port, spec->pin);
}

int gpio_emul_flags_get(const struct device *port, gpio_pin_t pin, gpio_flags_t *flags);

static inline int gpio_emul_flags_get_dt(const struct gpio_dt_spec *spec, gpio_flags_t *flags)
{
        return gpio_emul_flags_get(spec->port, spec->pin, flags);
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_EMUL_H_ */
```

## 296.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Friedt Professional Engineering Services, Inc。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 185 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_EMUL_H_`。

## 296.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gpio__emul_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [gpio_emul_input_set_masked](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gaa7eae6a0f85d0f0fb6a8aa41329f4709)
- [device](../device_reference/P002_设备对象结构.md)
- [gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)
- [gpio_port_value_t](../hardware/P266_GPIO公共接口.md#gabcebe24c93486896e1dfc2459ec25693)
- [gpio_emul_input_set](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga3962e337bc22e532f2c181724621fcf8)
- [gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [gpio_emul_input_set_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gab937159126e992126de136f6b1523191)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [port](../hardware/P267_GPIO设备树描述.md#a5d617d47e2f568c7a4402a8f5a40ed4f)
- [pin](../hardware/P267_GPIO设备树描述.md#ad7e6fbb0cba0be94a47d4f2add056c84)
- [gpio_emul_output_get_masked](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gaa6e4c5c2c53d421e9635c0a977172205)
- [gpio_emul_output_get](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gaa62613aa6eb442d2c4e436893316124f)
- [gpio_emul_output_get_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga5fdc3ebb295074bb5befeaaa75f05da0)
- [gpio_emul_flags_get](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga86bd5ff4f557e4d520a4f760fb74cdd5)
- [gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [gpio_emul_flags_get_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga781faaeb7570b8cc1095ebe99c3efdf9)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [gpio_dt_spec::port](../hardware/P267_GPIO设备树描述.md#a5d617d47e2f568c7a4402a8f5a40ed4f)
- [gpio_dt_spec::pin](../hardware/P267_GPIO设备树描述.md#ad7e6fbb0cba0be94a47d4f2add056c84)

---

[上一章](P295_gpio_ambiq.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P297_gpio_intel.h_源码浏览.md)
