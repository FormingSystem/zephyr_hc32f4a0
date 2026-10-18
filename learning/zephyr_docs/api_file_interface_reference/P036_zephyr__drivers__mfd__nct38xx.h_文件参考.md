---
id: learning.zephyr-docs.api-file-interface-reference.page-36
title: zephyr__drivers__mfd__nct38xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nct38xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_zephyr\_\_drivers\_\_mfd\_\_nct38xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nct38xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
#include <zephyr/drivers/i2c.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 36.1\_函数（Functions）

<a id="r_a14924372c0c4ffb5cb5d7f69cf22df7d"></a>

```c
struct k_sem * mfd_nct38xx_get_lock_reference (const struct device *dev)
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[mfd_nct38xx_get_lock_reference](#a14924372c0c4ffb5cb5d7f69cf22df7d)、[device](../device_reference/P002_设备对象结构.md)。

获取 NCT38xx 实例的信号量（semaphore）引用。

<a id="r_af32ad6d2c437c5a1ebb4abe660903bde"></a>

```c
const struct i2c_dt_spec * mfd_nct38xx_get_i2c_dt_spec (const struct device *dev)
```

相关声明：[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[mfd_nct38xx_get_i2c_dt_spec](#af32ad6d2c437c5a1ebb4abe660903bde)、[device](../device_reference/P002_设备对象结构.md)。

获取 NCT38xx 实例的 I2C 设备树描述（I2C DT spec）引用。

## 36.2\_详细说明（Detailed Documentation）

<a id="af32ad6d2c437c5a1ebb4abe660903bde"></a>

### `mfd_nct38xx_get_i2c_dt_spec()`

```c
const struct i2c_dt_spec * mfd_nct38xx_get_i2c_dt_spec ( const struct device * dev)
```

获取 NCT38xx 实例的 I2C 设备树描述（I2C DT spec）引用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例设备结构体（Device Struct of the Driver Instance）的指针（Pointer）。 |

**返回（Returns）**：返回值：I2C 设备树描述的地址。

<a id="a14924372c0c4ffb5cb5d7f69cf22df7d"></a>

### `mfd_nct38xx_get_lock_reference()`

```c
struct k_sem * mfd_nct38xx_get_lock_reference ( const struct device * dev)
```

获取 NCT38xx 实例的信号量（semaphore）引用。

调用者应将返回值传递给 `k_sem_take`／`k_sem_give`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例设备结构体（Device Struct of the Driver Instance）的指针（Pointer）。 |

返回（Returns）：信号量地址（Semaphore Address）。


## 36.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/i2c.h](../i2c_driver_reference/P002_I2C驱动头文件源码.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P573_nct38xx.h_源码浏览.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [device](../device_reference/P002_设备对象结构.md)
- [i2c_dt_spec](../hardware/P306_I2C设备树描述.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P035_zephyr__mpipe__mpipe_transform.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P037_zephyr__net__net_core.h_文件参考.md)
