---
id: learning.zephyr-docs.api-packet-provision-topic-reference.page-1
title: 电池备份 RAM（BBRAM）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_电池备份 RAM（BBRAM）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电池备份 RAM（Battery-Backed RAM，BBRAM）接口。

<a id="details"></a>

电池备份 RAM（Battery-Backed RAM，BBRAM）接口。自 2.7 起提供，版本 1.0.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_bbram_5Finterface_5Fbackend"></a>

相关声明：[BBRAM 驱动后端 API（Driver Backend API）](../api_auxiliary_topic_reference/P001_BBRAM 驱动后端 API（Driver Backend API）.md)。

<a id="r_bbram_5Femulator_5Fbackend"></a>

相关声明：[BBRAM 仿真器后端 API（Emulator backend API）](../hardware/P490_BBRAM仿真后端接口.md)。

BBRAM 仿真器后端 API（Emulator backend API）

<a id="header-files"></a>
<a id="files"></a>

## 1.2\_文件（Files）

<a id="r_bbram_2Eh"></a>

```c
file bbram.h
```

相关声明：[bbram.h](../api_file_network_device_reference/P001_zephyr__drivers__bbram.h_文件参考.md)。

电池备份RAM（Battery-Backed RAM，BBRAM）驱动API的主头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_ga7164969f308616696a9ab71a4d19b70b"></a>

```c
int bbram_check_invalid (const struct device *dev)
```

