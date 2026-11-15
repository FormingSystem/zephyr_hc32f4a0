---
id: learning.zephyr-docs.api-protocol-topic-reference.page-31
title: MFD Infineon MXCRYPTO 接口
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcrypto.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_MFD Infineon MXCRYPTO 接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__infineon__mxcrypto.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 31.1\_文件（Files）

<a id="r_infineon_5Fmxcrypto_2Eh"></a>

```c
file infineon_mxcrypto.h
```

相关声明：[infineon_mxcrypto.h](../api_file_runtime_reference/P022_zephyr__drivers__mfd__infineon_mxcrypto.h_文件参考.md)。

MXCRYPTO多功能设备（MFD）驱动的公共API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 31.2\_函数（Functions）

<a id="r_ga13bfa154453a651ad9db64cccfe29911"></a>

```c
CRYPTO_Type * mfd_infineon_mxcrypto_get_base (const struct device *dev)
```

相关声明：[mfd_infineon_mxcrypto_get_base](#ga13bfa154453a651ad9db64cccfe29911)、[device](../device_reference/P002_设备对象结构.md)。

获取 MXCRYPTO 寄存器基地址（Register Base Address）。

<a id="r_ga22a1877404d491be13303ae7f1356b84"></a>

```c
int mfd_infineon_mxcrypto_lock (const struct device *dev, k_timeout_t timeout)
```

相关声明：[mfd_infineon_mxcrypto_lock](#ga22a1877404d491be13303ae7f1356b84)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

获取共享的 MXCRYPTO 访问互斥锁（Access Mutex）。

<a id="r_ga786996a9934b87fe322e98bff53858e8"></a>

```c
void mfd_infineon_mxcrypto_unlock (const struct device *dev)
```

相关声明：[mfd_infineon_mxcrypto_unlock](#ga786996a9934b87fe322e98bff53858e8)、[device](../device_reference/P002_设备对象结构.md)。

释放共享的 MXCRYPTO 访问互斥锁（Access Mutex）。

## 31.3\_详细说明（Detailed Documentation）

<a id="ga13bfa154453a651ad9db64cccfe29911"></a>

### `mfd_infineon_mxcrypto_get_base()`

```c
CRYPTO_Type * mfd_infineon_mxcrypto_get_base ( const struct device * dev)
```

```c
#include <zephyr/drivers/mfd/infineon_mxcrypto.h>
```

获取 MXCRYPTO 寄存器基地址（Register Base Address）。

MXCRYPTO 模块的真随机数发生器（TRNG）子功能和加密（AES／SHA）子功能共享此基地址（base address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向父多功能设备（MFD）的指针。 |

**返回（Returns）**：返回值：指向 CRYPTO 寄存器组（register block）的指针。

<a id="ga22a1877404d491be13303ae7f1356b84"></a>

### `mfd_infineon_mxcrypto_lock()`

```c
int mfd_infineon_mxcrypto_lock ( const struct device * dev, k_timeout_t timeout )
```

```c
#include <zephyr/drivers/mfd/infineon_mxcrypto.h>
```

获取共享的 MXCRYPTO 访问互斥锁（Access Mutex）。

TRNG 和加密子功能共享同一个硬件模块。因此，对于不得与另一子功能交错执行的任何多步骤硬件操作，子功能必须在整个操作期间持有此锁（lock）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向父多功能设备（MFD）的指针。 |
| `[in] timeout` | 获取锁的超时（lock acquisition timeout）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EAGAIN` | 未能在超时时间内获取锁。 |

<a id="ga786996a9934b87fe322e98bff53858e8"></a>

### `mfd_infineon_mxcrypto_unlock()`

```c
void mfd_infineon_mxcrypto_unlock ( const struct device * dev)
```

```c
#include <zephyr/drivers/mfd/infineon_mxcrypto.h>
```

释放共享的 MXCRYPTO 访问互斥锁（Access Mutex）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向父多功能设备（MFD）的指针。 |


## 31.4\_原页交叉引用（Cross References）

- [infineon_mxcrypto.h](../api_file_runtime_reference/P022_zephyr__drivers__mfd__infineon_mxcrypto.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P030_MEMC 驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P032_MFD Infineon MXCRYPTOLITE 接口.md)
