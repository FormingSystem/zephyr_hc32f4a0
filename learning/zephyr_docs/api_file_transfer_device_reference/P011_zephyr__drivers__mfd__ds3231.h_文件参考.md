---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-11
title: zephyr__drivers__mfd__ds3231.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ds3231_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_drivers\_\_mfd\_\_ds3231.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ds3231_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/i2c.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.1\_函数（Functions）

<a id="r_aa7f2419f0d2555e24cd94ed8c7b67ccf"></a>

```c
int mfd_ds3231_i2c_get_registers (const struct device *dev, uint8_t start_reg, uint8_t *buf, const size_t buf_size)
```

相关声明：[mfd_ds3231_i2c_get_registers](#aa7f2419f0d2555e24cd94ed8c7b67ccf)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从给定寄存器地址（Register Address）开始，读取 I2C 设备上指定数量的寄存器。

<a id="r_a478705fd7794fa3002ac36fb2fcef17e"></a>

```c
int mfd_ds3231_i2c_set_registers (const struct device *dev, uint8_t start_reg, const uint8_t *buf, const size_t buf_size)
```

相关声明：[mfd_ds3231_i2c_set_registers](#a478705fd7794fa3002ac36fb2fcef17e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在给定寄存器地址（Register Address）处设置 I2C 设备的寄存器。

## 11.2\_详细说明（Detailed Documentation）

<a id="aa7f2419f0d2555e24cd94ed8c7b67ccf"></a>

### `mfd_ds3231_i2c_get_registers()`

```c
int mfd_ds3231_i2c_get_registers ( const struct device * dev, uint8_t start_reg, uint8_t * buf, const size_t buf_size )
```

从给定寄存器地址（Register Address）开始，读取 I2C 设备上指定数量的寄存器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | DS3231 多功能设备（MFD）。 |
| `start_reg` | 起始寄存器地址（Register Address）。 |
| `buf` | 用于存储结果的缓冲区数组指针（Buffer Array Pointer）。 |
| `buf_size` | 要返回的寄存器值（Register Values）数量。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 发生任何总线错误（Bus Error）时。 |

<a id="a478705fd7794fa3002ac36fb2fcef17e"></a>

### `mfd_ds3231_i2c_set_registers()`

```c
int mfd_ds3231_i2c_set_registers ( const struct device * dev, uint8_t start_reg, const uint8_t * buf, const size_t buf_size )
```

在给定寄存器地址（Register Address）处设置 I2C 设备的寄存器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | DS3231 多功能设备（MFD）。 |
| `start_reg` | 要设置的寄存器地址（Register Address）。 |
| `buf` | 要写入给定地址的值（Value）。 |
| `buf_size` | 要写入给定地址的缓冲区大小（Buffer Size）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 发生任何总线错误（Bus Error）时。 |


## 11.3\_原页交叉引用（Cross References）

- [zephyr/drivers/i2c.h](../i2c_driver_reference/P002_I2C驱动头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P185_ds3231.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_zephyr__drivers__sensor__tmp11x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__dsp__utils.h_文件参考.md)
