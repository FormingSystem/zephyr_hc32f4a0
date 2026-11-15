---
id: learning.zephyr-docs.hardware.canback-0
title: CAN控制器后端接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第369章\_CAN控制器后端接口

原文：[group__can__controller__backend](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html)。读取日期：2026-10-13，`latest`。

## 369.1\_驱动实现侧

本组包含实现控制器局域网（Controller Area Network，CAN）控制器驱动所需的应用程序编程接口（Application Programming Interface，API）类型、回调（Callback）签名和辅助定义，声明来自 `zephyr/drivers/can.h`。[`can_driver_config`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__config.html)、[`can_driver_data`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__data.html)、[`can_driver_api`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html) 分别保存公共配置、公共数据和操作函数表。

## 369.2\_发送延迟补偿与配置宏

<a id="ga0186885b4aaea6b77ae115b2faddabbb"></a>

`CAN_CALC_TDCO(_timing_data, _tdco_min, _tdco_max)` 根据灵活数据速率 CAN（CAN with Flexible Data-Rate，CAN FD）数据阶段时序，计算发送器延迟补偿偏移（Transmitter Delay Compensation Offset，TDCO）。它使用采样点和核心时钟预分频值，单位为最小时间量子（Minimum Time Quantum，mtq）；结果限制在给定最小/最大支持值之间。

