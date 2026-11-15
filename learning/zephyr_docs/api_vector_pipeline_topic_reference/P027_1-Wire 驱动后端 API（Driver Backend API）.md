---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-27
title: 1-Wire 驱动后端 API（Driver Backend API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_1-Wire 驱动后端 API（Driver Backend API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现单总线（1-Wire）驱动所需的 API 类型定义、回调签名及其他辅助项。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 27.1\_数据结构（Data Structures）

<a id="r_w1_5Fmaster_5Fconfig"></a>

```c
struct w1_master_config
```

相关声明：[w1_master_config](../peripheral_bus_storage_model_reference/P096_w1_master_config_结构体.md)。

全部单总线（1-Wire）主机实现共用的配置。

<a id="r_w1_5Fmaster_5Fdata"></a>

```c
struct w1_master_data
```

相关声明：[w1_master_data](../peripheral_bus_storage_model_reference/P097_w1_master_data_结构体.md)。

全部单总线（1-Wire）主机实现共用的数据。

<a id="r_w1_5Fdriver_5Fapi"></a>

```c
struct w1_driver_api
```

相关声明：[w1_driver_api](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md)。

驱动操作（Driver Operations）：单总线（1-Wire）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 27.2\_类型定义（Typedefs）

<a id="r_ga87232322cd487772d377aa0a8e9e5bfc"></a>

```c
typedef int(* w1_reset_bus_t) (const struct device *dev)
```

