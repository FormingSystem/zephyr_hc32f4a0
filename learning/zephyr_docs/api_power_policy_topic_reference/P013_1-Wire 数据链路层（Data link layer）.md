---
id: learning.zephyr-docs.api-power-policy-topic-reference.page-13
title: 1-Wire 数据链路层（Data link layer）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_1-Wire 数据链路层（Data link layer）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

1-Wire 数据链路层（Data link layer）

<a id="details"></a>

1-Wire 数据链路层（Data link layer）

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.1\_函数（Functions）

<a id="r_gab4eccd585c6f14330807055ccc151fd6"></a>

```c
int w1_reset_bus (const struct device *dev)
```

相关声明：[w1_reset_bus](#gab4eccd585c6f14330807055ccc151fd6)、[device](../device_reference/P002_设备对象结构.md)。

复位单总线（1-Wire），使从设备准备通信。

<a id="r_ga0f2b37163f3d7c9816371942765509b4"></a>

```c
int w1_read_bit (const struct device *dev)
```

相关声明：[w1_read_bit](#ga0f2b37163f3d7c9816371942765509b4)、[device](../device_reference/P002_设备对象结构.md)。

从 1-Wire 总线读取单个位。

<a id="r_ga3671d8bbf9d044c60d7e96e4190ba2fa"></a>

```c
int w1_write_bit (const struct device *dev, const bool bit)
```

相关声明：[w1_write_bit](#ga3671d8bbf9d044c60d7e96e4190ba2fa)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

向 1-Wire 总线写入单个位。

<a id="r_ga868980684bb98149af5b59e3fa8a83b6"></a>

```c
int w1_read_byte (const struct device *dev)
```

相关声明：[w1_read_byte](#ga868980684bb98149af5b59e3fa8a83b6)、[device](../device_reference/P002_设备对象结构.md)。

从 1-Wire 总线读取单个字节。

<a id="r_ga978a8f14fb8cb3a569f8b731b20cc840"></a>

```c
int w1_write_byte (const struct device *dev, uint8_t byte)
```

相关声明：[w1_write_byte](#ga978a8f14fb8cb3a569f8b731b20cc840)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 1-Wire 总线写入单个字节。

<a id="r_ga2967c99ec93b7c31beb9cf2a327a23f4"></a>

```c
int w1_read_block (const struct device *dev, uint8_t *buffer, size_t len)
```

相关声明：[w1_read_block](#ga2967c99ec93b7c31beb9cf2a327a23f4)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 1-Wire 总线读取一个数据块。

<a id="r_gab30a58c42c06088da9e0845de7d089ce"></a>

```c
int w1_write_block (const struct device *dev, const uint8_t *buffer, size_t len)
```

相关声明：[w1_write_block](#gab30a58c42c06088da9e0845de7d089ce)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 1-Wire 总线写入一个数据块。

<a id="r_ga65892855c763dccc27b508d870c1d144"></a>

```c
size_t w1_get_slave_count (const struct device *dev)
```

相关声明：[w1_get_slave_count](#ga65892855c763dccc27b508d870c1d144)、[device](../device_reference/P002_设备对象结构.md)。

获取总线上的从设备数量。

<a id="r_gae989e0deebe5666edc9ff8a3839cf216"></a>

```c
int w1_configure (const struct device *dev, enum w1_settings_type type, uint32_t value)
```

相关声明：[w1_configure](#gae989e0deebe5666edc9ff8a3839cf216)、[device](../device_reference/P002_设备对象结构.md)、[w1_settings_type](../api_protocol_topic_reference/P062_单总线（1-Wire）.md#ga382989ef707709b5d26c40a394833612)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

配置 1-Wire 主机的参数。

## 13.2\_详细说明（Detailed Documentation）

<a id="gae989e0deebe5666edc9ff8a3839cf216"></a>

### `w1_configure()`

```c
int w1_configure ( const struct device * dev, enum w1_settings_type type, uint32_t value )
```

```c
#include <zephyr/drivers/w1.h>
```

配置 1-Wire 主机的参数。

允许的配置参数（Configuration Parameters）在 `enum w1_settings_type` 中定义，但主设备（Master Devices）不一定支持全部类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |
| ` type` | 指定设置类型（Setting Type）的枚举。 |
| ` value` | 传入设置类型（Settings Type）的新值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOTSUP` | 主设备（Master）不支持配置给定类型。 |
| `-EIO` | 一般输入／输出错误（Input/Output Error），配置主设备（Master Devices）失败。 |

<a id="ga65892855c763dccc27b508d870c1d144"></a>

### `w1_get_slave_count()`

```c
size_t w1_get_slave_count ( const struct device * dev)
```

```c
#include <zephyr/drivers/w1.h>
```

获取总线上的从设备数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回表示已连接 1-Wire 从设备数量（Number of Slaves）的正数，失败返回负 `errno`。

<a id="ga0f2b37163f3d7c9816371942765509b4"></a>

### `w1_read_bit()`

```c
int w1_read_bit ( const struct device * dev)
```

```c
#include <zephyr/drivers/w1.h>
```

从 1-Wire 总线读取单个位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回读取的位值（Bit Value），失败返回负 `errno`。

<a id="ga2967c99ec93b7c31beb9cf2a327a23f4"></a>

### `w1_read_block()`

```c
int w1_read_block ( const struct device * dev, uint8_t * buffer, size_t len )
```

```c
#include <zephyr/drivers/w1.h>
```

从 1-Wire 总线读取一个数据块。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `[out] buffer` | 指向接收缓冲区（Receive Buffer）的指针。 |
| ` len` | 接收缓冲区长度（Buffer Length），单位为字节。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga868980684bb98149af5b59e3fa8a83b6"></a>

### `w1_read_byte()`

```c
int w1_read_byte ( const struct device * dev)
```

```c
#include <zephyr/drivers/w1.h>
```

从 1-Wire 总线读取单个字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回读取的字节值（Byte Value），失败返回负 `errno`。

<a id="gab4eccd585c6f14330807055ccc151fd6"></a>

### `w1_reset_bus()`

```c
int w1_reset_bus ( const struct device * dev)
```

```c
#include <zephyr/drivers/w1.h>
```

复位单总线（1-Wire），使从设备准备通信。

本例程复位全部 1-Wire 总线从设备（Bus Slaves），使它们准备好接收命令。已连接的从设备准备好接收数据后，会以存在脉冲（Presence Pulse）回应。

若驱动同时支持标准速度（Standard Speed）和超速（Overdrive Speed），复位例程会根据当前状态发送短或长复位脉冲（Reset Pulse）。可通过 `w1_configure()` 更改速度。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 没有从设备以存在脉冲（Presence Pulse）回应。 |
| `1` | 至少一个从设备以存在脉冲（Presence Pulse）回应。 |

**返回（Returns）**：**返回值（Returns）：**失败时返回负 `errno`。

<a id="ga3671d8bbf9d044c60d7e96e4190ba2fa"></a>

### `w1_write_bit()`

```c
int w1_write_bit ( const struct device * dev, const bool bit )
```

```c
#include <zephyr/drivers/w1.h>
```

向 1-Wire 总线写入单个位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |
| ` bit` | 要发送的位值（Bit Value），为 `1` 或 `0`。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gab30a58c42c06088da9e0845de7d089ce"></a>

### `w1_write_block()`

```c
int w1_write_block ( const struct device * dev, const uint8_t * buffer, size_t len )
```

```c
#include <zephyr/drivers/w1.h>
```

向 1-Wire 总线写入一个数据块。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `[in] buffer` | 指向发送缓冲区（Transmit Buffer）的指针。 |
| ` len` | 发送缓冲区长度（Buffer Length），单位为字节。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga978a8f14fb8cb3a569f8b731b20cc840"></a>

### `w1_write_byte()`

```c
int w1_write_byte ( const struct device * dev, uint8_t byte )
```

```c
#include <zephyr/drivers/w1.h>
```

向 1-Wire 总线写入单个字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |
| ` byte` | 要发送的字节（Byte）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 13.3\_原页交叉引用（Cross References）

- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [w1_settings_type](../api_protocol_topic_reference/P062_单总线（1-Wire）.md#ga382989ef707709b5d26c40a394833612)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/drivers/w1.h](../peripheral_bus_storage_header_reference/P029_zephyr__drivers__w1.h_头文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P012_视频类型（Video Types）.md) · [返回大纲](大纲.md)
