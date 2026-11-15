---
id: learning.zephyr-docs.bluetooth.page-16
title: L2CAP接口
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/l2cap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="logical-link-control-and-adaptation-protocol-l2cap"></a>
<a id="bt-l2cap"></a>

# 第16章\_L2CAP接口

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/l2cap.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）提供面向连接信道（Connection-oriented Channels），通过 [`CONFIG_BT_L2CAP_DYNAMIC_CHANNEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_DYNAMIC_CHANNEL) 启用。这些信道透明支持分段与重组（Segmentation and Reassembly），也支持基于信用值的流控（Credit-based Flow Control），适合传输数据流。

信道实例用 [`bt_l2cap_chan`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__chan.html) 表示，通过 [`bt_l2cap_chan_ops`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__chan__ops.html) 中的回调通知信道连接、断开或加密状态变化。收到数据时调用 `recv`：同步处理完成可返回0；异步处理则通过 [`bt_l2cap_chan_recv_complete()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gad53f5fc31314121ff84e740879eae3cf) 标记完成。

> 原文说明：`recv`直接从接收线程（RX Thread）调用，因此不建议在其中长时间阻塞。

> 译注——异步接收：按[官方L2CAP头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/bluetooth/l2cap.h)，采用异步方式时，`recv`应返回 `-EINPROGRESS`；完成后将收到的缓冲区交回 [`bt_l2cap_chan_recv_complete()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gad53f5fc31314121ff84e740879eae3cf)，保留其原始 `user_data`，其中记录该包所用分段／信用值数量。

发送数据使用 [`bt_l2cap_chan_send()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga97b7909749667f910f83e6fcb54495c3)。原文指出，无可用信用值时它可能阻塞，收到更多信用值后恢复。

> 译注——发送语义的版本差异：本次读取的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/bluetooth/l2cap.h)明确说明动态信道无信用值时把 `buf` 排队，待对端补充信用值后发送。不要把指南上述旧描述解释为“调用一定等到有信用值或发送完毕才返回”。头文件还规定成功时缓冲区所有权移交协议栈，失败时仍由调用者持有；`user_data`会被改写，不能用来保存应用数据。应以实际使用版本的接口约定判断返回值、生命周期及阻塞行为。

服务器通过 [`bt_l2cap_server_register()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga1a5e8c81c086872d7fb8da5329f982c6) 注册，传入 [`bt_l2cap_server`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__server.html)。其中 `psm` 指定监听的协议／服务复用值（Protocol/Service Multiplexer，PSM），`sec_level` 指定所需安全等级，`accept`回调用于批准传入连接请求并分配信道实例。分配对象必须为 [`bt_l2cap_le_chan`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__le__chan.html)，通过 `accept` 返回的信道引用应指向对象的 `chan` 成员。

```c
#define PSM 0x29 /* example PSM */

static int l2cap_recv(struct bt_l2cap_chan *chan, struct net_buf *buf);
static void l2cap_connected(struct bt_l2cap_chan *chan);
static void l2cap_disconnected(struct bt_l2cap_chan *chan);

/* ops used for every channel instance */
static struct bt_l2cap_chan_ops l2cap_ops = {
	.recv       = l2cap_recv,
	.connected  = l2cap_connected,
	.disconnected = l2cap_disconnected,
};

/* Fixed array of channel instances, one per possible connection */
static struct bt_l2cap_le_chan l2cap_chans[CONFIG_BT_MAX_CONN];

static int accept_cb(struct bt_conn *conn, struct bt_l2cap_server *server,
		     struct bt_l2cap_chan **chan)
{
	uint8_t conn_index = bt_conn_index(conn);

	/* initialize the chosen entry */
	(void)memset(&l2cap_chans[conn_index], 0, sizeof(l2cap_chans[conn_index]));
	l2cap_chans[conn_index].chan.ops = &l2cap_ops;

	*chan = &l2cap_chans[conn_index].chan;

	printk("L2CAP channel accepted, assigned chan[%d]\n", conn_index);

	return 0; /* accept */
}

static struct bt_l2cap_server server = {
	.psm = PSM,
	.sec_level = BT_SECURITY_L1,
	.accept = accept_cb,
};
```

> 译注——代码注释与输出：`PSM 0x29`是示例PSM；`l2cap_ops`供每个信道实例使用；固定数组为每个可能连接安排一个实例，使用 `bt_conn_index()` 选择并初始化条目。输出 `L2CAP channel accepted, assigned chan[%d]` 表示已接受信道并分配相应数组项；返回0表示接受。这段示意按每连接一个信道组织，不能不加修改地用于同一连接上多个同时存在的信道。它只声明回调和服务器对象；完整注册与处理见下方示例。

完整可运行的动态信道接受端（Acceptor，即服务器）示例见 [L2CAP面向连接信道接受端](../bluetooth_samples/P009_L2CAP信道接受端.md#bluetooth_l2cap_coc_acceptor)。

<a id="fixed-channels"></a>

## 16.1\_固定信道（Fixed Channels）

用户也可以通过 [`BT_L2CAP_FIXED_CHANNEL_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga334ced39f199394971d1600fac42abc8) 定义固定信道。固定信道在连接建立时初始化，不支持分段。尽管 `accept` 回调以 [`bt_l2cap_chan`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__chan.html) 形式返回引用，实际分配对象仍必须是 [`bt_l2cap_le_chan`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__le__chan.html)，引用指向其 `chan` 成员。

