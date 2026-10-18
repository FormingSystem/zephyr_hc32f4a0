---
id: learning.zephyr-docs.bluetooth.page-79
title: Mesh健康服务端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/health_srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="health-server"></a>

<a id="bluetooth-mesh-models-health-srv"></a>

# 第79章\_健康服务端（Health Server）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/health_srv.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：关注状态（attention state）要求应用回调实际驱动灯、蜂鸣器或振动器；模型本身不会自动识别板上的提示硬件。故障值与公司标识一起解释，厂商区间不应当作全厂商通用故障表。

健康服务端模型为健康客户端提供关注回调和节点诊断，主要用于报告节点故障，并帮助把网络中的 Mesh 节点对应到实际物理位置。 相关链接：[健康客户端（Health Client）](P078_Mesh健康客户端.md#bluetooth-mesh-models-health-cli)。

若存在健康服务端模型，必须在主元素上实例化。

<a id="faults"></a>

## 79.1 故障（Faults）

健康服务端可报告设备生命周期内发生的故障列表。故障通常是可能改变节点行为的事件或条件，例如断电、外设故障。故障分为警告（warning）和错误（error）：警告表示接近设计承受极限但未必损伤设备的情况；错误表示已超出设计极限，可能导致异常行为或永久损伤。

故障值 `0x01` 到 `0x7f` 保留给 Bluetooth Mesh 规范，完整列表见健康故障。`0x80` 到 `0xff` 由厂商定义。报告故障列表时始终附带公司标识（Company ID），以便解释厂商专用故障。 相关链接：[健康故障（Health faults）](#bluetooth-mesh-health-faults)。

<a id="attention-state"></a>

<a id="bluetooth-mesh-models-health-srv-attention"></a>

## 79.2 关注状态（Attention state）

关注状态让设备通过闪烁、发声或振动等物理行为引起注意。它可在配网时提示用户当前操作的是哪台设备，也可在运行期间通过健康模型使用。

关注状态启用时，必须设置 1—255 秒的超时。健康服务端 API 提供两个回调，让应用执行引起注意的行为：关注期开始时调用 [`bt_mesh_health_srv_cb.attn_on`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__srv__cb.html#ad9e8a392943d4848190c4513327bc52c)，结束时调用 [`bt_mesh_health_srv_cb.attn_off`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__srv__cb.html#abd881db6cf849433808bc6464e109b60)。

可通过 [`bt_mesh_health_srv.attn_timer`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__srv.html#a8df7f6c7e434cb717b9b51a3167b5e86) 查询关注期剩余时间。

<a id="api-reference"></a>

## 79.3 API 参考（API reference）

[健康服务端模型（Health Server Model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html)

<a id="health-faults"></a>

<a id="bluetooth-mesh-health-faults"></a>

### 79.3.1 健康故障（Health faults）

Bluetooth Mesh 规范定义的故障值。

[健康故障（Health faults）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__faults.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/health_srv.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/health_srv.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/health_srv.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh健康客户端](P078_Mesh健康客户端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh大型组成数据客户端](P080_Mesh大型组成数据客户端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P078_Mesh健康客户端.md) · [返回大纲](大纲.md) · [下一章](P080_Mesh大型组成数据客户端.md)

</details>

<!-- reading-navigation:end -->
