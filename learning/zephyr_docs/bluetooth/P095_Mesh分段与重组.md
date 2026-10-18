---
id: learning.zephyr-docs.bluetooth.page-95
title: Mesh分段与重组
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/sar_cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="segmentation-and-reassembly-sar"></a>

<a id="bluetooth-mesh-sar-cfg"></a>

# 第95章\_分段与重组（Segmentation and Reassembly，SAR）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/sar_cfg.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：SAR 即分段与重组（Segmentation and Reassembly）。上／下传输层是 Bluetooth Mesh 协议分层，PDU 是协议数据单元（Protocol Data Unit）。384 字节是本页所述传输 PDU 上限，不应直接当作应用可用参数长度；还须考虑实际消息编码、完整性校验和所选配置。

分段与重组（SAR）用于处理 Mesh 网络中较大的上传输层消息，以增强 Bluetooth Mesh 吞吐能力；该机制由下传输层（lower transport layer）使用。

下传输层规定如何把上传输层 PDU（Upper Transport PDU）分成多个下传输层 PDU（Lower Transport PDU）并在对端重组，再将这些 PDU 发送到对端的下传输层。上传输层 PDU 能容纳时，用一个下传输层 PDU 发送；不能容纳的较长数据包则分成多个分段（segment）。

接收设备的下传输层先将各段重组为一个上传输层 PDU，再向上传递。分段消息的交付由接收节点下传输层确认，未分段消息则没有这一确认。即使 PDU 能放入一个下传输层 PDU，若需要下传输层确认，也可按仅含一段的分段消息发送。设置原文所称 `send rel` 标志，见 [`bt_mesh_msg_ctx`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__msg__ctx.html)，即可使用可靠传输并确认单段分段消息。

SAR 最多传输 32 段，消息 PDU 最大为 384 个八位字节（octet）。使用以下 Kconfig 选项配置协议栈消息大小：

- [`CONFIG_BT_MESH_RX_SEG_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_RX_SEG_MAX)：设置入站消息的最大分段数。

- [`CONFIG_BT_MESH_TX_SEG_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_TX_SEG_MAX)：设置出站消息的最大分段数。

[`CONFIG_BT_MESH_TX_SEG_MSG_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_TX_SEG_MSG_COUNT) 和 [`CONFIG_BT_MESH_RX_SEG_MSG_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_RX_SEG_MSG_COUNT) 定义可同时处理的出站和入站分段消息数量。多条分段消息发往同一目的地址时，会排队逐条发送。