```c
static struct bt_l2cap_le_chan fixed_chan[CONFIG_BT_MAX_CONN];

/* Callbacks are assumed to be defined prior. */
static struct bt_l2cap_chan_ops ops = {
    .recv = recv_cb,
    .sent = sent_cb,
    .connected = connected_cb,
    .disconnected = disconnected_cb,
};

static int l2cap_fixed_accept(struct bt_conn *conn, struct bt_l2cap_chan **chan)
{
    uint8_t conn_index = bt_conn_index(conn);

    fixed_chan[conn_index] = (struct bt_l2cap_le_chan){
        .chan.ops = &ops,
    };

    *chan = &fixed_chan[conn_index].chan;

    return 0;
}

BT_L2CAP_FIXED_CHANNEL_DEFINE(fixed_channel) = {
    .cid = 0x0010,
    .accept = l2cap_fixed_accept,
};
```

> 译注——代码注释：原例假定此前已定义接收、发送、连接与断连回调；数组按连接索引保存 [`bt_l2cap_le_chan`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__le__chan.html)，返回其内部 `chan`，最后通过宏定义带有信道标识符（Channel Identifier，CID）和接受回调的固定信道。代码及示例CID按原文保留，不将其解释为新协议可任意占用的已分配信道号。

<a id="client-channels"></a>

## 16.2\_客户端信道（Client Channels）

客户端用 [`bt_l2cap_chan_connect()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga3c3cfb4b151c808c0a3d2562a5c26a20) 发起信道连接，用 [`bt_l2cap_chan_disconnect()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga7165f82a05e3a19d6b2baf0ba292a3fe) 断开。后者也可断开服务器创建的信道实例。完整发起端（Initiator，即客户端）示例见 [L2CAP面向连接信道发起端](../bluetooth_samples/P010_L2CAP信道发起端.md#bluetooth_l2cap_coc_initiator)。

<a id="api-reference"></a>

## 16.3\_API参考（API Reference）

[L2CAP API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html)。

## 16.4\_相关代码示例（Related code samples）

- [L2CAP接受端（Acceptor）](../bluetooth_samples/P009_L2CAP信道接受端.md#bluetooth_l2cap_coc_acceptor)：接受传入的L2CAP面向连接信道连接。
- [L2CAP发起端（Initiator）](../bluetooth_samples/P010_L2CAP信道发起端.md#bluetooth_l2cap_coc_initiator)：发起L2CAP面向连接信道连接并发送数据。

> 译注——源码跟踪：本仓库的[接口头文件](../../../include/zephyr/bluetooth/l2cap.h)与[Host实现](../../../subsys/bluetooth/host)均以相对路径定位。对照时注意网页与本地版本差异；本次没有构建或执行示例。


对应官方文档源码：[doc/services/connectivity/bluetooth/api/l2cap.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/l2cap.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/api/l2cap.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：HCI原始通道](P015_HCI原始通道.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：属性协议](P017_属性协议.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P015_HCI原始通道.md) · [返回大纲](大纲.md) · [下一章](P017_属性协议.md)

</details>

<!-- reading-navigation:end -->
