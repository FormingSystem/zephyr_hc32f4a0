---
id: learning.zephyr-docs.api-file-display-management-reference.page-12
title: zephyr__mgmt__mcumgr__transport__smp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_mgmt\_\_mcumgr\_\_transport\_\_smp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel.h>
#include <zcbor_common.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.1\_数据结构（Data Structures）

<a id="r_smp_5Ftransport_5Fapi_5Ft"></a>

```c
struct smp_transport_api_t
```

相关声明：[smp_transport_api_t](../system_service_model_reference/P082_smp_transport_api_t_结构体.md)。

简单管理协议（SMP）传输函数的函数指针；处理函数为NULL表示不支持或尚未实现。

<a id="r_smp_5Ftransport"></a>

```c
struct smp_transport
```

相关声明：[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)。

用于发送简单管理协议（SMP）响应的传输对象。

<a id="r_smp_5Ftransport_5Fbridge"></a>

```c
struct smp_transport_bridge
```

相关声明：[smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)。

桥接传输（Bridged Transport）的上下文。

<a id="r_smp_5Fclient_5Ftransport_5Fentry"></a>

```c
struct smp_client_transport_entry
```

相关声明：[smp_client_transport_entry](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md)。

简单管理协议（SMP）的客户端传输结构。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 12.2\_类型定义（Typedefs）

<a id="r_ga4da3579b031ba6a90448ad9248f52155"></a>

```c
typedef int(* smp_transport_out_fn) (struct net_buf *nb)
```

相关声明：[smp_transport_out_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga4da3579b031ba6a90448ad9248f52155)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

SMP 传输层发送回调（Transmit Callback）。

<a id="r_ga2085e89b99428a61596d90e084d7c5e2"></a>

```c
typedef uint16_t(* smp_transport_get_mtu_fn) (const struct net_buf *nb)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[smp_transport_get_mtu_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga2085e89b99428a61596d90e084d7c5e2)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

SMP 传输层最大传输单元查询回调（MTU Query Callback）。

<a id="r_ga840da7e00d590459b656dcbe0dd6f6f4"></a>

```c
typedef int(* smp_transport_ud_copy_fn) (struct net_buf *dst, const struct net_buf *src)
```

相关声明：[smp_transport_ud_copy_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga840da7e00d590459b656dcbe0dd6f6f4)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

SMP `user_data` 复制回调（Copy Callback）。

<a id="r_ga0f249aa3fed3044d9bad811e92e4135c"></a>

```c
typedef void(* smp_transport_ud_free_fn) (void *ud)
```

相关声明：[smp_transport_ud_free_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga0f249aa3fed3044d9bad811e92e4135c)。

SMP `user_data` 释放回调（Free Callback）。

<a id="r_ga77d54c0bd6afc69f73613575b671e089"></a>

```c
typedef bool(* smp_transport_query_valid_check_fn) (struct net_buf *nb, void *arg)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_transport_query_valid_check_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga77d54c0bd6afc69f73613575b671e089)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

用于检查排队数据是否仍然有效的函数（Queued Data Validation）。

<a id="r_ga095edd916780b458e8cbd701969c0640"></a>

```c
typedef void(* smp_transport_ud_req_init_fn) (struct net_buf *nb, void *priv)
```

相关声明：[smp_transport_ud_req_init_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga095edd916780b458e8cbd701969c0640)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

SMP 请求缓冲区初始化（Init Request Buffer）。

<a id="r_ga032db1c1b6f4d4212e6dc67fbd28c115"></a>

