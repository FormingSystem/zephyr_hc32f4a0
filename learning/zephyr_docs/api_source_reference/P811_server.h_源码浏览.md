---
id: learning.zephyr-docs.api-source-reference.page-811
title: server.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ssh_2server_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第811章\_server.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ssh_2server_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ssh_2server_8h.html)。

## 811.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="foldopen00037"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="agroup__ssh__common_html_gaed450ebb53a676fafc58bb6cfe82a448"></a>
<a id="agroup__ssh__server_html_ga017b274d7604ecca118aab5060bdfd7b"></a>
<a id="agroup__ssh__server_html_ga0ceb09a44c1d659d85f51dc5b842cef6"></a>
<a id="agroup__ssh__server_html_ga38729e64c5c13a3df058fba5481f56cd"></a>
<a id="agroup__ssh__server_html_ga41202a4f05c23393071d71df948fc91d"></a>
<a id="agroup__ssh__server_html_ga72953be174ebb5a948815f49d083105a"></a>
<a id="agroup__ssh__server_html_ga76a0afc5f12f7b3a7133c0e759a0bb25"></a>
<a id="agroup__ssh__server_html_gacd16569ffbf5b87530d27d9eba6229d4"></a>
<a id="agroup__ssh__server_html_gad14ab0c8d54711b60e73ff7d0409b9d9"></a>
<a id="agroup__ssh__server_html_gga38729e64c5c13a3df058fba5481f56cda127d2b9f2843207f6f206147a21b2c29"></a>
<a id="agroup__ssh__server_html_gga38729e64c5c13a3df058fba5481f56cda1eca79d603a6aa92a27eb0e636c34149"></a>
<a id="agroup__ssh__server_html_gga38729e64c5c13a3df058fba5481f56cda85d7f17dcdf41768d7fad6f356a9fc78"></a>
<a id="ainclude_2zephyr_2net_2ssh_2common_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="anet_2socket_8h_html"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="astructssh__server__event__client__connected_html"></a>
<a id="astructssh__server__event__client__connected_html_a1604bdb36cf125554c3355747c0ed2c1"></a>
<a id="astructssh__server__event__client__disconnected_html"></a>
<a id="astructssh__server__event__client__disconnected_html_af11ad585b8a21b1932612bc9c0f16d6d"></a>
<a id="astructssh__server__event_html"></a>
<a id="astructssh__server__event_html_a12c0b1ecce7fb8d50a771c47907909e3"></a>
<a id="astructssh__server__event_html_aa74854d6e2e6e05a5749ea65adb3eb22"></a>
<a id="astructssh__server__event_html_aff11456412dd9833beec1bdc610db868"></a>
<a id="astructssh__transport__conf_html"></a>

```c
/*
 * Copyright (c) 2024 Grant Ramsay <grant.ramsay@hotmail.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_SSH_SERVER_H_
#define ZEPHYR_INCLUDE_NET_SSH_SERVER_H_


#include <zephyr/kernel.h>
#include <zephyr/net/socket.h>
#include <zephyr/net/ssh/common.h>

#ifdef __cplusplus
extern "C" {
#endif


struct ssh_server;


enum ssh_server_event_type {
        SSH_SERVER_EVENT_CLOSED,
        SSH_SERVER_EVENT_CLIENT_CONNECTED,
        SSH_SERVER_EVENT_CLIENT_DISCONNECTED,
};

struct ssh_server_event_client_connected {
        struct ssh_transport *transport;
};

struct ssh_server_event_client_disconnected {
        struct ssh_transport *transport;
};

struct ssh_server_event {
        enum ssh_server_event_type type;

        union {
                struct ssh_server_event_client_connected client_connected;

                struct ssh_server_event_client_disconnected client_disconnected;
        };
};

typedef int (*ssh_server_event_callback_t)(struct ssh_server *sshd,
                                           const struct ssh_server_event *event,
                                           void *user_data);


struct ssh_server *ssh_server_instance(int instance);



int ssh_server_start(struct ssh_server *sshd,
                     const struct net_sockaddr *bind_addr,
                     int host_key_index,
                     const char *username,
                     const char *password,
                     const int *authorized_keys,
                     size_t authorized_keys_len,
                     ssh_server_event_callback_t server_callback,
                     ssh_transport_event_callback_t transport_callback,
                     void *user_data);

int ssh_server_stop(struct ssh_server *sshd);

int ssh_server_transport_close(struct ssh_server *sshd, int idx);

int ssh_server_register_transport_callback(struct ssh_transport_conf *conf);

int ssh_server_unregister_transport_callback(struct ssh_transport_conf *conf);

struct ssh_server *ssh_transport_get_server(struct ssh_transport *transport);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_SSH_SERVER_H_ */
```

