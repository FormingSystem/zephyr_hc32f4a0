---
id: learning.zephyr-docs.network-service-model-reference.page-4
title: dsa_switch_context_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdsa__switch__context.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_dsa\_switch\_context\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdsa__switch__context.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

分布式交换架构（DSA）交换机的上下文数据。

```c
#include <zephyr/net/dsa_core.h>
```

<a id="details"></a>

分布式交换架构（DSA）交换机的上下文数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_ad6670b8743639c7837b9188a9e8a70eb"></a>

```c
struct net_if * iface_user [DSA_PORT_MAX_COUNT]
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[iface_user](#ad6670b8743639c7837b9188a9e8a70eb)。

指向所有 DSA 用户网络接口的指针。

<a id="r_a227551d262998fb83dcd06ebfccdb4d7"></a>

```c
struct net_if * iface_conduit
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[iface_conduit](#a227551d262998fb83dcd06ebfccdb4d7)。

指向 DSA 传输网络接口（conduit network interface）的指针。

<a id="r_a4ca4e815b96c29cb26aef7ff02d8b03c"></a>

```c
struct dsa_api * dapi
```

相关声明：[dsa_api](P002_dsa_api_结构体.md)、[dapi](#a4ca4e815b96c29cb26aef7ff02d8b03c)。

DSA 专用 API 回调。

<a id="r_a0eb8ee97a922eaefdaed00cf75ec5a26"></a>

```c
void * prv_data
```

相关声明：[prv_data](#a0eb8ee97a922eaefdaed00cf75ec5a26)。

实例专用数据。

<a id="r_ae9437d8ef21a64cdb297623096cd77f3"></a>

```c
uint8_t num_ports
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_ports](#ae9437d8ef21a64cdb297623096cd77f3)。

DSA 交换机中的端口数量。

<a id="r_a68a619b3db141ba6127ccc4577f2edf5"></a>

```c
uint8_t init_ports
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[init_ports](#a68a619b3db141ba6127ccc4577f2edf5)。

DSA 交换机中已初始化的端口数量。

<a id="r_a0961bfc0c6ba7047328210245322a9d7"></a>

```c
void * tagger_data
```

相关声明：[tagger_data](#a0961bfc0c6ba7047328210245322a9d7)。

实例连接到标签协议时提供的 DSA 标签处理器（tagger）数据。

## 4.2\_详细说明（Detailed Documentation）

<a id="a4ca4e815b96c29cb26aef7ff02d8b03c"></a>

### `dapi`

```c
struct dsa_api* dsa_switch_context::dapi
```

DSA 专用 API 回调。

<a id="a227551d262998fb83dcd06ebfccdb4d7"></a>

### `iface_conduit`

```c
struct net_if* dsa_switch_context::iface_conduit
```

指向 DSA 传输网络接口（conduit network interface）的指针。

<a id="ad6670b8743639c7837b9188a9e8a70eb"></a>

### `iface_user`

```c
struct net_if* dsa_switch_context::iface_user[DSA_PORT_MAX_COUNT]
```

指向所有 DSA 用户网络接口的指针。

<a id="a68a619b3db141ba6127ccc4577f2edf5"></a>

### `init_ports`

```c
uint8_t dsa_switch_context::init_ports
```

DSA 交换机中已初始化的端口数量。

<a id="ae9437d8ef21a64cdb297623096cd77f3"></a>

### `num_ports`

```c
uint8_t dsa_switch_context::num_ports
```

DSA 交换机中的端口数量。

<a id="a0eb8ee97a922eaefdaed00cf75ec5a26"></a>

### `prv_data`

```c
void* dsa_switch_context::prv_data
```

实例专用数据。

<a id="a0961bfc0c6ba7047328210245322a9d7"></a>

### `tagger_data`

```c
void* dsa_switch_context::tagger_data
```

实例连接到标签协议时提供的 DSA 标签处理器（tagger）数据。

本数据类型文档由以下文件生成：

- `zephyr/net/dsa_core.h`

## 4.3\_原页交叉引用（Cross References）

- [zephyr/net/dsa_core.h](https://docs.zephyrproject.org/latest/doxygen/html/dsa__core_8h_source.html)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [dsa_api](P002_dsa_api_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_dsa_port_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_dsa_tag_register_结构体.md)
