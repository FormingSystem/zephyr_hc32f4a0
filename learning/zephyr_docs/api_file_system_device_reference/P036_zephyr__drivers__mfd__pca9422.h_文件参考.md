---
id: learning.zephyr-docs.api-file-system-device-reference.page-36
title: zephyr__drivers__mfd__pca9422.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pca9422_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_zephyr\_\_drivers\_\_mfd\_\_pca9422.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pca9422_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stddef.h>
#include <stdint.h>
#include <zephyr/device.h>
```

查看此文件的源码。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 36.1\_类型定义（Typedefs）

<a id="r_gaf38501b5aa1350ebc2c03be9b6623353"></a>

```c
typedef void(* child_isr_t) (const struct device *dev)
```

相关声明：[child_isr_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#gaf38501b5aa1350ebc2c03be9b6623353)、[device](../device_reference/P002_设备对象结构.md)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 36.2\_枚举（Enumerations）

<a id="r_gae4d56fd30130dc4f332ecf43465a1558"></a>

```c
enum child_dev { PCA9422_DEV_REG = 0 , PCA9422_DEV_CHG , PCA9422_DEV_FG , PCA9422_DEV_MAX }
```

相关声明：[child_dev](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#gae4d56fd30130dc4f332ecf43465a1558)、[PCA9422_DEV_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#ggae4d56fd30130dc4f332ecf43465a1558a739091e8b24f33c0bb664a0636b345e3)、[PCA9422_DEV_CHG](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#ggae4d56fd30130dc4f332ecf43465a1558a32ebd0d53e721a4b2919018ee79d1349)、[PCA9422_DEV_FG](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#ggae4d56fd30130dc4f332ecf43465a1558a82543ee068c506d1a20e0eca2da59b24)、[PCA9422_DEV_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#ggae4d56fd30130dc4f332ecf43465a1558a041d23d899944b926aac7ced7ea3c316)。

PCA9422 的子设备（child device）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 36.3\_函数（Functions）

<a id="r_gaf58a47f2af68b27031f321010cc50dfb"></a>

```c
void mfd_pca9422_set_irqhandler (const struct device *dev, const struct device *child_dev, enum child_dev child_idx, child_isr_t handler)
```

相关声明：[mfd_pca9422_set_irqhandler](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#gaf58a47f2af68b27031f321010cc50dfb)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[child_dev](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gae4d56fd30130dc4f332ecf43465a1558)、[child_dev](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gae4d56fd30130dc4f332ecf43465a1558)、[child_isr_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#gaf38501b5aa1350ebc2c03be9b6623353)。

设置 PCA9422 子设备中断处理函数。

<a id="r_ga59e71a4771a3c99a44ce09ecd50b4ad2"></a>

```c
int mfd_pca9422_reg_burst_read (const struct device *dev, uint8_t reg, uint8_t *value, size_t len)
```

相关声明：[mfd_pca9422_reg_burst_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#ga59e71a4771a3c99a44ce09ecd50b4ad2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 PCA9422 读取多个寄存器。

<a id="r_ga12d405f7493f59e3b6c9629c92d56b54"></a>

```c
int mfd_pca9422_reg_read_byte (const struct device *dev, uint8_t reg, uint8_t *value)
```

相关声明：[mfd_pca9422_reg_read_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#ga12d405f7493f59e3b6c9629c92d56b54)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 PCA9422 读取单个寄存器。

<a id="r_gac88f26da112e9218380450ca8803ff57"></a>

```c
int mfd_pca9422_reg_burst_write (const struct device *dev, uint8_t reg, uint8_t *value, size_t len)
```

相关声明：[mfd_pca9422_reg_burst_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#gac88f26da112e9218380450ca8803ff57)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 PCA9422 写入多个寄存器。

<a id="r_ga04842dc1123f6702551d559034b6a511"></a>

```c
int mfd_pca9422_reg_write_byte (const struct device *dev, uint8_t reg, uint8_t value)
```

相关声明：[mfd_pca9422_reg_write_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#ga04842dc1123f6702551d559034b6a511)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 PCA9422 写入单个寄存器。

<a id="r_ga481356b77b7056567ebc3234980bf578"></a>

```c
int mfd_pca9422_reg_update_byte (const struct device *dev, uint8_t reg, uint8_t mask, uint8_t value)
```

相关声明：[mfd_pca9422_reg_update_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#ga481356b77b7056567ebc3234980bf578)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新 PCA9422 寄存器中的选定位。


## 36.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P648_pca9422.h_源码浏览.md)
- [child_isr_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#gaf38501b5aa1350ebc2c03be9b6623353)
- [device](../device_reference/P002_设备对象结构.md)
- [child_dev](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#gae4d56fd30130dc4f332ecf43465a1558)
- [PCA9422_DEV_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#ggae4d56fd30130dc4f332ecf43465a1558a739091e8b24f33c0bb664a0636b345e3)
- [PCA9422_DEV_CHG](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#ggae4d56fd30130dc4f332ecf43465a1558a32ebd0d53e721a4b2919018ee79d1349)
- [PCA9422_DEV_FG](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#ggae4d56fd30130dc4f332ecf43465a1558a82543ee068c506d1a20e0eca2da59b24)
- [PCA9422_DEV_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#ggae4d56fd30130dc4f332ecf43465a1558a041d23d899944b926aac7ced7ea3c316)
- [mfd_pca9422_set_irqhandler](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#gaf58a47f2af68b27031f321010cc50dfb)
- [child_dev](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gae4d56fd30130dc4f332ecf43465a1558)
- [mfd_pca9422_reg_burst_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#ga59e71a4771a3c99a44ce09ecd50b4ad2)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mfd_pca9422_reg_read_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#ga12d405f7493f59e3b6c9629c92d56b54)
- [mfd_pca9422_reg_burst_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#gac88f26da112e9218380450ca8803ff57)
- [mfd_pca9422_reg_write_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#ga04842dc1123f6702551d559034b6a511)
- [mfd_pca9422_reg_update_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__pca9422.html#ga481356b77b7056567ebc3234980bf578)

---

[上一章](P035_zephyr__dt-bindings__interrupt-controller__openisa-intmux.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P037_zephyr__drivers__sensor__pcnt_esp32.h_文件参考.md)
