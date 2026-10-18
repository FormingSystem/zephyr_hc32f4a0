---
id: learning.zephyr-docs.modem-wireless-model-reference.page-13
title: esp_wifi_mesh_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structesp__wifi__mesh__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_esp\_wifi\_mesh\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structesp__wifi__mesh__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

运行时可配置的Mesh凭据（Credentials）和树结构限制（Tree Limits）。

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

<a id="details"></a>

可在运行时配置的 Mesh 凭据（credentials）和树形拓扑限制。`esp_wifi_mesh_start()` 读取此配置，以代替驱动的 Kconfig 默认值。必须在调用 `esp_wifi_mesh_start()` 前设置；Mesh 协议栈不支持运行时重新配置或拆除，因此启动后的更改不会生效。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_a72ef51dca5f383486898cafbbefa4d88"></a>

```c
char ssid [33]
```

相关声明：[ssid](#a72ef51dca5f383486898cafbbefa4d88)。

路由器 SSID：根节点为访问外部网络而关联的上游 Wi-Fi 网络。

<a id="r_a25c487b261eda67fb0ade6ef4f6a3319"></a>

```c
char password [64]
```

相关声明：[password](#a25c487b261eda67fb0ade6ef4f6a3319)。

路由器密码。

<a id="r_a7271c57c8730a069771738d181508724"></a>

```c
char mesh_password [64]
```

相关声明：[mesh_password](#a7271c57c8730a069771738d181508724)。

用于保护节点间 Mesh 链路的 Mesh 软件接入点（softAP）密码。

<a id="r_a578c704181d4560d6851bba8839b3b42"></a>

```c
uint8_t channel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel](#a578c704181d4560d6851bba8839b3b42)。

Mesh 信道：0 表示通过扫描自动选择，在未知路由器信道时必须使用；1 至 13 表示固定信道，此时所有节点必须匹配。

<a id="r_a3f479fa2a96bd0141a26b307b21d5299"></a>

```c
uint8_t mesh_id [6]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mesh_id](#a3f479fa2a96bd0141a26b307b21d5299)。

6 字节 Mesh 网络标识符。

<a id="r_a794408d0ed1382cc9104e9a19d99560d"></a>

```c
enum wifi_security_type authmode
```

相关声明：[wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)、[authmode](#a794408d0ed1382cc9104e9a19d99560d)。

Mesh 软件接入点（softAP）的身份验证模式。

<a id="r_a820b4a655de29d7056c4ce15dbfa184d"></a>

```c
uint8_t num_layers
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_layers](#a820b4a655de29d7056c4ce15dbfa184d)。

此 Mesh 使用的树深度（层数，layers）。

<a id="r_a996b2ac59cff92df84e1a394549bf565"></a>

```c
uint8_t max_connections
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_connections](#a996b2ac59cff92df84e1a394549bf565)。

此 Mesh 中每个节点的直接子节点数量上限（fan-out）。

## 13.2\_详细说明（Detailed Documentation）

<a id="a794408d0ed1382cc9104e9a19d99560d"></a>

### `authmode`

```c
enum wifi_security_type esp_wifi_mesh_config::authmode
```

Mesh 软件接入点（softAP）的身份验证模式。

<a id="a578c704181d4560d6851bba8839b3b42"></a>

### `channel`

```c
uint8_t esp_wifi_mesh_config::channel
```

Mesh 信道：0 表示通过扫描自动选择，在未知路由器信道时必须使用；1 至 13 表示固定信道，此时所有节点必须匹配。

<a id="a996b2ac59cff92df84e1a394549bf565"></a>

### `max_connections`

```c
uint8_t esp_wifi_mesh_config::max_connections
```

此 Mesh 中每个节点的直接子节点数量上限（fan-out）。

必须至少为 1，且不大于构建时编入的 `CONFIG_WIFI_ESP32_MESH_MAX_CONNECTIONS`；该选项决定构建时路由表缓冲区的大小。

<a id="a3f479fa2a96bd0141a26b307b21d5299"></a>

### `mesh_id`

```c
uint8_t esp_wifi_mesh_config::mesh_id[6]
```

6 字节 Mesh 网络标识符。

节点只加入宣告相同 ID 的 Mesh，因此同一网络中的每个节点都必须使用相同的值。

<a id="a7271c57c8730a069771738d181508724"></a>

### `mesh_password`

```c
char esp_wifi_mesh_config::mesh_password[64]
```

用于保护节点间 Mesh 链路的 Mesh 软件接入点（softAP）密码。

必须为空（使用 `WIFI_SECURITY_TYPE_NONE` 时），或者为 8 至 63 个字符；Mesh 中每个节点都必须相同。

<a id="a820b4a655de29d7056c4ce15dbfa184d"></a>

### `num_layers`

```c
uint8_t esp_wifi_mesh_config::num_layers
```

此 Mesh 使用的树深度（层数，layers）。

必须至少为 1，且不大于构建时编入的 `CONFIG_WIFI_ESP32_MESH_MAX_LAYER`；该选项决定构建时路由表缓冲区的大小。

<a id="a25c487b261eda67fb0ade6ef4f6a3319"></a>

### `password`

```c
char esp_wifi_mesh_config::password[64]
```

路由器密码。

以空字符（NUL）结尾，最多 63 个字符；对于开放路由器，设为空字符串。

<a id="a72ef51dca5f383486898cafbbefa4d88"></a>

### `ssid`

```c
char esp_wifi_mesh_config::ssid[33]
```

路由器 SSID：根节点为访问外部网络而关联的上游 Wi-Fi 网络。

为空时形成无路由器、固定根节点的 Mesh，参见 `esp_wifi_mesh_start()`。以空字符（NUL）结尾，最多 32 个字符。

本数据类型文档由以下文件生成：

- `zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/esp__wifi__mesh_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)
- [esp_wifi_mesh_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga1839da0700018e749326a870f1de972c)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_esp_wifi_mesh_addr_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_esp_wifi_mesh_event_info_结构体.md)
