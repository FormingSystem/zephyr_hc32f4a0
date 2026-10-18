---
id: learning.zephyr-docs.bluetooth.page-99
title: Mesh大对象传输客户端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/blob_cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="blob-transfer-client"></a>

<a id="bluetooth-mesh-blob-cli"></a>

# 第99章\_大对象传输客户端（BLOB Transfer Client）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/blob_cli.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

二进制大对象传输客户端（BLOB Transfer Client）是 BLOB 传输的发送方，支持在推送模式和拉取模式下向任意数量的目标节点发送任意大小的 BLOB。

> 译注——适用范围：这里的“任意”沿用原文，仍受[BLOB 能力与大小限制](P098_Mesh大对象传输.md#transfer-capabilities)、所用实现和目标节点资源约束。示例中的回调、节点列表和密钥等由应用提供，代码片段不是独立的完整固件。

<a id="usage"></a>

## 99.1 使用方法（Usage）

<a id="initialization"></a>

### 99.1.1 初始化（Initialization）

在一个元素（Element）上实例化客户端，并配置一组事件处理回调：

```text
static const struct bt_mesh_blob_cli_cb blob_cb = {
      /* Callbacks */
};

static struct bt_mesh_blob_cli blob_cli = {
      .cb = &blob_cb,
};

static const struct bt_mesh_model models[] = {
      BT_MESH_MODEL_BLOB_CLI(&blob_cli),
};
```

<a id="transfer-context"></a>

### 99.1.2 传输上下文（Transfer context）

传输能力查询过程和 BLOB 传输过程都使用 [`bt_mesh_blob_cli_inputs`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli__inputs.html) 实例决定传输方式。使用前，客户端输入结构体至少要初始化目标节点列表、应用密钥（Application key）和生存时间（TTL）：

```text
static struct bt_mesh_blob_target targets[3] = {
        { .addr = 0x0001 },
        { .addr = 0x0002 },
        { .addr = 0x0003 },
};
static struct bt_mesh_blob_cli_inputs inputs = {
        .app_idx = MY_APP_IDX,
        .ttl = BT_MESH_TTL_DEFAULT,
};

sys_slist_init(&inputs.targets);
sys_slist_append(&inputs.targets, &targets[0].n);
sys_slist_append(&inputs.targets, &targets[1].n);
sys_slist_append(&inputs.targets, &targets[2].n);
```

注意，参与传输的所有服务端都必须绑定到所选应用密钥。

<a id="group-address"></a>

#### 99.1.2.1 组地址（Group address）

应用还可以在上下文结构体中指定组地址。如果该地址不是 [`BT_MESH_ADDR_UNASSIGNED`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga6d11790af686e6d48f08c6f1cd65317c)，传输消息将发送到组地址，而不是逐个发送给各目标节点。Mesh 管理器（Mesh Manager）必须确保所有目标节点上的大对象传输服务端模型都订阅了这个组地址。

使用组地址通常能够提高 BLOB 传输速度，因为客户端可以同时向所有目标节点发送同一条消息。不过，在蓝牙 Mesh 中，向组地址发送大型分段消息通常不如向单播地址发送可靠，因为组地址没有传输层确认机制。这可能延长每个块结束时的丢包恢复时间，并增加目标节点退出传输的风险。通常只有目标节点较多时，使用组地址才更有收益；不同寻址策略的效果还会随实际部署和 Chunk 大小显著变化。

<a id="transfer-timeout"></a>

#### 99.1.2.2 传输超时（Transfer timeout）

如果目标节点未在客户端时限内响应需要确认的消息，就会被移出本次传输。应用可以通过上下文结构体给予客户端更多等待时间，降低这种情况发生的概率。在 20 秒基本时间之外，额外时间以 10 秒为单位递增，最高约 182 小时。等待时间还会根据传输 TTL 自动调整。

注意，客户端只在以下情况下继续推进传输：

- 所有目标节点都已响应。

- 某个节点已从目标节点列表中移除。

- 客户端等待超时。

增加等待时间也会增加这部分延迟。

<a id="blob-transfer-capabilities-retrieval"></a>

### 99.1.3 查询 BLOB 传输能力（BLOB transfer capabilities retrieval）

通常建议在开始传输前查询 BLOB 传输能力。查询过程汇总所有目标节点的能力，选择能够让所有目标参与传输的、限制最少的一组参数。不响应或返回不兼容参数的目标节点会被移除。

目标节点的优先级由其在列表中的顺序决定。如果某个节点与前面任一节点不兼容，例如报告的块大小范围没有交集，该节点就会被移除。失去的目标节点通过 [`lost_target`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli__cb.html#a26a5ebe87db105900b150f71d770234d) 回调报告。

查询结束时调用 [`caps`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli__cb.html#a58e749cadeb464299495ee74456c592c) 回调。应用可根据得到的能力，确定传输所需的块大小和 Chunk 大小。

<a id="blob-transfer"></a>

### 99.1.4 BLOB 传输（BLOB transfer）

调用 [`bt_mesh_blob_cli_send()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga708e4afb3d9e1d6a8fb02d8fd5ab78c2) 启动 BLOB 传输。除上述输入外，还需提供一组传输参数和一个 BLOB 流实例。参数包括 64 位 BLOB ID、BLOB 大小、传输模式、以对数表示的块大小及 Chunk 大小。BLOB ID 由应用定义，但必须与服务端启动接收时使用的 ID 相同。

传输持续到至少一个目标节点成功完成，或者传输被取消。结束时通过 [`end`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli__cb.html#a60bc49eab376b055a8c21099f86fdde7) 回调通知应用，失去的目标节点通过 [`lost_target`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli__cb.html#a26a5ebe87db105900b150f71d770234d) 回调报告。

<a id="api-reference"></a>

## 99.2 API 参考（API reference）

[蓝牙 Mesh 大对象传输客户端模型 API（Bluetooth Mesh BLOB Transfer Client model API）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/blob_cli.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/blob_cli.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/blob_cli.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh大对象传输](P098_Mesh大对象传输.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh大对象传输服务端](P100_Mesh大对象传输服务端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P098_Mesh大对象传输.md) · [返回大纲](大纲.md) · [下一章](P100_Mesh大对象传输服务端.md)

</details>

<!-- reading-navigation:end -->