相关声明：[bbram_check_invalid](#ga7164969f308616696a9ab71a4d19b70b)、[device](../device_reference/P002_设备对象结构.md)。

检查电池备份 RAM（BBRAM）是否无效。

<a id="r_ga948ed0a7d3824f950ad46b99ba3d86f4"></a>

```c
int bbram_check_standby_power (const struct device *dev)
```

相关声明：[bbram_check_standby_power](#ga948ed0a7d3824f950ad46b99ba3d86f4)、[device](../device_reference/P002_设备对象结构.md)。

检查待机（Volt SBY）电源是否发生故障。

<a id="r_ga8fc2a647bda90e96f866514300180a96"></a>

```c
int bbram_check_power (const struct device *dev)
```

相关声明：[bbram_check_power](#ga8fc2a647bda90e96f866514300180a96)、[device](../device_reference/P002_设备对象结构.md)。

检查 V CC1 电源是否发生故障。

<a id="r_gab6bdb4a1cba88ca645c256366a696bdd"></a>

```c
int bbram_get_size (const struct device *dev, size_t *size)
```

相关声明：[bbram_get_size](#gab6bdb4a1cba88ca645c256366a696bdd)、[device](../device_reference/P002_设备对象结构.md)。

获取电池备份 RAM（BBRAM）的大小，单位为字节。

<a id="r_ga9ef786b0fbac3f8523be2bb87b7cff7b"></a>

```c
int bbram_read (const struct device *dev, size_t offset, size_t size, uint8_t *data)
```

相关声明：[bbram_read](#ga9ef786b0fbac3f8523be2bb87b7cff7b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从电池备份 RAM（BBRAM）读取字节。

<a id="r_ga51007eed4820aed341d20e4562607564"></a>

```c
int bbram_write (const struct device *dev, size_t offset, size_t size, const uint8_t *data)
```

相关声明：[bbram_write](#ga51007eed4820aed341d20e4562607564)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向电池备份 RAM（BBRAM）写入字节。

<a id="r_gae2b89f8a44e38fe7df2219397bad139b"></a>

```c
int bbram_emul_set_invalid (const struct device *dev, bool is_invalid)
```

相关声明：[bbram_emul_set_invalid](#gae2b89f8a44e38fe7df2219397bad139b)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置仿真 BBRAM 驱动的无效状态（Invalid State）。

<a id="r_ga08a2c565ba0ec6ac5894a718a652eec2"></a>

```c
int bbram_emul_set_standby_power_state (const struct device *dev, bool failure)
```

相关声明：[bbram_emul_set_standby_power_state](#ga08a2c565ba0ec6ac5894a718a652eec2)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置仿真 BBRAM 驱动的待机电源状态（Standby Power State）。

<a id="r_gadc0243187b853832b08af36c9baf9cb0"></a>

```c
int bbram_emul_set_power_state (const struct device *dev, bool failure)
```

相关声明：[bbram_emul_set_power_state](#gadc0243187b853832b08af36c9baf9cb0)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置仿真 BBRAM 驱动的电源状态（Power State）。

## 1.4\_详细说明（Detailed Documentation）

<a id="ga7164969f308616696a9ab71a4d19b70b"></a>

### `bbram_check_invalid()`

```c
int bbram_check_invalid ( const struct device * dev)
```

```c
#include <zephyr/drivers/bbram.h>
```

检查电池备份 RAM（BBRAM）是否无效。

检查“电池备份 RAM 无效”（Invalid Battery-Backed RAM）状态是否置位，然后清除该状态位。VBAT 引脚电压过低可能导致此状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | BBRAM 设备指针（Device Pointer）。 |

**返回（Returns）**：返回值：电池备份 RAM 数据有效时返回 0，否则返回 `-EFAULT`。

<a id="ga8fc2a647bda90e96f866514300180a96"></a>

### `bbram_check_power()`

```c
int bbram_check_power ( const struct device * dev)
```

```c
#include <zephyr/drivers/bbram.h>
```

检查 V CC1 电源是否发生故障。

若 V CC1 电源域（Power Domain）在关闭后重新开启，则返回错误，并清除状态位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | BBRAM 设备指针（Device Pointer）。 |

**返回（Returns）**：返回值：V CC1 电源域正常工作时返回 0，否则返回 `-EFAULT`。

<a id="ga948ed0a7d3824f950ad46b99ba3d86f4"></a>

### `bbram_check_standby_power()`

```c
int bbram_check_standby_power ( const struct device * dev)
```

```c
#include <zephyr/drivers/bbram.h>
```

检查待机（Volt SBY）电源是否发生故障。

检查 V standby 待机电源域（Standby Power Domain）是否在关闭后重新开启，然后清除状态位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | BBRAM 设备指针（Device Pointer）。 |

**返回（Returns）**：返回值：V SBY 待机电源域（Power Domain）正常工作时返回 0。

<a id="gae2b89f8a44e38fe7df2219397bad139b"></a>

### `bbram_emul_set_invalid()`

```c
int bbram_emul_set_invalid ( const struct device * dev, bool is_invalid )
```

```c
#include <zephyr/drivers/bbram.h>
```

设置仿真 BBRAM 驱动的无效状态（Invalid State）。

调用此函数将影响 `bbram_check_invalid()` 的仿真行为（Emulated Behavior）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 要修改的仿真设备（Emulated Device）。 |
| `[in] is_invalid` | 新的无效状态（Invalid State）。 |

**返回（Returns）**：返回值：成功返回 0，出错时返回负值。

<a id="gadc0243187b853832b08af36c9baf9cb0"></a>

### `bbram_emul_set_power_state()`

```c
int bbram_emul_set_power_state ( const struct device * dev, bool failure )
```

```c
#include <zephyr/drivers/bbram.h>
```

设置仿真 BBRAM 驱动的电源状态（Power State）。

调用此函数将影响 `bbram_check_power()` 的仿真行为（Emulated Behavior）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 要修改的仿真设备（Emulated Device）。 |
| `[in] failure` | 是否仿真电源故障（Power Failure）。 |

**返回（Returns）**：返回值：成功返回 0，出错时返回负值。

<a id="ga08a2c565ba0ec6ac5894a718a652eec2"></a>

### `bbram_emul_set_standby_power_state()`

```c
int bbram_emul_set_standby_power_state ( const struct device * dev, bool failure )
```

```c
#include <zephyr/drivers/bbram.h>
```

设置仿真 BBRAM 驱动的待机电源状态（Standby Power State）。

调用此函数将影响 `bbram_check_standby_power()` 的仿真行为（Emulated Behavior）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 要修改的仿真设备（Emulated Device）。 |
| `[in] failure` | 是否仿真待机电源故障（Standby Power Failure）。 |

**返回（Returns）**：返回值：成功返回 0，出错时返回负值。

<a id="gab6bdb4a1cba88ca645c256366a696bdd"></a>

### `bbram_get_size()`

```c
int bbram_get_size ( const struct device * dev, size_t * size )
```

```c
#include <zephyr/drivers/bbram.h>
```

获取电池备份 RAM（BBRAM）的大小，单位为字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | BBRAM 设备指针（Device Pointer）。 |
| `[out] size` | 用于写入大小的指针。 |

**返回（Returns）**：返回值：成功返回 0，否则返回 `-EFAULT`。

<a id="ga9ef786b0fbac3f8523be2bb87b7cff7b"></a>

### `bbram_read()`

```c
int bbram_read ( const struct device * dev, size_t offset, size_t size, uint8_t * data )
```

```c
#include <zephyr/drivers/bbram.h>
```

从电池备份 RAM（BBRAM）读取字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 要从中读取数据的 BBRAM 设备指针（Device Pointer）。 |
| `[in] offset` | 开始读取的 RAM 地址偏移量（Offset）。 |
| `[in] size` | 要读取的字节数（Number of Bytes）。 |
| `[out] data` | 用于装入数据的缓冲区（Buffer）。 |

**返回（Returns）**：返回值：成功返回 0；地址范围越界（Out of Bounds）时返回 `-EFAULT`。

<a id="ga51007eed4820aed341d20e4562607564"></a>

### `bbram_write()`

```c
int bbram_write ( const struct device * dev, size_t offset, size_t size, const uint8_t * data )
```

```c
#include <zephyr/drivers/bbram.h>
```

向电池备份 RAM（BBRAM）写入字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 要向其写入数据的 BBRAM 设备指针（Device Pointer）。 |
| `[in] offset` | 开始写入的 RAM 地址偏移量（Offset）。 |
| `[in] size` | 要写入的字节数（Number of Bytes）。 |
| `[in] data` | 指向待写入数据起始位置的指针。 |

**返回（Returns）**：返回值：成功返回 0；地址范围越界（Out of Bounds）时返回 `-EFAULT`。


## 1.5\_原页交叉引用（Cross References）

- [BBRAM 驱动后端 API（Driver Backend API）](../api_auxiliary_topic_reference/P001_BBRAM 驱动后端 API（Driver Backend API）.md)
- [BBRAM 仿真器后端 API（Emulator backend API）](../hardware/P490_BBRAM仿真后端接口.md)
- [bbram.h](../api_file_network_device_reference/P001_zephyr__drivers__bbram.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md)
