---
id: learning.zephyr-docs.hardware.gpiobackend-1
title: GPIO驱动函数表
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第272章\_GPIO驱动函数表

原文：[structgpio__driver__api](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__api.html)。读取日期：2026-10-13，`latest`。

## 272.1\_结构约定

结构 [`gpio_driver_api`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__api.html) 是每个 **通用输入/输出（General Purpose Input/Output，GPIO）**驱动都需定义的驱动应用程序接口（Application Programming Interface，API）结构，声明来自 `zephyr/drivers/gpio.h`。它包含驱动所实现操作的函数指针，以及其他驱动专用常量数据。

标记为必需（Required，REQ）的成员必须由驱动设置；标记为可选（Optional，OPT）的成员可以不实现。各回调签名见[GPIO驱动后端](P271_GPIO驱动后端.md)。

## 272.2\_成员

| 成员 | 类型 | 要求 | 操作 |
| --- | --- | --- | --- |
| <a id="a6b79f508317faa0f2959fe63449534c5"></a>[`pin_configure`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__api.html#a6b79f508317faa0f2959fe63449534c5) | [`gpio_api_pin_configure_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#ga6e7f6f2052ba10b6482445faaef4245f) | REQ | 配置单个引脚 |
| <a id="abdc60c3175e972aef218978ea5ad6c38"></a>[`pin_get_config`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__api.html#abdc60c3175e972aef218978ea5ad6c38) | [`gpio_api_pin_get_config_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#ga0b30055e6722031df85b712b6b151710) | OPT | 取得单个引脚配置 |
| <a id="a2663c69ada10dd209cc2f266b733c97c"></a>[`port_get_raw`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__api.html#a2663c69ada10dd209cc2f266b733c97c) | [`gpio_api_port_get_raw_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gad31b73d23fa7f6c96ec2f4a2523d61fb) | REQ | 取得端口所有输入引脚物理电平 |
| <a id="af1d1268ef57bcedce138c64b95ba2878"></a>[`port_set_masked_raw`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__api.html#af1d1268ef57bcedce138c64b95ba2878) | [`gpio_api_port_set_masked_raw_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gab3d809d4ffbba78cfad45bcdb8f5ce5a) | REQ | 设置端口输出引脚物理电平 |
| <a id="a12abf1e8eaa9e92af931b1045fe0e377"></a>[`port_set_bits_raw`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__api.html#a12abf1e8eaa9e92af931b1045fe0e377) | [`gpio_api_port_set_bits_raw_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gabca79087ebe1c21911ef9a80eaaee43e) | REQ | 将所选输出引脚设置为物理高电平 |
| <a id="ad8ceab5ca80067db8d7c8be884ac9de1"></a>[`port_clear_bits_raw`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__api.html#ad8ceab5ca80067db8d7c8be884ac9de1) | [`gpio_api_port_clear_bits_raw_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#ga43e339579ea19b4cc7d90a04c208e587) | REQ | 将所选输出引脚设置为物理低电平 |
| <a id="a676651f5ef63de226e244ffe7a6c0ece"></a>[`port_toggle_bits`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__api.html#a676651f5ef63de226e244ffe7a6c0ece) | [`gpio_api_port_toggle_bits_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#ga8486f9d9925531757b49e745ca7fdab2) | REQ | 翻转所选输出引脚电平 |
| <a id="a77fbd18d3c4d7f48f3f640a80d8b0555"></a>[`pin_interrupt_configure`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__api.html#a77fbd18d3c4d7f48f3f640a80d8b0555) | [`gpio_api_pin_interrupt_configure_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gafa0e73e50f77890699cfe1a04ed9f155) | OPT | 配置引脚中断 |
| <a id="a92cdd5aeab396e756773cb00dbe87c33"></a>[`manage_callback`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__api.html#a92cdd5aeab396e756773cb00dbe87c33) | [`gpio_api_manage_callback_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#ga2aaa71c0dd3728fdd2f8bd111245c456) | OPT | 添加或移除应用回调（Callback） |
| <a id="a1c66d09d500fbed09cf9c85973dc9bcf"></a>[`get_pending_int`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__api.html#a1c66d09d500fbed09cf9c85973dc9bcf) | [`gpio_api_get_pending_int_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#ga2a4ec98edb4dfb38cde49ab796fcbff3) | OPT | 取得挂起中断（Pending Interrupt） |
| <a id="a7e4adc56ec0cb667cf4d4f711de52be4"></a>[`port_get_direction`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__api.html#a7e4adc56ec0cb667cf4d4f711de52be4) | [`gpio_api_port_get_direction_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#ga5d175c3355e88ee78b08539b61fc84fd) | OPT | 取得端口所选引脚方向 |

成员 `pin_get_config` 仅在配置系统 Kconfig 的 [`CONFIG_GPIO_GET_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_GET_CONFIG) 启用时可用；`port_get_direction` 仅在 [`CONFIG_GPIO_GET_DIRECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_GET_DIRECTION) 启用时可用。`manage_callback` 的公共入口是 [`gpio_add_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga05fd15af20386d69f9332354285b0cca) 与 [`gpio_remove_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gac1e94ba8faac79f469447e9b5d2f8c06)。

## 272.3\_相关设备宏

相关设备定义宏为 [`DEVICE_DT_INST_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)、[`DEVICE_DT_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)，驱动接口声明宏为 [`DEVICE_API()`](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)。

---

[上一章：GPIO驱动后端](P271_GPIO驱动后端.md) · [下一章：GPIO模拟接口](P273_GPIO模拟接口.md) · [返回大纲](大纲.md)
