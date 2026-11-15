---
id: learning.zephyr-docs.api-file-host-video-reference.page-8
title: zephyr__drivers__interrupt_controller__intel_vtd.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intel\_vtd.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/pcie/msi.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

<a id="r_vtd_5Fdriver_5Fapi"></a>

```c
struct vtd_driver_api
```

相关声明：[vtd_driver_api](../platform_security_model_reference/P074_vtd_driver_api_结构体.md)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.2\_类型定义（Typedefs）

<a id="r_a3bded96a42bec41476ff6bc9f75676b4"></a>

```c
typedef int(* vtd_alloc_entries_f) (const struct device *dev, uint8_t n_entries)
```

相关声明：[vtd_alloc_entries_f](#a3bded96a42bec41476ff6bc9f75676b4)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_aadb69e257884026693109510e20dc2b4"></a>

```c
typedef uint32_t(* vtd_remap_msi_f) (const struct device *dev, msi_vector_t *vector, uint8_t n_vector)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[vtd_remap_msi_f](#aadb69e257884026693109510e20dc2b4)、[device](../device_reference/P002_设备对象结构.md)、[msi_vector_t](../api_vector_pipeline_topic_reference/P025_PCIe 主机消息信号中断（MSI）接口.md#ga9ede6a7a472ee62f0975256a1b5f1231)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_afefa59b2064053d90445127da9b64bfb"></a>

```c
typedef int(* vtd_remap_f) (const struct device *dev, uint8_t irte_idx, uint16_t vector, uint32_t flags, uint16_t src_id)
```

相关声明：[vtd_remap_f](#afefa59b2064053d90445127da9b64bfb)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

<a id="r_a06190d6273d0adeb92e9e4e4fa79d9b4"></a>

```c
typedef int(* vtd_set_irte_vector_f) (const struct device *dev, uint8_t irte_idx, uint16_t vector)
```

相关声明：[vtd_set_irte_vector_f](#a06190d6273d0adeb92e9e4e4fa79d9b4)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

<a id="r_a944bfa2dc643fd3ff182eee12d836ae5"></a>

```c
typedef int(* vtd_get_irte_by_vector_f) (const struct device *dev, uint16_t vector)
```

相关声明：[vtd_get_irte_by_vector_f](#a944bfa2dc643fd3ff182eee12d836ae5)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

<a id="r_af3ddf5e22fcb4956e4887e1982fae28e"></a>

```c
typedef uint16_t(* vtd_get_irte_vector_f) (const struct device *dev, uint8_t irte_idx)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[vtd_get_irte_vector_f](#af3ddf5e22fcb4956e4887e1982fae28e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_a63733309814847ba4204776e8ace9a85"></a>

```c
typedef int(* vtd_set_irte_irq_f) (const struct device *dev, uint8_t irte_idx, unsigned int irq)
```

相关声明：[vtd_set_irte_irq_f](#a63733309814847ba4204776e8ace9a85)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

<a id="r_a0a2e483fe9159a46d6265b257841f43a"></a>

```c
typedef int(* vtd_get_irte_by_irq_f) (const struct device *dev, unsigned int irq)
```

相关声明：[vtd_get_irte_by_irq_f](#a0a2e483fe9159a46d6265b257841f43a)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

<a id="r_a0118f224100f721a508ce00c3ae99698"></a>

```c
typedef void(* vtd_set_irte_msi_f) (const struct device *dev, uint8_t irte_idx, bool msi)
```

相关声明：[vtd_set_irte_msi_f](#a0118f224100f721a508ce00c3ae99698)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

<a id="r_a622083e8841c3899ca7b7156f526581f"></a>

```c
typedef bool(* vtd_irte_is_msi_f) (const struct device *dev, uint8_t irte_idx)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[vtd_irte_is_msi_f](#a622083e8841c3899ca7b7156f526581f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.3\_函数（Functions）

<a id="r_a87b1cea7c86d724da0c379bfd3742879"></a>

```c
static int vtd_allocate_entries (const struct device *dev, uint8_t n_entries)
```

相关声明：[vtd_allocate_entries](#a87b1cea7c86d724da0c379bfd3742879)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

分配连续的中断重映射表项（IRTEs）。

<a id="r_ab7b8ad9dbee740c9e97021853f1131fc"></a>

```c
static uint32_t vtd_remap_msi (const struct device *dev, msi_vector_t *vector, uint8_t n_vector)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[vtd_remap_msi](#ab7b8ad9dbee740c9e97021853f1131fc)、[device](../device_reference/P002_设备对象结构.md)、[msi_vector_t](../api_vector_pipeline_topic_reference/P025_PCIe 主机消息信号中断（MSI）接口.md#ga9ede6a7a472ee62f0975256a1b5f1231)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为所给向量（Vector）生成消息信号中断（MSI）的消息地址数据（Message Address Data）。

<a id="r_a3cc5ff5183e80aeb18115d8b5a541546"></a>

```c
static int vtd_remap (const struct device *dev, uint8_t irte_idx, uint16_t vector, uint32_t flags, uint16_t src_id)
```

相关声明：[vtd_remap](#a3cc5ff5183e80aeb18115d8b5a541546)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

重映射（Remap）所给中断向量。

<a id="r_a342e4745949ed1bd50b4d51de482be57"></a>

```c
static int vtd_set_irte_vector (const struct device *dev, uint8_t irte_idx, uint16_t vector)
```

相关声明：[vtd_set_irte_vector](#a342e4745949ed1bd50b4d51de482be57)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

为已分配的中断重映射表项（IRTE）设置向量。

<a id="r_a4645558c4f9e461e86e6d0caf96311ad"></a>

```c
static int vtd_get_irte_by_vector (const struct device *dev, uint16_t vector)
```

相关声明：[vtd_get_irte_by_vector](#a4645558c4f9e461e86e6d0caf96311ad)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取为所给向量分配的中断重映射表项（IRTE）。

<a id="r_a76d5a655a925c9ec9536e6c906c2192e"></a>

```c
static uint16_t vtd_get_irte_vector (const struct device *dev, uint8_t irte_idx)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[vtd_get_irte_vector](#a76d5a655a925c9ec9536e6c906c2192e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取赋给中断重映射表项（IRTE）的向量。

<a id="r_ab067e306959a0774ee5e896eafab2132"></a>

```c
static int vtd_set_irte_irq (const struct device *dev, uint8_t irte_idx, unsigned int irq)
```

相关声明：[vtd_set_irte_irq](#ab067e306959a0774ee5e896eafab2132)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

为已分配的中断重映射表项（IRTE）设置中断请求（IRQ）。

<a id="r_a214bd683e7331adbe5afbca41e3a6bc9"></a>

```c
static int vtd_get_irte_by_irq (const struct device *dev, unsigned int irq)
```

相关声明：[vtd_get_irte_by_irq](#a214bd683e7331adbe5afbca41e3a6bc9)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

获取为所给中断请求（IRQ）分配的中断重映射表项（IRTE）。

<a id="r_ae81918a2c81e03cc4e02603781e8ca21"></a>

```c
static void vtd_set_irte_msi (const struct device *dev, uint8_t irte_idx, bool msi)
```

相关声明：[vtd_set_irte_msi](#ae81918a2c81e03cc4e02603781e8ca21)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

<a id="r_a82018e41e5bbb12f98c16b0d416596fe"></a>

```c
static bool vtd_irte_is_msi (const struct device *dev, uint8_t irte_idx)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[vtd_irte_is_msi](#a82018e41e5bbb12f98c16b0d416596fe)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

## 8.4\_详细说明（Detailed Documentation）

<a id="a3bded96a42bec41476ff6bc9f75676b4"></a>

### `vtd_alloc_entries_f`

```c
typedef int(* vtd_alloc_entries_f) (const struct device *dev, uint8_t n_entries)
```

<a id="a0a2e483fe9159a46d6265b257841f43a"></a>

### `vtd_get_irte_by_irq_f`

```c
typedef int(* vtd_get_irte_by_irq_f) (const struct device *dev, unsigned int irq)
```

<a id="a944bfa2dc643fd3ff182eee12d836ae5"></a>

### `vtd_get_irte_by_vector_f`

```c
typedef int(* vtd_get_irte_by_vector_f) (const struct device *dev, uint16_t vector)
```

<a id="af3ddf5e22fcb4956e4887e1982fae28e"></a>

### `vtd_get_irte_vector_f`

```c
typedef uint16_t(* vtd_get_irte_vector_f) (const struct device *dev, uint8_t irte_idx)
```

<a id="a622083e8841c3899ca7b7156f526581f"></a>

### `vtd_irte_is_msi_f`

```c
typedef bool(* vtd_irte_is_msi_f) (const struct device *dev, uint8_t irte_idx)
```

<a id="afefa59b2064053d90445127da9b64bfb"></a>

### `vtd_remap_f`

```c
typedef int(* vtd_remap_f) (const struct device *dev, uint8_t irte_idx, uint16_t vector, uint32_t flags, uint16_t src_id)
```

<a id="aadb69e257884026693109510e20dc2b4"></a>

### `vtd_remap_msi_f`

```c
typedef uint32_t(* vtd_remap_msi_f) (const struct device *dev, msi_vector_t *vector, uint8_t n_vector)
```

<a id="a63733309814847ba4204776e8ace9a85"></a>

### `vtd_set_irte_irq_f`

```c
typedef int(* vtd_set_irte_irq_f) (const struct device *dev, uint8_t irte_idx, unsigned int irq)
```

<a id="a0118f224100f721a508ce00c3ae99698"></a>

### `vtd_set_irte_msi_f`

```c
typedef void(* vtd_set_irte_msi_f) (const struct device *dev, uint8_t irte_idx, bool msi)
```

<a id="a06190d6273d0adeb92e9e4e4fa79d9b4"></a>

### `vtd_set_irte_vector_f`

```c
typedef int(* vtd_set_irte_vector_f) (const struct device *dev, uint8_t irte_idx, uint16_t vector)
```

<a id="a87b1cea7c86d724da0c379bfd3742879"></a>

### `vtd_allocate_entries()`

```c
int vtd_allocate_entries ( const struct device * dev, uint8_t n_entries )
```

声明属性：`inline`、`static`。

分配连续的中断重映射表项（IRTEs）。

注意：将尝试全部分配；不能全部分配时即失败。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `n_entries` | 要分配的中断重映射表项（IRTE）数量。 |

**返回（Returns）**：返回值：首个已分配中断重映射表项（IRTE）的索引；失败返回 `-EBUSY`。

<a id="a214bd683e7331adbe5afbca41e3a6bc9"></a>

### `vtd_get_irte_by_irq()`

```c
int vtd_get_irte_by_irq ( const struct device * dev, unsigned int irq )
```

声明属性：`inline`、`static`。

获取为所给中断请求（IRQ）分配的中断重映射表项（IRTE）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `irq` | 有效的中断请求（IRQ）编号。 |

**返回（Returns）**：返回值：成功返回 0 或正值，否则返回负 errno 错误码。

<a id="a4645558c4f9e461e86e6d0caf96311ad"></a>

### `vtd_get_irte_by_vector()`

```c
int vtd_get_irte_by_vector ( const struct device * dev, uint16_t vector )
```

声明属性：`inline`、`static`。

获取为所给向量分配的中断重映射表项（IRTE）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `vector` | 已分配的中断向量（Interrupt Vector）。 |

**返回（Returns）**：返回值：成功返回 0 或正值，否则返回负 errno 错误码。

<a id="a76d5a655a925c9ec9536e6c906c2192e"></a>

### `vtd_get_irte_vector()`

```c
uint16_t vtd_get_irte_vector ( const struct device * dev, uint8_t irte_idx )
```

声明属性：`inline`、`static`。

获取赋给中断重映射表项（IRTE）的向量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `irte_idx` | 先前分配的中断重映射表项（IRTE）索引编号。 |

**返回（Returns）**：返回值：为此中断重映射表项（IRTE）设置的向量。

<a id="a82018e41e5bbb12f98c16b0d416596fe"></a>

### `vtd_irte_is_msi()`

```c
bool vtd_irte_is_msi ( const struct device * dev, uint8_t irte_idx )
```

声明属性：`inline`、`static`。

<a id="a3cc5ff5183e80aeb18115d8b5a541546"></a>

### `vtd_remap()`

```c
int vtd_remap ( const struct device * dev, uint8_t irte_idx, uint16_t vector, uint32_t flags, uint16_t src_id )
```

声明属性：`inline`、`static`。

重映射（Remap）所给中断向量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `irte_idx` | 先前分配的中断重映射表项（IRTE）索引编号。 |
| `vector` | 已分配的中断向量（Interrupt Vector）。 |
| `flags` | 中断标志（interrupt flags）。 |
| `src_id` | 有效源 ID（Source ID）；没有时为 `USHRT_MAX`。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，否则返回负的 `errno` 值。

<a id="ab7b8ad9dbee740c9e97021853f1131fc"></a>

### `vtd_remap_msi()`

```c
uint32_t vtd_remap_msi ( const struct device * dev, msi_vector_t * vector, uint8_t n_vector )
```

声明属性：`inline`、`static`。

为所给向量（Vector）生成消息信号中断（MSI）的消息地址数据（Message Address Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `vector` | 有效且已分配的消息信号中断向量数组（MSI Vector Array）。 |
| `n_vector` | 向量数组（Vector Array）的大小。 |

**返回（Returns）**：返回值：消息信号中断消息地址（MSI Message Address）值。

<a id="ab067e306959a0774ee5e896eafab2132"></a>

### `vtd_set_irte_irq()`

```c
int vtd_set_irte_irq ( const struct device * dev, uint8_t irte_idx, unsigned int irq )
```

声明属性：`inline`、`static`。

为已分配的中断重映射表项（IRTE）设置中断请求（IRQ）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `irte_idx` | 先前分配的中断重映射表项（IRTE）索引编号。 |
| `irq` | 有效的中断请求（IRQ）编号。 |

**返回（Returns）**：返回值：0，否则为负 errno 错误码。

<a id="ae81918a2c81e03cc4e02603781e8ca21"></a>

### `vtd_set_irte_msi()`

```c
void vtd_set_irte_msi ( const struct device * dev, uint8_t irte_idx, bool msi )
```

声明属性：`inline`、`static`。

<a id="a342e4745949ed1bd50b4d51de482be57"></a>

### `vtd_set_irte_vector()`

```c
int vtd_set_irte_vector ( const struct device * dev, uint8_t irte_idx, uint16_t vector )
```

声明属性：`inline`、`static`。

为已分配的中断重映射表项（IRTE）设置向量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `irte_idx` | 先前分配的中断重映射表项（IRTE）索引编号。 |
| `vector` | 已分配的中断向量（Interrupt Vector）。 |

**返回（Returns）**：返回值：0，否则为负 errno 错误码。


## 8.5\_原页交叉引用（Cross References）

- [zephyr/drivers/pcie/msi.h](../api_source_register_time_reference/P005_msi.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P406_intel_vtd.h_源码浏览.md)
- [vtd_driver_api](../platform_security_model_reference/P074_vtd_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [msi_vector_t](../api_vector_pipeline_topic_reference/P025_PCIe 主机消息信号中断（MSI）接口.md#ga9ede6a7a472ee62f0975256a1b5f1231)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_zephyr__drivers__interrupt_controller__gpio_intc_stm32.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__dt-bindings__sensor__mc3419.h_文件参考.md)