入站与出站分段消息共用分段分配池，池大小由 [`CONFIG_BT_MESH_SEG_BUFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SEG_BUFS) 配置。两者都在事务开始时分配分段；出站消息的分段被接收方确认后逐一释放，入站消息则等到全部接收完成后才释放。确定缓冲区大小时应考虑这一差别。

SAR 不会为每个分段的访问层载荷额外增加开销。

> 译注——字段拼写与确认范围：原文的 `send rel` 在[官方 msg.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/bluetooth/mesh/msg.h)中实际为 `bt_mesh_msg_ctx.send_rel`。它请求传输层分段确认，不等于应用已执行成功；原文的载荷开销表述也不表示分段传输没有协议头或空口开销。

<a id="segmentation-and-reassembly-sar-configuration-models"></a>

## 95.1 SAR 配置模型（Segmentation and reassembly (SAR) Configuration models）

从《Bluetooth Mesh Protocol Specification》1.1 版开始，可通过 Mesh 网络使用以下 SAR 配置模型，配置间隔、定时器和重传计数等行为：

- [SAR 配置客户端（SAR Configuration Client）](P096_MeshSAR配置客户端.md#bluetooth-mesh-sar-cfg-cli)

- [SAR 配置服务端（SAR Configuration Server）](P097_MeshSAR配置服务端.md#bluetooth-mesh-sar-cfg-srv)

无论节点是否具有 SAR 配置服务端，以下 SAR 行为都适用。

各分段的发送以分段发送间隔隔开，见 SAR 分段间隔步进状态。其他可配置的时间间隔和延迟包括： 相关链接：[SAR 分段间隔步进（SAR Segment Interval Step）](#sar-segment-interval-step)。

- 单播重传间隔，见 SAR 单播重传间隔步进与间隔增量状态。 相关链接：[SAR 单播重传间隔步进（SAR Unicast Retransmissions Interval Step）](#sar-unicast-retransmissions-interval-step)；[SAR 单播重传间隔增量（SAR Unicast Retransmissions Interval Increment）](#sar-unicast-retransmissions-interval-increment)。

- 多播重传间隔，见 SAR 多播重传间隔步进状态。 相关链接：[SAR 多播重传间隔步进（SAR Multicast Retransmissions Interval Step）](#sar-multicast-retransmissions-interval-step)。

- 分段接收间隔，见 SAR 接收端分段间隔步进状态。 相关链接：[SAR 接收端分段间隔步进（SAR Receiver Segment Interval Step）](#sar-receiver-segment-interval-step)。

- 确认延迟增量，见 SAR 确认延迟增量状态。 相关链接：[SAR 确认延迟增量（SAR Acknowledgment Delay Increment）](#sar-acknowledgment-delay-increment)。

最后一段标记为未确认的分段发出后，下传输层启动重传定时器。SAR 单播重传定时器的初值取决于消息的生存时间（Time To Live，TTL）字段。TTL 大于 `0` 时，初值按下式设置：

$$
unicast~retransmissions~interval~step + unicast~retransmissions~interval~increment \times (TTL - 1)
$$

TTL 为 `0` 时，定时器初值设为单播重传间隔步进。

SAR 多播重传定时器初值设为多播重传间隔。

下传输层收到消息分段时，启动 SAR 丢弃定时器（Discard timer），表示在丢弃该段所属分段消息之前等待多久。初值为 SAR 丢弃超时状态所指示的时间。 相关链接：[SAR 丢弃超时（SAR Discard Timeout）](#sar-discard-timeout)。

> 译注——公式变量：`unicast retransmissions interval step` 是单播重传间隔步进，`unicast retransmissions interval increment` 是随 TTL 增加的间隔增量；`acknowledgment delay increment` 是确认延迟增量，`segment reception interval` 是分段接收间隔。`min` 取较小值。Kconfig 编码值与毫秒／秒的实际值通过后文公式换算，不能直接把编码值当作时间。

SAR 确认定时器（Acknowledgment timer）记录收到分段后、发送分段确认消息（Segment Acknowledgment）之前的等待时间，初值按下式计算：

$$
min(SegN + 0.5 , acknowledgment~delay~increment) \times segment~reception~interval
$$

原文称 `SegN` 字段标识上传输层 PDU 被分成的总段数。

> 译注——计数差一：在[官方 transport.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/mesh/transport.c)中，`tx->seg_n = (sdu->len - 1) / seg_len(...)`，总段数使用 `seg_n + 1`。因此 SegN 实际是最后一段的编号，即总段数减 1；例如 3 段对应 SegN = 2。上方原公式按该编码值使用，不能直接代入总段数。仓库[同名源码](../../../subsys/bluetooth/mesh/transport.c)可作版本对照。

四类计数器与 SAR 行为相关：

- 两个单播重传计数，见 SAR 单播重传次数和无进展单播重传次数状态。 相关链接：[SAR 单播重传次数（SAR Unicast Retransmissions Count）](#sar-unicast-retransmissions-count)；[SAR 无进展单播重传次数（SAR Unicast Retransmissions Without Progress Count）](#sar-unicast-retransmissions-without-progress-count)。

- 多播重传计数，见 SAR 多播重传次数状态。 相关链接：[SAR 多播重传次数（SAR Multicast Retransmissions Count）](#sar-multicast-retransmissions-count)。

- 确认重传计数，见 SAR 确认重传次数状态。 相关链接：[SAR 确认重传次数（SAR Acknowledgment Retransmissions Count）](#sar-acknowledgment-retransmissions-count)。

传输段数超过 SAR 分段阈值状态时，按 SAR 确认重传次数状态的值重传分段确认消息。 相关链接：[SAR 分段阈值（SAR Segments Threshold）](#sar-segments-threshold)；[SAR 确认重传次数（SAR Acknowledgment Retransmissions Count）](#sar-acknowledgment-retransmissions-count)。

<a id="sar-states"></a>

<a id="bt-mesh-sar-cfg-states"></a>

## 95.2 SAR 状态（SAR states）

分段与重组定义了两种状态：

- SAR 发送端状态（SAR Transmitter state）

- SAR 接收端状态（SAR Receiver state）

SAR 发送端状态是控制分段消息发送次数与时序的复合状态，包含：

- SAR 分段间隔步进（SAR Segment Interval Step）

- SAR 单播重传次数（SAR Unicast Retransmissions Count）

- SAR 无进展单播重传次数（SAR Unicast Retransmissions Without Progress Count）

- SAR 单播重传间隔步进（SAR Unicast Retransmissions Interval Step）

- SAR 单播重传间隔增量（SAR Unicast Retransmissions Interval Increment）

- SAR 多播重传次数（SAR Multicast Retransmissions Count）

- SAR 多播重传间隔步进（SAR Multicast Retransmissions Interval Step）

SAR 接收端状态是控制分段确认发送次数、时序及丢弃分段消息重组的复合状态，包含：

- SAR 分段阈值（SAR Segments Threshold）

- SAR 丢弃超时（SAR Discard Timeout）

- SAR 确认延迟增量（SAR Acknowledgment Delay Increment）

- SAR 确认重传次数（SAR Acknowledgment Retransmissions Count）

- SAR 接收端分段间隔步进（SAR Receiver Segment Interval Step）

<a id="sar-segment-interval-step"></a>

### 95.2.1 SAR 分段间隔步进（SAR Segment Interval Step）

SAR 分段间隔步进状态控制同一分段消息各段之间的发送间隔，单位为毫秒。

使用 [`CONFIG_BT_MESH_SAR_TX_SEG_INT_STEP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_TX_SEG_INT_STEP) 设置默认值，再按下式计算分段发送间隔：

