---
id: learning.zephyr-docs.network-core-model-reference.page-172
title: wifi_eap_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__eap__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第172章\_wifi\_eap\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__eap__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可扩展认证协议（EAP）的方法配置。

```c
#include <zephyr/net/wifi.h>
```

<a id="details"></a>

可扩展认证协议（EAP）的方法配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 172.1\_数据成员（Data Fields）

<a id="r_a031a5c86551f90130ff74ed53977c49d"></a>

```c
enum wifi_security_type type
```

相关声明：[wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)、[type](#a031a5c86551f90130ff74ed53977c49d)。

安全类型（Security type）。

<a id="r_ab44893426c89416ab24e3bfb57bf49ad"></a>

```c
enum wifi_eap_type eap_type_phase1
```

相关声明：[wifi_eap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga92b6fa6755491c3bd61f895213d07331)、[eap_type_phase1](#ab44893426c89416ab24e3bfb57bf49ad)。

第一阶段的 EAP 方法类型（Phase 1 EAP method type）。

<a id="r_aaf73f2f986d56f95d196d02dcecbaff1"></a>

```c
enum wifi_eap_type eap_type_phase2
```

相关声明：[wifi_eap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga92b6fa6755491c3bd61f895213d07331)、[eap_type_phase2](#aaf73f2f986d56f95d196d02dcecbaff1)。

第二阶段的 EAP 方法类型（Phase 2 EAP method type）。

<a id="r_aa7a42a1256ef26562e83f47498d87113"></a>

```c
char * method
```

相关声明：[method](#aa7a42a1256ef26562e83f47498d87113)。

EAP 方法字符串（EAP method string）。

<a id="r_abeed60cdf6c01751a4bb3c7ab67ea4e6"></a>

```c
char * phase2
```

相关声明：[phase2](#abeed60cdf6c01751a4bb3c7ab67ea4e6)。

第二阶段设置字符串（Phase 2 setting string）。

## 172.2\_详细说明（Detailed Documentation）

<a id="ab44893426c89416ab24e3bfb57bf49ad"></a>

### `eap_type_phase1`

```c
enum wifi_eap_type wifi_eap_config::eap_type_phase1
```

第一阶段的 EAP 方法类型（Phase 1 EAP method type）。

<a id="aaf73f2f986d56f95d196d02dcecbaff1"></a>

### `eap_type_phase2`

```c
enum wifi_eap_type wifi_eap_config::eap_type_phase2
```

第二阶段的 EAP 方法类型（Phase 2 EAP method type）。

<a id="aa7a42a1256ef26562e83f47498d87113"></a>

### `method`

```c
char* wifi_eap_config::method
```

EAP 方法字符串（EAP method string）。

<a id="abeed60cdf6c01751a4bb3c7ab67ea4e6"></a>

### `phase2`

```c
char* wifi_eap_config::phase2
```

第二阶段设置字符串（Phase 2 setting string）。

<a id="a031a5c86551f90130ff74ed53977c49d"></a>

### `type`

```c
enum wifi_security_type wifi_eap_config::type
```

安全类型（Security type）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi.h`

## 172.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h_source.html)
- [wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)
- [wifi_eap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga92b6fa6755491c3bd61f895213d07331)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P171_wifi_eap_cipher_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P173_wifi_enterprise_creds_params_结构体.md)
