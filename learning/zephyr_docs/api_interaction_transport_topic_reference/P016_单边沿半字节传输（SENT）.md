---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-16
title: 单边沿半字节传输（SENT）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_单边沿半字节传输（SENT）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

单边沿半字节传输（Single Edge Nibble Transmission，SENT）外设接口。

<a id="details"></a>

单边沿半字节传输（Single Edge Nibble Transmission，SENT）外设接口。**引入版本（Since）：**4.2。**版本（Version）：**0.1.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 16.1\_主题（Topics）

<a id="r_sent_5Finterface_5Fbackend"></a>

相关声明：[SENT 驱动后端 API](../api_platform_topic_reference/P122_SENT 驱动后端 API.md)。

<a id="header-files"></a>
<a id="files"></a>

## 16.2\_文件（Files）

<a id="r_sent_2Eh"></a>

```c
file sent.h
```

相关声明：[sent.h](../peripheral_bus_storage_header_reference/P026_zephyr__drivers__sent__sent.h_头文件参考.md)。

单边沿半字节传输（Single Edge Nibble Transmission，SENT）的驱动API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 16.3\_数据结构（Data Structures）

<a id="r_sent_5Fframe"></a>

```c
struct sent_frame
```

相关声明：[sent_frame](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md)。

单边沿半字节传输（SENT）的帧结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.4\_宏定义（Macros）

<a id="r_ga19bb6e9149dfb7af97ca90289e33bdac"></a>

```c
#define SENT_MAX_DATA_NIBBLES 8
```

