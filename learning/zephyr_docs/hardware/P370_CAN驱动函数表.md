---
id: learning.zephyr-docs.hardware.canback-1
title: CAN驱动函数表
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第370章\_CAN驱动函数表

原文：[structcan__driver__api](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html)。读取日期：2026-10-13，`latest`。

## 370.1\_操作表约束

[`can_driver_api`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html) 是所有控制器局域网（Controller Area Network，CAN）控制器驱动需要定义的操作表，声明来自 `zephyr/drivers/can.h`。它保存实现的操作函数指针以及驱动专用常量数据。

必需（Required，REQ）成员必须设置；可选（Optional，OPT）成员允许不实现。应用程序编程接口（Application Programming Interface，API）的相关定义入口为 `DEVICE_DT_INST_DEFINE`、`DEVICE_DT_DEFINE` 和 `DEVICE_API`。

## 370.2\_操作及配置条件

接收（Receive，RX）过滤器决定哪些帧进入应用；总线关闭（Bus-Off）恢复与灵活数据速率 CAN（CAN with Flexible Data-Rate，CAN FD）数据阶段时序按配置可选。

| 字段 | 类型 | 要求与作用 |
| --- | --- | --- |
| <a id="a11d2ff416d459faf84905e7ffdc1a536"></a>[`get_capabilities`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#a11d2ff416d459faf84905e7ffdc1a536) | [`can_get_capabilities_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga2fd489217c19977d239d51f0b3fcfc19) | REQ：查询支持模式 |
| <a id="ac42f6d438d3e88f0db8e64c236621f8a"></a>[`start`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#ac42f6d438d3e88f0db8e64c236621f8a) | [`can_start_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#gaecca113e6b8cc7caba3d19fdd104aaa7) | REQ：启动控制器 |
| <a id="a3ca1cb8bcd6713bfdf20f76cee3bc3a4"></a>[`stop`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#a3ca1cb8bcd6713bfdf20f76cee3bc3a4) | [`can_stop_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga1ab69e7991b8492e36c4b3f359db1961) | REQ：停止控制器 |
| <a id="accfe8e3e40e5bae33b8c31b1af55c644"></a>[`set_mode`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#accfe8e3e40e5bae33b8c31b1af55c644) | [`can_set_mode_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga231b61f4d1413e0d28dd5a8bc25a89b3) | REQ：设置操作模式 |
| <a id="a356b3761926c2a5a85fcc80b2e8a4643"></a>[`set_timing`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#a356b3761926c2a5a85fcc80b2e8a4643) | [`can_set_timing_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga01a5f028d947582dd4195b467dae8b94) | REQ：设置总线时序 |
| <a id="a9b5ec5c71a126798c24a19d1c91f879b"></a>[`send`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#a9b5ec5c71a126798c24a19d1c91f879b) | [`can_send_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga89108f1d99fa1ba784808f1e99763a58) | REQ：排队发送 CAN 帧 |
| <a id="a56225a8cb458baa0d1745ff5e9202ae6"></a>[`add_rx_filter`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#a56225a8cb458baa0d1745ff5e9202ae6) | [`can_add_rx_filter_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga3bc249502cb65bf89bce2ca87535ac6b) | REQ：为指定过滤器添加回调 |
| <a id="ac264f4d66a29a5f42aaf2b6c9665f8f3"></a>[`remove_rx_filter`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#ac264f4d66a29a5f42aaf2b6c9665f8f3) | [`can_remove_rx_filter_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga20ee94c5122acb6fd7fe5939a20ba748) | REQ：移除接收过滤器 |
| <a id="aba563aff4e114b7956bb824efdebb0c6"></a>[`recover`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#aba563aff4e114b7956bb824efdebb0c6) | [`can_recover_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga8bcafa14e23f2ba70e17c1432449d744) | OPT：从 Bus-Off 恢复；仅启用 Kconfig 配置项 [`CONFIG_CAN_MANUAL_RECOVERY_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_MANUAL_RECOVERY_MODE) 时可用 |
| <a id="aa6b8b2b7c544cf78930b45cab1e6dbb4"></a>[`get_state`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#aa6b8b2b7c544cf78930b45cab1e6dbb4) | [`can_get_state_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga14210ea7870ef23072cd61c10043540f) | REQ：查询当前控制器状态 |
| <a id="a90547b28015e2b7eea6a548b0ab2b576"></a>[`state_change_callbacks_enabled`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#a90547b28015e2b7eea6a548b0ab2b576) | [`can_state_change_callbacks_enabled_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga80424a027933c3bc0d973f37333d2618) | OPT：通知状态变化回调是否启用 |
| <a id="ae969c18839dc5f1cb4356df6d1ee1e20"></a>[`get_core_clock`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#ae969c18839dc5f1cb4356df6d1ee1e20) | [`can_get_core_clock_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga4d44354cda4cfe0af5262189549d6523) | REQ：查询核心时钟频率 |
| <a id="a24a90bc4d49818985479bfe101cc21d4"></a>[`get_max_filters`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#a24a90bc4d49818985479bfe101cc21d4) | [`can_get_max_filters_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga946dd40c12eba40c34afa7572d61456c) | OPT：查询最大接收过滤器数量 |
| <a id="a1951bfc3135824e364d5f18aa9b15d09"></a>[`set_timing_data`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#a1951bfc3135824e364d5f18aa9b15d09) | [`can_set_timing_data_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller__backend.html#ga7be2d21503b59cde52369d589ccff80f) | OPT：设置 CAN FD 数据阶段时序；仅启用 Kconfig 配置项 [`CONFIG_CAN_FD_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_FD_MODE) 时可用 |

## 370.3\_时序范围数据

| 字段 | 类型 | 要求与作用 |
| --- | --- | --- |
| <a id="aeaa8022843f787bddbb18aa407d340a5"></a>[`timing_min`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#aeaa8022843f787bddbb18aa407d340a5) | `struct can_timing` | REQ：时序寄存器最小值 |
| <a id="a90dca9dd3baef96c4d3849be367129b5"></a>[`timing_max`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#a90dca9dd3baef96c4d3849be367129b5) | `struct can_timing` | REQ：时序寄存器最大值 |
| <a id="a5ad424b27606f9de8f37524594d396dc"></a>[`timing_data_min`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#a5ad424b27606f9de8f37524594d396dc) | `struct can_timing` | 数据阶段时序寄存器最小值；实现 [`set_timing_data`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#a1951bfc3135824e364d5f18aa9b15d09) 时必需 |
| <a id="ac07eeec7b96543b19041a28d70e19a97"></a>[`timing_data_max`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#ac07eeec7b96543b19041a28d70e19a97) | `struct can_timing` | 数据阶段时序寄存器最大值；实现 [`set_timing_data`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#a1951bfc3135824e364d5f18aa9b15d09) 时必需 |

---

[上一章：CAN控制器后端接口](P369_CAN控制器后端接口.md) · [下一章：CAN驱动公共配置](P371_CAN驱动公共配置.md) · [返回大纲](大纲.md)
