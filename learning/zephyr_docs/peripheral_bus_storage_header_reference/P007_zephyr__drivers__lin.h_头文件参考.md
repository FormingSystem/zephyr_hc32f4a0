---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-7
title: zephyr__drivers__lin.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lin_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_lin.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lin_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

局部互连网络（Local Interconnect Network，LIN）的驱动API。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/clock.h>
#include <zephyr/sys/util.h>
#include <zephyr/syscalls/lin.h>
```

查看此文件的源码。

局部互连网络（Local Interconnect Network，LIN）驱动 API。此文件包含 LIN 通信所需的定义和 API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_lin_5Fconfig"></a>

```c
struct lin_config
```

相关声明：[lin_config](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md)。

局部互连网络（LIN）的配置结构。

<a id="r_lin_5Fmsg"></a>

```c
struct lin_msg
```

相关声明：[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)。

局部互连网络（LIN）的消息结构。

<a id="r_lin_5Fevent"></a>

```c
struct lin_event
```

相关声明：[lin_event](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md)。

局部互连网络（LIN）的事件结构。

<a id="r_lin_5Ffilter"></a>

```c
struct lin_filter
```

相关声明：[lin_filter](../peripheral_bus_storage_model_reference/P024_lin_filter_结构体.md)。

LIN帧过滤器配置（Frame Filter Configuration），仅用于响应者模式。

<a id="r_lin_5Fdriver_5Fconfig"></a>

```c
struct lin_driver_config
```

相关声明：[lin_driver_config](../peripheral_bus_storage_model_reference/P021_lin_driver_config_结构体.md)。

通用LIN驱动配置结构。

<a id="r_lin_5Fdriver_5Fdata"></a>

```c
struct lin_driver_data
```

相关声明：[lin_driver_data](../peripheral_bus_storage_model_reference/P022_lin_driver_data_结构体.md)。

通用LIN驱动数据结构。

<a id="r_lin_5Fdriver_5Fapi"></a>

```c
struct lin_driver_api
```

相关声明：[lin_driver_api](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md)。

驱动操作（Driver Operations）：LIN控制器（Controller）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_gaef5f7c158f409b0655658def9b70b2c4"></a>

```c
#define LIN_ERR_BUS_COLLISION BIT(0)
```

相关声明：[LIN_ERR_BUS_COLLISION](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaef5f7c158f409b0655658def9b70b2c4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

LIN 错误标志（Error flags）。

<a id="r_ga281f21c91817109632824eda43be87c3"></a>

```c
#define LIN_ERR_INVALID_CHECKSUM BIT(1)
```

相关声明：[LIN_ERR_INVALID_CHECKSUM](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga281f21c91817109632824eda43be87c3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

LIN 校验和错误（Checksum error）。

<a id="r_gaf308060dd15eddaaa5307216ed3ea133"></a>

```c
#define LIN_ERR_COUNTER_OVERFLOW BIT(2)
```

相关声明：[LIN_ERR_COUNTER_OVERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaf308060dd15eddaaa5307216ed3ea133)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

LIN 计数器溢出（Counter overflow）。

<a id="r_gab9bea91c4da9809424c41d5d6a52b2f9"></a>

```c
#define LIN_ERR_OVERRUN BIT(3)
```

相关声明：[LIN_ERR_OVERRUN](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gab9bea91c4da9809424c41d5d6a52b2f9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

LIN 数据溢出错误（Overrun error）。

<a id="r_gaa3f54d1c0aa552ac6a59dfdfde2c7353"></a>

```c
#define LIN_ERR_PARITY BIT(4)
```

相关声明：[LIN_ERR_PARITY](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaa3f54d1c0aa552ac6a59dfdfde2c7353)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

LIN 奇偶校验错误（Parity error）。

<a id="r_gaa79791d878cbed37a33cc470b2942321"></a>

```c
#define LIN_ERR_FRAMING BIT(5)
```

相关声明：[LIN_ERR_FRAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaa79791d878cbed37a33cc470b2942321)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

LIN 帧格式错误（Framing error）。

<a id="r_ga2d95ba106f4608f1b71dd99a387719cf"></a>

```c
#define LIN_DT_DRIVER_CONFIG_GET(node_id, _min_bitrate, _max_bitrate)
```

相关声明：[LIN_DT_DRIVER_CONFIG_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga2d95ba106f4608f1b71dd99a387719cf)。

`lin_driver_config` 结构体的静态初始化器（Static initializer）。

<a id="r_gaaa094da48b5566adc8b3ef401da3c652"></a>

```c
#define LIN_DT_DRIVER_CONFIG_INST_GET(inst, _min_bitrate, _max_bitrate)
```

相关声明：[LIN_DT_DRIVER_CONFIG_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaaa094da48b5566adc8b3ef401da3c652)。

根据 `DT_DRV_COMPAT` 实例生成 `lin_driver_config` 结构体的静态初始化器。

<a id="define-members-0"></a>

<a id="r_gad37ddea1dbcc29151c7a504813eebfac"></a>

```c
#define LIN_ID_MASK 0x3FU
```

相关声明：[LIN_ID_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gad37ddea1dbcc29151c7a504813eebfac)。

LIN 帧定义。

<a id="define-members-1"></a>

<a id="r_ga6c506247ef9d1c0d8f1838a31e6df77b"></a>

```c
#define LIN_BUS_CONFLICT_DETECTION BIT(0)
```

相关声明：[LIN_BUS_CONFLICT_DETECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga6c506247ef9d1c0d8f1838a31e6df77b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

LIN 设备配置标志。

<a id="r_gaf1ce3f05c51587ab291ab2b297569edd"></a>

```c
#define LIN_BUS_AUTO_SYNC BIT(1)
```

相关声明：[LIN_BUS_AUTO_SYNC](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaf1ce3f05c51587ab291ab2b297569edd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

启用 LIN 总线自动同步（Auto synchronization）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.3\_类型定义（Typedefs）

<a id="r_ga560c00e1f3b7990836a06c83ab0eca43"></a>

```c
typedef uint32_t lin_config_flags_t
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[lin_config_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga560c00e1f3b7990836a06c83ab0eca43)。

