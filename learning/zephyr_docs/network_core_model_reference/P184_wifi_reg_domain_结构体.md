---
id: learning.zephyr-docs.network-core-model-reference.page-184
title: wifi_reg_domain_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__reg__domain.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第184章\_wifi\_reg\_domain\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__reg__domain.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

监管域（Regulatory Domain）的信息或配置。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

监管域（Regulatory Domain）的信息或配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 184.1\_数据成员（Data Fields）

<a id="r_a3bbfdf1497a87bbb6b6211c7035e1002"></a>

```c
enum wifi_mgmt_op oper
```

相关声明：[wifi_mgmt_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae129d0783276e662575af2314eef86cd)、[oper](#a3bbfdf1497a87bbb6b6211c7035e1002)。

监管域操作（Regulatory domain operation）。

<a id="r_a567c6fcae8032567aea83c18cd211c33"></a>

```c
bool force
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[force](#a567c6fcae8032567aea83c18cd211c33)。

以此监管提示（Regulatory hint）为准，忽略其他所有提示；具体行为由实现决定（Implementation specific）。

<a id="r_abf191495814c227fbbfaccb2f727762e"></a>

```c
uint8_t country_code [WIFI_COUNTRY_CODE_LEN]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[country_code](#abf191495814c227fbbfaccb2f727762e)、[WIFI_COUNTRY_CODE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga6766ef7bcb001f1fb526a4083b6cd8bc)。

国家代码（Country code）：ISO/IEC 3166-1 两字母代码（Alpha-2）。

<a id="r_a3278e9f43893f49ab9f9d0d7f24009c1"></a>

```c
unsigned int num_channels
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[num_channels](#a3278e9f43893f49ab9f9d0d7f24009c1)。

支持的信道数量（Number of channels supported）。

<a id="r_a4c8c9c11e41123cd7738fdb0d33ae5fb"></a>

```c
struct wifi_reg_chan_info * chan_info
```

相关声明：[wifi_reg_chan_info](P183_wifi_reg_chan_info_结构体.md)、[chan_info](#a4c8c9c11e41123cd7738fdb0d33ae5fb)。

信道信息（Channels information）。

## 184.2\_详细说明（Detailed Documentation）

<a id="a4c8c9c11e41123cd7738fdb0d33ae5fb"></a>

### `chan_info`

```c
struct wifi_reg_chan_info* wifi_reg_domain::chan_info
```

信道信息（Channels information）。

<a id="abf191495814c227fbbfaccb2f727762e"></a>

### `country_code`

```c
uint8_t wifi_reg_domain::country_code[WIFI_COUNTRY_CODE_LEN]
```

国家代码（Country code）：ISO/IEC 3166-1 两字母代码（Alpha-2）。

<a id="a567c6fcae8032567aea83c18cd211c33"></a>

### `force`

```c
bool wifi_reg_domain::force
```

以此监管提示（Regulatory hint）为准，忽略其他所有提示；具体行为由实现决定（Implementation specific）。

<a id="a3278e9f43893f49ab9f9d0d7f24009c1"></a>

### `num_channels`

```c
unsigned int wifi_reg_domain::num_channels
```

支持的信道数量（Number of channels supported）。

<a id="a3bbfdf1497a87bbb6b6211c7035e1002"></a>

### `oper`

```c
enum wifi_mgmt_op wifi_reg_domain::oper
```

监管域操作（Regulatory domain operation）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 184.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [wifi_mgmt_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae129d0783276e662575af2314eef86cd)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [WIFI_COUNTRY_CODE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga6766ef7bcb001f1fb526a4083b6cd8bc)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [wifi_reg_chan_info](P183_wifi_reg_chan_info_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P183_wifi_reg_chan_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P185_wifi_scan_params_结构体.md)