```c
typedef bool(* smp_transport_bridge_connect_fn) (struct smp_transport_bridge *bridge, bool direction, uint32_t mode, bool same_transport, zcbor_state_t *input_data, zcbor_state_t *output_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_transport_bridge_connect_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga032db1c1b6f4d4212e6dc67fbd28c115)、[smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

SMP 传输桥接连接（Transport Bridge Connect）。

<a id="r_ga50fcdcef18ae4c937ced9f323715e1e1"></a>

```c
typedef void(* smp_transport_bridge_disconnect_fn) (struct smp_transport_bridge *bridge, bool direction)
```

相关声明：[smp_transport_bridge_disconnect_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga50fcdcef18ae4c937ced9f323715e1e1)、[smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

SMP 传输桥接断开（Transport Bridge Disconnect）。

<a id="r_gadadf97eb50e871f5942b4774c643eba2"></a>

```c
typedef int(* smp_transport_bridge_out_fn) (const struct smp_transport_bridge *bridge, struct net_buf *nb, bool direction)
```

相关声明：[smp_transport_bridge_out_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gadadf97eb50e871f5942b4774c643eba2)、[smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

SMP 传输桥接输出数据（Transport Bridge Output Data）。

<a id="r_ga477587b2b514bdc74560c5ab94ff792a"></a>

```c
typedef bool(* mgmt_client_transport_cb_t) (const struct smp_client_transport_entry *transport, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mgmt_client_transport_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga477587b2b514bdc74560c5ab94ff792a)、[smp_client_transport_entry](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md)。

SMP 客户端传输回调（Client Transport Callback）。

<a id="r_ga4570f81d545ae51e68f5a2c3ede4f170"></a>

```c
typedef bool(* smp_transport_bridge_modes_fn) (zcbor_state_t *output_data, int *rc)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_transport_bridge_modes_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga4570f81d545ae51e68f5a2c3ede4f170)。

SMP 传输桥接详情（Transport Bridge Details）。

<a id="r_ga0d8277e9da18c896749e2392c7ea1ac7"></a>

```c
typedef bool(* smp_transport_bridge_config_details_fn) (uint32_t mode, zcbor_state_t *output_data, int *rc)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_transport_bridge_config_details_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga0d8277e9da18c896749e2392c7ea1ac7)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

SMP 传输桥接配置详情（Transport Bridge Config Details）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.3\_枚举（Enumerations）

<a id="r_ga5d886a11df0c49ca18e23e246ab2fab9"></a>

```c
enum smp_transport_type { SMP_SERIAL_TRANSPORT = 0 , SMP_RAW_SERIAL_TRANSPORT , SMP_BLUETOOTH_TRANSPORT , SMP_SHELL_TRANSPORT , SMP_UDP_IPV4_TRANSPORT , SMP_UDP_IPV6_TRANSPORT , SMP_LORAWAN_TRANSPORT , SMP_SPI_TRANSPORT , SMP_USER_DEFINED_TRANSPORT = 64 }
```

相关声明：[smp_transport_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga5d886a11df0c49ca18e23e246ab2fab9)、[SMP_SERIAL_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9ab1660bb2a08be903905358e410761342)、[SMP_RAW_SERIAL_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9a06953c39575f3903299011cde915ac13)、[SMP_BLUETOOTH_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9a952714e2058663eb43695a9a3b65dcbe)、[SMP_SHELL_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9a71731051dadd60e06afe426da4ed7b43)、[SMP_UDP_IPV4_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9adc8f1680bea910f7daaf191f3f07b74f)、[SMP_UDP_IPV6_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9a1fbca254a684aac8d15c8b067aa994f7)、[SMP_LORAWAN_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9addcf3d287f359bad85104d2a37b4e5c8)、[SMP_SPI_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9a3de5af5fe47980cdf749abc1694d84eb)、[SMP_USER_DEFINED_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9aa25faa37d758689aa33a3c7d1320b863)。

用于客户端注册（Client Registration）的 SMP 传输类型（Transport Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.4\_函数（Functions）

<a id="r_gaf275034765327b52b900046d71c411ee"></a>

```c
int smp_transport_init (struct smp_transport *smpt)
```

相关声明：[smp_transport_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gaf275034765327b52b900046d71c411ee)、[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)。

初始化 Zephyr SMP 传输对象（Transport Object）。

<a id="r_ga87ccc623b5907d7d65b24ed99bd57ec5"></a>

```c
void smp_rx_remove_invalid (struct smp_transport *zst, void *arg)
```

相关声明：[smp_rx_remove_invalid](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga87ccc623b5907d7d65b24ed99bd57ec5)、[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)。

移除某个 SMP 传输中已不再有效的排队请求（Queued Requests）。

<a id="r_ga662f893037193923610de1e8793fd971"></a>

```c
void smp_rx_clear (struct smp_transport *zst)
```

相关声明：[smp_rx_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga662f893037193923610de1e8793fd971)、[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)。

清除某个 SMP 传输中待处理的排队请求（Pending Queued Requests）。

