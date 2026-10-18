---
id: learning.zephyr-docs.bluetooth.page-66
title: Mesh核心
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/core.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="core"></a>

<a id="bluetooth-mesh-core"></a>

# 第66章\_Mesh 核心（Core）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/core.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：本章的“距离”或通信角色均属于 Mesh 协议概念。LPN 是低功耗角色，Friend 代为缓存并转发消息；是否能在某块板上使用，还取决于实际蓝牙控制器、协议栈和配置，不能从接口存在推断硬件已支持。

核心模块提供管理蓝牙网状网络（Bluetooth Mesh）总体状态的功能。

<a id="low-power-node"></a>

<a id="bluetooth-mesh-lpn"></a>

## 66.1 低功耗节点（Low Power Node）

低功耗节点（Low Power Node，LPN）角色允许电池供电设备作为叶节点参与 Mesh 网络。LPN 通过友谊节点（Friend node）与网络交互，Friend 负责转发发往 LPN 的消息。LPN 通过关闭无线电节省电能，仅在发送消息或向 Friend 轮询入站消息时唤醒。

无线电控制和轮询由 Mesh 协议栈自动管理；LPN API 也允许应用随时通过 [`bt_mesh_lpn_poll()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga3fd66605950a55e299ca3a7cc697d453) 触发轮询。轮询间隔、轮询事件时序及 Friend 要求等 LPN 运行参数由 [`CONFIG_BT_MESH_LOW_POWER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_LOW_POWER) 及相关配置选项控制。

同时使用 LPN 和日志功能时，强烈建议仅采用 [`CONFIG_LOG_MODE_DEFERRED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MODE_DEFERRED)。其他日志模式可能在处理日志消息时引入意外延迟，进而影响接收延迟和接收窗口的调度。启用 [`CONFIG_BT_MESH_FRIEND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_FRIEND) 时也有同样限制。

<a id="replay-protection-list"></a>

## 66.2 重放保护列表（Replay Protection List）

重放保护列表（Replay Protection List，RPL）保存最近从 Mesh 网络各元素收到的序列号，用于防御重放攻击（replay attack）。

为了在重启后仍能抵御重放攻击，节点需要在断电前把整个 RPL 写入持久化存储。根据网络流量大小，持续存储最近观察到的序列号迟早会造成 Flash 磨损。可通过 [`CONFIG_BT_MESH_RPL_STORE_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_RPL_STORE_TIMEOUT) 延后 RPL 条目的持久化写入，以缓解磨损。

这一选项不能完全解决问题，因为节点可能在 RPL 存储定时器触发前断电。为确保消息不能被重放，节点可随时调用 [`bt_mesh_rpl_pending_store()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga62f9a72c4e9dc5e4f3f42bd4df4fe452)，主动存储待写入的一个或多个 RPL 条目，也可在预计断电前预留足够时间调用。此时保存哪些条目由节点决定。

将 [`CONFIG_BT_MESH_RPL_STORE_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_RPL_STORE_TIMEOUT) 设为 -1 可以完全关闭该定时器，从而显著减少 Flash 磨损。这会把保存 RPL 的责任交给用户应用，并要求从调用此 API 起到所有 RPL 条目写入 Flash 为止，始终有足够的备用电源。

在 [`CONFIG_BT_MESH_RPL_STORE_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_RPL_STORE_TIMEOUT) 与主动调用 [`bt_mesh_rpl_pending_store()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga62f9a72c4e9dc5e4f3f42bd4df4fe452) 之间取得适当平衡，有助于降低安全漏洞风险与 Flash 磨损。

<a id="persistent-storage"></a>

<a id="bluetooth-mesh-persistent-storage"></a>

## 66.3 持久化存储（Persistent storage）

Mesh 协议栈使用[设置子系统（Settings Subsystem）](../storage/P005_设置子系统.md#settings-api)持久化设备配置。配置变化且需要保存时，协议栈调度一个工作项（work item）；从调度到提交到工作队列（workqueue）的延迟由 [`CONFIG_BT_MESH_STORE_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_STORE_TIMEOUT) 定义。一旦安排了存储，在该工作项处理之前不能重新安排，但下述情况例外。

需要保存 IV 索引（IV index）、序列号（Sequence Number）、CDB 配置或重放保护列表重置状态时，工作项会立即提交到工作队列，不作延迟。若此前已安排该工作项，也会改为立即执行。

