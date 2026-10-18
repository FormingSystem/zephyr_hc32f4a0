---
id: learning.zephyr-docs.api-file-interface-reference.page-54
title: zephyr__net__ssh__client.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ssh_2client_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_zephyr\_\_net\_\_ssh\_\_client.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ssh_2client_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全Shell（SSH）客户端的API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/net/socket.h>
#include <zephyr/net/ssh/common.h>
```

查看此文件的源码。

安全Shell（SSH）客户端的API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 54.1\_函数（Functions）

<a id="r_ga44a3e816f22b34290374158f4cd8702b"></a>

```c
int ssh_client_start (struct ssh_client *ssh, const char *user_name, const struct net_sockaddr *addr, int host_key_index, ssh_transport_event_callback_t callback, void *user_data)
```

相关声明：[ssh_client_start](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html#ga44a3e816f22b34290374158f4cd8702b)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[ssh_transport_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaed450ebb53a676fafc58bb6cfe82a448)。

启动 SSH 客户端连接（SSH client connection）。

<a id="r_ga4e7daf40096a0494012065cdd8f635a5"></a>

```c
int ssh_client_stop (struct ssh_client *ssh)
```

相关声明：[ssh_client_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html#ga4e7daf40096a0494012065cdd8f635a5)。

停止 SSH 客户端连接。

<a id="r_ga59ee3f15001a09bb7acb780dbbd2bfb4"></a>

```c
int ssh_client_register_transport_callback (struct ssh_transport_conf *conf)
```

相关声明：[ssh_client_register_transport_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html#ga59ee3f15001a09bb7acb780dbbd2bfb4)、[ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)。

注册回调函数，以获取与服务器连接关联的传输对象（transport）。

<a id="r_gacea3dba8b5ae41b94b941607288de66e"></a>

```c
int ssh_client_unregister_transport_callback (struct ssh_transport_conf *conf)
```

相关声明：[ssh_client_unregister_transport_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html#gacea3dba8b5ae41b94b941607288de66e)、[ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)。

注销用于获取与服务器连接关联传输对象的回调函数。

<a id="r_gad5147237b87360043d68f2d91eb12ee5"></a>

```c
struct ssh_client * ssh_transport_get_client (struct ssh_transport *transport)
```

相关声明：[ssh_transport_get_client](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html#gad5147237b87360043d68f2d91eb12ee5)。

获取拥有指定传输对象的 SSH 客户端实例。


## 54.2\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h_source.html)
- [zephyr/net/ssh/common.h](../api_source_architecture_reference/P010_common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P810_client.h_源码浏览.md)
- [ssh_client_start](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html#ga44a3e816f22b34290374158f4cd8702b)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [ssh_transport_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaed450ebb53a676fafc58bb6cfe82a448)
- [ssh_client_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html#ga4e7daf40096a0494012065cdd8f635a5)
- [ssh_client_register_transport_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html#ga59ee3f15001a09bb7acb780dbbd2bfb4)
- [ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)
- [ssh_client_unregister_transport_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html#gacea3dba8b5ae41b94b941607288de66e)
- [ssh_transport_get_client](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html#gad5147237b87360043d68f2d91eb12ee5)

<a id="header-details"></a>

---

[上一章](P053_zephyr__net__socketcan_utils.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P055_zephyr__dt-bindings__gpio__stm32-gpio.h_文件参考.md)
