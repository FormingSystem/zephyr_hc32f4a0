---
id: learning.zephyr-docs.api-service-topic-reference.page-24
title: 串行线调试端口（SWDP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_串行线调试端口（SWDP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

串行线调试端口（Serial Wire Debug Port，SWDP）接口。

<a id="details"></a>

串行线调试端口（Serial Wire Debug Port，SWDP）的接口。

自 3.7 版提供（Since 3.7）；接口版本（Version）0.1.0。

<a id="header-files"></a>
<a id="files"></a>

## 24.1\_文件（Files）

<a id="r_swdp_2Eh"></a>

```c
file swdp.h
```

相关声明：[swdp.h](../peripheral_bus_storage_header_reference/P028_zephyr__drivers__swdp.h_头文件参考.md)。

串行线调试端口（Serial Wire Debug Port，SWDP）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 24.2\_数据结构（Data Structures）

<a id="r_swdp_5Fapi"></a>

```c
struct swdp_api
```

相关声明：[swdp_api](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md)。

串行线调试端口（Serial Wire Debug Port，SWDP）的驱动API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 24.3\_宏定义（Macros）

<a id="r_ga0c5587d14f0b68fa639558f768f24e90"></a>

```c
#define SWDP_TRANSFER_ERROR BIT(3)
```

