---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-6
title: 管理数据输入_输出（MDIO）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_管理数据输入\_输出（MDIO）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

管理数据输入/输出（Management Data Input/Output，MDIO）控制器接口。

<a id="details"></a>

管理数据输入输出（Management Data Input/Output，MDIO）控制器接口。**引入版本（Since）：**2.7。**版本（Version）：**0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 6.1\_主题（Topics）

<a id="r_mdio_5Finterface_5Fbackend"></a>

相关声明：[MDIO 驱动后端 API](../api_connection_topic_reference/P013_MDIO 驱动后端 API.md)。

<a id="header-files"></a>
<a id="files"></a>

## 6.2\_文件（Files）

<a id="r_mdio_2Eh"></a>

```c
file mdio.h
```

相关声明：[mdio.h](../api_file_system_device_reference/P009_zephyr__drivers__mdio.h_文件参考.md)。

管理数据输入输出（Management Data Input/Output，MDIO）驱动API的主头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.3\_函数（Functions）

<a id="r_gae056ee61011eb6e8d68254680f918434"></a>

```c
int mdio_read (const struct device *dev, uint8_t prtad, uint8_t regad, uint16_t *data)
```

相关声明：[mdio_read](#gae056ee61011eb6e8d68254680f918434)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从管理数据输入／输出（MDIO）总线读取数据。

<a id="r_ga6a18c3d67c6dc7ef1f3f0e3780015d48"></a>

```c
int mdio_write (const struct device *dev, uint8_t prtad, uint8_t regad, uint16_t data)
```

相关声明：[mdio_write](#ga6a18c3d67c6dc7ef1f3f0e3780015d48)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 MDIO 总线写入数据。

<a id="r_ga93e360a1201c2bb1ddd33b94e6fce619"></a>

```c
int mdio_read_c45 (const struct device *dev, uint8_t prtad, uint8_t devad, uint16_t regad, uint16_t *data)
```

相关声明：[mdio_read_c45](#ga93e360a1201c2bb1ddd33b94e6fce619)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过第 45 条款访问方式（Clause 45 access）从 MDIO 总线读取数据。

<a id="r_gad8868e94f7335fea3cd9fea338ef9bd5"></a>

```c
int mdio_write_c45 (const struct device *dev, uint8_t prtad, uint8_t devad, uint16_t regad, uint16_t data)
```

相关声明：[mdio_write_c45](#gad8868e94f7335fea3cd9fea338ef9bd5)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过 Clause 45 访问方式向 MDIO 总线写入数据。

## 6.4\_详细说明（Detailed Documentation）

<a id="gae056ee61011eb6e8d68254680f918434"></a>

### `mdio_read()`

```c
int mdio_read ( const struct device * dev, uint8_t prtad, uint8_t regad, uint16_t * data )
```

```c
#include <zephyr/drivers/mdio.h>
```

从管理数据输入／输出（MDIO）总线读取数据。

本函数提供在 MDIO 总线上执行读取的通用接口（Generic Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向控制器设备结构体的指针。 |
| `[in] prtad` | 端口地址（Port Address）。 |
| `[in] regad` | 寄存器地址（Register Address）。 |
| ` data` | 用于接收读取数据的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ETIMEDOUT` | 总线事务超时（Transaction Timeout）时。 |
| `-ENOSYS` | 不支持读取时。 |

<a id="ga93e360a1201c2bb1ddd33b94e6fce619"></a>

### `mdio_read_c45()`

```c
int mdio_read_c45 ( const struct device * dev, uint8_t prtad, uint8_t devad, uint16_t regad, uint16_t * data )
```

```c
#include <zephyr/drivers/mdio.h>
```

通过第 45 条款访问方式（Clause 45 access）从 MDIO 总线读取数据。

本函数提供使用 IEEE 802.3 第 45 条（Clause 45）访问方式，在 MDIO 总线上读取的接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向控制器设备结构体的指针。 |
| `[in] prtad` | 端口地址（Port Address）。 |
| `[in] devad` | 设备地址。 |
| `[in] regad` | 寄存器地址（Register Address）。 |
| ` data` | 用于接收读取数据的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ETIMEDOUT` | 总线事务超时（Transaction Timeout）时。 |
| `-ENOSYS` | 不支持 Clause 45 访问方式读取时。 |

<a id="ga6a18c3d67c6dc7ef1f3f0e3780015d48"></a>

### `mdio_write()`

```c
int mdio_write ( const struct device * dev, uint8_t prtad, uint8_t regad, uint16_t data )
```

```c
#include <zephyr/drivers/mdio.h>
```

向 MDIO 总线写入数据。

本函数提供在 MDIO 总线上执行写入的通用接口（Generic Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向控制器设备结构体的指针。 |
| `[in] prtad` | 端口地址（Port Address）。 |
| `[in] regad` | 寄存器地址（Register Address）。 |
| `[in] data` | 要写入的数据。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ETIMEDOUT` | 总线事务超时（Transaction Timeout）时。 |
| `-ENOSYS` | 不支持写入时。 |

<a id="gad8868e94f7335fea3cd9fea338ef9bd5"></a>

### `mdio_write_c45()`

```c
int mdio_write_c45 ( const struct device * dev, uint8_t prtad, uint8_t devad, uint16_t regad, uint16_t data )
```

```c
#include <zephyr/drivers/mdio.h>
```

通过 Clause 45 访问方式向 MDIO 总线写入数据。

本函数提供使用 IEEE 802.3 第 45 条（Clause 45）访问方式，在 MDIO 总线上写入的接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向控制器设备结构体的指针。 |
| `[in] prtad` | 端口地址（Port Address）。 |
| `[in] devad` | 设备地址。 |
| `[in] regad` | 寄存器地址（Register Address）。 |
| `[in] data` | 要写入的数据。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ETIMEDOUT` | 总线事务超时（Transaction Timeout）时。 |
| `-ENOSYS` | 不支持 Clause 45 访问方式写入时。 |


## 6.5\_原页交叉引用（Cross References）

- [MDIO 驱动后端 API](../api_connection_topic_reference/P013_MDIO 驱动后端 API.md)
- [mdio.h](../api_file_system_device_reference/P009_zephyr__drivers__mdio.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_堆内核地址消毒器 API（Heap KASAN APIs）.md) · [返回大纲](大纲.md) · [下一章](P007_存储器控制器（MEMC）.md)