$$
(\mathtt{CONFIG\_BT\_MESH\_SAR\_TX\_SEG\_INT\_STEP} + 1) \times 10~\text{ms}
$$

<a id="sar-unicast-retransmissions-count"></a>

### 95.2.2 SAR 单播重传次数（SAR Unicast Retransmissions Count）

SAR 单播重传次数规定向单播目的地址重传分段消息的最大次数，默认值由 [`CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_COUNT) 设置。

<a id="sar-unicast-retransmissions-without-progress-count"></a>

### 95.2.3 SAR 无进展单播重传次数（SAR Unicast Retransmissions Without Progress Count）

在超时期间未收到确认，或收到的确认只包含已确认分段时，此状态规定向单播地址继续重传分段消息的最大次数。用 [`CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_WITHOUT_PROG_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_WITHOUT_PROG_COUNT) 设置该上限。

<a id="sar-unicast-retransmissions-interval-step"></a>

### 95.2.4 SAR 单播重传间隔步进（SAR Unicast Retransmissions Interval Step）

此状态控制向单播地址重传尚未确认分段时所用的间隔步进，单位为毫秒。

用 [`CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_STEP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_STEP) 设置默认值，再按下式计算间隔步进：

$$
(\mathtt{CONFIG\_BT\_MESH\_SAR\_TX\_UNICAST\_RETRANS\_INT\_STEP} + 1) \times 25~\text{ms}
$$

<a id="sar-unicast-retransmissions-interval-increment"></a>

### 95.2.5 SAR 单播重传间隔增量（SAR Unicast Retransmissions Interval Increment）

SAR 单播重传间隔增量控制向单播地址重传尚未确认分段时增加的等待间隔，单位为毫秒。

用 [`CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_INC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_INC) 设置默认值，再按下式计算增量：

$$
(\mathtt{CONFIG\_BT\_MESH\_SAR\_TX\_UNICAST\_RETRANS\_INT\_INC} + 1) \times 25~\text{ms}
$$

<a id="sar-multicast-retransmissions-count"></a>

