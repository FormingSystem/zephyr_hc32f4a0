---
id: learning.zephyr-docs.services-overview.page-6
title: LoRa与LoRaWAN
kind: reference
status: maintained
domains: [zephyr, services, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/lora_lorawan/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->


<a id="lora-and-lorawan"></a>
<a id="lorawan-api"></a>
<a id="lora-api"></a>

# 第6章\_LoRa与LoRaWAN

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/lora_lorawan/index.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。


<a id="overview"></a>

## 6.1\_概览（Overview）

LoRa 是远距离（Long Range）的缩写，是 [Semtech 公司](https://www.semtech.com/)开发的专有低功耗无线通信协议。它使用线性调频扩频（Chirp Spread Spectrum，CSS）调制技术，承担物理层（Physical Layer，PHY）功能。LoRaWAN，即远距离广域网（Long Range Wide Area Network），在 LoRa PHY 之上定义网络层。

Zephyr 的 LoRa API 可以直接通过无线接口发送原始数据包；LoRaWAN API 则让终端设备经网关连接互联网。

Zephyr 提供两种 LoRaWAN 后端：

- **LoRaMac-node，默认后端：** 基于 Semtech 的 [LoRaMac-node 库](https://github.com/Lora-net/LoRaMac-node)，以 Zephyr 模块形式引入，支持 LoRaWAN 规范定义的全部区域。通过 [`CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE) 选择。
- **原生后端（Native）：** 按 Zephyr 习惯实现的 LoRaWAN 1.0.x Class A，直接访问 LoRa 无线驱动，无外部依赖。当前支持 EU868 区域，通过 [`CONFIG_LORA_MODULE_BACKEND_NATIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA_MODULE_BACKEND_NATIVE) 选择。

> 注意：Semtech 已弃用 LoRaMac-node，转而采用 [LoRa Basics Modem](https://github.com/Lora-net/SWL2001)。将 Zephyr API 移植到该后端的工作正在进行。当前，通过 [`CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM)，仅为 SX1261、SX1262、SX1272 和 SX1276 芯片提供基础 LoRa API 支持。

LoRaWAN 规范由 [LoRa 联盟（LoRa Alliance）](https://lora-alliance.org/)发布。


<a id="configuration-options"></a>

## 6.2\_配置选项（Configuration Options）


<a id="lora-phy"></a>

### 6.2.1\_LoRa物理层（LoRa PHY）

相关配置位于 [`drivers/lora/Kconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig)：

- [`CONFIG_LORA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA)。
- [`CONFIG_LORA_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA_SHELL)。
- [`CONFIG_LORA_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA_INIT_PRIORITY)。


<a id="lorawan"></a>

### 6.2.2\_LoRaWAN

相关配置位于 [`subsys/lorawan/Kconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/Kconfig)：

- [`CONFIG_LORAWAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN)。
- [`CONFIG_LORAWAN_SYSTEM_MAX_RX_ERROR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_SYSTEM_MAX_RX_ERROR)。
- [`CONFIG_LORAWAN_REGION_AS923`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_AS923)。
- [`CONFIG_LORAWAN_REGION_AU915`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_AU915)。
- [`CONFIG_LORAWAN_REGION_CN470`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_CN470)。
- [`CONFIG_LORAWAN_REGION_CN779`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_CN779)。
- [`CONFIG_LORAWAN_REGION_EU433`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_EU433)。
- [`CONFIG_LORAWAN_REGION_EU868`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_EU868)。
- [`CONFIG_LORAWAN_REGION_KR920`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_KR920)。
- [`CONFIG_LORAWAN_REGION_IN865`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_IN865)。
- [`CONFIG_LORAWAN_REGION_US915`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_US915)。
- [`CONFIG_LORAWAN_REGION_RU864`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_RU864)。


<a id="native-backend"></a>

### 6.2.3\_原生后端（Native Backend）

通过 [`CONFIG_LORA_MODULE_BACKEND_NATIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA_MODULE_BACKEND_NATIVE) 选择原生后端，[`subsys/lorawan/native/Kconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/native/Kconfig) 还提供：

- [`CONFIG_LORAWAN_NATIVE_ENGINE_STACK_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_NATIVE_ENGINE_STACK_SIZE)。
- [`CONFIG_LORAWAN_NATIVE_ENGINE_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_NATIVE_ENGINE_PRIORITY)。
- [`CONFIG_LORAWAN_NATIVE_PUBLIC_NETWORK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_NATIVE_PUBLIC_NETWORK)。
- [`CONFIG_LORAWAN_NATIVE_DUTY_CYCLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_NATIVE_DUTY_CYCLE)。


<a id="api-reference"></a>

## 6.3\_API参考（API Reference）


<a id="id1"></a>

### 6.3.1\_LoRa物理层

[LoRa API](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html)；相关代码示例为：

- [LoRa 占空比接收](../driver_samples/P015_LoRa占空比示例.md#lora-duty-cycle)：利用硬件接收占空比（RX duty cycling），即无线唤醒（wake-on-radio），接收 LoRa 数据包。
- [LoRa 接收](../driver_samples/P016_LoRa接收示例.md#lora-receive)：使用 LoRa 无线设备，以同步和异步模式接收数据包。
- [LoRa 发送](../driver_samples/P017_LoRa发送示例.md#lora-send)：每秒发送一次预先配置的载荷。


<a id="id2"></a>

### 6.3.2\_LoRaWAN

[LoRaWAN API](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html)；相关代码示例为：

- [LoRaWAN Class A 设备](../basic_samples/P059_LoRaWANA类设备示例.md#lorawan-class-a)：加入 LoRaWAN 网络并周期性发送消息。
- [LoRaWAN 空中固件升级（Firmware Upgrade Over the Air，FUOTA）](../basic_samples/P060_LoRaWAN空中固件升级示例.md#lorawan-fuota)：执行 LoRaWAN FUOTA 操作。


对应官方文档源码：[doc/services/connectivity/lora_lorawan/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/lora_lorawan/index.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/lora_lorawan/index.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：连接服务入口](P005_连接服务入口.md) · [本模块主线目录](../reading/services_overview.md) · [全部主线](../reading/README.md) · [下一篇：调制解调器模块](P007_调制解调器模块.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P005_连接服务入口.md) · [返回大纲](大纲.md) · [下一章](P007_调制解调器模块.md)

</details>

<!-- reading-navigation:end -->
