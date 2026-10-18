---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-19
title: TMC6460 其他功能（MISC）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_TMC6460 其他功能（MISC）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 19.1\_文件（Files）

<a id="r_tmc6460_2Eh"></a>

```c
file tmc6460.h
```

相关声明：[tmc6460.h](../api_file_service_interface_reference/P052_zephyr__drivers__misc__tmc6460__tmc6460.h_文件参考.md)。

TMC6460磁场定向控制（FOC）栅极驱动器的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 19.2\_数据结构（Data Structures）

<a id="r_tmc6460_5Ffield"></a>

```c
struct tmc6460_field
```

相关声明：[tmc6460_field](../device_power_control_model_reference/P096_tmc6460_field_结构体.md)。

描述TMC6460寄存器中的位域（Bitfield）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.3\_函数（Functions）

<a id="r_ga59b012bb5bced0ce523f73ee1386e84e"></a>

```c
int tmc6460_write (const struct device *dev, uint16_t reg_addr, uint32_t reg_val)
```

相关声明：[tmc6460_write](#ga59b012bb5bced0ce523f73ee1386e84e)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 TMC6460 寄存器写入一个值。

<a id="r_gac5859fa6261be5e1b887ba76731b8423"></a>

```c
int tmc6460_read (const struct device *dev, uint16_t reg_addr, uint32_t *reg_val)
```

相关声明：[tmc6460_read](#gac5859fa6261be5e1b887ba76731b8423)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 TMC6460 寄存器读取一个值。

<a id="r_ga86cd8bceebe0ebcfd038c1eaea9d275e"></a>

```c
int tmc6460_rtmi_stream_write (const struct device *dev, uint8_t rtmi_index, uint32_t value)
```

相关声明：[tmc6460_rtmi_stream_write](#ga86cd8bceebe0ebcfd038c1eaea9d275e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向RTMI 流式寄存器槽（Streamed Register Slot）写入一个值，仅适用于 UART。

<a id="r_ga65e91ddd2249dfefc8261ca2a806c491"></a>

```c
int tmc6460_enable (const struct device *dev)
```

相关声明：[tmc6460_enable](#ga65e91ddd2249dfefc8261ca2a806c491)、[device](../device_reference/P002_设备对象结构.md)。

启用 TMC6460 栅极驱动器（Gate Driver）。

<a id="r_ga1d7408f27b645db9718d17163921f9a8"></a>

```c
int tmc6460_disable (const struct device *dev)
```

相关声明：[tmc6460_disable](#ga1d7408f27b645db9718d17163921f9a8)、[device](../device_reference/P002_设备对象结构.md)。

禁用 TMC6460 栅极驱动器（Gate Driver）。

<a id="r_ga52909d4e6831887c5d4e8835ab93c164"></a>

```c
int tmc6460_poll_flag (const struct device *dev, uint16_t reg_addr, uint32_t flag_mask, uint32_t poll_interval_ms, uint32_t timeout_ms)
```

相关声明：[tmc6460_poll_flag](#ga52909d4e6831887c5d4e8835ab93c164)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

轮询寄存器，直到指定标志位（Flag Bits）全部置位或超时。

<a id="r_ga00038972be11ffdaa324845f79f85387"></a>

```c
static uint32_t tmc6460_field_update (uint32_t reg_val, struct tmc6460_field field, uint32_t field_val)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[tmc6460_field_update](#ga00038972be11ffdaa324845f79f85387)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[tmc6460_field](../device_power_control_model_reference/P096_tmc6460_field_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

更新寄存器值中的位域（Bitfield），仅操作内存中的值。

<a id="r_ga65fdd1bbdc1cc88a341c63fc1894c748"></a>

```c
static int tmc6460_field_write (const struct device *dev, struct tmc6460_field field, uint32_t field_val)
```

相关声明：[tmc6460_field_write](#ga65fdd1bbdc1cc88a341c63fc1894c748)、[device](../device_reference/P002_设备对象结构.md)、[tmc6460_field](../device_power_control_model_reference/P096_tmc6460_field_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

对设备上的位域（Bitfield）执行读－改－写（Read-modify-write）。

## 19.4\_详细说明（Detailed Documentation）

<a id="ga1d7408f27b645db9718d17163921f9a8"></a>

### `tmc6460_disable()`

```c
int tmc6460_disable ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/tmc6460/tmc6460.h>
```

禁用 TMC6460 栅极驱动器（Gate Driver）。

清除 `MCC_CONFIG_GDRV` 寄存器中的 `DRV_EN` 位，禁用栅极驱动输出级（Gate Driver Output Stage）。采用读改写（Read-modify-write）操作，因此保留寄存器中的其他位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TMC6460 设备（Device）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 总线故障（Bus Failure）时。 |

<a id="ga65e91ddd2249dfefc8261ca2a806c491"></a>

### `tmc6460_enable()`

```c
int tmc6460_enable ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/tmc6460/tmc6460.h>
```

启用 TMC6460 栅极驱动器（Gate Driver）。

设置 `MCC_CONFIG_GDRV` 寄存器中的 `DRV_EN` 位，启用栅极驱动输出级（Gate Driver Output Stage）。采用读改写（Read-modify-write）操作，因此保留寄存器中的其他位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TMC6460 设备（Device）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 总线故障（Bus Failure）时。 |

<a id="ga00038972be11ffdaa324845f79f85387"></a>

### `tmc6460_field_update()`

```c
uint32_t tmc6460_field_update ( uint32_t reg_val, struct tmc6460_field field, uint32_t field_val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/tmc6460/tmc6460.h>
```

更新寄存器值中的位域（Bitfield），仅操作内存中的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reg_val` | 当前寄存器值（Register Value）。 |
| `field` | 字段描述符（Field Descriptor）。 |
| `field_val` | 要插入的新字段值（Field Value）。 |

**返回（Returns）**：**返回值（Returns）：**更新后的寄存器值（Register Value）。

<a id="ga65fdd1bbdc1cc88a341c63fc1894c748"></a>

### `tmc6460_field_write()`

```c
int tmc6460_field_write ( const struct device * dev, struct tmc6460_field field, uint32_t field_val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/tmc6460/tmc6460.h>
```

对设备上的位域（Bitfield）执行读－改－写（Read-modify-write）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TMC6460 设备（Device）的指针。 |
| `field` | 字段描述符（Field Descriptor）。 |
| `field_val` | 要写入的新字段值（Field Value）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 失败。 |

<a id="ga52909d4e6831887c5d4e8835ab93c164"></a>

### `tmc6460_poll_flag()`

```c
int tmc6460_poll_flag ( const struct device * dev, uint16_t reg_addr, uint32_t flag_mask, uint32_t poll_interval_ms, uint32_t timeout_ms )
```

```c
#include <zephyr/drivers/misc/tmc6460/tmc6460.h>
```

轮询寄存器，直到指定标志位（Flag Bits）全部置位或超时。

反复读取 `reg_addr`，检查 `flag_mask` 中的所有位是否均已置位，两次读取之间休眠 `poll_interval_ms`。此可复用辅助函数用于常见的“等待就绪／锁定状态位”（Ready/Lock Status Bit）模式，例如 PLL 锁定、ADC 就绪。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TMC6460 设备（Device）的指针。 |
| `reg_addr` | 要轮询的 16 位状态寄存器地址（Status Register Address）。 |
| `flag_mask` | 必须全部置位才能判定成功的位掩码（Bit Mask）。 |
| `poll_interval_ms` | 两次读取之间的延迟（Delay），单位为毫秒；`0` 表示紧密循环（Tight Loop）。 |
| `timeout_ms` | 最长等待时间（Maximum Wait Time），单位为毫秒。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 标志位（Flag Bits）已置位时。 |
| `-ETIMEDOUT` | 先达到超时时间（Timeout）时。 |
| `-EIO` | 总线故障（Bus Failure）时。 |

<a id="gac5859fa6261be5e1b887ba76731b8423"></a>

### `tmc6460_read()`

```c
int tmc6460_read ( const struct device * dev, uint16_t reg_addr, uint32_t * reg_val )
```

```c
#include <zephyr/drivers/misc/tmc6460/tmc6460.h>
```

从 TMC6460 寄存器读取一个值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TMC6460 设备（Device）的指针。 |
| `reg_addr` | 16 位寄存器地址（Register Address）。 |
| `reg_val` | 用于存储读取的 32 位值的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 总线故障（Bus Failure）时。 |

<a id="ga86cd8bceebe0ebcfd038c1eaea9d275e"></a>

### `tmc6460_rtmi_stream_write()`

```c
int tmc6460_rtmi_stream_write ( const struct device * dev, uint8_t rtmi_index, uint32_t value )
```

```c
#include <zephyr/drivers/misc/tmc6460/tmc6460.h>
```

向RTMI 流式寄存器槽（Streamed Register Slot）写入一个值，仅适用于 UART。

使用发送后不等待应答（Fire-and-forget）的流写入协议（Stream Write Protocol），同步字节为 `0x41`。仅启用 `CONFIG_TMC6460_UART` 时提供此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TMC6460 设备（Device）的指针。 |
| `rtmi_index` | RTMI 槽位索引（Slot Index），范围 `0..7`。 |
| `value` | 要流式发送的 32 位值（Value）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 失败。 |

<a id="ga59b012bb5bced0ce523f73ee1386e84e"></a>

### `tmc6460_write()`

```c
int tmc6460_write ( const struct device * dev, uint16_t reg_addr, uint32_t reg_val )
```

```c
#include <zephyr/drivers/misc/tmc6460/tmc6460.h>
```

向 TMC6460 寄存器写入一个值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TMC6460 设备（Device）的指针。 |
| `reg_addr` | 16 位寄存器地址（Register Address）。 |
| `reg_val` | 要写入的 32 位值（32-bit Value）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 总线故障（Bus Failure）时。 |


## 19.5\_原页交叉引用（Cross References）

- [tmc6460.h](../api_file_service_interface_reference/P052_zephyr__drivers__misc__tmc6460__tmc6460.h_文件参考.md)
- [tmc6460_field](../device_power_control_model_reference/P096_tmc6460_field_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P018_供电端回调（Source Callbacks）.md) · [返回大纲](大纲.md) · [下一章](P020_视频控制项（Video Controls）.md)
