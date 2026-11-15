---
id: learning.zephyr-docs.api-source-reference.page-810
title: client.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ssh_2client_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第810章\_client.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ssh_2client_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ssh_2client_8h.html)。

## 810.1\_原始可见代码（Source Code）

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
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="agroup__ssh__client_html_ga44a3e816f22b34290374158f4cd8702b"></a>
<a id="agroup__ssh__client_html_ga4e7daf40096a0494012065cdd8f635a5"></a>
<a id="agroup__ssh__client_html_ga59ee3f15001a09bb7acb780dbbd2bfb4"></a>
<a id="agroup__ssh__client_html_gacea3dba8b5ae41b94b941607288de66e"></a>
<a id="agroup__ssh__client_html_gad5147237b87360043d68f2d91eb12ee5"></a>
<a id="agroup__ssh__common_html_gaed450ebb53a676fafc58bb6cfe82a448"></a>
<a id="ainclude_2zephyr_2net_2ssh_2common_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="anet_2socket_8h_html"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="astructssh__transport__conf_html"></a>

```c
/*
 * Copyright (c) 2024 Grant Ramsay <grant.ramsay@hotmail.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_SSH_CLIENT_H_
#define ZEPHYR_INCLUDE_NET_SSH_CLIENT_H_


#include <zephyr/kernel.h>
#include <zephyr/net/socket.h>
#include <zephyr/net/ssh/common.h>

#ifdef __cplusplus
extern "C" {
#endif


struct ssh_client;

struct ssh_client *ssh_client_instance(int instance);


int ssh_client_start(struct ssh_client *ssh,
                     const char *user_name,
                     const struct net_sockaddr *addr,
                     int host_key_index,
                     ssh_transport_event_callback_t callback,
                     void *user_data);

int ssh_client_stop(struct ssh_client *ssh);

int ssh_client_register_transport_callback(struct ssh_transport_conf *conf);

int ssh_client_unregister_transport_callback(struct ssh_transport_conf *conf);

struct ssh_client *ssh_transport_get_client(struct ssh_transport *transport);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_SSH_CLIENT_H_ */
```

## 810.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Grant Ramsay <grant.ramsay@hotmail.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 121 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_SSH_CLIENT_H_`。

## 810.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ssh_2client_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [zephyr/net/ssh/common.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h.html)
- [ssh_client_start](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html#ga44a3e816f22b34290374158f4cd8702b)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [ssh_transport_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaed450ebb53a676fafc58bb6cfe82a448)
- [ssh_client_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html#ga4e7daf40096a0494012065cdd8f635a5)
- [ssh_client_register_transport_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html#ga59ee3f15001a09bb7acb780dbbd2bfb4)
- [ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)
- [ssh_client_unregister_transport_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html#gacea3dba8b5ae41b94b941607288de66e)
- [ssh_transport_get_client](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html#gad5147237b87360043d68f2d91eb12ee5)
- [common.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)

---

[上一章](P809_ssd16xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P811_server.h_源码浏览.md)
