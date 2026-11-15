---
id: learning.zephyr-docs.api-file-signal-device-reference.page-17
title: zephyr__drivers__pulse_io.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pulse__io_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_drivers\_\_pulse\_io.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pulse__io_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

脉冲输入输出（Pulse IO）子系统API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/rtio/rtio.h>
#include <zephyr/sys/util.h>
#include <zephyr/syscalls/pulse_io.h>
```

查看此文件的源码。

脉冲输入输出（Pulse IO）子系统API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 17.1\_数据结构（Data Structures）

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

## 17.2\_枚举（Enumerations）

<a id="r_ga8a69608ee00587642aca6e0d69878b07"></a>

```c
enum pulse_io_mode { PULSE_IO_MODE_SYMBOL = BIT(0) , PULSE_IO_MODE_CELL = BIT(1) }
```

相关声明：[pulse_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga8a69608ee00587642aca6e0d69878b07)、[PULSE_IO_MODE_SYMBOL](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gga8a69608ee00587642aca6e0d69878b07a72babf2ca6b039635cb177be4f2e5e19)、[PULSE_IO_MODE_CELL](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gga8a69608ee00587642aca6e0d69878b07ae89d6f0f750e30719501cf32fbe2b220)。

脉冲流提交模式（Pulse Stream Submission Modes）。

<a id="r_ga1188071d39a4018b719f18d019ba6f89"></a>

```c
enum pulse_io_dir { PULSE_IO_DIR_TX , PULSE_IO_DIR_RX }
```

相关声明：[pulse_io_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga1188071d39a4018b719f18d019ba6f89)、[PULSE_IO_DIR_TX](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gga1188071d39a4018b719f18d019ba6f89ad4c6756a1f8972376620492ab1943ee3)、[PULSE_IO_DIR_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gga1188071d39a4018b719f18d019ba6f89ab41397616fbd4b428db60bc6d665186a)。

已配置通道的方向（Direction）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.3\_函数（Functions）

<a id="r_ga3d92ae937058d0675dd56b009aa1138f"></a>

```c
int pulse_io_get_capabilities (const struct device *dev, struct pulse_io_caps *caps)
```

相关声明：[pulse_io_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga3d92ae937058d0675dd56b009aa1138f)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_caps](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md)。

查询后端能力（Backend Capabilities）。

<a id="r_ga0a0eb57e852853da9c3ba1e262991091"></a>

```c
int pulse_io_channel_get (const struct device *dev, uint8_t channel_idx, struct pulse_io_channel **chan)
```

相关声明：[pulse_io_channel_get](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga0a0eb57e852853da9c3ba1e262991091)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

预留通道以供独占使用（Exclusive Use）。

<a id="r_gafcce0615be70ca39c346df4c260f09d2"></a>

```c
int pulse_io_channel_release (const struct device *dev, struct pulse_io_channel *chan)
```

相关声明：[pulse_io_channel_release](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gafcce0615be70ca39c346df4c260f09d2)、[device](../device_reference/P002_设备对象结构.md)。

释放先前通过 `pulse_io_channel_get` 获取的通道。

<a id="r_gaa3a5b31cb44647823aa60af4416e6d3f"></a>

```c
int pulse_io_channel_configure (const struct device *dev, struct pulse_io_channel *chan, const struct pulse_io_config *cfg)
```

相关声明：[pulse_io_channel_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gaa3a5b31cb44647823aa60af4416e6d3f)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_config](../device_power_control_model_reference/P064_pulse_io_config_结构体.md)。

配置已预留的通道（Reserved Channel）。

<a id="r_ga3e03e72bb73c8949c222d48f28c03612"></a>

```c
int pulse_io_transmit_sync (const struct device *dev, struct pulse_io_channel *chan, const struct pulse_io_tx_req *req, k_timeout_t timeout)
```

相关声明：[pulse_io_transmit_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga3e03e72bb73c8949c222d48f28c03612)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_tx_req](../device_power_control_model_reference/P069_pulse_io_tx_req_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

阻塞式发送（Blocking Transmit）。

<a id="r_ga1d122c085430f9d4408564b76dee0944"></a>

```c
int pulse_io_receive_sync (const struct device *dev, struct pulse_io_channel *chan, const struct pulse_io_rx_req *req, size_t *count, k_timeout_t timeout)
```

相关声明：[pulse_io_receive_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga1d122c085430f9d4408564b76dee0944)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_rx_req](../device_power_control_model_reference/P068_pulse_io_rx_req_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

阻塞式接收（Blocking Receive）。

<a id="r_ga8810dd66d863919cf3ea03ae27da4cf7"></a>

```c
int pulse_io_stop (const struct device *dev, struct pulse_io_channel *chan)
```

相关声明：[pulse_io_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga8810dd66d863919cf3ea03ae27da4cf7)、[device](../device_reference/P002_设备对象结构.md)。

停止该通道上任何正在进行的发送或接收操作。

<a id="func-members-0"></a>

### 编码器辅助函数：预展开（Encoder Helpers, Pre-expansion）

v1 仅提供预展开辅助函数（Pre-expansion Helpers）：每次调用都将协议有效载荷（Protocol Payload）展开为已完全确定的 `pulse_symbol` 数组，随后由调用方通过 `pulse_io_transmit_sync` 或实时输入输出（RTIO）路径提交该数组。

后续版本可能增加流式变体（Streaming Variant），由发送中断服务例程（TX ISR）逐步消耗有效载荷；该路径将作为新增能力提供，不会改变此处定义的入口点（Entry Points）。

<a id="r_gaca42826a8404d4e5e1eacefc5f17debf"></a>

```c
int pulse_io_encode_bytes (const struct pulse_io_bit_template *tmpl, const uint8_t *bytes, size_t nbytes, struct pulse_symbol *out, size_t out_cap, size_t *produced)
```

相关声明：[pulse_io_encode_bytes](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gaca42826a8404d4e5e1eacefc5f17debf)、[pulse_io_bit_template](../device_power_control_model_reference/P062_pulse_io_bit_template_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pulse_symbol](../device_power_control_model_reference/P070_pulse_symbol_结构体.md)。

使用位模板（Bit Template）将字节流展开为脉冲符号（Pulse Symbols）。

<a id="func-members-1"></a>

### 实时输入输出集成（RTIO Integration）

后端（Backend）可以提供实时输入输出（RTIO）提交路径，以及协议编码器和解码器虚函数表（Encoder and Decoder Vtables），采用与传感器子系统（Sensor Subsystem）相似的方式。

采用这些接口时，用户空间（Userspace）和异步输入输出（Asynchronous I/O）机制由 RTIO 提供：客户端将有效载荷编码到符号缓冲区（Symbol Buffer），经 RTIO 队列提交，再对捕获的回复进行解码。

<a id="r_gaf925af6fa08b119550e51024c5ebc408"></a>

```c
int pulse_io_get_encoder (const struct device *dev, const struct pulse_io_encoder_api **api)
```

相关声明：[pulse_io_get_encoder](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gaf925af6fa08b119550e51024c5ebc408)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_encoder_api](../device_power_control_model_reference/P067_pulse_io_encoder_api_结构体.md)。

获取后端编码器虚函数表（Encoder Vtable）。

<a id="r_ga382adc1d7095dba8dd087c47c551436c"></a>

```c
int pulse_io_get_decoder (const struct device *dev, const struct pulse_io_decoder_api **api)
```

相关声明：[pulse_io_get_decoder](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga382adc1d7095dba8dd087c47c551436c)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_decoder_api](../device_power_control_model_reference/P065_pulse_io_decoder_api_结构体.md)。

获取后端解码器虚函数表（Decoder Vtable）。

<a id="r_ga05add5c7dc934ad84ddafbfe4c08d2a6"></a>

```c
int pulse_io_decode_bytes (const struct pulse_io_bit_template *tmpl, uint32_t tolerance_ticks, const struct pulse_symbol *in, size_t nsyms, uint8_t *out, size_t out_cap, size_t *produced)
```

相关声明：[pulse_io_decode_bytes](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga05add5c7dc934ad84ddafbfe4c08d2a6)、[pulse_io_bit_template](../device_power_control_model_reference/P062_pulse_io_bit_template_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pulse_symbol](../device_power_control_model_reference/P070_pulse_symbol_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

默认符号流解码器（Symbol-stream Decoder）。


## 17.4\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/rtio/rtio.h](../rtio_core_reference/P003_RTIO核心头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_configuration_reference/P072_pulse_io.h_源码浏览.md)
- [pulse_symbol](../device_power_control_model_reference/P070_pulse_symbol_结构体.md)
- [pulse_cell](../device_power_control_model_reference/P061_pulse_cell_结构体.md)
- [pulse_io_caps](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md)
- [pulse_io_config](../device_power_control_model_reference/P064_pulse_io_config_结构体.md)
- [pulse_io_tx_req](../device_power_control_model_reference/P069_pulse_io_tx_req_结构体.md)
- [pulse_io_rx_req](../device_power_control_model_reference/P068_pulse_io_rx_req_结构体.md)
- [pulse_io_driver_api](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md)
- [pulse_io_bit_template](../device_power_control_model_reference/P062_pulse_io_bit_template_结构体.md)
- [pulse_io_encode_bytes](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gaca42826a8404d4e5e1eacefc5f17debf)
- [pulse_io_encoder_api](../device_power_control_model_reference/P067_pulse_io_encoder_api_结构体.md)
- [pulse_io_decoder_api](../device_power_control_model_reference/P065_pulse_io_decoder_api_结构体.md)
- [pulse_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga8a69608ee00587642aca6e0d69878b07)
- [PULSE_IO_MODE_SYMBOL](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gga8a69608ee00587642aca6e0d69878b07a72babf2ca6b039635cb177be4f2e5e19)
- [PULSE_IO_MODE_CELL](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gga8a69608ee00587642aca6e0d69878b07ae89d6f0f750e30719501cf32fbe2b220)
- [pulse_io_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga1188071d39a4018b719f18d019ba6f89)
- [PULSE_IO_DIR_TX](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gga1188071d39a4018b719f18d019ba6f89ad4c6756a1f8972376620492ab1943ee3)
- [PULSE_IO_DIR_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gga1188071d39a4018b719f18d019ba6f89ab41397616fbd4b428db60bc6d665186a)
- [pulse_io_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga3d92ae937058d0675dd56b009aa1138f)
- [device](../device_reference/P002_设备对象结构.md)
- [pulse_io_channel_get](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga0a0eb57e852853da9c3ba1e262991091)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [pulse_io_channel_release](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gafcce0615be70ca39c346df4c260f09d2)
- [pulse_io_channel_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gaa3a5b31cb44647823aa60af4416e6d3f)
- [pulse_io_transmit_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga3e03e72bb73c8949c222d48f28c03612)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [pulse_io_receive_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga1d122c085430f9d4408564b76dee0944)
- [pulse_io_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga8810dd66d863919cf3ea03ae27da4cf7)
- [pulse_io_get_encoder](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gaf925af6fa08b119550e51024c5ebc408)
- [pulse_io_get_decoder](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga382adc1d7095dba8dd087c47c551436c)
- [pulse_io_decode_bytes](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga05add5c7dc934ad84ddafbfe4c08d2a6)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>

---

[上一章](P016_zephyr__net__phy.h_文件参考.md) · [返回大纲](大纲.md)