相关声明：[SENT_MAX_DATA_NIBBLES](#ga19bb6e9149dfb7af97ca90289e33bdac)。

数据半字节（Nibble）的最大数量。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 16.5\_类型定义（Typedefs）

<a id="r_ga47d05656177dae0a388e1155be82494f"></a>

```c
typedef void(* sent_rx_frame_callback_t) (const struct device *dev, uint8_t channel, uint32_t num_frame, void *user_data)
```

相关声明：[sent_rx_frame_callback_t](#ga47d05656177dae0a388e1155be82494f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

定义用于接收帧的应用程序回调处理函数签名。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 16.6\_枚举（Enumerations）

<a id="r_ga069232b79943be845df411539ef04993"></a>

```c
enum sent_frame_type { SENT_SHORT_SERIAL_FRAME , SENT_ENHANCED_SERIAL_FRAME_4_BIT_ID , SENT_ENHANCED_SERIAL_FRAME_8_BIT_ID , SENT_FAST_FRAME }
```

相关声明：[sent_frame_type](#ga069232b79943be845df411539ef04993)、[SENT_SHORT_SERIAL_FRAME](#gga069232b79943be845df411539ef04993adbbb93e3efeeb6d2330bc4c9cb0ae4d5)、[SENT_ENHANCED_SERIAL_FRAME_4_BIT_ID](#gga069232b79943be845df411539ef04993a44b400409bb8a00ba23022490a6e6e73)、[SENT_ENHANCED_SERIAL_FRAME_8_BIT_ID](#gga069232b79943be845df411539ef04993aeef9ade678a8b59d7a8e0d0154f9b137)、[SENT_FAST_FRAME](#gga069232b79943be845df411539ef04993afb15bcda86b0faef89c8dc1662f060a1)。

SENT 帧类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.7\_函数（Functions）

<a id="r_ga227aafdbe8f93dbdb97f3969517e6c63"></a>

```c
int sent_start_listening (const struct device *dev, uint8_t channel)
```

相关声明：[sent_start_listening](#ga227aafdbe8f93dbdb97f3969517e6c63)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启用指定通道，使其开始从总线接收。

<a id="r_gae1eacde97297c97e27b67a7ae7e121cb"></a>

```c
int sent_stop_listening (const struct device *dev, uint8_t channel)
```

相关声明：[sent_stop_listening](#gae1eacde97297c97e27b67a7ae7e121cb)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

禁用指定通道，使其停止从总线接收。

<a id="r_ga9deb810297f7d42159187bbb8dddb8d2"></a>

```c
int sent_register_callback (const struct device *dev, uint8_t channel, struct sent_rx_callback_configs callback_configs)
```

相关声明：[sent_register_callback](#ga9deb810297f7d42159187bbb8dddb8d2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sent_rx_callback_configs](../peripheral_bus_storage_model_reference/P090_sent_rx_callback_configs_结构体.md)。

添加回调函数，以处理指定通道接收到的消息。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 16.8\_快速消息 CRC 配置标志（Fast Message CRC Configuration Flags）

<a id="r_ga9a90bf30c6bfb4a945ec74c30ea45c1c"></a>

```c
#define FAST_CRC_DISABLE 0
```

相关声明：[FAST_CRC_DISABLE](#ga9a90bf30c6bfb4a945ec74c30ea45c1c)。

禁用快速消息（fast message）的循环冗余校验（CRC）检查。

<a id="r_ga4eecd87726aae09803ffcc9b573e42d7"></a>

```c
#define FAST_CRC_LEGACY_IMPLEMENTATION 1
```

相关声明：[FAST_CRC_LEGACY_IMPLEMENTATION](#ga4eecd87726aae09803ffcc9b573e42d7)。

为快速消息使用传统 CRC 算法（legacy CRC algorithm）。

<a id="r_ga62ecd1c5a6f449c6301373bbec0c9672"></a>

```c
#define FAST_CRC_RECOMMENDED_IMPLEMENTATION 2
```

相关声明：[FAST_CRC_RECOMMENDED_IMPLEMENTATION](#ga62ecd1c5a6f449c6301373bbec0c9672)。

为快速消息使用推荐的 CRC 算法。

<a id="r_ga335f899503c1992d586d771798ded503"></a>

```c
#define FAST_CRC_STATUS_INCLUDE 4
```

相关声明：[FAST_CRC_STATUS_INCLUDE](#ga335f899503c1992d586d771798ded503)。

在快速消息中包含 CRC 状态。

## 16.9\_短串行消息 CRC 配置标志（Short Serial Message CRC Configuration Flags）

<a id="r_ga8d7724675d1e0b0a5dc5df5e857f147f"></a>

```c
#define SHORT_CRC_LEGACY_IMPLEMENTATION 0
```

相关声明：[SHORT_CRC_LEGACY_IMPLEMENTATION](#ga8d7724675d1e0b0a5dc5df5e857f147f)。

短串行消息（short serial message）的传统 CRC 算法。

<a id="r_gaf5a1b613a202a6f4df67f9dadbfea3f6"></a>

```c
#define SHORT_CRC_RECOMMENDED_IMPLEMENTATION 1
```

相关声明：[SHORT_CRC_RECOMMENDED_IMPLEMENTATION](#gaf5a1b613a202a6f4df67f9dadbfea3f6)。

短串行消息的推荐 CRC 算法。

## 16.10\_详细说明（Detailed Documentation）

<a id="ga9a90bf30c6bfb4a945ec74c30ea45c1c"></a>

### `FAST_CRC_DISABLE`

```c
#define FAST_CRC_DISABLE 0
```

```c
#include <zephyr/dt-bindings/sent/sent.h>
```

禁用快速消息（fast message）的循环冗余校验（CRC）检查。

<a id="ga4eecd87726aae09803ffcc9b573e42d7"></a>

### `FAST_CRC_LEGACY_IMPLEMENTATION`

```c
#define FAST_CRC_LEGACY_IMPLEMENTATION 1
```

```c
#include <zephyr/dt-bindings/sent/sent.h>
```

为快速消息使用传统 CRC 算法（legacy CRC algorithm）。

<a id="ga62ecd1c5a6f449c6301373bbec0c9672"></a>

### `FAST_CRC_RECOMMENDED_IMPLEMENTATION`

```c
#define FAST_CRC_RECOMMENDED_IMPLEMENTATION 2
```

```c
#include <zephyr/dt-bindings/sent/sent.h>
```

为快速消息使用推荐的 CRC 算法。

<a id="ga335f899503c1992d586d771798ded503"></a>

### `FAST_CRC_STATUS_INCLUDE`

```c
#define FAST_CRC_STATUS_INCLUDE 4
```

```c
#include <zephyr/dt-bindings/sent/sent.h>
```

在快速消息中包含 CRC 状态。

<a id="ga19bb6e9149dfb7af97ca90289e33bdac"></a>

### `SENT_MAX_DATA_NIBBLES`

```c
#define SENT_MAX_DATA_NIBBLES 8
```

```c
#include <zephyr/drivers/sent/sent.h>
```

数据半字节（Nibble）的最大数量。

<a id="ga8d7724675d1e0b0a5dc5df5e857f147f"></a>

### `SHORT_CRC_LEGACY_IMPLEMENTATION`

```c
#define SHORT_CRC_LEGACY_IMPLEMENTATION 0
```

```c
#include <zephyr/dt-bindings/sent/sent.h>
```

短串行消息（short serial message）的传统 CRC 算法。

<a id="gaf5a1b613a202a6f4df67f9dadbfea3f6"></a>

### `SHORT_CRC_RECOMMENDED_IMPLEMENTATION`

```c
#define SHORT_CRC_RECOMMENDED_IMPLEMENTATION 1
```

```c
#include <zephyr/dt-bindings/sent/sent.h>
```

短串行消息的推荐 CRC 算法。

<a id="ga47d05656177dae0a388e1155be82494f"></a>

### `sent_rx_frame_callback_t`

```c
typedef void(* sent_rx_frame_callback_t) (const struct device *dev, uint8_t channel, uint32_t num_frame, void *user_data)
```

```c
#include <zephyr/drivers/sent/sent.h>
```

定义用于接收帧的应用程序回调处理函数签名。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 驱动实例的硬件通道（Hardware Channel）。 |
| `num_frame` | 接收到的帧（Frame）数量。 |
| `user_data` | 接收帧（Frame）时提供的用户数据（User Data）。 |

<a id="ga069232b79943be845df411539ef04993"></a>

### `sent_frame_type`

```c
enum sent_frame_type
```

```c
#include <zephyr/drivers/sent/sent.h>
```

SENT 帧类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENT_SHORT_SERIAL_FRAME` | 短串行消息帧（Short Serial Message Frame）。 |
| `SENT_ENHANCED_SERIAL_FRAME_4_BIT_ID` | 消息 ID 为 4 位的增强串行消息帧（Enhanced Serial Message Frame）。 |
| `SENT_ENHANCED_SERIAL_FRAME_8_BIT_ID` | 消息 ID 为 8 位的增强串行消息帧（Enhanced Serial Message Frame）。 |
| `SENT_FAST_FRAME` | 快速消息帧（Fast Message Frame）。 |

<a id="ga9deb810297f7d42159187bbb8dddb8d2"></a>

### `sent_register_callback()`

```c
int sent_register_callback ( const struct device * dev, uint8_t channel, struct sent_rx_callback_configs callback_configs )
```

```c
#include <zephyr/drivers/sent/sent.h>
```

添加回调函数，以处理指定通道接收到的消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 驱动实例的硬件通道（Hardware Channel）。 |
| `callback_configs` | 回调配置（Callback Configurations）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 通道（Channel）无效。 |

<a id="ga227aafdbe8f93dbdb97f3969517e6c63"></a>

### `sent_start_listening()`

```c
int sent_start_listening ( const struct device * dev, uint8_t channel )
```

```c
#include <zephyr/drivers/sent/sent.h>
```

启用指定通道，使其开始从总线接收。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 驱动实例的硬件通道（Hardware Channel）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 给定通道（Channel）无效。 |
| `-EALREADY` | 设备已经启动（Started）。 |
| `-EIO` | 一般输入／输出错误（Input/Output Error），启动设备失败。 |

<a id="gae1eacde97297c97e27b67a7ae7e121cb"></a>

### `sent_stop_listening()`

```c
int sent_stop_listening ( const struct device * dev, uint8_t channel )
```

```c
#include <zephyr/drivers/sent/sent.h>
```

禁用指定通道，使其停止从总线接收。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 驱动实例的硬件通道（Hardware Channel）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 通道（Channel）无效。 |
| `-EALREADY` | 设备已经停止（Stopped）。 |
| `-EIO` | 一般输入／输出错误（Input/Output Error），停止设备失败。 |


## 16.11\_原页交叉引用（Cross References）

- [SENT 驱动后端 API](../api_platform_topic_reference/P122_SENT 驱动后端 API.md)
- [sent.h](../peripheral_bus_storage_header_reference/P026_zephyr__drivers__sent__sent.h_头文件参考.md)
- [sent_frame](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [sent_rx_callback_configs](../peripheral_bus_storage_model_reference/P090_sent_rx_callback_configs_结构体.md)
- [zephyr/dt-bindings/sent/sent.h](../api_file_management_reference/P013_zephyr__dt-bindings__sent__sent.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga069232b79943be845df411539ef04993adbbb93e3efeeb6d2330bc4c9cb0ae4d5"></a>
<a id="gga069232b79943be845df411539ef04993a44b400409bb8a00ba23022490a6e6e73"></a>
<a id="gga069232b79943be845df411539ef04993aeef9ade678a8b59d7a8e0d0154f9b137"></a>
<a id="gga069232b79943be845df411539ef04993afb15bcda86b0faef89c8dc1662f060a1"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P015_NXP CPU 域协议（NXP CPU Domain Protocol）.md) · [返回大纲](大纲.md) · [下一章](P017_简单网络时间协议（SNTP）.md)
