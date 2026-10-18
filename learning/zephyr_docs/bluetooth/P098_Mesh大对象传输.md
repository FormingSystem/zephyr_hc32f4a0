---
id: learning.zephyr-docs.bluetooth.page-98
title: Mesh大对象传输
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/blob.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="blob-transfer-models"></a>

<a id="bluetooth-mesh-blob"></a>

# 第98章\_大对象传输模型（BLOB Transfer models）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/blob.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

二进制大对象（Binary Large Object，BLOB）传输模型实现《Bluetooth Mesh Binary Large Object Transfer Model》规范 1.0 版，用于通过蓝牙 Mesh 网络，将大型二进制对象从单个源节点发送到多个目标节点（Target node）。它是[设备固件更新（Device Firmware Update，DFU）](P102_Mesh设备固件更新.md#bluetooth-mesh-dfu)的底层传输方式，也可用于其他对象传输。目前该实现处于实验阶段。

BLOB 传输模型支持传输最大 4 GB（2³² 字节）的连续二进制对象。BLOB 传输协议内置丢包恢复过程，通过设置检查点，确保所有目标收到全部数据后再继续推进。数据传输的顺序不保证固定。

> 译注——单位与数据边界：这里按原文保留 4 GB 与 2³² 字节的写法；按二进制单位，2³² 字节为 4 GiB。它描述协议中的对象规模，不保证每个设备都能接收这么大的对象，还受配置、块／Chunk 能力和存储容量限制。

BLOB 传输受到下层 Mesh 网络传输速度和可靠性的限制。理想条件下，BLOB 传输速率最高可达 1 kbps，传输一个 100 kB 的 BLOB 约需 10—15 分钟。然而，网络状况、传输能力和其他限制很容易使数据速率下降数个数量级。根据应用和网络配置调整传输参数，并安排在网络流量较低的时段传输，可以显著改善协议的速度和可靠性。不过，在实际部署中通常难以达到接近理想值的速率。

BLOB 传输包含两个模型：

- [大对象传输服务端（BLOB Transfer Server）](P100_Mesh大对象传输服务端.md)

- [大对象传输客户端（BLOB Transfer Client）](P099_Mesh大对象传输客户端.md)

发送节点实例化大对象传输客户端（BLOB Transfer Client），接收节点实例化大对象传输服务端（BLOB Transfer Server）。

<a id="concepts"></a>

## 98.1 基本概念（Concepts）

BLOB 传输协议引入以下概念，用于实现大对象传输。

<a id="blobs"></a>

### 98.1.1 二进制大对象（BLOB）

BLOB 是大小不超过 4 GB 的二进制对象，可以包含应用希望通过 Mesh 网络传送的任意数据。BLOB 是连续的数据对象，为保证可靠传输并便于处理，划分为块（Block）和分块数据单元（Chunk）。协议不限制 BLOB 的内容和结构，应用可以自行定义数据的编码方式或压缩方式。

BLOB 传输协议自身不提供 BLOB 数据的完整性检查（Integrity check）、加密（Encryption）或身份认证（Authentication）。不过，下层蓝牙 Mesh 协议提供数据完整性检查，并通过网络层和应用层加密保护 BLOB 内容，防止第三方读取。

> 译注——固件验证职责：网络与应用层保护不等于固件来源签名验证。BLOB 负责搬运数据；固件映像是否可信、是否适用于本设备以及是否允许安装，由 DFU 应用验证，见[映像验证](P104_Mesh固件更新服务端.md#image-verification)。

<a id="blocks"></a>

#### 98.1.1.1 块（Block）

二进制对象划分为多个块，每块通常为数百至数千字节。各块分别传输，大对象传输客户端确保所有大对象传输服务端收到完整的当前块后，才进入下一块。块大小由传输参数 `block_size_log` 决定；一次传输中的块大小相同，但最后一块可以更小。对于存储在 Flash 中的 BLOB，块大小通常取目标设备 Flash 页大小的整数倍。

<a id="chunks"></a>

#### 98.1.1.2 分块数据单元（Chunk）

每个块进一步划分为多个分块数据单元（Chunk）。Chunk 是 BLOB 传输的最小数据单元，必须能够装入一条蓝牙 Mesh 访问消息除操作码外的部分中，即不超过 379 字节。Chunk 的传输机制取决于所选传输模式。

> 译注——消息容量：379 字节是原文给出的访问消息除操作码外的容量上限，不应直接作为应用可填的 Chunk 净数据长度；具体报文还需容纳相应的模型参数。Chunk 大小应采用能力协商结果和实际配置。

在推送传输模式（Push BLOB Transfer Mode）下，大对象传输客户端以无需确认的数据包向所有目标服务端发送 Chunk。发送完一个块中的所有 Chunk 后，客户端询问各服务端是否有缺失，并重发缺失部分。该过程持续进行，直到所有服务端收到全部 Chunk，或客户端放弃传输。

在拉取传输模式（Pull BLOB Transfer Mode）下，大对象传输服务端每次向客户端请求少量 Chunk，等待客户端发来这些 Chunk 后，再请求下一批。该过程重复进行，直到所有 Chunk 传输完毕，或服务端放弃传输。

有关这两种模式的更多说明，见[传输模式（Transfer modes）](#bluetooth-mesh-blob-transfer-modes)。

<a id="blob-streams"></a>

<a id="bluetooth-mesh-blob-stream"></a>

### 98.1.2 大对象流（BLOB streams）

BLOB 传输模型的 API 将 BLOB 数据处理与上层传输控制分离，使不同应用能够复用不同的 BLOB 存储和传输策略。应用直接控制上层传输过程，BLOB 数据本身则通过大对象流（BLOB stream）访问。

大对象流类似于标准库的文件流。无论 BLOB 位于 Flash、RAM 还是外设中，传输模型都可以通过打开、关闭、读取和写入操作访问其全部数据。使用前需要按访问模式（读取或写入）打开流，随后模型以块和 Chunk 为单位在 BLOB 数据中定位，并通过这个流完成访问。

<a id="interaction"></a>

#### 98.1.2.1 交互过程（Interaction）

读取或写入 BLOB 之前，先调用流的 [`open`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__io.html#a4666a3fafde0ee9fdd51d27732bec6bc) 回调打开它。服务端始终以写模式打开 BLOB 流，客户端始终以读模式打开 BLOB 流。

处理 BLOB 中的每个块时，传输模型先调用 [`block_start`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__io.html#a900f049b6a778d9e0973ee66b46dc046)；随后根据访问模式反复调用流的 [`wr`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__io.html#ae0b27ea814e5c939d708ae20d452ca09) 或 [`rd`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__io.html#a330ec5dcc8d18b84e7fdab9ef6d75f49) 回调，向 BLOB 写入数据或从中读取数据。处理完该块后调用 [`block_end`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__io.html#a57381249bf63924b2345ece6e12909cb)。传输完成后，通过 [`close`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__io.html#aac42902d0bbbef10a5e9cc35e8a3ea64) 关闭 BLOB 流。

<a id="implementations"></a>

#### 98.1.2.2 流的实现（Implementations）

应用可以实现自己的 BLOB 流，也可以使用 Zephyr 提供的实现：

- [BLOB Flash 存储（BLOB Flash）](P101_Mesh大对象Flash存储.md)；[BLOB Flash 读取器（BLOB Flash Reader）](P101_Mesh大对象Flash存储.md#blob-flash-reader)；[BLOB Flash 写入器（BLOB Flash Writer）](P101_Mesh大对象Flash存储.md#blob-flash-writer)；[API 参考（API Reference）](P101_Mesh大对象Flash存储.md#api-reference)。

<a id="transfer-capabilities"></a>

### 98.1.3 传输能力（Transfer capabilities）

不同大对象传输服务端的能力可能不同。各设备的传输能力由以下配置选项控制：

- [`CONFIG_BT_MESH_BLOB_SIZE_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_BLOB_SIZE_MAX)

- [`CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MIN)

- [`CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MAX)

- [`CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX)

客户端同样使用 [`CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX) 选项，该选项会影响客户端模型结构体占用的内存。

为使尽可能多的服务端能够接收传输，客户端可以在开始传输前查询各服务端的能力，然后使用共同支持范围内尽可能大的块大小和 Chunk 大小传输 BLOB。

<a id="transfer-modes"></a>

<a id="bluetooth-mesh-blob-transfer-modes"></a>

### 98.1.4 传输模式（Transfer modes）

BLOB 有两种传输模式：推送传输模式（Push BLOB Transfer Mode）和拉取传输模式（Pull BLOB Transfer Mode）。大多数情况下应采用推送模式。

推送模式由客户端控制发送速率，客户端推送每个块的全部 Chunk，不使用上层流量控制。该模式支持任意数量的目标节点，应作为默认传输模式。

拉取模式由服务端按自己的速率从客户端“拉取”Chunk，可以同时用于多个目标节点，主要面向充当[低功耗节点（Low Power Node）](P066_Mesh核心.md#bluetooth-mesh-lpn)的接收设备。服务端每次请求一小批 Chunk，等待它们全部到达后再请求下一批，直到收到当前块的所有 Chunk。接着，客户端启动下一个块，服务端再请求该块中的全部 Chunk。

<a id="transfer-timeout"></a>

<a id="bluetooth-mesh-blob-timeout"></a>

### 98.1.5 传输超时（Transfer timeout）

BLOB 传输超时基于超时基数（Timeout Base）计算。客户端和服务端使用相同的超时基数，但计算公式不同。

大对象传输服务端使用以下公式计算传输超时：

```text
10 * (Timeout Base + 1) seconds
```

大对象传输客户端使用以下公式：

```text
(10000 * (Timeout Base + 2)) + (100 * TTL) milliseconds
```

其中 TTL 是该次传输设置的生存时间（Time to Live）值。

<a id="api-reference"></a>

## 98.2 API 参考（API reference）

本节包含 BLOB 传输模型共用的类型和宏定义。

[蓝牙 Mesh BLOB 模型 API（Bluetooth Mesh BLOB model API）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/blob.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/blob.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/blob.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：MeshSAR配置服务端](P097_MeshSAR配置服务端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh大对象传输客户端](P099_Mesh大对象传输客户端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P097_MeshSAR配置服务端.md) · [返回大纲](大纲.md) · [下一章](P099_Mesh大对象传输客户端.md)

</details>

<!-- reading-navigation:end -->