提供用于保存 LIN 控制器配置标志的类型。

<a id="r_ga344a6eade12faa423b8bd2718009b0c5"></a>

```c
typedef uint32_t lin_error_flags_t
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[lin_error_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga344a6eade12faa423b8bd2718009b0c5)。

提供用于保存 LIN 错误标志的类型。

<a id="r_gae69d33055fe07087a19b33dbe7a7252f"></a>

```c
typedef void(* lin_event_callback_t) (const struct device *dev, const struct lin_event *event, void *user_data)
```

相关声明：[lin_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gae69d33055fe07087a19b33dbe7a7252f)、[device](../device_reference/P002_设备对象结构.md)、[lin_event](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md)。

LIN 事件回调函数类型。

<a id="r_ga149ca3972fc800c4fd2bbb0b5d8a85e3"></a>

```c
typedef int(* lin_start_t) (const struct device *dev)
```

相关声明：[lin_start_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga149ca3972fc800c4fd2bbb0b5d8a85e3)、[device](../device_reference/P002_设备对象结构.md)。

启动 LIN 控制器的回调 API。

<a id="r_gab0f27d3ad3637f9040920b3088c1e239"></a>

```c
typedef int(* lin_stop_t) (const struct device *dev)
```

相关声明：[lin_stop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gab0f27d3ad3637f9040920b3088c1e239)、[device](../device_reference/P002_设备对象结构.md)。

停止 LIN 控制器的回调 API。

<a id="r_ga39766c7605a50fcb600e9d72bfcf07d5"></a>

```c
typedef int(* lin_configure_t) (const struct device *dev, const struct lin_config *config)
```

相关声明：[lin_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga39766c7605a50fcb600e9d72bfcf07d5)、[device](../device_reference/P002_设备对象结构.md)、[lin_config](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md)。

配置 LIN 控制器的回调 API。

<a id="r_ga305d83d265245ed657a9974c0bab1962"></a>

```c
typedef int(* lin_get_config_t) (const struct device *dev, struct lin_config *config)
```

相关声明：[lin_get_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga305d83d265245ed657a9974c0bab1962)、[device](../device_reference/P002_设备对象结构.md)、[lin_config](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md)。

获取 LIN 配置的回调 API。

<a id="r_ga8091d2d225709439f9afb2eddeb73792"></a>

```c
typedef int(* lin_send_t) (const struct device *dev, const struct lin_msg *msg, k_timeout_t timeout)
```

相关声明：[lin_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga8091d2d225709439f9afb2eddeb73792)、[device](../device_reference/P002_设备对象结构.md)、[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

发送 LIN 消息的回调 API。

<a id="r_gad77d365c000a2f9c7f2558ec24d0f455"></a>

```c
typedef int(* lin_receive_t) (const struct device *dev, struct lin_msg *msg, k_timeout_t timeout)
```

相关声明：[lin_receive_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gad77d365c000a2f9c7f2558ec24d0f455)、[device](../device_reference/P002_设备对象结构.md)、[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

接收 LIN 消息的回调 API。

<a id="r_ga42976918cdbcec388095d77e398e7633"></a>

```c
typedef int(* lin_response_t) (const struct device *dev, const struct lin_msg *msg, k_timeout_t timeout)
```

相关声明：[lin_response_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga42976918cdbcec388095d77e398e7633)、[device](../device_reference/P002_设备对象结构.md)、[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

处理 LIN 响应消息（Response messages）的回调 API。

<a id="r_gabcad96f6950ec45b71adfd14e4c0c363"></a>

```c
typedef int(* lin_read_t) (const struct device *dev, struct lin_msg *msg, k_timeout_t timeout)
```

相关声明：[lin_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gabcad96f6950ec45b71adfd14e4c0c363)、[device](../device_reference/P002_设备对象结构.md)、[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

读取 LIN 响应消息的回调 API。参数说明见 `lin_read()`。

<a id="r_ga16889d5f804b14ef80a608f6b8a86193"></a>

```c
typedef int(* lin_wakeup_send_t) (const struct device *dev)
```

相关声明：[lin_wakeup_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga16889d5f804b14ef80a608f6b8a86193)、[device](../device_reference/P002_设备对象结构.md)。

发送 LIN 唤醒信号的回调 API。

<a id="r_gad1df29d89982f09a9652db231e36c0c4"></a>

```c
typedef int(* lin_set_event_callback_t) (const struct device *dev, lin_event_callback_t callback, void *user_data)
```

相关声明：[lin_set_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gad1df29d89982f09a9652db231e36c0c4)、[device](../device_reference/P002_设备对象结构.md)、[lin_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gae69d33055fe07087a19b33dbe7a7252f)。

设置 LIN 发送事件回调的回调 API。

<a id="r_ga727b0f7fe4949e3fd17a303e239586bb"></a>

```c
typedef int(* lin_set_rx_filter_t) (const struct device *dev, const struct lin_filter *filter)
```

相关声明：[lin_set_rx_filter_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga727b0f7fe4949e3fd17a303e239586bb)、[device](../device_reference/P002_设备对象结构.md)、[lin_filter](../peripheral_bus_storage_model_reference/P024_lin_filter_结构体.md)。

设置 LIN 接收过滤器（RX filter）的回调 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.4\_枚举（Enumerations）

<a id="r_gaf97478fd971b8b6913386a225078a24f"></a>

```c
enum lin_checksum_type { LIN_CHECKSUM_CLASSIC = 0 , LIN_CHECKSUM_ENHANCED }
```

相关声明：[lin_checksum_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaf97478fd971b8b6913386a225078a24f)、[LIN_CHECKSUM_CLASSIC](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggaf97478fd971b8b6913386a225078a24fa6b6c53f36bcccb2f099e63977bd2391a)、[LIN_CHECKSUM_ENHANCED](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggaf97478fd971b8b6913386a225078a24fa9a93132138ea30a19f03d6bd52c8de5e)。

LIN 校验和类型。

<a id="r_gab7aca457453e6e6409c02903bcdf9bab"></a>

```c
enum lin_event_type { LIN_EVT_RX_HEADER = 0 , LIN_EVT_TX_HEADER , LIN_EVT_RX_DATA , LIN_EVT_TX_DATA , LIN_EVT_TX_WAKEUP , LIN_EVT_RX_WAKEUP , LIN_EVT_ERR }
```

相关声明：[lin_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gab7aca457453e6e6409c02903bcdf9bab)、[LIN_EVT_RX_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9baba9ee3a39dbc2ff9448a5cf443db5c1625)、[LIN_EVT_TX_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9babac57f7922e1bc6328afa742e8efa22211)、[LIN_EVT_RX_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9baba3e30d82061bbcf51d89b63e94d362301)、[LIN_EVT_TX_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9babaa0770ae0419aadfc97ded5e9a524a6eb)、[LIN_EVT_TX_WAKEUP](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9babadd5da0e9a1ceb2536f11991702784508)、[LIN_EVT_RX_WAKEUP](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9baba3d1c9ec13a13ce51893bf4c59f22cc2e)、[LIN_EVT_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9babab70beb6e355ef5c01fe3f8f285e8dd45)。

LIN 事件类型。

<a id="r_ga4d80ed442a8a83985c6ba3658f96fd16"></a>

```c
enum lin_mode { LIN_MODE_COMMANDER = 0 , LIN_MODE_RESPONDER }
```

相关声明：[lin_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga4d80ed442a8a83985c6ba3658f96fd16)、[LIN_MODE_COMMANDER](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gga4d80ed442a8a83985c6ba3658f96fd16aab1c3507ec82321e02c98f4878e6475d)、[LIN_MODE_RESPONDER](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gga4d80ed442a8a83985c6ba3658f96fd16a71650e86f1cd26ae46011a2cdce767b8)。

LIN 工作模式（Operation mode）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.5\_函数（Functions）

<a id="r_gac3d1d8680c88765a49ca9c6d04763158"></a>

```c
static uint8_t lin_get_frame_id (uint8_t pid)
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[lin_get_frame_id](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gac3d1d8680c88765a49ca9c6d04763158)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从受保护标识符（Protected Identifier，PID）中提取 LIN 帧标识符的辅助函数。