重放保护列表与请求重放保护列表（Solicitation Replay Protection List）由独立工作项存储，其调度延迟由 [`CONFIG_BT_MESH_RPL_STORE_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_RPL_STORE_TIMEOUT) 定义。其他类型的待存储数据不会缩短这一延迟。若该选项设为 `-1`，重放保护列表会与其他协议栈配置一起存储。

工作项执行时，协议栈会存储归该工作项负责的全部待保存配置。

> 译注——版本对照：本次保存的官方原文将 RPL／SRPL 与其他设置分为不同工作项；独立存储的实现可在[官方 settings.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/mesh/settings.c)的 `RPL_OWN_TIMEOUT`、`rpl_pending_store` 和 `bt_mesh_settings_store_schedule()` 中追踪。本仓库[同名文件](../../../subsys/bluetooth/mesh/settings.c)可能属于不同版本，不能仅因文件名一致就套用旧调度行为。

<a id="work-item-execution-context"></a>

### 66.3.1 工作项执行上下文（Work item execution context）

[`CONFIG_BT_MESH_SETTINGS_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SETTINGS_WORKQ) 配置工作项的执行上下文。该选项默认开启，使协议栈用专用协作式线程（cooperative thread）处理工作项。这样，在配置存储期间仍可处理其他收发消息，以及提交到系统工作队列的其他工作项。

禁用该选项时，工作项提交到系统工作队列，因此保存协议栈配置的整个期间都会阻塞系统工作队列。不建议禁用，因为这会使设备在一段明显可感知的时间内无响应。

<a id="advertisement-identity"></a>

<a id="bluetooth-mesh-adv-identity"></a>

## 66.4 广播身份（Advertisement identity）

所有 Mesh 协议栈承载（bearer）都使用本地身份 [`BT_ID_DEFAULT`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaded4b52c9bb87fd4d19b1eb9361973e5) 广播数据，该值预设在实现中。当低功耗蓝牙（Bluetooth Low Energy，LE）与 Bluetooth Mesh 共存于同一设备时，应用应在开始通信前为 Bluetooth LE 分配并配置另一个本地身份。

<a id="api-reference"></a>

## 66.5 API 参考（API reference）

[蓝牙 Mesh（Bluetooth Mesh）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html)

相关代码示例（Related code samples）

- [蓝牙 Mesh 徽章（Bluetooth Mesh badge）](https://docs.zephyrproject.org/latest/samples/boards/phytec/reel_board/mesh_badge/README.html#mesh_badge)：使用 reel board 和 Bluetooth Mesh 实现智能徽章。

- [Mesh](https://docs.zephyrproject.org/latest/samples/bluetooth/mesh/README.html#ble_mesh)：使用基本 Bluetooth Mesh 功能。

- [Mesh 演示（Mesh Demo）](https://docs.zephyrproject.org/latest/samples/bluetooth/mesh_demo/README.html#ble_mesh_demo)：实现 Bluetooth Mesh 演示应用。

- [Mesh 模型（Mesh Models）](https://docs.zephyrproject.org/latest/samples/boards/nordic/mesh/onoff_level_lighting_vnd_app/README.html#nrf_bluetooth_mesh_onoff_level_lighting_vnd_app)：配置包含通用开关、通用等级等多种模型的 Bluetooth Mesh 节点。

- [Mesh 开关模型（Mesh OnOff Model）](https://docs.zephyrproject.org/latest/samples/boards/nordic/mesh/onoff-app/README.html#nrf_bluetooth_mesh_onoff)：使用 Bluetooth Mesh OnOff 模型控制 Mesh 网络中的 LED。

- [Mesh 配网器（Mesh Provisioner）](https://docs.zephyrproject.org/latest/samples/bluetooth/mesh_provisioner/README.html#ble_mesh_provisioner)：通过 Bluetooth Mesh API 为节点配网并配置节点。

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/core.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/core.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/core.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Windows10上的AutoPTS](P065_Windows10上的AutoPTS.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh访问层](P067_Mesh访问层.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P065_Windows10上的AutoPTS.md) · [返回大纲](大纲.md) · [下一章](P067_Mesh访问层.md)

</details>

<!-- reading-navigation:end -->
