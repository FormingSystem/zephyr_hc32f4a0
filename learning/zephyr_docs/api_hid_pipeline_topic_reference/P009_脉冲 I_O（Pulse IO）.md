---
id: learning.zephyr-docs.api-hid-pipeline-topic-reference.page-9
title: 脉冲 I_O（Pulse IO）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_脉冲 I\_O（Pulse IO）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

脉冲 I/O 接口（Pulse IO Interface）

<a id="details"></a>

脉冲输入输出接口（Pulse IO Interface）。自 4.4 起提供，版本 0.1.0。`pulse_io` 子系统抽象了在单条 GPIO 线上生成和捕获定时数字边沿（Timed Digital Edges）的硬件外设。多种 MCU 系列以不同名称提供专用边沿计时外设（Edge-timing Peripherals），此接口旨在为它们提供通用 API。API 支持两种提交模式（Submission Modes），通过能力信息公布：`PULSE_IO_MODE_SYMBOL` 使用任意的 `{level, duration}` 电平与持续时间对；`PULSE_IO_MODE_CELL` 使用周期固定、占空比或电平可变的单元，适用于 PWM 类硬件。客户端在探测时调用 `pulse_io_get_capabilities`，决定使用哪种模式和功能集。

<a id="header-files"></a>
<a id="files"></a>

## 9.1\_文件（Files）

<a id="r_pulse_5Fio_2Eh"></a>

```c
file pulse_io.h
```

相关声明：[pulse_io.h](../api_file_signal_device_reference/P017_zephyr__drivers__pulse_io.h_文件参考.md)。

脉冲输入输出（Pulse IO）子系统API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.2\_数据结构（Data Structures）

<a id="r_pulse_5Fsymbol"></a>

```c
struct pulse_symbol
```

相关声明：[pulse_symbol](../device_power_control_model_reference/P070_pulse_symbol_结构体.md)。

脉冲流（Pulse Stream）的一个符号。

<a id="r_pulse_5Fcell"></a>

```c
struct pulse_cell
```

相关声明：[pulse_cell](../device_power_control_model_reference/P061_pulse_cell_结构体.md)。

固定周期脉冲流（Fixed-Period Pulse Stream）的一个单元。

<a id="r_pulse_5Fio_5Fcaps"></a>

```c
struct pulse_io_caps
```

相关声明：[pulse_io_caps](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md)。

每个实例的能力描述符（Capability Descriptor）。

<a id="r_pulse_5Fio_5Fconfig"></a>

```c
struct pulse_io_config
```

相关声明：[pulse_io_config](../device_power_control_model_reference/P064_pulse_io_config_结构体.md)。

通道配置（Channel Configuration）。

<a id="r_pulse_5Fio_5Ftx_5Freq"></a>

```c
struct pulse_io_tx_req
```

相关声明：[pulse_io_tx_req](../device_power_control_model_reference/P069_pulse_io_tx_req_结构体.md)。

发送提交描述符（TX Submission Descriptor）。

<a id="r_pulse_5Fio_5Frx_5Freq"></a>

```c
struct pulse_io_rx_req
```

相关声明：[pulse_io_rx_req](../device_power_control_model_reference/P068_pulse_io_rx_req_结构体.md)。

接收提交描述符（RX Submission Descriptor）。

<a id="r_pulse_5Fio_5Fdriver_5Fapi"></a>

```c
struct pulse_io_driver_api
```

相关声明：[pulse_io_driver_api](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md)。

驱动虚表（Driver Vtable）。

<a id="r_pulse_5Fio_5Fbit_5Ftemplate"></a>

```c
struct pulse_io_bit_template
```

相关声明：[pulse_io_bit_template](../device_power_control_model_reference/P062_pulse_io_bit_template_结构体.md)。

pulse_io_encode_bytes使用的逐位模板（Per-Bit Template）。

<a id="r_pulse_5Fio_5Fencoder_5Fapi"></a>

```c
struct pulse_io_encoder_api
```

相关声明：[pulse_io_encoder_api](../device_power_control_model_reference/P067_pulse_io_encoder_api_结构体.md)。

编码器虚表（Encoder Vtable）：将协议字节转换为脉冲符号。

<a id="r_pulse_5Fio_5Fdecoder_5Fapi"></a>

```c
struct pulse_io_decoder_api
```

