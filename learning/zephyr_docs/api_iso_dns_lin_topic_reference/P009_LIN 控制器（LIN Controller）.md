---
id: learning.zephyr-docs.api-iso-dns-lin-topic-reference.page-9
title: LIN 控制器（LIN Controller）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_LIN 控制器（LIN Controller）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LIN 控制器接口。

<a id="details"></a>

LIN 控制器接口（LIN Controller Interfaces）。自 4.5 引入，版本 0.1.0。

<a id="header-files"></a>
<a id="files"></a>

## 9.1\_文件（Files）

<a id="r_lin_2Eh"></a>

```c
file lin.h
```

相关声明：[lin.h](../peripheral_bus_storage_header_reference/P007_zephyr__drivers__lin.h_头文件参考.md)。

局部互连网络（Local Interconnect Network，LIN）的驱动API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.2\_数据结构（Data Structures）

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

## 9.3\_宏定义（Macros）

<a id="r_gaef5f7c158f409b0655658def9b70b2c4"></a>

```c
#define LIN_ERR_BUS_COLLISION BIT(0)
```

相关声明：[LIN_ERR_BUS_COLLISION](#gaef5f7c158f409b0655658def9b70b2c4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

LIN 错误标志（Error flags）。

<a id="r_ga281f21c91817109632824eda43be87c3"></a>

```c
#define LIN_ERR_INVALID_CHECKSUM BIT(1)
```

相关声明：[LIN_ERR_INVALID_CHECKSUM](#ga281f21c91817109632824eda43be87c3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

LIN 校验和错误（Checksum error）。

<a id="r_gaf308060dd15eddaaa5307216ed3ea133"></a>

```c
#define LIN_ERR_COUNTER_OVERFLOW BIT(2)
```

相关声明：[LIN_ERR_COUNTER_OVERFLOW](#gaf308060dd15eddaaa5307216ed3ea133)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

LIN 计数器溢出（Counter overflow）。

<a id="r_gab9bea91c4da9809424c41d5d6a52b2f9"></a>

```c
#define LIN_ERR_OVERRUN BIT(3)
```

相关声明：[LIN_ERR_OVERRUN](#gab9bea91c4da9809424c41d5d6a52b2f9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

LIN 数据溢出错误（Overrun error）。

<a id="r_gaa3f54d1c0aa552ac6a59dfdfde2c7353"></a>

```c
#define LIN_ERR_PARITY BIT(4)
```

相关声明：[LIN_ERR_PARITY](#gaa3f54d1c0aa552ac6a59dfdfde2c7353)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

LIN 奇偶校验错误（Parity error）。

<a id="r_gaa79791d878cbed37a33cc470b2942321"></a>

```c
#define LIN_ERR_FRAMING BIT(5)
```

相关声明：[LIN_ERR_FRAMING](#gaa79791d878cbed37a33cc470b2942321)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

LIN 帧格式错误（Framing error）。

<a id="r_ga2d95ba106f4608f1b71dd99a387719cf"></a>

```c
#define LIN_DT_DRIVER_CONFIG_GET(node_id, _min_bitrate, _max_bitrate)
```

相关声明：[LIN_DT_DRIVER_CONFIG_GET](#ga2d95ba106f4608f1b71dd99a387719cf)。

`lin_driver_config` 结构体的静态初始化器（Static initializer）。

<a id="r_gaaa094da48b5566adc8b3ef401da3c652"></a>

```c
#define LIN_DT_DRIVER_CONFIG_INST_GET(inst, _min_bitrate, _max_bitrate)
```

相关声明：[LIN_DT_DRIVER_CONFIG_INST_GET](#gaaa094da48b5566adc8b3ef401da3c652)。

根据 `DT_DRV_COMPAT` 实例生成 `lin_driver_config` 结构体的静态初始化器。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.4\_类型定义（Typedefs）

<a id="r_ga560c00e1f3b7990836a06c83ab0eca43"></a>

```c
typedef uint32_t lin_config_flags_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[lin_config_flags_t](#ga560c00e1f3b7990836a06c83ab0eca43)。

提供用于保存 LIN 控制器配置标志的类型。

<a id="r_ga344a6eade12faa423b8bd2718009b0c5"></a>

```c
typedef uint32_t lin_error_flags_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[lin_error_flags_t](#ga344a6eade12faa423b8bd2718009b0c5)。

提供用于保存 LIN 错误标志的类型。

<a id="r_gae69d33055fe07087a19b33dbe7a7252f"></a>

```c
typedef void(* lin_event_callback_t) (const struct device *dev, const struct lin_event *event, void *user_data)
```

相关声明：[lin_event_callback_t](#gae69d33055fe07087a19b33dbe7a7252f)、[device](../device_reference/P002_设备对象结构.md)、[lin_event](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md)。

LIN 事件回调函数类型。

<a id="r_ga149ca3972fc800c4fd2bbb0b5d8a85e3"></a>

```c
typedef int(* lin_start_t) (const struct device *dev)
```

相关声明：[lin_start_t](#ga149ca3972fc800c4fd2bbb0b5d8a85e3)、[device](../device_reference/P002_设备对象结构.md)。

启动 LIN 控制器的回调 API。

<a id="r_gab0f27d3ad3637f9040920b3088c1e239"></a>

```c
typedef int(* lin_stop_t) (const struct device *dev)
```

相关声明：[lin_stop_t](#gab0f27d3ad3637f9040920b3088c1e239)、[device](../device_reference/P002_设备对象结构.md)。

停止 LIN 控制器的回调 API。

<a id="r_ga39766c7605a50fcb600e9d72bfcf07d5"></a>

```c
typedef int(* lin_configure_t) (const struct device *dev, const struct lin_config *config)
```

相关声明：[lin_configure_t](#ga39766c7605a50fcb600e9d72bfcf07d5)、[device](../device_reference/P002_设备对象结构.md)、[lin_config](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md)。

配置 LIN 控制器的回调 API。

<a id="r_ga305d83d265245ed657a9974c0bab1962"></a>

```c
typedef int(* lin_get_config_t) (const struct device *dev, struct lin_config *config)
```

相关声明：[lin_get_config_t](#ga305d83d265245ed657a9974c0bab1962)、[device](../device_reference/P002_设备对象结构.md)、[lin_config](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md)。

获取 LIN 配置的回调 API。

<a id="r_ga8091d2d225709439f9afb2eddeb73792"></a>

```c
typedef int(* lin_send_t) (const struct device *dev, const struct lin_msg *msg, k_timeout_t timeout)
```

相关声明：[lin_send_t](#ga8091d2d225709439f9afb2eddeb73792)、[device](../device_reference/P002_设备对象结构.md)、[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

发送 LIN 消息的回调 API。

<a id="r_gad77d365c000a2f9c7f2558ec24d0f455"></a>

```c
typedef int(* lin_receive_t) (const struct device *dev, struct lin_msg *msg, k_timeout_t timeout)
```

相关声明：[lin_receive_t](#gad77d365c000a2f9c7f2558ec24d0f455)、[device](../device_reference/P002_设备对象结构.md)、[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

接收 LIN 消息的回调 API。

<a id="r_ga42976918cdbcec388095d77e398e7633"></a>

```c
typedef int(* lin_response_t) (const struct device *dev, const struct lin_msg *msg, k_timeout_t timeout)
```

相关声明：[lin_response_t](#ga42976918cdbcec388095d77e398e7633)、[device](../device_reference/P002_设备对象结构.md)、[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

处理 LIN 响应消息（Response messages）的回调 API。

<a id="r_gabcad96f6950ec45b71adfd14e4c0c363"></a>

```c
typedef int(* lin_read_t) (const struct device *dev, struct lin_msg *msg, k_timeout_t timeout)
```

相关声明：[lin_read_t](#gabcad96f6950ec45b71adfd14e4c0c363)、[device](../device_reference/P002_设备对象结构.md)、[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

读取 LIN 响应消息的回调 API。参数说明见 `lin_read()`。

<a id="r_ga16889d5f804b14ef80a608f6b8a86193"></a>

```c
typedef int(* lin_wakeup_send_t) (const struct device *dev)
```

相关声明：[lin_wakeup_send_t](#ga16889d5f804b14ef80a608f6b8a86193)、[device](../device_reference/P002_设备对象结构.md)。

发送 LIN 唤醒信号的回调 API。

<a id="r_gad1df29d89982f09a9652db231e36c0c4"></a>

```c
typedef int(* lin_set_event_callback_t) (const struct device *dev, lin_event_callback_t callback, void *user_data)
```

相关声明：[lin_set_event_callback_t](#gad1df29d89982f09a9652db231e36c0c4)、[device](../device_reference/P002_设备对象结构.md)、[lin_event_callback_t](#gae69d33055fe07087a19b33dbe7a7252f)。

设置 LIN 发送事件回调的回调 API。

<a id="r_ga727b0f7fe4949e3fd17a303e239586bb"></a>

```c
typedef int(* lin_set_rx_filter_t) (const struct device *dev, const struct lin_filter *filter)
```

相关声明：[lin_set_rx_filter_t](#ga727b0f7fe4949e3fd17a303e239586bb)、[device](../device_reference/P002_设备对象结构.md)、[lin_filter](../peripheral_bus_storage_model_reference/P024_lin_filter_结构体.md)。

设置 LIN 接收过滤器（RX filter）的回调 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.5\_枚举（Enumerations）

<a id="r_gaf97478fd971b8b6913386a225078a24f"></a>

```c
enum lin_checksum_type { LIN_CHECKSUM_CLASSIC = 0 , LIN_CHECKSUM_ENHANCED }
```

相关声明：[lin_checksum_type](#gaf97478fd971b8b6913386a225078a24f)、[LIN_CHECKSUM_CLASSIC](#ggaf97478fd971b8b6913386a225078a24fa6b6c53f36bcccb2f099e63977bd2391a)、[LIN_CHECKSUM_ENHANCED](#ggaf97478fd971b8b6913386a225078a24fa9a93132138ea30a19f03d6bd52c8de5e)。

LIN 校验和类型。

<a id="r_gab7aca457453e6e6409c02903bcdf9bab"></a>

```c
enum lin_event_type { LIN_EVT_RX_HEADER = 0 , LIN_EVT_TX_HEADER , LIN_EVT_RX_DATA , LIN_EVT_TX_DATA , LIN_EVT_TX_WAKEUP , LIN_EVT_RX_WAKEUP , LIN_EVT_ERR }
```

相关声明：[lin_event_type](#gab7aca457453e6e6409c02903bcdf9bab)、[LIN_EVT_RX_HEADER](#ggab7aca457453e6e6409c02903bcdf9baba9ee3a39dbc2ff9448a5cf443db5c1625)、[LIN_EVT_TX_HEADER](#ggab7aca457453e6e6409c02903bcdf9babac57f7922e1bc6328afa742e8efa22211)、[LIN_EVT_RX_DATA](#ggab7aca457453e6e6409c02903bcdf9baba3e30d82061bbcf51d89b63e94d362301)、[LIN_EVT_TX_DATA](#ggab7aca457453e6e6409c02903bcdf9babaa0770ae0419aadfc97ded5e9a524a6eb)、[LIN_EVT_TX_WAKEUP](#ggab7aca457453e6e6409c02903bcdf9babadd5da0e9a1ceb2536f11991702784508)、[LIN_EVT_RX_WAKEUP](#ggab7aca457453e6e6409c02903bcdf9baba3d1c9ec13a13ce51893bf4c59f22cc2e)、[LIN_EVT_ERR](#ggab7aca457453e6e6409c02903bcdf9babab70beb6e355ef5c01fe3f8f285e8dd45)。

LIN 事件类型。

<a id="r_ga4d80ed442a8a83985c6ba3658f96fd16"></a>

```c
enum lin_mode { LIN_MODE_COMMANDER = 0 , LIN_MODE_RESPONDER }
```

相关声明：[lin_mode](#ga4d80ed442a8a83985c6ba3658f96fd16)、[LIN_MODE_COMMANDER](#gga4d80ed442a8a83985c6ba3658f96fd16aab1c3507ec82321e02c98f4878e6475d)、[LIN_MODE_RESPONDER](#gga4d80ed442a8a83985c6ba3658f96fd16a71650e86f1cd26ae46011a2cdce767b8)。

LIN 工作模式（Operation mode）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.6\_函数（Functions）

<a id="r_gac3d1d8680c88765a49ca9c6d04763158"></a>

```c
static uint8_t lin_get_frame_id (uint8_t pid)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[lin_get_frame_id](#gac3d1d8680c88765a49ca9c6d04763158)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从受保护标识符（Protected Identifier，PID）中提取 LIN 帧标识符的辅助函数。

<a id="r_ga136329dfada85698d56308d6157abea0"></a>

```c
static uint8_t lin_compute_pid (uint8_t id)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[lin_compute_pid](#ga136329dfada85698d56308d6157abea0)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据帧标识符计算 LIN 受保护标识符（PID）的辅助函数。

<a id="r_gaf8bd57bf6e9306a30fa025c1f9fe09e8"></a>

```c
static bool lin_verify_pid (uint8_t pid)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[lin_verify_pid](#gaf8bd57bf6e9306a30fa025c1f9fe09e8)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

验证 LIN 受保护标识符（PID）的辅助函数。

<a id="r_ga880b0c5dd454342160bcf454de5105e9"></a>

```c
const struct device * lin_get_transceiver (const struct device *dev)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[lin_get_transceiver](#ga880b0c5dd454342160bcf454de5105e9)、[device](../device_reference/P002_设备对象结构.md)。

获取与 LIN 控制器关联的 LIN 收发器（Transceiver）设备。

<a id="r_ga752004d89d50932711c3aa6189874478"></a>

```c
int lin_start (const struct device *dev)
```

相关声明：[lin_start](#ga752004d89d50932711c3aa6189874478)、[device](../device_reference/P002_设备对象结构.md)。

启动 LIN 控制器。

<a id="r_gaefe6f3853ea2f70d8ba4d6ab86f62b57"></a>

```c
int lin_stop (const struct device *dev)
```

相关声明：[lin_stop](#gaefe6f3853ea2f70d8ba4d6ab86f62b57)、[device](../device_reference/P002_设备对象结构.md)。

停止 LIN 控制器。

<a id="r_ga97468832dddf9e21b33e93a36c60102a"></a>

```c
int lin_configure (const struct device *dev, const struct lin_config *config)
```

相关声明：[lin_configure](#ga97468832dddf9e21b33e93a36c60102a)、[device](../device_reference/P002_设备对象结构.md)、[lin_config](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md)。

配置 LIN 控制器。

<a id="r_ga9410aa6989aea2cc173e7f36dcaf6be7"></a>

```c
int lin_get_config (const struct device *dev, struct lin_config *config)
```

相关声明：[lin_get_config](#ga9410aa6989aea2cc173e7f36dcaf6be7)、[device](../device_reference/P002_设备对象结构.md)、[lin_config](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md)。

获取当前 LIN 配置。

<a id="r_ga2a2afff5c7524504f24860673c24a217"></a>

```c
int lin_send (const struct device *dev, const struct lin_msg *msg, k_timeout_t timeout)
```

相关声明：[lin_send](#ga2a2afff5c7524504f24860673c24a217)、[device](../device_reference/P002_设备对象结构.md)、[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

发送 LIN 消息，仅适用于命令方模式（Commander mode）。

<a id="r_ga13e0a57996ba2f010bcda6561298b658"></a>

```c
int lin_receive (const struct device *dev, struct lin_msg *msg, k_timeout_t timeout)
```

相关声明：[lin_receive](#ga13e0a57996ba2f010bcda6561298b658)、[device](../device_reference/P002_设备对象结构.md)、[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

接收 LIN 消息，仅适用于命令方模式（Commander mode）。

<a id="r_gafae0fa8e806c2856f61642ef80368ec8"></a>

```c
int lin_response (const struct device *dev, const struct lin_msg *msg, k_timeout_t timeout)
```

相关声明：[lin_response](#gafae0fa8e806c2856f61642ef80368ec8)、[device](../device_reference/P002_设备对象结构.md)、[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

响应收到的帧头，仅适用于响应方模式。

<a id="r_ga58c5052899f49601a91d6da614ea8c82"></a>

```c
int lin_read (const struct device *dev, struct lin_msg *msg, k_timeout_t timeout)
```

相关声明：[lin_read](#ga58c5052899f49601a91d6da614ea8c82)、[device](../device_reference/P002_设备对象结构.md)、[lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

开始数据接收，仅适用于响应方模式。

<a id="r_ga0fe3631c3f9b7100162b5f48e83bd6e3"></a>

```c
int lin_wakeup_send (const struct device *dev)
```

相关声明：[lin_wakeup_send](#ga0fe3631c3f9b7100162b5f48e83bd6e3)、[device](../device_reference/P002_设备对象结构.md)。

发送 LIN 唤醒信号（Wakeup signal）。

<a id="r_ga07ec84c466d94f6057d7852998b2fbb2"></a>

```c
static int lin_set_event_callback (const struct device *dev, lin_event_callback_t callback, void *user_data)
```

相关声明：[lin_set_event_callback](#ga07ec84c466d94f6057d7852998b2fbb2)、[device](../device_reference/P002_设备对象结构.md)、[lin_event_callback_t](#gae69d33055fe07087a19b33dbe7a7252f)。

设置 LIN 事件回调。

<a id="r_ga7594e89b4fc3a018c1cd0010bd4a6ac1"></a>

```c
int lin_set_rx_filter (const struct device *dev, const struct lin_filter *filter)
```

相关声明：[lin_set_rx_filter](#ga7594e89b4fc3a018c1cd0010bd4a6ac1)、[device](../device_reference/P002_设备对象结构.md)、[lin_filter](../peripheral_bus_storage_model_reference/P024_lin_filter_结构体.md)。

设置 LIN 接收过滤器，仅适用于响应方模式（Responder mode）。

<a id="r_gad37ddea1dbcc29151c7a504813eebfac"></a>

```c
#define LIN_ID_MASK 0x3FU
```

相关声明：[LIN_ID_MASK](#gad37ddea1dbcc29151c7a504813eebfac)。

LIN 帧定义。

<a id="r_ga6c506247ef9d1c0d8f1838a31e6df77b"></a>

```c
#define LIN_BUS_CONFLICT_DETECTION BIT(0)
```

相关声明：[LIN_BUS_CONFLICT_DETECTION](#ga6c506247ef9d1c0d8f1838a31e6df77b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

LIN 设备配置标志。

<a id="r_gaf1ce3f05c51587ab291ab2b297569edd"></a>

```c
#define LIN_BUS_AUTO_SYNC BIT(1)
```

相关声明：[LIN_BUS_AUTO_SYNC](#gaf1ce3f05c51587ab291ab2b297569edd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

启用 LIN 总线自动同步（Auto synchronization）。

## 9.7\_详细说明（Detailed Documentation）

<a id="gaf1ce3f05c51587ab291ab2b297569edd"></a>

### `LIN_BUS_AUTO_SYNC`

```c
#define LIN_BUS_AUTO_SYNC BIT(1)
```

```c
#include <zephyr/drivers/lin.h>
```

启用 LIN 总线自动同步（Auto synchronization）。

<a id="ga6c506247ef9d1c0d8f1838a31e6df77b"></a>

### `LIN_BUS_CONFLICT_DETECTION`

```c
#define LIN_BUS_CONFLICT_DETECTION BIT(0)
```

```c
#include <zephyr/drivers/lin.h>
```

LIN 设备配置标志。

已启用 LIN 总线冲突检测（Bus Conflict Detection）。

<a id="ga2d95ba106f4608f1b71dd99a387719cf"></a>

### `LIN_DT_DRIVER_CONFIG_GET`

```c
#define LIN_DT_DRIVER_CONFIG_GET ( node_id, _min_bitrate, _max_bitrate )
```

```c
#include <zephyr/drivers/lin.h>
```

展开值（Value）：

```c
{                                                                                          \
        .phy = DEVICE_DT_GET_OR_NULL(DT_PHANDLE(node_id, phys)),                           \
        .min_bitrate = DT_PROP_OR(node_id, min_bitrate, _min_bitrate),                     \
        .max_bitrate = DT_PROP_OR(node_id, max_bitrate, _max_bitrate),                     \
        .bitrate = DT_PROP_OR(node_id, bitrate, 0),                                        \
}
```

`lin_driver_config` 结构体的静态初始化器（Static initializer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `_min_bitrate` | LIN 控制器支持的最小比特率（Minimum Bitrate）。 |
| `_max_bitrate` | LIN 控制器支持的最大比特率（Maximum Bitrate）。 |

<a id="gaaa094da48b5566adc8b3ef401da3c652"></a>

### `LIN_DT_DRIVER_CONFIG_INST_GET`

```c
#define LIN_DT_DRIVER_CONFIG_INST_GET ( inst, _min_bitrate, _max_bitrate )
```

```c
#include <zephyr/drivers/lin.h>
```

展开值（Value）：

```c
LIN_DT_DRIVER_CONFIG_GET(DT_DRV_INST(inst), _min_bitrate, _max_bitrate)
```

根据 `DT_DRV_COMPAT` 实例生成 `lin_driver_config` 结构体的静态初始化器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |
| `_min_bitrate` | LIN 控制器支持的最小比特率（Minimum Bitrate）。 |
| `_max_bitrate` | LIN 控制器支持的最大比特率（Maximum Bitrate）。 |

**参阅（See Also）**：另请参见 LIN_DT_DRIVER_CONFIG_GET()。

<a id="gaef5f7c158f409b0655658def9b70b2c4"></a>

### `LIN_ERR_BUS_COLLISION`

```c
#define LIN_ERR_BUS_COLLISION BIT(0)
```

```c
#include <zephyr/drivers/lin.h>
```

LIN 错误标志（Error flags）。

检测到 LIN 总线碰撞（Bus Collision）。

<a id="gaf308060dd15eddaaa5307216ed3ea133"></a>

### `LIN_ERR_COUNTER_OVERFLOW`

```c
#define LIN_ERR_COUNTER_OVERFLOW BIT(2)
```

```c
#include <zephyr/drivers/lin.h>
```

LIN 计数器溢出（Counter overflow）。

<a id="gaa79791d878cbed37a33cc470b2942321"></a>

### `LIN_ERR_FRAMING`

```c
#define LIN_ERR_FRAMING BIT(5)
```

```c
#include <zephyr/drivers/lin.h>
```

LIN 帧格式错误（Framing error）。

<a id="ga281f21c91817109632824eda43be87c3"></a>

### `LIN_ERR_INVALID_CHECKSUM`

```c
#define LIN_ERR_INVALID_CHECKSUM BIT(1)
```

```c
#include <zephyr/drivers/lin.h>
```

LIN 校验和错误（Checksum error）。

<a id="gab9bea91c4da9809424c41d5d6a52b2f9"></a>

### `LIN_ERR_OVERRUN`

```c
#define LIN_ERR_OVERRUN BIT(3)
```

```c
#include <zephyr/drivers/lin.h>
```

LIN 数据溢出错误（Overrun error）。

<a id="gaa3f54d1c0aa552ac6a59dfdfde2c7353"></a>

### `LIN_ERR_PARITY`

```c
#define LIN_ERR_PARITY BIT(4)
```

```c
#include <zephyr/drivers/lin.h>
```

LIN 奇偶校验错误（Parity error）。

<a id="gad37ddea1dbcc29151c7a504813eebfac"></a>

### `LIN_ID_MASK`

```c
#define LIN_ID_MASK 0x3FU
```

```c
#include <zephyr/drivers/lin.h>
```

LIN 帧定义。

LIN 标识符的位掩码（Bit Mask）。

<a id="ga560c00e1f3b7990836a06c83ab0eca43"></a>

### `lin_config_flags_t`

```c
typedef uint32_t lin_config_flags_t
```

```c
#include <zephyr/drivers/lin.h>
```

提供用于保存 LIN 控制器配置标志的类型。

**参阅（See Also）**：另请参见 LIN_CONFIG_FLAGS。

<a id="ga39766c7605a50fcb600e9d72bfcf07d5"></a>

### `lin_configure_t`

```c
typedef int(* lin_configure_t) (const struct device *dev, const struct lin_config *config)
```

```c
#include <zephyr/drivers/lin.h>
```

配置 LIN 控制器的回调 API。

参数说明参见 lin_configure()。

<a id="ga344a6eade12faa423b8bd2718009b0c5"></a>

### `lin_error_flags_t`

```c
typedef uint32_t lin_error_flags_t
```

```c
#include <zephyr/drivers/lin.h>
```

提供用于保存 LIN 错误标志的类型。

**参阅（See Also）**：另请参见 LIN_ERR_FLAGS。

<a id="gae69d33055fe07087a19b33dbe7a7252f"></a>

### `lin_event_callback_t`

```c
typedef void(* lin_event_callback_t) (const struct device *dev, const struct lin_event *event, void *user_data)
```

```c
#include <zephyr/drivers/lin.h>
```

LIN 事件回调函数类型。

发生 LIN 事件（LIN Event）时调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 LIN 设备结构体（Device Structure）的指针。 |
| `event` | 指向 LIN 事件结构体（Event Structure）的指针。 |
| `user_data` | 指向任意用户数据（User Data）的指针。 |

<a id="ga305d83d265245ed657a9974c0bab1962"></a>

### `lin_get_config_t`

```c
typedef int(* lin_get_config_t) (const struct device *dev, struct lin_config *config)
```

```c
#include <zephyr/drivers/lin.h>
```

获取 LIN 配置的回调 API。

参数说明参见 lin_get_config()。

<a id="gabcad96f6950ec45b71adfd14e4c0c363"></a>

### `lin_read_t`

```c
typedef int(* lin_read_t) (const struct device *dev, struct lin_msg *msg, k_timeout_t timeout)
```

```c
#include <zephyr/drivers/lin.h>
```

读取 LIN 响应消息的回调 API。参数说明见 `lin_read()`。

<a id="gad77d365c000a2f9c7f2558ec24d0f455"></a>

### `lin_receive_t`

```c
typedef int(* lin_receive_t) (const struct device *dev, struct lin_msg *msg, k_timeout_t timeout)
```

```c
#include <zephyr/drivers/lin.h>
```

接收 LIN 消息的回调 API。

参数说明参见 lin_receive()。

<a id="ga42976918cdbcec388095d77e398e7633"></a>

### `lin_response_t`

```c
typedef int(* lin_response_t) (const struct device *dev, const struct lin_msg *msg, k_timeout_t timeout)
```

```c
#include <zephyr/drivers/lin.h>
```

处理 LIN 响应消息（Response messages）的回调 API。

参数说明参见 lin_response()。

<a id="ga8091d2d225709439f9afb2eddeb73792"></a>

### `lin_send_t`

```c
typedef int(* lin_send_t) (const struct device *dev, const struct lin_msg *msg, k_timeout_t timeout)
```

```c
#include <zephyr/drivers/lin.h>
```

发送 LIN 消息的回调 API。

参数说明参见 lin_send()。

<a id="gad1df29d89982f09a9652db231e36c0c4"></a>

### `lin_set_event_callback_t`

```c
typedef int(* lin_set_event_callback_t) (const struct device *dev, lin_event_callback_t callback, void *user_data)
```

```c
#include <zephyr/drivers/lin.h>
```

设置 LIN 发送事件回调的回调 API。

参数说明参见 lin_set_event_callback()。

<a id="ga727b0f7fe4949e3fd17a303e239586bb"></a>

### `lin_set_rx_filter_t`

```c
typedef int(* lin_set_rx_filter_t) (const struct device *dev, const struct lin_filter *filter)
```

```c
#include <zephyr/drivers/lin.h>
```

设置 LIN 接收过滤器（RX filter）的回调 API。

参数说明参见 lin_set_rx_filter()。

<a id="ga149ca3972fc800c4fd2bbb0b5d8a85e3"></a>

### `lin_start_t`

```c
typedef int(* lin_start_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/lin.h>
```

启动 LIN 控制器的回调 API。

参数说明参见 lin_start()。

<a id="gab0f27d3ad3637f9040920b3088c1e239"></a>

### `lin_stop_t`

```c
typedef int(* lin_stop_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/lin.h>
```

停止 LIN 控制器的回调 API。

参数说明参见 lin_stop()。

<a id="ga16889d5f804b14ef80a608f6b8a86193"></a>

### `lin_wakeup_send_t`

```c
typedef int(* lin_wakeup_send_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/lin.h>
```

发送 LIN 唤醒信号的回调 API。

参数说明参见 lin_wakeup_send()。

<a id="gaf97478fd971b8b6913386a225078a24f"></a>

### `lin_checksum_type`

```c
enum lin_checksum_type
```

```c
#include <zephyr/drivers/lin.h>
```

LIN 校验和类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LIN_CHECKSUM_CLASSIC` | 经典校验和（Classic Checksum）。 |
| `LIN_CHECKSUM_ENHANCED` | 增强校验和（Enhanced Checksum）。 |

<a id="gab7aca457453e6e6409c02903bcdf9bab"></a>

### `lin_event_type`

```c
enum lin_event_type
```

```c
#include <zephyr/drivers/lin.h>
```

LIN 事件类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LIN_EVT_RX_HEADER` | 报头接收事件（Header Received Event），仅用于响应节点模式（Responder Mode）。 |
| `LIN_EVT_TX_HEADER` | 报头发送完成事件（Header Transmission Complete Event），仅用于指挥节点模式（Commander Mode）。 |
| `LIN_EVT_RX_DATA` | 数据接收事件（Data Received Event）。 |
| `LIN_EVT_TX_DATA` | 数据发送完成事件（Data Transmission Complete Event）。 |
| `LIN_EVT_TX_WAKEUP` | 发送唤醒完成事件（Transmit Wake Up Complete Event）。 |
| `LIN_EVT_RX_WAKEUP` | 接收唤醒完成事件（Receive Wake Up Complete Event）。 |
| `LIN_EVT_ERR` | 错误事件（Error Event）。 |

<a id="ga4d80ed442a8a83985c6ba3658f96fd16"></a>

### `lin_mode`

```c
enum lin_mode
```

```c
#include <zephyr/drivers/lin.h>
```

LIN 工作模式（Operation mode）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LIN_MODE_COMMANDER` | LIN 指挥节点（Commander Node）。 |
| `LIN_MODE_RESPONDER` | LIN 响应节点（Responder Node）。 |

<a id="ga136329dfada85698d56308d6157abea0"></a>

### `lin_compute_pid()`

```c
uint8_t lin_compute_pid ( uint8_t id)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lin.h>
```

根据帧标识符计算 LIN 受保护标识符（PID）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 帧标识符（Frame Identifier）。 |

**返回（Returns）**：返回：uint8_t 类型的受保护标识符（Protected Identifier）。

<a id="ga97468832dddf9e21b33e93a36c60102a"></a>

### `lin_configure()`

```c
int lin_configure ( const struct device * dev, const struct lin_config * config )
```

```c
#include <zephyr/drivers/lin.h>
```

配置 LIN 控制器。

此函数使用给定设置配置 LIN 控制器（LIN Controller）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 LIN 设备结构体（Device Structure）的指针。 |
| `config` | 指向配置结构体（Configuration Structure）的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga9410aa6989aea2cc173e7f36dcaf6be7"></a>

### `lin_get_config()`

```c
int lin_get_config ( const struct device * dev, struct lin_config * config )
```

```c
#include <zephyr/drivers/lin.h>
```

获取当前 LIN 配置。

此函数获取 LIN 控制器（LIN Controller）的当前配置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 LIN 设备结构体（Device Structure）的指针。 |
| `config` | 指向配置结构体（Configuration Structure）的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="gac3d1d8680c88765a49ca9c6d04763158"></a>

### `lin_get_frame_id()`

```c
uint8_t lin_get_frame_id ( uint8_t pid)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lin.h>
```

从受保护标识符（Protected Identifier，PID）中提取 LIN 帧标识符的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pid` | 受保护标识符（Protected Identifier）。 |

**返回（Returns）**：返回：uint8_t 类型的帧标识符（Frame Identifier）。

<a id="ga880b0c5dd454342160bcf454de5105e9"></a>

### `lin_get_transceiver()`

```c
const struct device * lin_get_transceiver ( const struct device * dev)
```

```c
#include <zephyr/drivers/lin.h>
```

获取与 LIN 控制器关联的 LIN 收发器（Transceiver）设备。

此函数获取与指定 LIN 控制器关联的 LIN 收发器设备（LIN Transceiver Device）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 LIN 设备结构体（Device Structure）的指针。 |

**返回（Returns）**：返回：指向 LIN 收发器设备结构体的指针；不可用时为 NULL。

<a id="ga58c5052899f49601a91d6da614ea8c82"></a>

### `lin_read()`

```c
int lin_read ( const struct device * dev, struct lin_msg * msg, k_timeout_t timeout )
```

```c
#include <zephyr/drivers/lin.h>
```

开始数据接收，仅适用于响应方模式。

这是中断驱动 API（Interrupt-driven API），供响应节点（Responder Node）发起 LIN 报文数据的非阻塞接收（Non-blocking Reception）。发生 LIN_EVT_RX_HEADER 事件时应调用它，以接收对应报头的响应。

只有在已收到报头（Header）时才能调用此 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 LIN 设备结构体（Device Structure）的指针。 |
| `msg` | 指向 LIN 报文结构体（Message Structure）的指针。 |
| `timeout` | 等待接收完成的超时时间（Timeout）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EPERM` | 设备未处于响应节点模式（Responder Mode）。 |
| `-EFAULT` | 尚未接收到报头（Header）。 |
| `negative` | 失败时的 errno 错误码。 |

<a id="ga13e0a57996ba2f010bcda6561298b658"></a>

### `lin_receive()`

```c
int lin_receive ( const struct device * dev, struct lin_msg * msg, k_timeout_t timeout )
```

```c
#include <zephyr/drivers/lin.h>
```

接收 LIN 消息，仅适用于命令方模式（Commander mode）。

此函数使用指定 LIN 标识符（Identifier）建立异步 LIN 读事务（Asynchronous Read Transaction）。设备在指挥节点模式（Commander Mode）下工作时：

- 发送带有指定 ID 的报头（Header），请求数据。
- 从响应节点（Responder）读回数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 LIN 设备结构体（Device Structure）的指针。 |
| `msg` | 指向 LIN 报文结构体（Message Structure）的指针。 |
| `timeout` | 等待发送完成的超时时间（Timeout）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EPERM` | 设备未处于指挥节点模式（Commander Mode）。 |
| `negative` | 失败时的 errno 错误码。 |

<a id="gafae0fa8e806c2856f61642ef80368ec8"></a>

### `lin_response()`

```c
int lin_response ( const struct device * dev, const struct lin_msg * msg, k_timeout_t timeout )
```

```c
#include <zephyr/drivers/lin.h>
```

响应收到的帧头，仅适用于响应方模式。

这是中断驱动 API（Interrupt-driven API），供响应节点（Responder Node）响应指挥节点（Commander Node）发送的 LIN 报头。响应节点应在发生 LIN_EVT_RX_HEADER 事件时调用它，以发布对已接收报头的响应。

只有在已收到报头（Header）时才能调用此 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 LIN 设备结构体（Device Structure）的指针。 |
| `msg` | 指向 LIN 报文结构体（Message Structure）的指针。 |
| `timeout` | 等待响应完成的超时时间（Timeout）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EPERM` | 设备未处于响应节点模式（Responder Mode）。 |
| `-EFAULT` | 尚未接收到报头（Header）。 |
| `negative` | 失败时的 errno 错误码。 |

<a id="ga2a2afff5c7524504f24860673c24a217"></a>

### `lin_send()`

```c
int lin_send ( const struct device * dev, const struct lin_msg * msg, k_timeout_t timeout )
```

```c
#include <zephyr/drivers/lin.h>
```

发送 LIN 消息，仅适用于命令方模式（Commander mode）。

此函数使用指定 LIN 标识符（Identifier）建立异步 LIN 写事务（Asynchronous Write Transaction）。设备在指挥节点模式（Commander Mode）下工作时：

- 发送带有指定 ID 的报头（Header）。
- 发送数据有效载荷（Data Payload），此步骤可选。如果不需要响应数据，将 msg->data_len 保持为 0。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 LIN 设备结构体（Device Structure）的指针。 |
| `msg` | 指向输入 LIN 报文结构体（Input Message Structure）的指针。 |
| `timeout` | 等待发送完成的超时时间（Timeout）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EPERM` | 设备未处于指挥节点模式（Commander Mode）。 |
| `negative` | 失败时的 errno 错误码。 |

<a id="ga07ec84c466d94f6057d7852998b2fbb2"></a>

### `lin_set_event_callback()`

```c
int lin_set_event_callback ( const struct device * dev, lin_event_callback_t callback, void * user_data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lin.h>
```

设置 LIN 事件回调。

此函数设置发生 LIN 事件（LIN Events）时调用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 LIN 设备结构体（Device Structure）的指针。 |
| `callback` | 指向回调函数（Callback Function）的指针。 |
| `user_data` | 指向传给回调函数的用户数据的指针。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga7594e89b4fc3a018c1cd0010bd4a6ac1"></a>

### `lin_set_rx_filter()`

```c
int lin_set_rx_filter ( const struct device * dev, const struct lin_filter * filter )
```

```c
#include <zephyr/drivers/lin.h>
```

设置 LIN 接收过滤器，仅适用于响应方模式（Responder mode）。

此函数根据 ID 和掩码（Mask）为 LIN 报文设置报头过滤器（Header Filter）。若未设置过滤器，则接受全部传入报文。

收到被接受的报头时，生成 LIN_EVT_RX_HEADER 事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 LIN 设备结构体（Device Structure）的指针。 |
| `filter` | 指向 LIN 过滤器结构体（Filter Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EPERM` | 设备处于指挥节点模式（Commander Mode）。 |
| `negative` | 失败时的错误码（Error Code）。 |

<a id="ga752004d89d50932711c3aa6189874478"></a>

### `lin_start()`

```c
int lin_start ( const struct device * dev)
```

```c
#include <zephyr/drivers/lin.h>
```

启动 LIN 控制器。

此函数将 LIN 控制器置于活动状态（Active State），使其可以参与 LIN 通信；还会启用 LIN 收发器（Transceiver），前提是支持该操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 LIN 设备结构体（Device Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EALREADY` | LIN 控制器已经启动（Started）。 |
| `negative` | 失败时的 errno 错误码。 |

<a id="gaefe6f3853ea2f70d8ba4d6ab86f62b57"></a>

### `lin_stop()`

```c
int lin_stop ( const struct device * dev)
```

```c
#include <zephyr/drivers/lin.h>
```

停止 LIN 控制器。

此函数将 LIN 控制器置于停用状态（Deactivated State），使其无法参与 LIN 通信；还会禁用 LIN 收发器（Transceiver），前提是支持该操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 LIN 设备结构体（Device Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EALREADY` | LIN 控制器已经停止（Stopped）。 |
| `negative` | 失败时的 errno 错误码。 |

<a id="gaf8bd57bf6e9306a30fa025c1f9fe09e8"></a>

### `lin_verify_pid()`

```c
bool lin_verify_pid ( uint8_t pid)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lin.h>
```

验证 LIN 受保护标识符（PID）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pid` | 要验证的受保护标识符（Protected Identifier）。 |

**返回（Returns）**：返回：PID 有效时为 true，否则为 false。

<a id="ga0fe3631c3f9b7100162b5f48e83bd6e3"></a>

### `lin_wakeup_send()`

```c
int lin_wakeup_send ( const struct device * dev)
```

```c
#include <zephyr/drivers/lin.h>
```

发送 LIN 唤醒信号（Wakeup signal）。

将总线驱动为显性电平（Dominant），持续时间满足 LIN 规范要求，以唤醒睡眠节点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LIN 设备（Device）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。


## 9.8\_原页交叉引用（Cross References）

- [lin.h](../peripheral_bus_storage_header_reference/P007_zephyr__drivers__lin.h_头文件参考.md)
- [lin_config](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md)
- [lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)
- [lin_event](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md)
- [lin_filter](../peripheral_bus_storage_model_reference/P024_lin_filter_结构体.md)
- [lin_driver_config](../peripheral_bus_storage_model_reference/P021_lin_driver_config_结构体.md)
- [lin_driver_data](../peripheral_bus_storage_model_reference/P022_lin_driver_data_结构体.md)
- [lin_driver_api](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [device](../device_reference/P002_设备对象结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [DEVICE_DT_GET_OR_NULL](../device_reference/P001_设备模型公共接口.md#ga6ce1dbfda6847ca6c3858712e9b41989)
- [DT_PHANDLE](../dt_property_reference/P001_设备树属性读取宏.md#ga7bd77c49472ba4547d87f00f40fd7171)
- [DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)

<a id="LIN_ERR_FLAGS"></a>
<a id="LIN_CONFIG_FLAGS"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__device__model_html_ga6ce1dbfda6847ca6c3858712e9b41989"></a>
<a id="agroup__devicetree-generic-prop_html_ga5e5bfc9b1a6627b3f73014329e96340f"></a>
<a id="agroup__devicetree-generic-prop_html_ga7bd77c49472ba4547d87f00f40fd7171"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__lin__controller_html_ga2d95ba106f4608f1b71dd99a387719cf"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaf97478fd971b8b6913386a225078a24fa6b6c53f36bcccb2f099e63977bd2391a"></a>
<a id="ggaf97478fd971b8b6913386a225078a24fa9a93132138ea30a19f03d6bd52c8de5e"></a>
<a id="ggab7aca457453e6e6409c02903bcdf9baba9ee3a39dbc2ff9448a5cf443db5c1625"></a>
<a id="ggab7aca457453e6e6409c02903bcdf9babac57f7922e1bc6328afa742e8efa22211"></a>
<a id="ggab7aca457453e6e6409c02903bcdf9baba3e30d82061bbcf51d89b63e94d362301"></a>
<a id="ggab7aca457453e6e6409c02903bcdf9babaa0770ae0419aadfc97ded5e9a524a6eb"></a>
<a id="ggab7aca457453e6e6409c02903bcdf9babadd5da0e9a1ceb2536f11991702784508"></a>
<a id="ggab7aca457453e6e6409c02903bcdf9baba3d1c9ec13a13ce51893bf4c59f22cc2e"></a>
<a id="ggab7aca457453e6e6409c02903bcdf9babab70beb6e355ef5c01fe3f8f285e8dd45"></a>
<a id="gga4d80ed442a8a83985c6ba3658f96fd16aab1c3507ec82321e02c98f4878e6475d"></a>
<a id="gga4d80ed442a8a83985c6ba3658f96fd16a71650e86f1cd26ae46011a2cdce767b8"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_IEEE 802.3 管理接口。.md) · [返回大纲](大纲.md) · [下一章](P010_能力结构（Capability Structure）.md)