相关声明：[SWDP_TRANSFER_ERROR](#ga0c5587d14f0b68fa639558f768f24e90)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

事务期间检测到传输错误或奇偶校验错误。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 24.4\_函数（Functions）

<a id="r_ga084283204c12b2eb0de05c6d72217ee7"></a>

```c
int swdp_output_sequence (const struct device *dev, const uint32_t count, const uint8_t *const data)
```

相关声明：[swdp_output_sequence](#ga084283204c12b2eb0de05c6d72217ee7)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将 `data` 中的 `count` 位写入 SWDIO，最低有效位优先（LSB first）。

<a id="r_ga1b652fa82819ea8a393eb08b47acb33f"></a>

```c
int swdp_input_sequence (const struct device *dev, const uint32_t count, uint8_t *const buf)
```

相关声明：[swdp_input_sequence](#ga1b652fa82819ea8a393eb08b47acb33f)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 SWDIO 读取 `count` 位到 `data`，最低有效位优先（LSB first）。

<a id="r_gab71cacb48078e8f76349354d915514e1"></a>

```c
int swdp_transfer (const struct device *dev, const uint8_t request, uint32_t *const data, const uint8_t idle_cycles, uint8_t *const response)
```

相关声明：[swdp_transfer](#gab71cacb48078e8f76349354d915514e1)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SWDP 传输并存储响应。

<a id="r_ga8466b58965837c3cdf8c259ae38a2d1a"></a>

```c
int swdp_set_pins (const struct device *dev, const uint8_t pins, const uint8_t value)
```

相关声明：[swdp_set_pins](#ga8466b58965837c3cdf8c259ae38a2d1a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 `SWCLK`、`SWDPIO` 和 `nRESET` 引脚状态。

<a id="r_ga3b23bf1ffc3d378bc19c3d50d5476dda"></a>

```c
int swdp_get_pins (const struct device *dev, uint8_t *const state)
```

相关声明：[swdp_get_pins](#ga3b23bf1ffc3d378bc19c3d50d5476dda)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

获取 `SWCLK`、`SWDPIO` 和 `nRESET` 引脚状态。

<a id="r_gaf9b640f9a4b59c2294f45f238287d6eb"></a>

```c
int swdp_set_clock (const struct device *dev, const uint32_t clock)
```

相关声明：[swdp_set_clock](#gaf9b640f9a4b59c2294f45f238287d6eb)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置 SWDP 时钟频率。

<a id="r_ga02e1b57447bd836cff26cc007ced6b59"></a>

```c
int swdp_port_on (const struct device *dev)
```

相关声明：[swdp_port_on](#ga02e1b57447bd836cff26cc007ced6b59)、[device](../device_reference/P002_设备对象结构.md)。

启用接口，并将引脚设置为默认状态。

<a id="r_gaeac761589b00b889adebf3bd94d4253f"></a>

```c
int swdp_port_off (const struct device *dev)
```

相关声明：[swdp_port_off](#gaeac761589b00b889adebf3bd94d4253f)、[device](../device_reference/P002_设备对象结构.md)。

禁用接口，并将引脚设置为高阻态（High-Z）。

<a id="r_gae1f3d9d1bb1f7f588196ec30e75b3952"></a>

```c
int swdp_configure (const struct device *dev, const uint8_t turnaround, const bool data_phase)
```

相关声明：[swdp_configure](#gae1f3d9d1bb1f7f588196ec30e75b3952)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

配置 SWDP 接口。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 24.5\_SWD 数据包请求位（Packet Request Bits）

SWD 数据包请求字段的位定义（Bit definitions）。

这些位用于构造 SWD 事务期间发送的 8 位请求包头。

<a id="r_ga8a41667b3516d49ad5785669a659fa0b"></a>

```c
#define SWDP_REQUEST_APnDP BIT(0)
```

相关声明：[SWDP_REQUEST_APnDP](#ga8a41667b3516d49ad5785669a659fa0b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

访问端口（Access Port，AP）或调试端口（Debug Port，DP）。

<a id="r_gadc8522fcb5dd2d68b07d82b60d2324e3"></a>

```c
#define SWDP_REQUEST_RnW BIT(1)
```

相关声明：[SWDP_REQUEST_RnW](#gadc8522fcb5dd2d68b07d82b60d2324e3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

读取（`1`）或写入（`0`）操作。

<a id="r_ga2a48349320bd17c6495e96f53738645c"></a>

```c
#define SWDP_REQUEST_A2 BIT(2)
```

相关声明：[SWDP_REQUEST_A2](#ga2a48349320bd17c6495e96f53738645c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

用于寄存器选择的地址位 2。

<a id="r_ga30ec6eccc9dc5f4254eceb887b33caf7"></a>

```c
#define SWDP_REQUEST_A3 BIT(3)
```

相关声明：[SWDP_REQUEST_A3](#ga30ec6eccc9dc5f4254eceb887b33caf7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

用于寄存器选择的地址位 3。

## 24.6\_SWD 确认响应位（Acknowledge Response Bits，ACK）

SWD 确认响应（Acknowledge response）字段的位定义。

这些位用于表示 SWD 事务的结果。

<a id="r_gaccc95b6569bfdcb9969b62e49e4a7869"></a>

```c
#define SWDP_ACK_OK BIT(0)
```

相关声明：[SWDP_ACK_OK](#gaccc95b6569bfdcb9969b62e49e4a7869)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

事务成功完成。

<a id="r_gaaa8df6e1403dd7ca964acdfd3eba5c42"></a>

```c
#define SWDP_ACK_WAIT BIT(1)
```

相关声明：[SWDP_ACK_WAIT](#gaaa8df6e1403dd7ca964acdfd3eba5c42)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

目标请求稍后重试事务。

<a id="r_ga6f67ce6246bda2a4f11fbef88de8050e"></a>

```c
#define SWDP_ACK_FAULT BIT(2)
```

相关声明：[SWDP_ACK_FAULT](#ga6f67ce6246bda2a4f11fbef88de8050e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

目标检测到故障条件（Fault condition）。

## 24.7\_SWDP 接口引脚定义（Interface Pin Definitions）

SWDP 接口控制的引脚标识符。

这些常量定义了控制 SWDP 接口各引脚所使用的位位置。

<a id="r_ga04d9dbfa1c6303adfbf22ea14c589a5d"></a>

```c
#define SWDP_SWCLK_PIN 0U
```

相关声明：[SWDP_SWCLK_PIN](#ga04d9dbfa1c6303adfbf22ea14c589a5d)。

串行线时钟（Serial Wire Clock，SWCLK）引脚标识符。

<a id="r_gaf0d50f9d503900ad9a7e3dd0d40aae4e"></a>

```c
#define SWDP_SWDIO_PIN 1U
```

相关声明：[SWDP_SWDIO_PIN](#gaf0d50f9d503900ad9a7e3dd0d40aae4e)。

串行线数据输入/输出（Serial Wire Data Input/Output，SWDIO）引脚标识符。

<a id="r_ga2cad01a3a938093f7b7ec2ddc0fcdc2d"></a>

```c
#define SWDP_nRESET_PIN 7U
```

相关声明：[SWDP_nRESET_PIN](#ga2cad01a3a938093f7b7ec2ddc0fcdc2d)。

低电平有效复位（nRESET）引脚标识符。

## 24.8\_详细说明（Detailed Documentation）

<a id="ga6f67ce6246bda2a4f11fbef88de8050e"></a>

### `SWDP_ACK_FAULT`

```c
#define SWDP_ACK_FAULT BIT(2)
```

```c
#include <zephyr/drivers/swdp.h>
```

目标检测到故障条件（Fault condition）。

<a id="gaccc95b6569bfdcb9969b62e49e4a7869"></a>

### `SWDP_ACK_OK`

```c
#define SWDP_ACK_OK BIT(0)
```

```c
#include <zephyr/drivers/swdp.h>
```

事务成功完成。

<a id="gaaa8df6e1403dd7ca964acdfd3eba5c42"></a>

### `SWDP_ACK_WAIT`

```c
#define SWDP_ACK_WAIT BIT(1)
```

```c
#include <zephyr/drivers/swdp.h>
```

目标请求稍后重试事务。

<a id="ga2cad01a3a938093f7b7ec2ddc0fcdc2d"></a>

### `SWDP_nRESET_PIN`

```c
#define SWDP_nRESET_PIN 7U
```

```c
#include <zephyr/drivers/swdp.h>
```

低电平有效复位（nRESET）引脚标识符。

<a id="ga2a48349320bd17c6495e96f53738645c"></a>

### `SWDP_REQUEST_A2`

```c
#define SWDP_REQUEST_A2 BIT(2)
```

```c
#include <zephyr/drivers/swdp.h>
```

用于寄存器选择的地址位 2。

<a id="ga30ec6eccc9dc5f4254eceb887b33caf7"></a>

### `SWDP_REQUEST_A3`

```c
#define SWDP_REQUEST_A3 BIT(3)
```

```c
#include <zephyr/drivers/swdp.h>
```

用于寄存器选择的地址位 3。

<a id="ga8a41667b3516d49ad5785669a659fa0b"></a>

### `SWDP_REQUEST_APnDP`

```c
#define SWDP_REQUEST_APnDP BIT(0)
```

```c
#include <zephyr/drivers/swdp.h>
```

访问端口（Access Port，AP）或调试端口（Debug Port，DP）。

1 表示访问端口（AP），0 表示调试端口（DP）。

<a id="gadc8522fcb5dd2d68b07d82b60d2324e3"></a>

### `SWDP_REQUEST_RnW`

```c
#define SWDP_REQUEST_RnW BIT(1)
```

```c
#include <zephyr/drivers/swdp.h>
```

读取（`1`）或写入（`0`）操作。

<a id="ga04d9dbfa1c6303adfbf22ea14c589a5d"></a>

### `SWDP_SWCLK_PIN`

```c
#define SWDP_SWCLK_PIN 0U
```

```c
#include <zephyr/drivers/swdp.h>
```

串行线时钟（Serial Wire Clock，SWCLK）引脚标识符。

<a id="gaf0d50f9d503900ad9a7e3dd0d40aae4e"></a>

### `SWDP_SWDIO_PIN`

```c
#define SWDP_SWDIO_PIN 1U
```

```c
#include <zephyr/drivers/swdp.h>
```

串行线数据输入/输出（Serial Wire Data Input/Output，SWDIO）引脚标识符。

<a id="ga0c5587d14f0b68fa639558f768f24e90"></a>

### `SWDP_TRANSFER_ERROR`

```c
#define SWDP_TRANSFER_ERROR BIT(3)
```

```c
#include <zephyr/drivers/swdp.h>
```

事务期间检测到传输错误或奇偶校验错误。

<a id="gae1f3d9d1bb1f7f588196ec30e75b3952"></a>

### `swdp_configure()`

```c
int swdp_configure ( const struct device * dev, const uint8_t turnaround, const bool data_phase )
```

```c
#include <zephyr/drivers/swdp.h>
```

配置 SWDP 接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |
| `turnaround` | 线路方向切换周期数（Line turnaround cycles）。 |
| `data_phase` | 始终生成数据阶段（Data Phase），包括收到 `WAIT`/`FAULT` 时。 |

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

<a id="ga3b23bf1ffc3d378bc19c3d50d5476dda"></a>

### `swdp_get_pins()`

```c
int swdp_get_pins ( const struct device * dev, uint8_t *const state )
```

```c
#include <zephyr/drivers/swdp.h>
```

获取 `SWCLK`、`SWDPIO` 和 `nRESET` 引脚状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |
| `state` | 用于存储引脚状态的位置。 |

**说明（Note）**：注意：位位置由 `SWDP_*_PIN` 宏定义。

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

<a id="ga1b652fa82819ea8a393eb08b47acb33f"></a>

### `swdp_input_sequence()`

```c
int swdp_input_sequence ( const struct device * dev, const uint32_t count, uint8_t *const buf )
```

```c
#include <zephyr/drivers/swdp.h>
```

从 SWDIO 读取 `count` 位到 `data`，最低有效位优先（LSB first）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |
| `count` | 要读取的位数。 |
| `buf` | 存储已读位的缓冲区。 |

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

<a id="ga084283204c12b2eb0de05c6d72217ee7"></a>

### `swdp_output_sequence()`

```c
int swdp_output_sequence ( const struct device * dev, const uint32_t count, const uint8_t *const data )
```

```c
#include <zephyr/drivers/swdp.h>
```

将 `data` 中的 `count` 位写入 SWDIO，最低有效位优先（LSB first）。

通常用于线路复位序列（Line Reset Sequence），或在 JTAG 与串行线调试（SWD）操作之间切换。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |
| `count` | 要写入的位数。 |
| `data` | 要写入的位。 |

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

<a id="gaeac761589b00b889adebf3bd94d4253f"></a>

### `swdp_port_off()`

```c
int swdp_port_off ( const struct device * dev)
```

```c
#include <zephyr/drivers/swdp.h>
```

禁用接口，并将引脚设置为高阻态（High-Z）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

<a id="ga02e1b57447bd836cff26cc007ced6b59"></a>

### `swdp_port_on()`

```c
int swdp_port_on ( const struct device * dev)
```

```c
#include <zephyr/drivers/swdp.h>
```

启用接口，并将引脚设置为默认状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |

**说明（Note）**：注意：将 `SWDPIO` 设为输出模式，将 `SWCLK` 和 `nRESET` 设为高电平。

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

<a id="gaf9b640f9a4b59c2294f45f238287d6eb"></a>

### `swdp_set_clock()`

```c
int swdp_set_clock ( const struct device * dev, const uint32_t clock )
```

```c
#include <zephyr/drivers/swdp.h>
```

设置 SWDP 时钟频率。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |
| `clock` | 时钟频率，单位为 Hz。 |

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

<a id="ga8466b58965837c3cdf8c259ae38a2d1a"></a>

### `swdp_set_pins()`

```c
int swdp_set_pins ( const struct device * dev, const uint8_t pins, const uint8_t value )
```

```c
#include <zephyr/drivers/swdp.h>
```

设置 `SWCLK`、`SWDPIO` 和 `nRESET` 引脚状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |
| `pins` | 待设置引脚的位掩码（Bitmask）。 |
| `value` | 要将引脚设置为的值。 |

**说明（Note）**：注意：位位置由 `SWDP_*_PIN` 宏定义。

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。

<a id="gab71cacb48078e8f76349354d915514e1"></a>

### `swdp_transfer()`

```c
int swdp_transfer ( const struct device * dev, const uint8_t request, uint32_t *const data, const uint8_t idle_cycles, uint8_t *const response )
```

```c
#include <zephyr/drivers/swdp.h>
```

执行 SWDP 传输并存储响应。

请求（Request）必须采用 `APnDP | RnW | A[2:3]` 形式，不包含起始位（Start Bit）、停止位（Stop Bit）或奇偶校验位（Parity Bit）。如果 SWDCLK 始终提供时钟，驱动可以忽略 `idle_cycles`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SWDP 设备。 |
| `request` | SWDP 请求位（Request bits）。 |
| `data` | 与请求一同传输的数据。 |
| `idle_cycles` | 请求与响应之间的空闲周期数（Idle cycles）。 |
| `response` | 用于存储响应（`ACK`/`WAIT`/`FAULT`）的缓冲区。 |

**返回（Returns）**：返回值：成功时为 `0`，否则为错误码。


## 24.9\_原页交叉引用（Cross References）

- [swdp.h](../peripheral_bus_storage_header_reference/P028_zephyr__drivers__swdp.h_头文件参考.md)
- [swdp_api](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P023_套接字 NET_MGMT 库.md) · [返回大纲](大纲.md) · [下一章](P025_VEAA X-3 API主题.md)
