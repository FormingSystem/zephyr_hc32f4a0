---
id: learning.zephyr-docs.modem-wireless-model-reference.page-71
title: st87mxx_wifiscan_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structst87mxx__wifiscan__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_st87mxx\_wifiscan\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structst87mxx__wifiscan__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ST87Mxx Wi-Fi扫描操作（Scan Operation）的参数。

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

<a id="details"></a>

ST87Mxx Wi-Fi 扫描操作的参数。此结构体保存执行 Wi-Fi 扫描所需的全部相关参数，包括信道列表、扫描轮数、信标数据回调和超时时间。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 71.1\_数据成员（Data Fields）

<a id="r_a0164e513719020494343e3dd0c36dd44"></a>

```c
char * channel_list
```

相关声明：[channel_list](#a0164e513719020494343e3dd0c36dd44)。

指向 Wi-Fi 信道字符串列表的指针，信道范围为 1 至 14，例如下列列表。

<a id="r_a8f3c22343e1cbdc1f35f98456e0d98fb"></a>

```c
uint32_t nb_scan_iterations
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[nb_scan_iterations](#a8f3c22343e1cbdc1f35f98456e0d98fb)。

遍历信道列表进行扫描的次数。

<a id="r_a19622385234cf2d09ef29c4b478e9d3d"></a>

```c
st87mxx_get_beacon_data_callback_t * get_beacon_data_callback_func
```

相关声明：[st87mxx_get_beacon_data_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga36695a0b14a8ac128692a3a543a2e1b1)、[get_beacon_data_callback_func](#a19622385234cf2d09ef29c4b478e9d3d)。

指向回调函数的指针，每当信标（beacon）数据可用时调用。

<a id="r_a12e93569611996ca3e14906f1cc2103c"></a>

```c
uint32_t timeout
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timeout](#a12e93569611996ca3e14906f1cc2103c)。

超时时间，单位为秒。

## 71.2\_详细说明（Detailed Documentation）

<a id="a0164e513719020494343e3dd0c36dd44"></a>

### `channel_list`

```c
char* st87mxx_wifiscan_params::channel_list
```

指向 Wi-Fi 信道字符串列表的指针，信道范围为 1 至 14，例如下列列表。

`"1,6,11"`。

<a id="a19622385234cf2d09ef29c4b478e9d3d"></a>

### `get_beacon_data_callback_func`

```c
st87mxx_get_beacon_data_callback_t* st87mxx_wifiscan_params::get_beacon_data_callback_func
```

指向回调函数的指针，每当信标（beacon）数据可用时调用。

信标格式为：信道编号、接收电平（RxLevel）、MAC 地址（BSSID）和 SSID 名称。

<a id="a8f3c22343e1cbdc1f35f98456e0d98fb"></a>

### `nb_scan_iterations`

```c
uint32_t st87mxx_wifiscan_params::nb_scan_iterations
```

遍历信道列表进行扫描的次数。

值为 0 表示系统将无限循环运行。

<a id="a12e93569611996ca3e14906f1cc2103c"></a>

### `timeout`

```c
uint32_t st87mxx_wifiscan_params::timeout
```

超时时间，单位为秒。

超时后取消请求。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/st87mxx_app_services.h`

## 71.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/st87mxx_app_services.h](https://docs.zephyrproject.org/latest/doxygen/html/st87mxx__app__services_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [st87mxx_get_beacon_data_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga36695a0b14a8ac128692a3a543a2e1b1)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P070_sim7080_ue_sys_info_lte_结构体.md) · [返回大纲](大纲.md)