### 95.2.6 SAR 多播重传次数（SAR Multicast Retransmissions Count）

此状态控制向多播地址重传分段消息的总次数，通过 [`CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_COUNT) 设置。

<a id="sar-multicast-retransmissions-interval-step"></a>

### 95.2.7 SAR 多播重传间隔步进（SAR Multicast Retransmissions Interval Step）

此状态控制向多播地址重传一条分段消息全部分段之间的间隔，单位为毫秒。

用 [`CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_INT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_INT) 设置默认值，再按下式计算间隔：

$$
(\mathtt{CONFIG\_BT\_MESH\_SAR\_TX\_MULTICAST\_RETRANS\_INT} + 1) \times 25~\text{ms}
$$

<a id="sar-discard-timeout"></a>

### 95.2.8 SAR 丢弃超时（SAR Discard Timeout）

此状态规定下传输层收到分段后，在丢弃所属分段消息前等待的秒数。用 [`CONFIG_BT_MESH_SAR_RX_DISCARD_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_RX_DISCARD_TIMEOUT) 设置默认值，再按下式计算丢弃超时：

$$
(\mathtt{CONFIG\_BT\_MESH\_SAR\_RX\_DISCARD\_TIMEOUT} + 1) \times 5~\text{seconds}
$$

<a id="sar-acknowledgment-delay-increment"></a>

### 95.2.9 SAR 确认延迟增量（SAR Acknowledgment Delay Increment）

此状态控制收到新分段后、延迟发送确认消息的间隔增量，单位为分段数。

用 [`CONFIG_BT_MESH_SAR_RX_ACK_DELAY_INC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_RX_ACK_DELAY_INC) 设置默认值；增量计算为 \(\verb|CONFIG_BT_MESH_SAR_RX_ACK_DELAY_INC| + 1.5\)。

> 译注——单位示例：发送分段间隔编码 0 对应 10 毫秒，丢弃超时编码 0 对应 5 秒；确认延迟增量编码 0 对应 1.5 个分段间隔单位。上述值是换算示例，不是在替读者选择网络配置。

<a id="sar-segments-threshold"></a>

### 95.2.10 SAR 分段阈值（SAR Segments Threshold）

SAR 分段阈值状态规定触发确认重传的分段数量阈值，通过 [`CONFIG_BT_MESH_SAR_RX_SEG_THRESHOLD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_RX_SEG_THRESHOLD) 设置。

分段消息的段数超过阈值时，协议栈会对每条确认消息额外重传 [`CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT) 指定的次数。

<a id="sar-acknowledgment-retransmissions-count"></a>

### 95.2.11 SAR 确认重传次数（SAR Acknowledgment Retransmissions Count）

SAR 确认重传次数控制下传输层发送分段确认消息的重传次数；分段数量超过 [`CONFIG_BT_MESH_SAR_RX_SEG_THRESHOLD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_RX_SEG_THRESHOLD) 时，协议栈额外发送的确认重传总数由此规定。

用 [`CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT) 设置默认值。分段确认消息的最大发送次数为 \(\verb|CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT| + 1\)。

<a id="sar-receiver-segment-interval-step"></a>

### 95.2.12 SAR 接收端分段间隔步进（SAR Receiver Segment Interval Step）

SAR 接收端分段间隔步进规定收到新分段后延迟发送确认所用的接收间隔步进，单位为毫秒。

用 [`CONFIG_BT_MESH_SAR_RX_SEG_INT_STEP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_RX_SEG_INT_STEP) 设置默认值，按下式计算间隔：

$$
(\mathtt{CONFIG\_BT\_MESH\_SAR\_RX\_SEG\_INT\_STEP} + 1) \times 10~\text{ms}
$$

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/sar_cfg.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/sar_cfg.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/sar_cfg.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh桥接配置服务端](P094_Mesh桥接配置服务端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：MeshSAR配置客户端](P096_MeshSAR配置客户端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P094_Mesh桥接配置服务端.md) · [返回大纲](大纲.md) · [下一章](P096_MeshSAR配置客户端.md)

</details>

<!-- reading-navigation:end -->
