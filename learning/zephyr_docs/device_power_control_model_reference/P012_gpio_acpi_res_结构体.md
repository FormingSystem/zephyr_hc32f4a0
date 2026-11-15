---
id: learning.zephyr-docs.device-power-control-model-reference.page-12
title: gpio_acpi_res_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgpio__acpi__res.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_gpio\_acpi\_res\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__acpi__res.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/gpio/gpio_intel.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_af89b2304ea9cfabeddc487d84c2297a9"></a>

```c
uint8_t num_pins
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_pins](#af89b2304ea9cfabeddc487d84c2297a9)。

<a id="r_a85c88312042b134a2f80f63853c086fa"></a>

```c
uint32_t pad_base
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pad_base](#a85c88312042b134a2f80f63853c086fa)。

<a id="r_ac0f83a85d2ff41fbc9f1b598d1ca4036"></a>

```c
uint32_t host_owner_reg
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[host_owner_reg](#ac0f83a85d2ff41fbc9f1b598d1ca4036)。

<a id="r_a53c789cbddde23ec54c39af61ee433fa"></a>

```c
uint32_t pad_owner_reg
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pad_owner_reg](#a53c789cbddde23ec54c39af61ee433fa)。

<a id="r_aa912c56ae09d4ef0fc0467b03091b8ef"></a>

```c
uint32_t intr_stat_reg
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[intr_stat_reg](#aa912c56ae09d4ef0fc0467b03091b8ef)。

<a id="r_a82ef9374bee9aeda5b825cf5179057e8"></a>

```c
uint16_t base_num
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[base_num](#a82ef9374bee9aeda5b825cf5179057e8)。

<a id="r_ad4738c083000ac8f4aa6770082c2ddbb"></a>

```c
uintptr_t reg_base
```

相关声明：[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)、[reg_base](#ad4738c083000ac8f4aa6770082c2ddbb)。

## 12.2\_详细说明（Detailed Documentation）

<a id="a82ef9374bee9aeda5b825cf5179057e8"></a>

### `base_num`

```c
uint16_t gpio_acpi_res::base_num
```

<a id="ac0f83a85d2ff41fbc9f1b598d1ca4036"></a>

### `host_owner_reg`

```c
uint32_t gpio_acpi_res::host_owner_reg
```

<a id="aa912c56ae09d4ef0fc0467b03091b8ef"></a>

### `intr_stat_reg`

```c
uint32_t gpio_acpi_res::intr_stat_reg
```

<a id="af89b2304ea9cfabeddc487d84c2297a9"></a>

### `num_pins`

```c
uint8_t gpio_acpi_res::num_pins
```

<a id="a85c88312042b134a2f80f63853c086fa"></a>

### `pad_base`

```c
uint32_t gpio_acpi_res::pad_base
```

<a id="a53c789cbddde23ec54c39af61ee433fa"></a>

### `pad_owner_reg`

```c
uint32_t gpio_acpi_res::pad_owner_reg
```

<a id="ad4738c083000ac8f4aa6770082c2ddbb"></a>

### `reg_base`

```c
uintptr_t gpio_acpi_res::reg_base
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/gpio/gpio_intel.h`

## 12.3\_原页交叉引用（Cross References）

- [zephyr/drivers/gpio/gpio_intel.h](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intel_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_fuel_gauge_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P013_gpio_cmsdk_ahb_结构体.md)