<a id="r_ga136329dfada85698d56308d6157abea0"></a>

```c
static uint8_t lin_compute_pid (uint8_t id)
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[lin_compute_pid](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga136329dfada85698d56308d6157abea0)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据帧标识符计算 LIN 受保护标识符（PID）的辅助函数。

<a id="r_gaf8bd57bf6e9306a30fa025c1f9fe09e8"></a>

```c
static bool lin_verify_pid (uint8_t pid)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[lin_verify_pid](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaf8bd57bf6e9306a30fa025c1f9fe09e8)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

验证 LIN 受保护标识符（PID）的辅助函数。

<a id="r_ga880b0c5dd454342160bcf454de5105e9"></a>

```c
const struct device * lin_get_transceiver (const struct device *dev)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[lin_get_transceiver](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga880b0c5dd454342160bcf454de5105e9)、[device](../device_reference/P002_设备对象结构.md)。

获取与 LIN 控制器关联的 LIN 收发器（Transceiver）设备。

<a id="r_ga752004d89d50932711c3aa6189874478"></a>

```c
int lin_start (const struct device *dev)
```

相关声明：[lin_start](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga752004d89d50932711c3aa6189874478)、[device](../device_reference/P002_设备对象结构.md)。

启动 LIN 控制器。

<a id="r_gaefe6f3853ea2f70d8ba4d6ab86f62b57"></a>

```c
int lin_stop (const struct device *dev)
```

相关声明：[lin_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaefe6f3853ea2f70d8ba4d6ab86f62b57)、[device](../device_reference/P002_设备对象结构.md)。

停止 LIN 控制器。

<a id="r_ga97468832dddf9e21b33e93a36c60102a"></a>

```c
int lin_configure (const struct device *dev, const struct lin_config *config)
```

相关声明：[lin_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga97468832dddf9e21b33e93a36c60102a)、[device](../device_reference/P002_设备对象结构.md)、[lin_config](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md)。

配置 LIN 控制器。

<a id="r_ga9410aa6989aea2cc173e7f36dcaf6be7"></a>

```c
int lin_get_config (const struct device *dev, struct lin_config *config)
```

相关声明：[lin_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga9410aa6989aea2cc173e7f36dcaf6be7)、[device](../device_reference/P002_设备对象结构.md)、[lin_config](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md)。

获取当前 LIN 配置。

<a id="r_ga2a2afff5c7524504f24860673c24a217"></a>

```c
int lin_send (const struct device *dev, const struct lin_msg *msg, k_timeout_t timeout)
```

相关声明：[lin_send](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga2a2afff5c7524504f24860673c24a217)、[device](../device_reference/P002_设备对象结构.md)、[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

发送 LIN 消息，仅适用于命令方模式（Commander mode）。

<a id="r_ga13e0a57996ba2f010bcda6561298b658"></a>

```c
int lin_receive (const struct device *dev, struct lin_msg *msg, k_timeout_t timeout)
```

相关声明：[lin_receive](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga13e0a57996ba2f010bcda6561298b658)、[device](../device_reference/P002_设备对象结构.md)、[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

接收 LIN 消息，仅适用于命令方模式（Commander mode）。

<a id="r_gafae0fa8e806c2856f61642ef80368ec8"></a>

```c
int lin_response (const struct device *dev, const struct lin_msg *msg, k_timeout_t timeout)
```

相关声明：[lin_response](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gafae0fa8e806c2856f61642ef80368ec8)、[device](../device_reference/P002_设备对象结构.md)、[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

响应收到的帧头，仅适用于响应方模式。

<a id="r_ga58c5052899f49601a91d6da614ea8c82"></a>

```c
int lin_read (const struct device *dev, struct lin_msg *msg, k_timeout_t timeout)
```

相关声明：[lin_read](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga58c5052899f49601a91d6da614ea8c82)、[device](../device_reference/P002_设备对象结构.md)、[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

开始数据接收，仅适用于响应方模式。

<a id="r_ga0fe3631c3f9b7100162b5f48e83bd6e3"></a>

```c
int lin_wakeup_send (const struct device *dev)
```

相关声明：[lin_wakeup_send](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga0fe3631c3f9b7100162b5f48e83bd6e3)、[device](../device_reference/P002_设备对象结构.md)。

发送 LIN 唤醒信号（Wakeup signal）。

<a id="r_ga07ec84c466d94f6057d7852998b2fbb2"></a>

```c
static int lin_set_event_callback (const struct device *dev, lin_event_callback_t callback, void *user_data)
```

相关声明：[lin_set_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga07ec84c466d94f6057d7852998b2fbb2)、[device](../device_reference/P002_设备对象结构.md)、[lin_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gae69d33055fe07087a19b33dbe7a7252f)。

设置 LIN 事件回调。

<a id="r_ga7594e89b4fc3a018c1cd0010bd4a6ac1"></a>

```c
int lin_set_rx_filter (const struct device *dev, const struct lin_filter *filter)
```

相关声明：[lin_set_rx_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga7594e89b4fc3a018c1cd0010bd4a6ac1)、[device](../device_reference/P002_设备对象结构.md)、[lin_filter](../peripheral_bus_storage_model_reference/P024_lin_filter_结构体.md)。

设置 LIN 接收过滤器，仅适用于响应方模式（Responder mode）。


## 7.6\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/sys/clock.h](../timer_reference/P091_系统时钟头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/lin_8h_source.html)
- [lin_config](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md)
- [lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)
- [lin_event](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md)
- [lin_filter](../peripheral_bus_storage_model_reference/P024_lin_filter_结构体.md)
- [lin_driver_config](../peripheral_bus_storage_model_reference/P021_lin_driver_config_结构体.md)
- [lin_driver_data](../peripheral_bus_storage_model_reference/P022_lin_driver_data_结构体.md)
- [lin_driver_api](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md)
- [LIN_ERR_BUS_COLLISION](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaef5f7c158f409b0655658def9b70b2c4)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [LIN_ERR_INVALID_CHECKSUM](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga281f21c91817109632824eda43be87c3)
- [LIN_ERR_COUNTER_OVERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaf308060dd15eddaaa5307216ed3ea133)
- [LIN_ERR_OVERRUN](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gab9bea91c4da9809424c41d5d6a52b2f9)
- [LIN_ERR_PARITY](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaa3f54d1c0aa552ac6a59dfdfde2c7353)
- [LIN_ERR_FRAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaa79791d878cbed37a33cc470b2942321)
- [LIN_DT_DRIVER_CONFIG_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga2d95ba106f4608f1b71dd99a387719cf)
- [LIN_DT_DRIVER_CONFIG_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaaa094da48b5566adc8b3ef401da3c652)
- [LIN_ID_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gad37ddea1dbcc29151c7a504813eebfac)
- [LIN_BUS_CONFLICT_DETECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga6c506247ef9d1c0d8f1838a31e6df77b)
- [LIN_BUS_AUTO_SYNC](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaf1ce3f05c51587ab291ab2b297569edd)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [lin_config_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga560c00e1f3b7990836a06c83ab0eca43)
- [lin_error_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga344a6eade12faa423b8bd2718009b0c5)
- [lin_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gae69d33055fe07087a19b33dbe7a7252f)
- [device](../device_reference/P002_设备对象结构.md)
- [lin_start_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga149ca3972fc800c4fd2bbb0b5d8a85e3)
- [lin_stop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gab0f27d3ad3637f9040920b3088c1e239)
- [lin_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga39766c7605a50fcb600e9d72bfcf07d5)
- [lin_get_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga305d83d265245ed657a9974c0bab1962)
- [lin_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga8091d2d225709439f9afb2eddeb73792)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [lin_receive_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gad77d365c000a2f9c7f2558ec24d0f455)
- [lin_response_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga42976918cdbcec388095d77e398e7633)
- [lin_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gabcad96f6950ec45b71adfd14e4c0c363)
- [lin_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga58c5052899f49601a91d6da614ea8c82)
- [lin_wakeup_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga16889d5f804b14ef80a608f6b8a86193)
- [lin_set_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gad1df29d89982f09a9652db231e36c0c4)
- [lin_set_rx_filter_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga727b0f7fe4949e3fd17a303e239586bb)
- [lin_checksum_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaf97478fd971b8b6913386a225078a24f)
- [LIN_CHECKSUM_CLASSIC](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggaf97478fd971b8b6913386a225078a24fa6b6c53f36bcccb2f099e63977bd2391a)
- [LIN_CHECKSUM_ENHANCED](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggaf97478fd971b8b6913386a225078a24fa9a93132138ea30a19f03d6bd52c8de5e)
- [lin_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gab7aca457453e6e6409c02903bcdf9bab)
- [LIN_EVT_RX_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9baba9ee3a39dbc2ff9448a5cf443db5c1625)
- [LIN_EVT_TX_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9babac57f7922e1bc6328afa742e8efa22211)
- [LIN_EVT_RX_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9baba3e30d82061bbcf51d89b63e94d362301)
- [LIN_EVT_TX_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9babaa0770ae0419aadfc97ded5e9a524a6eb)
- [LIN_EVT_TX_WAKEUP](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9babadd5da0e9a1ceb2536f11991702784508)
- [LIN_EVT_RX_WAKEUP](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9baba3d1c9ec13a13ce51893bf4c59f22cc2e)
- [LIN_EVT_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9babab70beb6e355ef5c01fe3f8f285e8dd45)
- [lin_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga4d80ed442a8a83985c6ba3658f96fd16)
- [LIN_MODE_COMMANDER](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gga4d80ed442a8a83985c6ba3658f96fd16aab1c3507ec82321e02c98f4878e6475d)
- [LIN_MODE_RESPONDER](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gga4d80ed442a8a83985c6ba3658f96fd16a71650e86f1cd26ae46011a2cdce767b8)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [lin_get_frame_id](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gac3d1d8680c88765a49ca9c6d04763158)
- [lin_compute_pid](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga136329dfada85698d56308d6157abea0)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [lin_verify_pid](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaf8bd57bf6e9306a30fa025c1f9fe09e8)
- [lin_get_transceiver](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga880b0c5dd454342160bcf454de5105e9)
- [lin_start](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga752004d89d50932711c3aa6189874478)
- [lin_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaefe6f3853ea2f70d8ba4d6ab86f62b57)
- [lin_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga97468832dddf9e21b33e93a36c60102a)
- [lin_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga9410aa6989aea2cc173e7f36dcaf6be7)
- [lin_send](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga2a2afff5c7524504f24860673c24a217)
- [lin_receive](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga13e0a57996ba2f010bcda6561298b658)
- [lin_response](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gafae0fa8e806c2856f61642ef80368ec8)
- [lin_wakeup_send](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga0fe3631c3f9b7100162b5f48e83bd6e3)
- [lin_set_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga07ec84c466d94f6057d7852998b2fbb2)
- [lin_set_rx_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga7594e89b4fc3a018c1cd0010bd4a6ac1)

<a id="LIN_ERR_FLAGS"></a>
<a id="LIN_CONFIG_FLAGS"></a>
<a id="header-details"></a>

---

[上一章](P006_zephyr__drivers__fpga.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__pmci__mctp__mctp_i2c_gpio_controller.h_头文件参考.md)
