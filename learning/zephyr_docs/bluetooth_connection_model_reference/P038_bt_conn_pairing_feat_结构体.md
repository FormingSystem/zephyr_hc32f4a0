---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-38
title: bt_conn_pairing_feat_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__pairing__feat.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_bt\_conn\_pairing\_feat\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__pairing__feat.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

配对请求（Pairing Request）与配对响应（Pairing Response）信息结构体。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

配对请求与配对响应信息结构（Pairing request and pairing response info structure）。此结构对 `smp_pairing_req` 和 `smp_pairing_rsp` 相同，表示数据包数据的一个子集，不包含开头的代码八位组（Code octet）。定义见核心规范（Core Spec.）第 3 卷 H 部分第 3.5.1 和 3.5.2 节。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 38.1\_数据成员（Data Fields）

<a id="r_a68005cea273c8e76c086502001b258b0"></a>

```c
uint8_t io_capability
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[io_capability](#a68005cea273c8e76c086502001b258b0)。

输入／输出能力（IO Capability），见核心规范（Core Spec.）。

<a id="r_afb03164960db62b4b4cf70d3f0134099"></a>

```c
uint8_t oob_data_flag
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[oob_data_flag](#afb03164960db62b4b4cf70d3f0134099)。

带外数据标志（OOB data flag），见核心规范（Core Spec.）。

<a id="r_af9a977b1e0f9d4eada26a82d92eaec54"></a>

```c
uint8_t auth_req
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[auth_req](#af9a977b1e0f9d4eada26a82d92eaec54)。

认证要求（AuthReq），见核心规范（Core Spec.）。

<a id="r_abe1d7d4bd9f4b551a2d0c69adc75bd40"></a>

```c
uint8_t max_enc_key_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_enc_key_size](#abe1d7d4bd9f4b551a2d0c69adc75bd40)。

最大加密密钥大小（Maximum Encryption Key Size），见核心规范（Core Spec.）。

<a id="r_a70adc125b875348ec8d273dea3b470d8"></a>

```c
uint8_t init_key_dist
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[init_key_dist](#a70adc125b875348ec8d273dea3b470d8)。

发起方密钥分发／生成（Initiator Key Distribution/Generation），见核心规范（Core Spec.）。

<a id="r_a49f9f02e232e91f7f7a530aa7f226cba"></a>

```c
uint8_t resp_key_dist
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[resp_key_dist](#a49f9f02e232e91f7f7a530aa7f226cba)。

响应方密钥分发／生成（Responder Key Distribution/Generation），见核心规范（Core Spec.）。

## 38.2\_详细说明（Detailed Documentation）

<a id="af9a977b1e0f9d4eada26a82d92eaec54"></a>

### `auth_req`

```c
uint8_t bt_conn_pairing_feat::auth_req
```

认证要求（AuthReq），见核心规范（Core Spec.）。

第 3 卷 H 部分第 3.5.1 节，图 3.3。

<a id="a70adc125b875348ec8d273dea3b470d8"></a>

### `init_key_dist`

```c
uint8_t bt_conn_pairing_feat::init_key_dist
```

发起方密钥分发／生成（Initiator Key Distribution/Generation），见核心规范（Core Spec.）。

第 3 卷 H 部分第 3.6.1 节，图 3.11。

<a id="a68005cea273c8e76c086502001b258b0"></a>

### `io_capability`

```c
uint8_t bt_conn_pairing_feat::io_capability
```

输入／输出能力（IO Capability），见核心规范（Core Spec.）。

第 3 卷 H 部分第 3.5.1 节，表 3.4。

<a id="abe1d7d4bd9f4b551a2d0c69adc75bd40"></a>

### `max_enc_key_size`

```c
uint8_t bt_conn_pairing_feat::max_enc_key_size
```

最大加密密钥大小（Maximum Encryption Key Size），见核心规范（Core Spec.）。

第 3 卷 H 部分第 3.5.1 节。

<a id="afb03164960db62b4b4cf70d3f0134099"></a>

### `oob_data_flag`

```c
uint8_t bt_conn_pairing_feat::oob_data_flag
```

带外数据标志（OOB data flag），见核心规范（Core Spec.）。

第 3 卷 H 部分第 3.5.1 节，表 3.5。

<a id="a49f9f02e232e91f7f7a530aa7f226cba"></a>

### `resp_key_dist`

```c
uint8_t bt_conn_pairing_feat::resp_key_dist
```

响应方密钥分发／生成（Responder Key Distribution/Generation），见核心规范（Core Spec.）。

第 3 卷 H 部分第 3.6.1 节，图 3.11。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 38.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P037_bt_conn_oob_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P039_bt_conn_remote_info_结构体.md)
