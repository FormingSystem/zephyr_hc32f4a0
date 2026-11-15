---
id: learning.zephyr-docs.api-file-management-reference.page-23
title: zephyr__drivers__i2c__i2c_nrfx_twim.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/i2c__nrfx__twim_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_drivers\_\_i2c\_\_i2c\_nrfx\_twim.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/i2c__nrfx__twim_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel.h>
#include <zephyr/drivers/i2c.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.1\_函数（Functions）

<a id="r_a465c42f64eb7d2dd4c5e173f9ae11745"></a>

```c
int i2c_nrfx_twim_exclusive_access_acquire (const struct device *dev, k_timeout_t timeout)
```

相关声明：[i2c_nrfx_twim_exclusive_access_acquire](#a465c42f64eb7d2dd4c5e173f9ae11745)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

获取对 I2C 总线控制器的独占访问权（exclusive access）。

<a id="r_a924fddc00479f92f98b05a91d08fa7da"></a>

```c
void i2c_nrfx_twim_exclusive_access_release (const struct device *dev)
```

相关声明：[i2c_nrfx_twim_exclusive_access_release](#a924fddc00479f92f98b05a91d08fa7da)、[device](../device_reference/P002_设备对象结构.md)。

释放对 I2C 总线控制器的独占访问权。

## 23.2\_详细说明（Detailed Documentation）

<a id="a465c42f64eb7d2dd4c5e173f9ae11745"></a>

### `i2c_nrfx_twim_exclusive_access_acquire()`

```c
int i2c_nrfx_twim_exclusive_access_acquire ( const struct device * dev, k_timeout_t timeout )
```

获取对 I2C 总线控制器的独占访问权（exclusive access）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向配置为控制器模式（controller mode）的 I2C 控制器驱动设备结构体的指针。 |
| `timeout` | 等待获取独占访问权的超时。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EBUSY` | 未等待便返回。 |
| `-EAGAIN` | 等待超时，或等待期间底层信号量（semaphore）被重置。 |

<a id="a924fddc00479f92f98b05a91d08fa7da"></a>

### `i2c_nrfx_twim_exclusive_access_release()`

```c
void i2c_nrfx_twim_exclusive_access_release ( const struct device * dev)
```

释放对 I2C 总线控制器的独占访问权。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 I2C 控制器驱动设备结构体的指针，且已对该设备成功调用 `i2c_nrfx_twim_exclusive_access_acquire`。 |


## 23.3\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/drivers/i2c.h](../i2c_driver_reference/P002_I2C驱动头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P329_i2c_nrfx_twim.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P022_zephyr__net__http__client.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__drivers__flash__it51xxx_flash_api_ex.h_文件参考.md)