<a id="r_gafb488cd9854b74c8e5802db3c8fe6116"></a>

```c
void smp_client_transport_register (struct smp_client_transport_entry *entry)
```

相关声明：[smp_client_transport_register](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gafb488cd9854b74c8e5802db3c8fe6116)、[smp_client_transport_entry](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md)。

为客户端注册 Zephyr SMP 传输对象（Transport Object）。

<a id="r_ga67c3481cdc81c20e0c35b4eaa185619e"></a>

```c
struct smp_transport * smp_client_transport_get (int smpt_type)
```

相关声明：[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)、[smp_client_transport_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga67c3481cdc81c20e0c35b4eaa185619e)。

查找已注册的 SMP 传输客户端对象（Transport Client Object）。

<a id="r_gae2531ab1dba2992b8465cd49349c5116"></a>

```c
bool smp_client_transport_foreach (mgmt_client_transport_cb_t user_cb, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_client_transport_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gae2531ab1dba2992b8465cd49349c5116)、[mgmt_client_transport_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga477587b2b514bdc74560c5ab94ff792a)。

遍历 SMP 客户端／传输对象（Clients/Transports）。


## 12.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [查看此文件的源码。](../api_source_system_reference/P018_smp.h_源码浏览.md)
- [smp_transport_api_t](../system_service_model_reference/P082_smp_transport_api_t_结构体.md)
- [smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)
- [smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)
- [smp_client_transport_entry](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md)
- [smp_transport_out_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga4da3579b031ba6a90448ad9248f52155)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [smp_transport_get_mtu_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga2085e89b99428a61596d90e084d7c5e2)
- [smp_transport_ud_copy_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga840da7e00d590459b656dcbe0dd6f6f4)
- [smp_transport_ud_free_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga0f249aa3fed3044d9bad811e92e4135c)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [smp_transport_query_valid_check_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga77d54c0bd6afc69f73613575b671e089)
- [smp_transport_ud_req_init_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga095edd916780b458e8cbd701969c0640)
- [smp_transport_bridge_connect_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga032db1c1b6f4d4212e6dc67fbd28c115)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [smp_transport_bridge_disconnect_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga50fcdcef18ae4c937ced9f323715e1e1)
- [smp_transport_bridge_out_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gadadf97eb50e871f5942b4774c643eba2)
- [mgmt_client_transport_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga477587b2b514bdc74560c5ab94ff792a)
- [smp_transport_bridge_modes_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga4570f81d545ae51e68f5a2c3ede4f170)
- [smp_transport_bridge_config_details_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga0d8277e9da18c896749e2392c7ea1ac7)
- [smp_transport_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga5d886a11df0c49ca18e23e246ab2fab9)
- [SMP_SERIAL_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9ab1660bb2a08be903905358e410761342)
- [SMP_RAW_SERIAL_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9a06953c39575f3903299011cde915ac13)
- [SMP_BLUETOOTH_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9a952714e2058663eb43695a9a3b65dcbe)
- [SMP_SHELL_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9a71731051dadd60e06afe426da4ed7b43)
- [SMP_UDP_IPV4_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9adc8f1680bea910f7daaf191f3f07b74f)
- [SMP_UDP_IPV6_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9a1fbca254a684aac8d15c8b067aa994f7)
- [SMP_LORAWAN_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9addcf3d287f359bad85104d2a37b4e5c8)
- [SMP_SPI_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9a3de5af5fe47980cdf749abc1694d84eb)
- [SMP_USER_DEFINED_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9aa25faa37d758689aa33a3c7d1320b863)
- [smp_transport_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gaf275034765327b52b900046d71c411ee)
- [smp_rx_remove_invalid](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga87ccc623b5907d7d65b24ed99bd57ec5)
- [smp_rx_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga662f893037193923610de1e8793fd971)
- [smp_client_transport_register](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gafb488cd9854b74c8e5802db3c8fe6116)
- [smp_client_transport_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga67c3481cdc81c20e0c35b4eaa185619e)
- [smp_client_transport_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gae2531ab1dba2992b8465cd49349c5116)

---

[上一章](P011_zephyr__mgmt__mcumgr__smp__smp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__bluetooth__audio__micp.h_文件参考.md)