## 811.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Grant Ramsay <grant.ramsay@hotmail.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 208 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_SSH_SERVER_H_`。

## 811.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ssh_2server_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [zephyr/net/ssh/common.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h.html)
- [ssh_server_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga38729e64c5c13a3df058fba5481f56cd)
- [SSH_SERVER_EVENT_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#gga38729e64c5c13a3df058fba5481f56cda85d7f17dcdf41768d7fad6f356a9fc78)
- [SSH_SERVER_EVENT_CLIENT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#gga38729e64c5c13a3df058fba5481f56cda1eca79d603a6aa92a27eb0e636c34149)
- [SSH_SERVER_EVENT_CLIENT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#gga38729e64c5c13a3df058fba5481f56cda127d2b9f2843207f6f206147a21b2c29)
- [ssh_server_event_client_connected](../network_service_model_reference/P062_ssh_server_event_client_connected_结构体.md)
- [transport](../network_service_model_reference/P062_ssh_server_event_client_connected_结构体.md#a1604bdb36cf125554c3355747c0ed2c1)
- [ssh_server_event_client_disconnected](../network_service_model_reference/P063_ssh_server_event_client_disconnected_结构体.md)
- [transport](../network_service_model_reference/P063_ssh_server_event_client_disconnected_结构体.md#af11ad585b8a21b1932612bc9c0f16d6d)
- [ssh_server_event](../network_service_model_reference/P061_ssh_server_event_结构体.md)
- [type](../network_service_model_reference/P061_ssh_server_event_结构体.md#aa74854d6e2e6e05a5749ea65adb3eb22)
- [client_connected](../network_service_model_reference/P061_ssh_server_event_结构体.md#a12c0b1ecce7fb8d50a771c47907909e3)
- [client_disconnected](../network_service_model_reference/P061_ssh_server_event_结构体.md#aff11456412dd9833beec1bdc610db868)
- [ssh_server_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga72953be174ebb5a948815f49d083105a)
- [ssh_server_start](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga017b274d7604ecca118aab5060bdfd7b)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [ssh_transport_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaed450ebb53a676fafc58bb6cfe82a448)
- [ssh_server_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga0ceb09a44c1d659d85f51dc5b842cef6)
- [ssh_server_transport_close](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#gacd16569ffbf5b87530d27d9eba6229d4)
- [ssh_server_register_transport_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#gad14ab0c8d54711b60e73ff7d0409b9d9)
- [ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)
- [ssh_server_unregister_transport_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga76a0afc5f12f7b3a7133c0e759a0bb25)
- [ssh_transport_get_server](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga41202a4f05c23393071d71df948fc91d)
- [common.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [ssh_server_event_client_connected::transport](../network_service_model_reference/P062_ssh_server_event_client_connected_结构体.md#a1604bdb36cf125554c3355747c0ed2c1)
- [ssh_server_event_client_disconnected::transport](../network_service_model_reference/P063_ssh_server_event_client_disconnected_结构体.md#af11ad585b8a21b1932612bc9c0f16d6d)
- [ssh_server_event::client_connected](../network_service_model_reference/P061_ssh_server_event_结构体.md#a12c0b1ecce7fb8d50a771c47907909e3)
- [ssh_server_event::type](../network_service_model_reference/P061_ssh_server_event_结构体.md#aa74854d6e2e6e05a5749ea65adb3eb22)
- [ssh_server_event::client_disconnected](../network_service_model_reference/P061_ssh_server_event_结构体.md#aff11456412dd9833beec1bdc610db868)

---

[上一章](P810_client.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P812_st-morpho-header.h_源码浏览.md)
