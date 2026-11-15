---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-28
title: zephyr__drivers__swdp.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/swdp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_zephyr\_\_drivers\_\_swdp.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/swdp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

串行线调试端口（Serial Wire Debug Port，SWDP）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/syscalls/swdp.h>
```

查看此文件的源码。

串行线调试端口（Serial Wire Debug Port，SWDP）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 28.1\_数据结构（Data Structures）

<a id="r_swdp_5Fapi"></a>

```c
struct swdp_api
```

相关声明：[swdp_api](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md)。

串行线调试端口（Serial Wire Debug Port，SWDP）的驱动API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 28.2\_宏定义（Macros）

<a id="r_ga0c5587d14f0b68fa639558f768f24e90"></a>

```c
#define SWDP_TRANSFER_ERROR BIT(3)
```

相关声明：[SWDP_TRANSFER_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga0c5587d14f0b68fa639558f768f24e90)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

事务期间检测到传输错误或奇偶校验错误。

<a id="define-members-0"></a>

### SWD 数据包请求位（Packet Request Bits）

SWD 数据包请求字段的位定义（Bit definitions）。

这些位用于构造 SWD 事务期间发送的 8 位请求包头。

<a id="r_ga8a41667b3516d49ad5785669a659fa0b"></a>

```c
#define SWDP_REQUEST_APnDP BIT(0)
```

相关声明：[SWDP_REQUEST_APnDP](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga8a41667b3516d49ad5785669a659fa0b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

访问端口（Access Port，AP）或调试端口（Debug Port，DP）。

<a id="r_gadc8522fcb5dd2d68b07d82b60d2324e3"></a>

```c
#define SWDP_REQUEST_RnW BIT(1)
```

相关声明：[SWDP_REQUEST_RnW](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gadc8522fcb5dd2d68b07d82b60d2324e3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

读取（`1`）或写入（`0`）操作。

<a id="r_ga2a48349320bd17c6495e96f53738645c"></a>

```c
#define SWDP_REQUEST_A2 BIT(2)
```

相关声明：[SWDP_REQUEST_A2](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga2a48349320bd17c6495e96f53738645c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

用于寄存器选择的地址位 2。

<a id="r_ga30ec6eccc9dc5f4254eceb887b33caf7"></a>

```c
#define SWDP_REQUEST_A3 BIT(3)
```

相关声明：[SWDP_REQUEST_A3](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga30ec6eccc9dc5f4254eceb887b33caf7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

用于寄存器选择的地址位 3。

<a id="define-members-1"></a>

### SWD 确认响应位（Acknowledge Response Bits，ACK）

SWD 确认响应（Acknowledge response）字段的位定义。

这些位用于表示 SWD 事务的结果。

<a id="r_gaccc95b6569bfdcb9969b62e49e4a7869"></a>

```c
#define SWDP_ACK_OK BIT(0)
```

相关声明：[SWDP_ACK_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gaccc95b6569bfdcb9969b62e49e4a7869)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

事务成功完成。

<a id="r_gaaa8df6e1403dd7ca964acdfd3eba5c42"></a>

```c
#define SWDP_ACK_WAIT BIT(1)
```

相关声明：[SWDP_ACK_WAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gaaa8df6e1403dd7ca964acdfd3eba5c42)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

目标请求稍后重试事务。

<a id="r_ga6f67ce6246bda2a4f11fbef88de8050e"></a>

```c
#define SWDP_ACK_FAULT BIT(2)
```

相关声明：[SWDP_ACK_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga6f67ce6246bda2a4f11fbef88de8050e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

目标检测到故障条件（Fault condition）。

<a id="define-members-2"></a>

### SWDP 接口引脚定义（Interface Pin Definitions）

SWDP 接口控制的引脚标识符。

这些常量定义了控制 SWDP 接口各引脚所使用的位位置。

<a id="r_ga04d9dbfa1c6303adfbf22ea14c589a5d"></a>

```c
#define SWDP_SWCLK_PIN 0U
```

相关声明：[SWDP_SWCLK_PIN](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga04d9dbfa1c6303adfbf22ea14c589a5d)。

串行线时钟（Serial Wire Clock，SWCLK）引脚标识符。

<a id="r_gaf0d50f9d503900ad9a7e3dd0d40aae4e"></a>

```c
#define SWDP_SWDIO_PIN 1U
```

相关声明：[SWDP_SWDIO_PIN](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gaf0d50f9d503900ad9a7e3dd0d40aae4e)。

串行线数据输入/输出（Serial Wire Data Input/Output，SWDIO）引脚标识符。

<a id="r_ga2cad01a3a938093f7b7ec2ddc0fcdc2d"></a>

```c
#define SWDP_nRESET_PIN 7U
```

相关声明：[SWDP_nRESET_PIN](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga2cad01a3a938093f7b7ec2ddc0fcdc2d)。

低电平有效复位（nRESET）引脚标识符。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 28.3\_函数（Functions）

<a id="r_ga084283204c12b2eb0de05c6d72217ee7"></a>

```c
int swdp_output_sequence (const struct device *dev, const uint32_t count, const uint8_t *const data)
```

相关声明：[swdp_output_sequence](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga084283204c12b2eb0de05c6d72217ee7)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将 `data` 中的 `count` 位写入 SWDIO，最低有效位优先（LSB first）。

<a id="r_ga1b652fa82819ea8a393eb08b47acb33f"></a>

```c
int swdp_input_sequence (const struct device *dev, const uint32_t count, uint8_t *const buf)
```

相关声明：[swdp_input_sequence](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga1b652fa82819ea8a393eb08b47acb33f)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 SWDIO 读取 `count` 位到 `data`，最低有效位优先（LSB first）。

<a id="r_gab71cacb48078e8f76349354d915514e1"></a>

```c
int swdp_transfer (const struct device *dev, const uint8_t request, uint32_t *const data, const uint8_t idle_cycles, uint8_t *const response)
```

相关声明：[swdp_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gab71cacb48078e8f76349354d915514e1)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SWDP 传输并存储响应。

<a id="r_ga8466b58965837c3cdf8c259ae38a2d1a"></a>

```c
int swdp_set_pins (const struct device *dev, const uint8_t pins, const uint8_t value)
```

相关声明：[swdp_set_pins](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga8466b58965837c3cdf8c259ae38a2d1a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 `SWCLK`、`SWDPIO` 和 `nRESET` 引脚状态。

<a id="r_ga3b23bf1ffc3d378bc19c3d50d5476dda"></a>

```c
int swdp_get_pins (const struct device *dev, uint8_t *const state)
```

相关声明：[swdp_get_pins](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga3b23bf1ffc3d378bc19c3d50d5476dda)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

获取 `SWCLK`、`SWDPIO` 和 `nRESET` 引脚状态。

<a id="r_gaf9b640f9a4b59c2294f45f238287d6eb"></a>

```c
int swdp_set_clock (const struct device *dev, const uint32_t clock)
```

相关声明：[swdp_set_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gaf9b640f9a4b59c2294f45f238287d6eb)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

设置 SWDP 时钟频率。

<a id="r_ga02e1b57447bd836cff26cc007ced6b59"></a>

```c
int swdp_port_on (const struct device *dev)
```

相关声明：[swdp_port_on](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga02e1b57447bd836cff26cc007ced6b59)、[device](../device_reference/P002_设备对象结构.md)。

启用接口，并将引脚设置为默认状态。

<a id="r_gaeac761589b00b889adebf3bd94d4253f"></a>

```c
int swdp_port_off (const struct device *dev)
```

相关声明：[swdp_port_off](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gaeac761589b00b889adebf3bd94d4253f)、[device](../device_reference/P002_设备对象结构.md)。

禁用接口，并将引脚设置为高阻态（High-Z）。

<a id="r_gae1f3d9d1bb1f7f588196ec30e75b3952"></a>

```c
int swdp_configure (const struct device *dev, const uint8_t turnaround, const bool data_phase)
```

相关声明：[swdp_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gae1f3d9d1bb1f7f588196ec30e75b3952)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

配置 SWDP 接口。


## 28.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/swdp_8h_source.html)
- [swdp_api](../peripheral_bus_storage_model_reference/P094_swdp_api_结构体.md)
- [SWDP_TRANSFER_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga0c5587d14f0b68fa639558f768f24e90)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [SWDP_REQUEST_APnDP](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga8a41667b3516d49ad5785669a659fa0b)
- [SWDP_REQUEST_RnW](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gadc8522fcb5dd2d68b07d82b60d2324e3)
- [SWDP_REQUEST_A2](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga2a48349320bd17c6495e96f53738645c)
- [SWDP_REQUEST_A3](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga30ec6eccc9dc5f4254eceb887b33caf7)
- [SWDP_ACK_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gaccc95b6569bfdcb9969b62e49e4a7869)
- [SWDP_ACK_WAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gaaa8df6e1403dd7ca964acdfd3eba5c42)
- [SWDP_ACK_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga6f67ce6246bda2a4f11fbef88de8050e)
- [SWDP_SWCLK_PIN](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga04d9dbfa1c6303adfbf22ea14c589a5d)
- [SWDP_SWDIO_PIN](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gaf0d50f9d503900ad9a7e3dd0d40aae4e)
- [SWDP_nRESET_PIN](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga2cad01a3a938093f7b7ec2ddc0fcdc2d)
- [swdp_output_sequence](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga084283204c12b2eb0de05c6d72217ee7)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [swdp_input_sequence](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga1b652fa82819ea8a393eb08b47acb33f)
- [swdp_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gab71cacb48078e8f76349354d915514e1)
- [swdp_set_pins](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga8466b58965837c3cdf8c259ae38a2d1a)
- [swdp_get_pins](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga3b23bf1ffc3d378bc19c3d50d5476dda)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [swdp_set_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gaf9b640f9a4b59c2294f45f238287d6eb)
- [swdp_port_on](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#ga02e1b57447bd836cff26cc007ced6b59)
- [swdp_port_off](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gaeac761589b00b889adebf3bd94d4253f)
- [swdp_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html#gae1f3d9d1bb1f7f588196ec30e75b3952)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>

---

[上一章](P027_zephyr__drivers__smbus.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P029_zephyr__drivers__w1.h_头文件参考.md)
