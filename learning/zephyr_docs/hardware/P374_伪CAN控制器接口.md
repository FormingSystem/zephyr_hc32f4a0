---
id: learning.zephyr-docs.hardware.canfake-0
title: 伪CAN控制器接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第374章\_伪CAN控制器接口

原文：[group__can__fake](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html)。读取日期：2026-10-13，`latest`。

## 374.1\_用于测试的伪函数实现

本页是控制器局域网（Controller Area Network，CAN）控制器的伪实现（Fake），使用伪函数框架（Fake Function Framework，FFF）实现 CAN 应用程序编程接口（Application Programming Interface，API），供测试使用。头文件为 `zephyr/drivers/can/can_fake.h`。

启用 Kconfig 配置项 [`CONFIG_CAN_FAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_FAKE)，即可从设备树（Devicetree）的 [`zephyr,fake-can` 节点](https://docs.zephyrproject.org/latest/build/dts/api/bindings/can/zephyr%2Cfake-can.html#std-dtcompatible-zephyr-fake-can)实例化驱动。

每个伪函数都有一个同名加 `_fake` 后缀的 FFF 控制结构，测试用它设置返回值、安装自定义伪函数或检查调用次数及捕获的实参。这些控制结构未列在原页面中，参见[使用 FFF 进行模拟](https://docs.zephyrproject.org/latest/develop/test/ztest.html#mocking-fff)。

## 374.2\_返回值、输出参数与测试复位

只报告状态的伪函数可以设置 `return_val`。具有输出参数的伪函数必须用 `custom_fake` 驱动：只设置 `return_val` 不会改写输出参数。

启用 Kconfig 配置项 [`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST) 后，Zephyr 测试框架 Ztest 的规则会在每个测试用例之前复位全部伪函数。[`fake_can_get_capabilities`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga5ab6c1a56f20e14e7a3ee7f41f77e722)、[`fake_can_get_state`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga18314694d1939ec4983ef33681a8dcb3) 和 [`fake_can_get_core_clock`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga657de26af4b7860d1b485640ce979535) 默认装有 `custom_fake`，负责向输出参数填入可用值；每次复位都会重新安装默认实现。需要改变其报告内容时，应在测试用例中安装自己的 `custom_fake`。

## 374.3\_启停、模式和时序

原页面仅保留参数类型而未提供参数名，以下签名同样保留这种形式：

```c
int fake_can_start(const struct device *);
int fake_can_stop(const struct device *);
int fake_can_set_timing(const struct device *, const struct can_timing *);
int fake_can_set_timing_data(const struct device *, const struct can_timing *);
int fake_can_get_capabilities(const struct device *, can_mode_t *);
int fake_can_set_mode(const struct device *, can_mode_t);
```

这些函数分别伪实现 `can_driver_api` 的 `start`、`stop`、`set_timing`、`set_timing_data`、`get_capabilities` 和 `set_mode` 操作，即启动、停止、设置普通/数据阶段时序、查询能力与设置模式。

## 374.4\_发送与接收过滤器

发送、添加及移除接收（Receive，RX）过滤器的伪函数为：

```c
int fake_can_send(const struct device *, const struct can_frame *,
                   k_timeout_t, can_tx_callback_t, void *);
int fake_can_add_rx_filter(const struct device *, can_rx_callback_t,
                            void *, const struct can_filter *);
void fake_can_remove_rx_filter(const struct device *, int);
```

它们分别对应 [`can_driver_api::send`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#a9b5ec5c71a126798c24a19d1c91f879b)、[`can_driver_api::add_rx_filter`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#a56225a8cb458baa0d1745ff5e9202ae6) 和 [`can_driver_api::remove_rx_filter`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#ac264f4d66a29a5f42aaf2b6c9665f8f3)。超时类型 [`k_timeout_t`](../timer_reference/P087_内核超时类型.md)、发送回调类型 [`can_tx_callback_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gab3675297d3e528bf19e2072f6a84bfca)、接收回调类型 [`can_rx_callback_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gaab9525fafab78c0da0a78a2dae39bd6f) 沿用控制器公共接口。

## 374.5\_恢复、状态、时钟和能力查询

其余伪操作声明如下：

```c
int fake_can_recover(const struct device *, k_timeout_t);
int fake_can_get_state(const struct device *, enum can_state *, struct can_bus_err_cnt *);
int fake_can_state_change_callbacks_enabled(const struct device *, bool);
int fake_can_get_max_filters(const struct device *, bool);
int fake_can_get_core_clock(const struct device *, uint32_t *);
```

[`fake_can_recover`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga6b2569d7a1e1409fbbc0a6fb8cb3b4d0) 对应 [`can_driver_api::recover`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__api.html#aba563aff4e114b7956bb824efdebb0c6)，用于恢复操作的伪实现；`fake_can_get_state` 对应 `get_state`，查询控制器状态和错误计数；[`fake_can_state_change_callbacks_enabled`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga0378d66c4a1d72d5431751e094c6f21a) 对应 `state_change_callbacks_enabled`，处理状态变化回调是否启用的通知；[`fake_can_get_max_filters`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga4d396abead1d8ed677f00b64198f2597) 对应 `get_max_filters`，查询最大过滤器数量；`fake_can_get_core_clock` 对应 `get_core_clock`，查询核心时钟。

这些是测试替身的操作对应关系，原页没有承诺真实总线传输或实际硬件状态变化；具体返回和输出按本章前述 FFF 控制结构设置。

---

[上一章：CAN设备树宏](P373_CAN设备树宏.md) · [下一章：CAN驱动示例目录](P375_CAN驱动示例目录.md) · [返回大纲](大纲.md)