`_timing_data` 为数据阶段时序指针，`_tdco_min`、`_tdco_max` 为以 mtq 计的下限和上限。返回值也是 mtq 数量；[`CLAMP`](../util_reference/P001_通用工具公共接口.md#gad6e7d4f6ba5a77f9ee3c04026f1c2b67) 为区间限幅宏：

```c
CLAMP((1U + _timing_data->prop_seg + _timing_data->phase_seg1) * _timing_data->prescaler,  \
      _tdco_min, _tdco_max)
```

<a id="ga86d706ecac2f5a50e6e550e9c0253668"></a>

`CAN_DT_DRIVER_CONFIG_GET(node_id, _min_bitrate, _max_bitrate)` 为 [`can_driver_config`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__config.html) 生成静态初始化器。`node_id` 是设备树（Devicetree）节点标识符，后两个参数为 CAN 控制器支持的最低、最高比特率（Bitrate）。

展开式从设备树读取收发器、速率和采样点；[`DT_PROP_OR`](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f) 在属性不存在时采用默认值，[`DEVICE_DT_GET_OR_NULL`](../device_reference/P001_设备模型公共接口.md#ga6ce1dbfda6847ca6c3858712e9b41989) 取得设备或空指针。Kconfig 配置项 `CONFIG_CAN_FD_MODE` 控制数据阶段字段，`CONFIG_CAN_DEFAULT_BITRATE` 与 `CONFIG_CAN_DEFAULT_BITRATE_DATA` 提供对应默认速率：

```c
{                                                                                       \
        .phy = DEVICE_DT_GET_OR_NULL(DT_PHANDLE(node_id, phys)),                        \
        .min_bitrate = DT_CAN_TRANSCEIVER_MIN_BITRATE(node_id, _min_bitrate),           \
        .max_bitrate = DT_CAN_TRANSCEIVER_MAX_BITRATE(node_id, _max_bitrate),           \
        .bitrate = DT_PROP_OR(node_id, bitrate, CONFIG_CAN_DEFAULT_BITRATE),            \
        .sample_point = DT_PROP_OR(node_id, sample_point, 0),                           \
        IF_ENABLED(CONFIG_CAN_FD_MODE,                                                  \
                (.bitrate_data = DT_PROP_OR(node_id, bitrate_data,                      \
                                            CONFIG_CAN_DEFAULT_BITRATE_DATA),           \
                 .sample_point_data = DT_PROP_OR(node_id, sample_point_data, 0),))      \
}
```

<a id="ga1bb18777df7e9fe397f86eea204965dc"></a>

`CAN_DT_DRIVER_CONFIG_INST_GET(inst, _min_bitrate, _max_bitrate)` 使用 `DT_DRV_COMPAT` 对应实例编号 `inst`，另外两个参数含义不变。[`DT_DRV_INST`](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1) 将实例编号转换为节点标识符：

```c
CAN_DT_DRIVER_CONFIG_GET(DT_DRV_INST(inst), _min_bitrate, _max_bitrate)
```

## 369.3\_配置、启停与能力回调

以下类型的参数和行为对应同名公共接口；`dev` 均为驱动实例设备结构指针。完整公共约定见[CAN 控制器接口](P362_CAN控制器接口.md)。

```c
typedef int (*can_set_timing_t)(const struct device *dev, const struct can_timing *timing);
typedef int (*can_set_timing_data_t)(const struct device *dev, const struct can_timing *timing_data);
typedef int (*can_get_capabilities_t)(const struct device *dev, can_mode_t *cap);
typedef int (*can_start_t)(const struct device *dev);
typedef int (*can_stop_t)(const struct device *dev);
typedef int (*can_set_mode_t)(const struct device *dev, can_mode_t mode);
```

<a id="ga01a5f028d947582dd4195b467dae8b94"></a>

<a id="ga7be2d21503b59cde52369d589ccff80f"></a>

<a id="ga2fd489217c19977d239d51f0b3fcfc19"></a>

<a id="gaecca113e6b8cc7caba3d19fdd104aaa7"></a>

<a id="ga1ab69e7991b8492e36c4b3f359db1961"></a>

<a id="ga231b61f4d1413e0d28dd5a8bc25a89b3"></a>

[`can_set_timing_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga01a5f028d947582dd4195b467dae8b94) 设置总线时序，参数见 `can_set_timing`；可选的 [`can_set_timing_data_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga7be2d21503b59cde52369d589ccff80f) 设置 CAN FD 数据阶段时序，参数见 `can_set_timing_data`。[`can_get_capabilities_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga2fd489217c19977d239d51f0b3fcfc19) 查询能力，参数见 `can_get_capabilities`。[`can_start_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#gaecca113e6b8cc7caba3d19fdd104aaa7)、[`can_stop_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga1ab69e7991b8492e36c4b3f359db1961) 启动/停止控制器，参数分别见 `can_start`、`can_stop`。[`can_set_mode_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga231b61f4d1413e0d28dd5a8bc25a89b3) 设置操作模式，参数见 `can_set_mode`。

## 369.4\_发送、过滤器、恢复与状态查询

发送（Transmit，TX）、接收（Receive，RX）以及错误状态操作使用以下签名：

```c
typedef int (*can_send_t)(const struct device *dev, const struct can_frame *frame,
                         k_timeout_t timeout, can_tx_callback_t callback, void *user_data);
typedef int (*can_add_rx_filter_t)(const struct device *dev, can_rx_callback_t callback,
                                  void *user_data, const struct can_filter *filter);
typedef void (*can_remove_rx_filter_t)(const struct device *dev, int filter_id);
typedef int (*can_recover_t)(const struct device *dev, k_timeout_t timeout);
typedef int (*can_get_state_t)(const struct device *dev, enum can_state *state,
                              struct can_bus_err_cnt *err_cnt);
typedef int (*can_get_core_clock_t)(const struct device *dev, uint32_t *rate);
typedef int (*can_get_max_filters_t)(const struct device *dev, bool ide);
```

<a id="ga89108f1d99fa1ba784808f1e99763a58"></a>

[`can_send_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga89108f1d99fa1ba784808f1e99763a58) 发送 CAN 帧，参数见 `can_send`。**从驱动视角看，`callback` 永远不为 `NULL`**：如果调用方未提供回调，上层会补充默认回调，从而简化驱动处理。

<a id="ga3bc249502cb65bf89bce2ca87535ac6b"></a>

<a id="ga20ee94c5122acb6fd7fe5939a20ba748"></a>

<a id="ga8bcafa14e23f2ba70e17c1432449d744"></a>

[`can_add_rx_filter_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga3bc249502cb65bf89bce2ca87535ac6b)、[`can_remove_rx_filter_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga20ee94c5122acb6fd7fe5939a20ba748) 添加/移除接收过滤器，参数分别见 `can_add_rx_filter`、`can_remove_rx_filter`。可选的 [`can_recover_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga8bcafa14e23f2ba70e17c1432449d744) 从总线关闭（Bus-Off）状态手动恢复，参数见 `can_recover`。

<a id="ga14210ea7870ef23072cd61c10043540f"></a>

<a id="ga4d44354cda4cfe0af5262189549d6523"></a>

<a id="ga946dd40c12eba40c34afa7572d61456c"></a>

[`can_get_state_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga14210ea7870ef23072cd61c10043540f) 查询控制器状态，参数见 `can_get_state`；[`can_get_core_clock_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga4d44354cda4cfe0af5262189549d6523) 查询核心时钟，参数见 `can_get_core_clock`。可选的 [`can_get_max_filters_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga946dd40c12eba40c34afa7572d61456c) 查询最大同时安装的接收过滤器数量，参数见 `can_get_max_filters`。

## 369.5\_状态回调启用通知与触发

<a id="ga80424a027933c3bc0d973f37333d2618"></a>

可选通知类型 [`can_state_change_callbacks_enabled_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga80424a027933c3bc0d973f37333d2618) 告知驱动是否启用了状态变化回调。驱动可据此使能/禁用用于报告状态变化的中断请求（Interrupt Request，IRQ）：

```c
typedef int (*can_state_change_callbacks_enabled_t)(const struct device *dev, bool enabled);
void can_fire_state_change_callbacks(const struct device *dev,
                                      enum can_state state, struct can_bus_err_cnt err_cnt);
```

通知的 `enabled=true` 表示回调已启用，`false` 表示未启用。成功返回 0，一般输入输出错误返回 `-EIO`。

<a id="gaba24cc4eb2fa759ff8394dd096021982"></a>

[`can_fire_state_change_callbacks`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#gaba24cc4eb2fa759ff8394dd096021982) 触发已经注册的状态变化处理回调；[`state`](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90) 为当前 CAN 控制器状态，`err_cnt` 为控制器错误计数值。

---

[上一章：CAN设备状态结构](P368_CAN设备状态结构.md) · [下一章：CAN驱动函数表](P370_CAN驱动函数表.md) · [返回大纲](大纲.md)
