---
id: learning.zephyr-docs.network-core-model-reference.page-180
title: wifi_ps_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__ps__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第180章\_wifi\_ps\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__ps__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi省电配置（Power Save Configuration）。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi省电配置（Power Save Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 180.1\_数据成员（Data Fields）

<a id="r_a9e83c10eaaa1d721cbc49b40aedb00df"></a>

```c
char num_twt_flows
```

相关声明：[num_twt_flows](#a9e83c10eaaa1d721cbc49b40aedb00df)。

目标唤醒时间流数量（Number of TWT flows）。

<a id="r_ab7460f0f253b2d552e49e98e2c770967"></a>

```c
struct wifi_twt_flow_info twt_flows [WIFI_MAX_TWT_FLOWS]
```

相关声明：[wifi_twt_flow_info](P188_wifi_twt_flow_info_结构体.md)、[twt_flows](#ab7460f0f253b2d552e49e98e2c770967)。

目标唤醒时间流详情（TWT flow details）。

<a id="r_a357aafc2dedda37755b1cb1fc07fe5a6"></a>

```c
struct wifi_ps_params ps_params
```

相关声明：[wifi_ps_params](P181_wifi_ps_params_结构体.md)、[ps_params](#a357aafc2dedda37755b1cb1fc07fe5a6)。

省电配置（Power save configuration）。

## 180.2\_详细说明（Detailed Documentation）

<a id="a9e83c10eaaa1d721cbc49b40aedb00df"></a>

### `num_twt_flows`

```c
char wifi_ps_config::num_twt_flows
```

目标唤醒时间流数量（Number of TWT flows）。

<a id="a357aafc2dedda37755b1cb1fc07fe5a6"></a>

### `ps_params`

```c
struct wifi_ps_params wifi_ps_config::ps_params
```

省电配置（Power save configuration）。

<a id="ab7460f0f253b2d552e49e98e2c770967"></a>

### `twt_flows`

```c
struct wifi_twt_flow_info wifi_ps_config::twt_flows[WIFI_MAX_TWT_FLOWS]
```

目标唤醒时间流详情（TWT flow details）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 180.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [wifi_twt_flow_info](P188_wifi_twt_flow_info_结构体.md)
- [wifi_ps_params](P181_wifi_ps_params_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P179_wifi_nm_mgd_iface_结构体.md) · [返回大纲](大纲.md) · [下一章](P181_wifi_ps_params_结构体.md)