相关声明：[w1_reset_bus_t](#ga87232322cd487772d377aa0a8e9e5bfc)、[device](../device_reference/P002_设备对象结构.md)。

复位单总线（1-Wire），使从设备准备通信。

<a id="r_gabb495014dd7b9583009b34d9eba02ddc"></a>

```c
typedef int(* w1_read_bit_t) (const struct device *dev)
```

相关声明：[w1_read_bit_t](#gabb495014dd7b9583009b34d9eba02ddc)、[device](../device_reference/P002_设备对象结构.md)。

从 1-Wire 总线读取单个位。

<a id="r_ga126e501ef9a74cbc3c375ca64025cdbc"></a>

```c
typedef int(* w1_write_bit_t) (const struct device *dev, bool bit)
```

相关声明：[w1_write_bit_t](#ga126e501ef9a74cbc3c375ca64025cdbc)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

向 1-Wire 总线写入单个位。

<a id="r_ga861af0744a5f102558294422de50f6ae"></a>

```c
typedef int(* w1_read_byte_t) (const struct device *dev)
```

相关声明：[w1_read_byte_t](#ga861af0744a5f102558294422de50f6ae)、[device](../device_reference/P002_设备对象结构.md)。

从 1-Wire 总线读取单个字节。

<a id="r_ga18924f833820d5f70d73ab33de6615dd"></a>

```c
typedef int(* w1_write_byte_t) (const struct device *dev, const uint8_t byte)
```

相关声明：[w1_write_byte_t](#ga18924f833820d5f70d73ab33de6615dd)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 1-Wire 总线写入单个字节。

<a id="r_gae2673a21841ad196af69e5b4e6769ea8"></a>

```c
typedef int(* w1_read_block_t) (const struct device *dev, uint8_t *buffer, size_t len)
```

相关声明：[w1_read_block_t](#gae2673a21841ad196af69e5b4e6769ea8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 1-Wire 总线读取一个数据块。

<a id="r_gafbbba20705697154d29a91ac94cc3747"></a>

```c
typedef int(* w1_write_block_t) (const struct device *dev, const uint8_t *buffer, size_t len)
```

相关声明：[w1_write_block_t](#gafbbba20705697154d29a91ac94cc3747)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 1-Wire 总线写入一个数据块。

<a id="r_ga5d3ee84858e35cdac923a6238a22e9a2"></a>

```c
typedef size_t(* w1_get_slave_count_t) (const struct device *dev)
```

相关声明：[w1_get_slave_count_t](#ga5d3ee84858e35cdac923a6238a22e9a2)、[device](../device_reference/P002_设备对象结构.md)。

获取总线上的从设备数量。

<a id="r_gab831da9314fce3e6ec10526ca5224515"></a>

```c
typedef int(* w1_configure_t) (const struct device *dev, enum w1_settings_type type, uint32_t value)
```

相关声明：[w1_configure_t](#gab831da9314fce3e6ec10526ca5224515)、[device](../device_reference/P002_设备对象结构.md)、[w1_settings_type](../api_protocol_topic_reference/P062_单总线（1-Wire）.md#ga382989ef707709b5d26c40a394833612)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

配置 1-Wire 主机的参数。

<a id="r_gaa64e8b894df8a3a44f3b91ea647cc0c1"></a>

```c
typedef int(* w1_change_bus_lock_t) (const struct device *dev, bool lock)
```

相关声明：[w1_change_bus_lock_t](#gaa64e8b894df8a3a44f3b91ea647cc0c1)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

锁定或解锁 1-Wire 总线。

## 27.3\_详细说明（Detailed Documentation）

<a id="gaa64e8b894df8a3a44f3b91ea647cc0c1"></a>

### `w1_change_bus_lock_t`

```c
typedef int(* w1_change_bus_lock_t) (const struct device *dev, bool lock)
```

```c
#include <zephyr/drivers/w1.h>
```

锁定或解锁 1-Wire 总线。

详细信息参见 `w1_lock_bus()` 和 `w1_unlock_bus()`。

<a id="gab831da9314fce3e6ec10526ca5224515"></a>

### `w1_configure_t`

```c
typedef int(* w1_configure_t) (const struct device *dev, enum w1_settings_type type, uint32_t value)
```

```c
#include <zephyr/drivers/w1.h>
```

配置 1-Wire 主机的参数。

参数说明参见 `w1_configure()`。

<a id="ga5d3ee84858e35cdac923a6238a22e9a2"></a>

### `w1_get_slave_count_t`

```c
typedef size_t(* w1_get_slave_count_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/w1.h>
```

获取总线上的从设备数量。

参数说明参见 `w1_get_slave_count()`。

<a id="gabb495014dd7b9583009b34d9eba02ddc"></a>

### `w1_read_bit_t`

```c
typedef int(* w1_read_bit_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/w1.h>
```

从 1-Wire 总线读取单个位。

参数说明参见 `w1_read_bit()`。

<a id="gae2673a21841ad196af69e5b4e6769ea8"></a>

### `w1_read_block_t`

```c
typedef int(* w1_read_block_t) (const struct device *dev, uint8_t *buffer, size_t len)
```

```c
#include <zephyr/drivers/w1.h>
```

从 1-Wire 总线读取一个数据块。

参数说明参见 `w1_read_block()`。

<a id="ga861af0744a5f102558294422de50f6ae"></a>

### `w1_read_byte_t`

```c
typedef int(* w1_read_byte_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/w1.h>
```

从 1-Wire 总线读取单个字节。

参数说明参见 `w1_read_byte()`。

<a id="ga87232322cd487772d377aa0a8e9e5bfc"></a>

### `w1_reset_bus_t`

```c
typedef int(* w1_reset_bus_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/w1.h>
```

复位单总线（1-Wire），使从设备准备通信。

参数说明参见 `w1_reset_bus()`。

<a id="ga126e501ef9a74cbc3c375ca64025cdbc"></a>

### `w1_write_bit_t`

```c
typedef int(* w1_write_bit_t) (const struct device *dev, bool bit)
```

```c
#include <zephyr/drivers/w1.h>
```

向 1-Wire 总线写入单个位。

参数说明参见 `w1_write_bit()`。

<a id="gafbbba20705697154d29a91ac94cc3747"></a>

### `w1_write_block_t`

```c
typedef int(* w1_write_block_t) (const struct device *dev, const uint8_t *buffer, size_t len)
```

```c
#include <zephyr/drivers/w1.h>
```

向 1-Wire 总线写入一个数据块。

参数说明参见 `w1_write_block()`。

<a id="ga18924f833820d5f70d73ab33de6615dd"></a>

### `w1_write_byte_t`

```c
typedef int(* w1_write_byte_t) (const struct device *dev, const uint8_t byte)
```

```c
#include <zephyr/drivers/w1.h>
```

向 1-Wire 总线写入单个字节。

参数说明参见 `w1_write_byte()`。


## 27.4\_原页交叉引用（Cross References）

- [w1_master_config](../peripheral_bus_storage_model_reference/P096_w1_master_config_结构体.md)
- [w1_master_data](../peripheral_bus_storage_model_reference/P097_w1_master_data_结构体.md)
- [w1_driver_api](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [w1_settings_type](../api_protocol_topic_reference/P062_单总线（1-Wire）.md#ga382989ef707709b5d26c40a394833612)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/drivers/w1.h](../peripheral_bus_storage_header_reference/P029_zephyr__drivers__w1.h_头文件参考.md)
- [w1_lock_bus()](../api_protocol_topic_reference/P062_单总线（1-Wire）.md#gab18b0f60a126d38c982730d3ad9756c1)
- [w1_unlock_bus()](../api_protocol_topic_reference/P062_单总线（1-Wire）.md#ga7230fad2428ab62fa963b50e67388c19)
- [w1_configure()](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#gae989e0deebe5666edc9ff8a3839cf216)
- [w1_get_slave_count()](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga65892855c763dccc27b508d870c1d144)
- [w1_read_bit()](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga0f2b37163f3d7c9816371942765509b4)
- [w1_read_block()](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga2967c99ec93b7c31beb9cf2a327a23f4)
- [w1_read_byte()](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga868980684bb98149af5b59e3fa8a83b6)
- [w1_reset_bus()](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#gab4eccd585c6f14330807055ccc151fd6)
- [w1_write_bit()](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga3671d8bbf9d044c60d7e96e4190ba2fa)
- [w1_write_block()](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#gab30a58c42c06088da9e0845de7d089ce)
- [w1_write_byte()](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga978a8f14fb8cb3a569f8b731b20cc840)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P026_传感器类型——感知子系统（Sensor Types，Sensing）.md) · [返回大纲](大纲.md) · [下一章](P028_Wireguard 虚拟专用网络（VPN）服务.md)
