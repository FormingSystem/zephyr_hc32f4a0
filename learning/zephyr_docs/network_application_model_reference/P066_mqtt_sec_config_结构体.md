---
id: learning.zephyr-docs.network-application-model-reference.page-66
title: mqtt_sec_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sec__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_mqtt\_sec\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sec__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全MQTT传输（Secure MQTT Transports）的TLS配置。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

安全MQTT传输（Secure MQTT Transports）的TLS配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 66.1\_数据成员（Data Fields）

<a id="r_a0e04768b6589823464c2d13c31230cad"></a>

```c
int peer_verify
```

相关声明：[peer_verify](#a0e04768b6589823464c2d13c31230cad)。

指示对端验证（Peer Verification）的偏好设置。

<a id="r_a25415e32e00808fb6a24187f4234059f"></a>

```c
uint32_t cipher_count
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cipher_count](#a25415e32e00808fb6a24187f4234059f)。

指示密码套件列表（Cipher List）的条目数量。

<a id="r_a179a97d56a7a12d5afb60257a67ce46c"></a>

```c
const int * cipher_list
```

相关声明：[cipher_list](#a179a97d56a7a12d5afb60257a67ce46c)。

指示会话所用的密码套件（Ciphers）列表。

<a id="r_a6d59afc061a749ea31f5bd415918a3e0"></a>

```c
uint32_t sec_tag_count
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[sec_tag_count](#a6d59afc061a749ea31f5bd415918a3e0)。

指示安全标签列表（Security Tag List）的条目数量。

<a id="r_adeb8630a9e73c4b3226afa1c9a5060fe"></a>

```c
const sec_tag_t * sec_tag_list
```

相关声明：[sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)、[sec_tag_list](#adeb8630a9e73c4b3226afa1c9a5060fe)。

指示会话所用的安全标签（Security Tags）列表。

<a id="r_af7a0ee827bf98fde264000f4c9020c15"></a>

```c
const char * hostname
```

相关声明：[hostname](#af7a0ee827bf98fde264000f4c9020c15)。

用于证书验证（Certificate Verification）的对端主机名。

<a id="r_a5beac5704fec3e399e5c0099a57ce115"></a>

```c
int cert_nocopy
```

相关声明：[cert_nocopy](#a5beac5704fec3e399e5c0099a57ce115)。

指示是否将证书复制到堆（Heap）的偏好设置。

<a id="r_a9bfafa25c9054fa0389927c72da60587"></a>

```c
bool set_native_tls
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[set_native_tls](#a9bfafa25c9054fa0389927c72da60587)。

将套接字设为使用原生TLS（Native TLS），配合套接字卸载使用。

## 66.2\_详细说明（Detailed Documentation）

<a id="a5beac5704fec3e399e5c0099a57ce115"></a>

### `cert_nocopy`

```c
int mqtt_sec_config::cert_nocopy
```

指示是否将证书复制到堆（Heap）的偏好设置。

<a id="a25415e32e00808fb6a24187f4234059f"></a>

### `cipher_count`

```c
uint32_t mqtt_sec_config::cipher_count
```

指示密码套件列表（Cipher List）的条目数量。

<a id="a179a97d56a7a12d5afb60257a67ce46c"></a>

### `cipher_list`

```c
const int* mqtt_sec_config::cipher_list
```

指示会话所用的密码套件（Ciphers）列表。

可为NULL，以使用默认密码套件（Ciphers）。

<a id="af7a0ee827bf98fde264000f4c9020c15"></a>

### `hostname`

```c
const char* mqtt_sec_config::hostname
```

用于证书验证（Certificate Verification）的对端主机名。

<a id="a0e04768b6589823464c2d13c31230cad"></a>

### `peer_verify`

```c
int mqtt_sec_config::peer_verify
```

指示对端验证（Peer Verification）的偏好设置。

<a id="a6d59afc061a749ea31f5bd415918a3e0"></a>

### `sec_tag_count`

```c
uint32_t mqtt_sec_config::sec_tag_count
```

指示安全标签列表（Security Tag List）的条目数量。

<a id="adeb8630a9e73c4b3226afa1c9a5060fe"></a>

### `sec_tag_list`

```c
const sec_tag_t* mqtt_sec_config::sec_tag_list
```

指示会话所用的安全标签（Security Tags）列表。

<a id="a9bfafa25c9054fa0389927c72da60587"></a>

### `set_native_tls`

```c
bool mqtt_sec_config::set_native_tls
```

将套接字设为使用原生TLS（Native TLS），配合套接字卸载使用。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 66.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P065_mqtt_pubrel_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P067_mqtt_sn_client_结构体.md)
