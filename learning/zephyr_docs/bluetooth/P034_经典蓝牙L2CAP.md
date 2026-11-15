---
id: learning.zephyr-docs.bluetooth.page-34
title: 经典蓝牙L2CAP
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/classic/l2cap_br.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-logical-link-control-and-adaptation-protocol-l2cap-for-br-edr"></a>
<a id="bt-l2cap-br"></a>

# 第34章\_经典蓝牙L2CAP

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/classic/l2cap_br.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

面向基本速率／增强数据速率（Basic Rate/Enhanced Data Rate，BR/EDR）的 L2CAP 提供经典蓝牙（Bluetooth Classic）逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）功能，包括回显（ECHO）请求／响应和无连接数据通道（connectionless data channel）。

<a id="echo-request-response"></a>

## 34.1 回显请求与响应（ECHO Request/Response）

L2CAP 的回显功能通过发送 ECHO 请求、接收 ECHO 响应来测试连接。应用可以注册回调（callback）以监测回显数据包并发送回显数据。通过配置选项 [`CONFIG_BT_CLASSIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CLASSIC) 启用此功能。

<a id="registering-echo-callbacks"></a>

### 34.1.1 注册回显回调（Registering ECHO Callbacks）

要监测 ECHO 请求／响应数据包，注册一个 [`bt_l2cap_br_echo_cb`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__br__echo__cb.html) 回调结构体：

```c
static void echo_req_cb(struct bt_conn *conn, uint8_t identifier, struct net_buf *buf)
{
    /* Handle ECHO request */
}

static void echo_rsp_cb(struct bt_conn *conn, struct net_buf *buf)
{
    /* Handle ECHO response */
}

static struct bt_l2cap_br_echo_cb echo_cb = {
    .req = echo_req_cb,
    .rsp = echo_rsp_cb,
};

bt_l2cap_br_echo_cb_register(&echo_cb);
```

<a id="sending-echo-request"></a>

### 34.1.2 发送回显请求（Sending ECHO Request）

发送 ECHO 请求时，分配缓冲区，并为 L2CAP 头部预留 [`BT_L2CAP_BR_ECHO_REQ_RESERVE`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga12c146741591a55dc50d7d07f0755daa) 字节：

```c
struct net_buf *buf;

buf = net_buf_alloc(&pool, K_FOREVER);
net_buf_reserve(buf, BT_L2CAP_BR_ECHO_REQ_RESERVE);
net_buf_add_mem(buf, data, data_len);

bt_l2cap_br_echo_req(conn, buf);
```

<a id="sending-echo-response"></a>

### 34.1.3 发送回显响应（Sending ECHO Response）

发送 ECHO 响应时（通常用于应答收到的 ECHO 请求），分配缓冲区，并为 L2CAP 头部预留 [`BT_L2CAP_BR_ECHO_RSP_RESERVE`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga2961971c1f80aa6168f6cd47b991bf4d) 字节：

```c
struct net_buf *buf;

buf = net_buf_alloc(&pool, K_FOREVER);
net_buf_reserve(buf, BT_L2CAP_BR_ECHO_RSP_RESERVE);
net_buf_add_mem(buf, data, data_len);

bt_l2cap_br_echo_rsp(conn, buf);
```

> 译注——原示例参数遗漏：上方代码保持官网原样，但当前官方头文件声明为 `int bt_l2cap_br_echo_rsp(struct bt_conn *conn, uint8_t identifier, struct net_buf *buf);`。实际调用应传入收到请求时的标识符，即 `bt_l2cap_br_echo_rsp(conn, identifier, buf)`。可跟踪本仓库[头文件](../../../include/zephyr/bluetooth/classic/l2cap_br.h)，并对照[本次读取的官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/bluetooth/classic/l2cap_br.h)；版本差异以实际编译所用声明为准。上述片段中的 `pool`、`data`、`data_len` 和 `conn` 还需要应用提供，不是完整可编译程序。

`identifier` 参数必须与收到的 ECHO 请求中的标识符（identifier）一致，才能正确关联请求和响应。

<a id="connectionless-data-channel"></a>

## 34.2 无连接数据通道（Connectionless Data Channel）

无连接数据通道允许向指定协议／服务复用器（Protocol/Service Multiplexer，PSM）发送数据或从中接收数据，无需建立面向连接的 L2CAP 通道。通过配置选项 [`CONFIG_BT_L2CAP_CONNLESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_CONNLESS) 启用此功能。

<a id="registering-connectionless-callbacks"></a>

### 34.2.1 注册无连接回调（Registering Connectionless Callbacks）

要接收无连接数据，注册一个 [`bt_l2cap_br_connless_cb`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__br__connless__cb.html) 回调结构体：

```c
static void connless_recv_cb(struct bt_conn *conn, uint16_t psm, struct net_buf *buf)
{
    /* Handle received connectionless data */
}

static struct bt_l2cap_br_connless_cb connless_cb = {
    .psm = MY_PSM,  /* Or 0 to receive all */
    .sec_level = BT_SECURITY_L1,
    .recv = connless_recv_cb,
};

bt_l2cap_br_connless_register(&connless_cb);
```

<a id="sending-connectionless-data"></a>

### 34.2.2 发送无连接数据（Sending Connectionless Data）

发送无连接数据时，分配缓冲区并预留 [`BT_L2CAP_CONNLESS_RESERVE`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#gac0c4332fa7020bdc52a4431c6a506524) 字节：

```c
struct net_buf *buf;

buf = net_buf_alloc(&pool, K_FOREVER);
net_buf_reserve(buf, BT_L2CAP_CONNLESS_RESERVE);
net_buf_add_mem(buf, data, data_len);

bt_l2cap_br_connless_send(conn, psm, buf);
```

<a id="api-reference"></a>

## 34.3 API 参考（API Reference）

[BR/EDR 逻辑链路控制与适配协议（L2CAP） API 参考](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html)。


对应官方文档源码：[doc/services/connectivity/bluetooth/api/classic/l2cap_br.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/classic/l2cap_br.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/api/classic/l2cap_br.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：免提配置文件HFP](P033_免提配置文件HFP.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：串口仿真RFCOMM](P035_串口仿真RFCOMM.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P033_免提配置文件HFP.md) · [返回大纲](大纲.md) · [下一章](P035_串口仿真RFCOMM.md)

</details>

<!-- reading-navigation:end -->
