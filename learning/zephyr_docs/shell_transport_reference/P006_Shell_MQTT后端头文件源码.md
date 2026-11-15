---
id: learning.zephyr-docs.shell-transport-reference.page-6
title: Shell_MQTT后端头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__mqtt_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_Shell\_MQTT后端头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__mqtt_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P005_Shell_MQTT后端头文件参考.md)和[公共接口](P004_Shell_MQTT后端接口.md)；访问语义和生命周期见本页译注。

## 6.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00129"></a>
<a id="aconn__mgr__monitor_8h_html"></a>
<a id="agroup__mcumgr__callback__api_html_gae61f705224a859776ee5161dfda5ed7d"></a>
<a id="agroup__shell__api_html_ga265807c2d8eba7b9ea633968627e085d"></a>
<a id="agroup__shell__mqtt_html_ga96c08138bf623c1b6ddabfb3742f6f18"></a>
<a id="agroup__shell__mqtt_html_gac3adcf640952f93e747c303724fc31bb"></a>
<a id="akernel_8h_html"></a>
<a id="amqtt_8h_html"></a>
<a id="anet_2socket_8h_html"></a>
<a id="anet__event_8h_html"></a>
<a id="anet__mgmt_8h_html"></a>
<a id="aring__buffer_8h_html"></a>
<a id="ashell_2shell_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructshell__transport__api_html"></a>
<a id="astructshell_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2022 G-Technologies Sdn. Bhd.
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_MQTT_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_MQTT_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;zephyr/kernel.h&gt;
<a id="l00017"></a>#include &lt;zephyr/shell/shell.h&gt;
<a id="l00018"></a>#include &lt;zephyr/net/socket.h&gt;
<a id="l00019"></a>#include &lt;zephyr/net/net_mgmt.h&gt;
<a id="l00020"></a>#include &lt;zephyr/net/net_event.h&gt;
<a id="l00021"></a>#include &lt;zephyr/net/conn_mgr_monitor.h&gt;
<a id="l00022"></a>#include &lt;zephyr/net/mqtt.h&gt;
<a id="l00023"></a>#include &lt;zephyr/sys/ring_buffer.h&gt;
<a id="l00024"></a>
<a id="l00025"></a>#ifdef __cplusplus
<a id="l00026"></a>extern "C" {
<a id="l00027"></a>#endif
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>#define RX_RB_SIZE CONFIG_SHELL_MQTT_RX_BUF_SIZE
<a id="l00032"></a>#define TX_BUF_SIZE CONFIG_SHELL_MQTT_TX_BUF_SIZE
<a id="l00033"></a>#define SH_MQTT_BUFFER_SIZE 64
<a id="l00034"></a>#define DEVICE_ID_BIN_MAX_SIZE 3
<a id="l00035"></a>#define DEVICE_ID_HEX_MAX_SIZE ((DEVICE_ID_BIN_MAX_SIZE * 2) + 1)
<a id="l00036"></a>#define SH_MQTT_TOPIC_RX_MAX_SIZE DEVICE_ID_HEX_MAX_SIZE + sizeof(CONFIG_SHELL_MQTT_TOPIC_RX_ID)
<a id="l00037"></a>#define SH_MQTT_TOPIC_TX_MAX_SIZE DEVICE_ID_HEX_MAX_SIZE + sizeof(CONFIG_SHELL_MQTT_TOPIC_TX_ID)
<a id="l00038"></a>
<a id="l00039"></a>extern const struct shell_transport_api shell_mqtt_transport_api;
<a id="l00040"></a>
<a id="l00041"></a>struct shell_mqtt_tx_buf {
<a id="l00043"></a>        char buf[TX_BUF_SIZE];
<a id="l00044"></a>
<a id="l00046"></a>        uint16_t len;
<a id="l00047"></a>};
<a id="l00048"></a>
<a id="l00050"></a>struct shell_mqtt {
<a id="l00051"></a>        char device_id[DEVICE_ID_HEX_MAX_SIZE];
<a id="l00052"></a>        char sub_topic[SH_MQTT_TOPIC_RX_MAX_SIZE];
<a id="l00053"></a>        char pub_topic[SH_MQTT_TOPIC_TX_MAX_SIZE];
<a id="l00054"></a>
<a id="l00056"></a>        shell_transport_handler_t shell_handler;
<a id="l00057"></a>
<a id="l00058"></a>        struct ring_buf rx_rb;
<a id="l00059"></a>        uint8_t rx_rb_buf[RX_RB_SIZE];
<a id="l00060"></a>        uint8_t *rx_rb_ptr;
<a id="l00061"></a>
<a id="l00062"></a>        struct shell_mqtt_tx_buf tx_buf;
<a id="l00063"></a>
<a id="l00065"></a>        void *shell_context;
<a id="l00066"></a>
<a id="l00068"></a>        struct mqtt_client mqtt_cli;
<a id="l00069"></a>
<a id="l00070"></a>        /* Buffers for MQTT client. */
<a id="l00071"></a>        struct buffer {
<a id="l00072"></a>                uint8_t rx[SH_MQTT_BUFFER_SIZE];
<a id="l00073"></a>                uint8_t tx[SH_MQTT_BUFFER_SIZE];
<a id="l00074"></a>        } buf;
<a id="l00075"></a>
<a id="l00076"></a>        struct k_mutex lock;
<a id="l00077"></a>
<a id="l00079"></a>        struct net_sockaddr_storage broker;
<a id="l00080"></a>
<a id="l00081"></a>        struct zsock_addrinfo *haddr;
<a id="l00082"></a>        struct zsock_pollfd fds[1];
<a id="l00083"></a>        int nfds;
<a id="l00084"></a>
<a id="l00085"></a>        struct mqtt_publish_param pub_data;
<a id="l00086"></a>
<a id="l00087"></a>        struct net_mgmt_event_callback mgmt_cb;
<a id="l00088"></a>
<a id="l00090"></a>        struct k_work_q workq;
<a id="l00091"></a>        struct k_work net_disconnected_work;
<a id="l00092"></a>        struct k_work_delayable connect_dwork;
<a id="l00093"></a>        struct k_work_delayable subscribe_dwork;
<a id="l00094"></a>        struct k_work_delayable process_dwork;
<a id="l00095"></a>        struct k_work_delayable publish_dwork;
<a id="l00096"></a>
<a id="l00098"></a>        enum sh_mqtt_transport_state {
<a id="l00099"></a>                SHELL_MQTT_TRANSPORT_DISCONNECTED,
<a id="l00100"></a>                SHELL_MQTT_TRANSPORT_CONNECTED,
<a id="l00101"></a>        } transport_state;
<a id="l00102"></a>
<a id="l00104"></a>        enum sh_mqtt_subscribe_state {
<a id="l00105"></a>                SHELL_MQTT_NOT_SUBSCRIBED,
<a id="l00106"></a>                SHELL_MQTT_SUBSCRIBED,
<a id="l00107"></a>        } subscribe_state;
<a id="l00108"></a>
<a id="l00110"></a>        enum sh_mqtt_network_state {
<a id="l00111"></a>                SHELL_MQTT_NETWORK_DISCONNECTED,
<a id="l00112"></a>                SHELL_MQTT_NETWORK_CONNECTED,
<a id="l00113"></a>        } network_state;
<a id="l00114"></a>};
<a id="l00116"></a>
<a id="l00123"></a>
<a id="l00129"></a>#define SHELL_MQTT_DEFINE(_name)                                                                   \
<a id="l00130"></a>        static struct shell_mqtt _name##_shell_mqtt;                                               \
<a id="l00131"></a>        struct shell_transport _name = { .api = &amp;shell_mqtt_transport_api,                         \
<a id="l00132"></a>                                         .ctx = (struct shell_mqtt *)&amp;_name##_shell_mqtt }
<a id="l00133"></a>
<a id="l00142"></a>const struct shell *shell_backend_mqtt_get_ptr(void);
<a id="l00143"></a>
<a id="l00156"></a>bool shell_mqtt_get_devid(char *id, int id_max_len);
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00160"></a>#ifdef __cplusplus
<a id="l00161"></a>}
<a id="l00162"></a>#endif
<a id="l00163"></a>
<a id="l00164"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_MQTT_H_ */
</code></pre>

## 6.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2022 G-Technologies Sdn. Bhd.；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. MQTT客户端（Client）使用的缓冲区。

3. ZEPHYR_INCLUDE_SHELL_SHELL_MQTT_H_头文件包含保护结束。

## 6.3\_原页符号提示（Symbol Descriptions）

### `conn_mgr_monitor.h`

用于监测网络连接与接口（Network Connections and Interfaces）的API。

符号定位：[conn_mgr_monitor.h](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__monitor_8h.html)。

### `mgmt_cb`

```c
enum mgmt_cb_return(* mgmt_cb)(uint32_t event, enum mgmt_cb_return prev_status, int32_t *rc, uint16_t *group, bool *abort_more, void *data, size_t data_size)
```

收到管理通知或事件（MGMT Notification/Event）时调用的函数。

定义位置（Definition）：callbacks.h:75。

符号定位：[mgmt_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gae61f705224a859776ee5161dfda5ed7d)。

### `shell_transport_handler_t`

```c
void(* shell_transport_handler_t)(enum shell_transport_evt evt, void *context)
```

Shell传输事件处理回调（Transport Event Handler Callback）。

定义位置（Definition）：shell.h:831。

符号定位：[shell_transport_handler_t](../shell_core_reference/P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)。

### `shell_mqtt_get_devid`

```c
bool shell_mqtt_get_devid(char *id, int id_max_len)
```

定义设备标识符（Device ID，devid）的函数；Shell MQTT后端将其作为客户端标识符……（原符号提示在此截断）

符号定位：[shell_mqtt_get_devid](P004_Shell_MQTT后端接口.md#ga96c08138bf623c1b6ddabfb3742f6f18)。

### `shell_backend_mqtt_get_ptr`

```c
const struct shell * shell_backend_mqtt_get_ptr(void)
```

此函数提供Shell MQTT后端实例的指针。

符号定位：[shell_backend_mqtt_get_ptr](P004_Shell_MQTT后端接口.md#gac3adcf640952f93e747c303724fc31bb)。

### `kernel.h`

公共内核 API（Public Kernel APIs）。

符号定位：[kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)。

### `mqtt.h`

MQTT客户端实现（MQTT Client Implementation）。

符号定位：[mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h.html)。

### `socket.h`

兼容BSD套接字（BSD Sockets）的API定义。

符号定位：[socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)。

### `net_event.h`

网络事件代码（Network Events）的公共头文件。

符号定位：[net_event.h](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h.html)。

### `net_mgmt.h`

网络管理API（Network Management API）的公共头文件。

符号定位：[net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)。

### `ring_buffer.h`

简单的纯头文件环形缓冲区（Ring Buffer）实现。

符号定位：[ring_buffer.h](../ringbuffer_reference/P003_环形缓冲区头文件参考.md)。

### `shell.h`

Shell子系统（Shell Subsystem）的头文件。

符号定位：[shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

### `shell_transport_api`

统一的Shell传输接口（Transport Interface）。

定义位置（Definition）：shell.h:864。

符号定位：[shell_transport_api](../shell_core_reference/P010_Shell传输接口结构.md)。

### `shell`

Shell实例内部结构（Instance Internals）。

定义位置（Definition）：shell.h:1129。

符号定位：[shell](../shell_core_reference/P004_Shell实例结构.md)。

## 6.4\_源码跟踪译注

> 译注——默认弱函数通过硬件信息接口（Hardware Information）取得二进制设备编号，再用bin2hex转为十六进制文本。默认实现失败时返回false；当前后端初始化随后使用dummy作为替代编号。需要设备间不同的客户端编号时，应结合实际硬件信息或覆盖函数的行为核对。

> 译注——官方接口说明使用devid_tx和devid_rx描述主题。当前实现将设备编号分别与CONFIG_SHELL_MQTT_TOPIC_TX_ID和CONFIG_SHELL_MQTT_TOPIC_RX_ID拼接，因此实际后缀由配置决定。get_devid返回true仅表示形成了非空编号，不表示已连接代理或订阅成功。

头文件定位：[include/zephyr/shell/shell_mqtt.h](../../../include/zephyr/shell/shell_mqtt.h)，关联实现／接口：[subsys/shell/backends/shell_mqtt.c](../../../subsys/shell/backends/shell_mqtt.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_mqtt.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/shell_mqtt.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 6.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P005_Shell_MQTT后端头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/shell/shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [zephyr/net/net_event.h](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h.html)
- [zephyr/net/conn_mgr_monitor.h](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__monitor_8h.html)
- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h.html)
- [zephyr/sys/ring_buffer.h](../ringbuffer_reference/P003_环形缓冲区头文件参考.md)
- [shell_transport_api](../shell_core_reference/P010_Shell传输接口结构.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [shell_transport_handler_t](../shell_core_reference/P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mgmt_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gae61f705224a859776ee5161dfda5ed7d)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_backend_mqtt_get_ptr](P004_Shell_MQTT后端接口.md#gac3adcf640952f93e747c303724fc31bb)
- [shell_mqtt_get_devid](P004_Shell_MQTT后端接口.md#ga96c08138bf623c1b6ddabfb3742f6f18)

---

[上一章](P005_Shell_MQTT后端头文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_Shell_Telnet后端接口.md)