相关声明：[pulse_io_decoder_api](../device_power_control_model_reference/P065_pulse_io_decoder_api_结构体.md)。

解码器虚表（Decoder Vtable）：将脉冲符号转换为协议字节。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.3\_枚举（Enumerations）

<a id="r_ga8a69608ee00587642aca6e0d69878b07"></a>

```c
enum pulse_io_mode { PULSE_IO_MODE_SYMBOL = BIT(0) , PULSE_IO_MODE_CELL = BIT(1) }
```

相关声明：[pulse_io_mode](#ga8a69608ee00587642aca6e0d69878b07)、[PULSE_IO_MODE_SYMBOL](#gga8a69608ee00587642aca6e0d69878b07a72babf2ca6b039635cb177be4f2e5e19)、[PULSE_IO_MODE_CELL](#gga8a69608ee00587642aca6e0d69878b07ae89d6f0f750e30719501cf32fbe2b220)。

脉冲流提交模式（Pulse Stream Submission Modes）。

<a id="r_ga1188071d39a4018b719f18d019ba6f89"></a>

```c
enum pulse_io_dir { PULSE_IO_DIR_TX , PULSE_IO_DIR_RX }
```

相关声明：[pulse_io_dir](#ga1188071d39a4018b719f18d019ba6f89)、[PULSE_IO_DIR_TX](#gga1188071d39a4018b719f18d019ba6f89ad4c6756a1f8972376620492ab1943ee3)、[PULSE_IO_DIR_RX](#gga1188071d39a4018b719f18d019ba6f89ab41397616fbd4b428db60bc6d665186a)。

已配置通道的方向（Direction）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.4\_函数（Functions）

<a id="r_ga3d92ae937058d0675dd56b009aa1138f"></a>

```c
int pulse_io_get_capabilities (const struct device *dev, struct pulse_io_caps *caps)
```

相关声明：[pulse_io_get_capabilities](#ga3d92ae937058d0675dd56b009aa1138f)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_caps](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md)。

查询后端能力（Backend Capabilities）。

<a id="r_ga0a0eb57e852853da9c3ba1e262991091"></a>

```c
int pulse_io_channel_get (const struct device *dev, uint8_t channel_idx, struct pulse_io_channel **chan)
```

相关声明：[pulse_io_channel_get](#ga0a0eb57e852853da9c3ba1e262991091)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

预留通道以供独占使用（Exclusive Use）。

<a id="r_gafcce0615be70ca39c346df4c260f09d2"></a>

```c
int pulse_io_channel_release (const struct device *dev, struct pulse_io_channel *chan)
```

相关声明：[pulse_io_channel_release](#gafcce0615be70ca39c346df4c260f09d2)、[device](../device_reference/P002_设备对象结构.md)。

释放先前通过 `pulse_io_channel_get` 获取的通道。

<a id="r_gaa3a5b31cb44647823aa60af4416e6d3f"></a>

```c
int pulse_io_channel_configure (const struct device *dev, struct pulse_io_channel *chan, const struct pulse_io_config *cfg)
```

相关声明：[pulse_io_channel_configure](#gaa3a5b31cb44647823aa60af4416e6d3f)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_config](../device_power_control_model_reference/P064_pulse_io_config_结构体.md)。

配置已预留的通道（Reserved Channel）。

<a id="r_ga3e03e72bb73c8949c222d48f28c03612"></a>

```c
int pulse_io_transmit_sync (const struct device *dev, struct pulse_io_channel *chan, const struct pulse_io_tx_req *req, k_timeout_t timeout)
```

相关声明：[pulse_io_transmit_sync](#ga3e03e72bb73c8949c222d48f28c03612)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_tx_req](../device_power_control_model_reference/P069_pulse_io_tx_req_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

阻塞式发送（Blocking Transmit）。

<a id="r_ga1d122c085430f9d4408564b76dee0944"></a>

```c
int pulse_io_receive_sync (const struct device *dev, struct pulse_io_channel *chan, const struct pulse_io_rx_req *req, size_t *count, k_timeout_t timeout)
```

相关声明：[pulse_io_receive_sync](#ga1d122c085430f9d4408564b76dee0944)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_rx_req](../device_power_control_model_reference/P068_pulse_io_rx_req_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

阻塞式接收（Blocking Receive）。

<a id="r_ga8810dd66d863919cf3ea03ae27da4cf7"></a>

```c
int pulse_io_stop (const struct device *dev, struct pulse_io_channel *chan)
```

相关声明：[pulse_io_stop](#ga8810dd66d863919cf3ea03ae27da4cf7)、[device](../device_reference/P002_设备对象结构.md)。

停止该通道上任何正在进行的发送或接收操作。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 9.5\_编码器辅助函数：预展开（Encoder Helpers, Pre-expansion）

v1 仅提供预展开辅助函数（Pre-expansion Helpers）：每次调用都将协议有效载荷（Protocol Payload）展开为已完全确定的 `pulse_symbol` 数组，随后由调用方通过 `pulse_io_transmit_sync` 或实时输入输出（RTIO）路径提交该数组。

后续版本可能增加流式变体（Streaming Variant），由发送中断服务例程（TX ISR）逐步消耗有效载荷；该路径将作为新增能力提供，不会改变此处定义的入口点（Entry Points）。

<a id="r_gaca42826a8404d4e5e1eacefc5f17debf"></a>

```c
int pulse_io_encode_bytes (const struct pulse_io_bit_template *tmpl, const uint8_t *bytes, size_t nbytes, struct pulse_symbol *out, size_t out_cap, size_t *produced)
```

相关声明：[pulse_io_encode_bytes](#gaca42826a8404d4e5e1eacefc5f17debf)、[pulse_io_bit_template](../device_power_control_model_reference/P062_pulse_io_bit_template_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pulse_symbol](../device_power_control_model_reference/P070_pulse_symbol_结构体.md)。

使用位模板（Bit Template）将字节流展开为脉冲符号（Pulse Symbols）。

## 9.6\_实时输入输出集成（RTIO Integration）

后端（Backend）可以提供实时输入输出（RTIO）提交路径，以及协议编码器和解码器虚函数表（Encoder and Decoder Vtables），采用与传感器子系统（Sensor Subsystem）相似的方式。

采用这些接口时，用户空间（Userspace）和异步输入输出（Asynchronous I/O）机制由 RTIO 提供：客户端将有效载荷编码到符号缓冲区（Symbol Buffer），经 RTIO 队列提交，再对捕获的回复进行解码。

<a id="r_gaf925af6fa08b119550e51024c5ebc408"></a>

```c
int pulse_io_get_encoder (const struct device *dev, const struct pulse_io_encoder_api **api)
```

相关声明：[pulse_io_get_encoder](#gaf925af6fa08b119550e51024c5ebc408)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_encoder_api](../device_power_control_model_reference/P067_pulse_io_encoder_api_结构体.md)。

获取后端编码器虚函数表（Encoder Vtable）。

<a id="r_ga382adc1d7095dba8dd087c47c551436c"></a>

```c
int pulse_io_get_decoder (const struct device *dev, const struct pulse_io_decoder_api **api)
```

相关声明：[pulse_io_get_decoder](#ga382adc1d7095dba8dd087c47c551436c)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_decoder_api](../device_power_control_model_reference/P065_pulse_io_decoder_api_结构体.md)。

获取后端解码器虚函数表（Decoder Vtable）。

<a id="r_ga05add5c7dc934ad84ddafbfe4c08d2a6"></a>

```c
int pulse_io_decode_bytes (const struct pulse_io_bit_template *tmpl, uint32_t tolerance_ticks, const struct pulse_symbol *in, size_t nsyms, uint8_t *out, size_t out_cap, size_t *produced)
```

相关声明：[pulse_io_decode_bytes](#ga05add5c7dc934ad84ddafbfe4c08d2a6)、[pulse_io_bit_template](../device_power_control_model_reference/P062_pulse_io_bit_template_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pulse_symbol](../device_power_control_model_reference/P070_pulse_symbol_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

默认符号流解码器（Symbol-stream Decoder）。

## 9.7\_详细说明（Detailed Documentation）

<a id="ga1188071d39a4018b719f18d019ba6f89"></a>

### `pulse_io_dir`

```c
enum pulse_io_dir
```

```c
#include <zephyr/drivers/pulse_io.h>
```

已配置通道的方向（Direction）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PULSE_IO_DIR_TX` | 发送，即生成边沿（Transmit/Generate Edges）。 |
| `PULSE_IO_DIR_RX` | 接收，即捕获边沿（Receive/Capture Edges）。 |

<a id="ga8a69608ee00587642aca6e0d69878b07"></a>

### `pulse_io_mode`

```c
enum pulse_io_mode
```

```c
#include <zephyr/drivers/pulse_io.h>
```

脉冲流提交模式（Pulse Stream Submission Modes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PULSE_IO_MODE_SYMBOL` | 由任意 `{level, duration}` 对组成的符号流（Symbol Stream）。 |
| `PULSE_IO_MODE_CELL` | 固定周期单元（Fixed-period Cells），每个单元具有各自的占空比或电平。 |

<a id="gaa3a5b31cb44647823aa60af4416e6d3f"></a>

### `pulse_io_channel_configure()`

```c
int pulse_io_channel_configure ( const struct device * dev, struct pulse_io_channel * chan, const struct pulse_io_config * cfg )
```

```c
#include <zephyr/drivers/pulse_io.h>
```

配置已预留的通道（Reserved Channel）。

必须在对该通道执行任何发送／接收之前调用。可以在操作之间再次调用以重新配置（Reconfigure）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOTSUP` | `cfg` 请求不支持的模式或功能（Mode or Feature）时。 |
| `-EINVAL` | `cfg` 包含超出范围的值时。 |

<a id="ga0a0eb57e852853da9c3ba1e262991091"></a>

### `pulse_io_channel_get()`

```c
int pulse_io_channel_get ( const struct device * dev, uint8_t channel_idx, struct pulse_io_channel ** chan )
```

```c
#include <zephyr/drivers/pulse_io.h>
```

预留通道以供独占使用（Exclusive Use）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 脉冲输入输出设备（Pulse IO Device）。 |
| `channel_idx` | 硬件通道索引（Hardware Channel Index），范围为 `0..caps.num_channels - 1`。 |
| `chan` | 输出：用于后续调用的句柄（Handle）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EBUSY` | 通道已被预留（Reserved）时。 |
| `-ENODEV` | `channel_idx` 超出范围时。 |

<a id="gafcce0615be70ca39c346df4c260f09d2"></a>

### `pulse_io_channel_release()`

```c
int pulse_io_channel_release ( const struct device * dev, struct pulse_io_channel * chan )
```

```c
#include <zephyr/drivers/pulse_io.h>
```

释放先前通过 `pulse_io_channel_get` 获取的通道。

<a id="ga05add5c7dc934ad84ddafbfe4c08d2a6"></a>

### `pulse_io_decode_bytes()`

```c
int pulse_io_decode_bytes ( const struct pulse_io_bit_template * tmpl, uint32_t tolerance_ticks, const struct pulse_symbol * in, size_t nsyms, uint8_t * out, size_t out_cap, size_t * produced )
```

```c
#include <zephyr/drivers/pulse_io.h>
```

默认符号流解码器（Symbol-stream Decoder）。

`pulse_io_encode_bytes()` 的逆操作：在 `tolerance_ticks` 容差内，将连续符号对（Symbol Pairs）与 `tmpl` 匹配，并重建字节流（Byte Stream）。后端可将其解码器虚函数表（Decoder Vtable）指向此函数。

<a id="gaca42826a8404d4e5e1eacefc5f17debf"></a>

### `pulse_io_encode_bytes()`

```c
int pulse_io_encode_bytes ( const struct pulse_io_bit_template * tmpl, const uint8_t * bytes, size_t nbytes, struct pulse_symbol * out, size_t out_cap, size_t * produced )
```

```c
#include <zephyr/drivers/pulse_io.h>
```

使用位模板（Bit Template）将字节流展开为脉冲符号（Pulse Symbols）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tmpl` | 位模板（Bit Template）。 |
| `bytes` | 输入字节流（Input Byte Stream）。 |
| `nbytes` | 字节长度（Length of Bytes）。 |
| `out` | 输出缓冲区（Output Buffer）。 |
| `out_cap` | `out` 的容量，以符号数（Symbols）计。 |
| `produced` | 输出：已写入符号数（Number of Symbols Written）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOMEM` | `out_cap` 不足时。 |

<a id="ga3d92ae937058d0675dd56b009aa1138f"></a>

### `pulse_io_get_capabilities()`

```c
int pulse_io_get_capabilities ( const struct device * dev, struct pulse_io_caps * caps )
```

```c
#include <zephyr/drivers/pulse_io.h>
```

查询后端能力（Backend Capabilities）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | 后端（Backend）未实现此功能时。 |

<a id="ga382adc1d7095dba8dd087c47c551436c"></a>

### `pulse_io_get_decoder()`

```c
int pulse_io_get_decoder ( const struct device * dev, const struct pulse_io_decoder_api ** api )
```

```c
#include <zephyr/drivers/pulse_io.h>
```

获取后端解码器虚函数表（Decoder Vtable）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | 后端未提供实时输入输出编解码器（RTIO Codec）时。 |

<a id="gaf925af6fa08b119550e51024c5ebc408"></a>

### `pulse_io_get_encoder()`

```c
int pulse_io_get_encoder ( const struct device * dev, const struct pulse_io_encoder_api ** api )
```

```c
#include <zephyr/drivers/pulse_io.h>
```

获取后端编码器虚函数表（Encoder Vtable）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | 后端未提供实时输入输出编解码器（RTIO Codec）时。 |

<a id="ga1d122c085430f9d4408564b76dee0944"></a>

### `pulse_io_receive_sync()`

```c
int pulse_io_receive_sync ( const struct device * dev, struct pulse_io_channel * chan, const struct pulse_io_rx_req * req, size_t * count, k_timeout_t timeout )
```

```c
#include <zephyr/drivers/pulse_io.h>
```

阻塞式接收（Blocking Receive）。

单次采集（One-shot Capture），达到空闲阈值（Idle Threshold）或缓冲区满时结束。成功时，`count` 被设置为有效条目数。

<a id="ga8810dd66d863919cf3ea03ae27da4cf7"></a>

### `pulse_io_stop()`

```c
int pulse_io_stop ( const struct device * dev, struct pulse_io_channel * chan )
```

```c
#include <zephyr/drivers/pulse_io.h>
```

停止该通道上任何正在进行的发送或接收操作。

<a id="ga3e03e72bb73c8949c222d48f28c03612"></a>

### `pulse_io_transmit_sync()`

```c
int pulse_io_transmit_sync ( const struct device * dev, struct pulse_io_channel * chan, const struct pulse_io_tx_req * req, k_timeout_t timeout )
```

```c
#include <zephyr/drivers/pulse_io.h>
```

阻塞式发送（Blocking Transmit）。

整个 `req` 发送完毕或超时后返回。此调用不能使用无限循环（Infinite Loops），即 `loop_count == UINT32_MAX`；这种情况应改用 RTIO 路径。


## 9.8\_原页交叉引用（Cross References）

- [pulse_io.h](../api_file_signal_device_reference/P017_zephyr__drivers__pulse_io.h_文件参考.md)
- [pulse_symbol](../device_power_control_model_reference/P070_pulse_symbol_结构体.md)
- [pulse_cell](../device_power_control_model_reference/P061_pulse_cell_结构体.md)
- [pulse_io_caps](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md)
- [pulse_io_config](../device_power_control_model_reference/P064_pulse_io_config_结构体.md)
- [pulse_io_tx_req](../device_power_control_model_reference/P069_pulse_io_tx_req_结构体.md)
- [pulse_io_rx_req](../device_power_control_model_reference/P068_pulse_io_rx_req_结构体.md)
- [pulse_io_driver_api](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md)
- [pulse_io_bit_template](../device_power_control_model_reference/P062_pulse_io_bit_template_结构体.md)
- [pulse_io_encoder_api](../device_power_control_model_reference/P067_pulse_io_encoder_api_结构体.md)
- [pulse_io_decoder_api](../device_power_control_model_reference/P065_pulse_io_decoder_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga1188071d39a4018b719f18d019ba6f89ad4c6756a1f8972376620492ab1943ee3"></a>
<a id="gga1188071d39a4018b719f18d019ba6f89ab41397616fbd4b428db60bc6d665186a"></a>
<a id="gga8a69608ee00587642aca6e0d69878b07a72babf2ca6b039635cb177be4f2e5e19"></a>
<a id="gga8a69608ee00587642aca6e0d69878b07ae89d6f0f750e30719501cf32fbe2b220"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_容器（Bins）.md) · [返回大纲](大纲.md) · [下一章](P010_虚拟网络接口支持函数（Virtual Network Interface Support Functions）.md)
