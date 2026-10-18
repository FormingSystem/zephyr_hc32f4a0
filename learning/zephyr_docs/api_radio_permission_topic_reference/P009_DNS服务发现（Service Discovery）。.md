---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-9
title: DNS服务发现（Service Discovery）。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_DNS服务发现（Service Discovery）。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DNS服务发现（Service Discovery）。

<a id="details"></a>

DNS 服务发现（DNS Service Discovery）。本 API 允许通过 DNS 通告服务。系统或应用代码应使用 DNS_SD_REGISTER_TCP_SERVICE 或 DNS_SD_REGISTER_UDP_SERVICE 通告服务。另请参阅（See Also）：RFC 6763。引入版本（Since）：2.5；API 版本（Version）：0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_dns_5Fsd_5Frec"></a>

```c
struct dns_sd_rec
```

相关声明：[dns_sd_rec](../network_application_model_reference/P025_dns_sd_rec_结构体.md)。

DNS服务发现（Service Discovery）记录。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="r_ga4d1f5462555d6051bdeaa21b02e7aa6e"></a>

```c
#define DNS_SD_INSTANCE_MIN_SIZE 1
```

相关声明：[DNS_SD_INSTANCE_MIN_SIZE](#ga4d1f5462555d6051bdeaa21b02e7aa6e)。

RFC 1034 第 3.1 节。

<a id="r_ga5c0993b8bc21d47fa15f56acb313ac31"></a>

```c
#define DNS_SD_INSTANCE_MAX_SIZE 63
```

相关声明：[DNS_SD_INSTANCE_MAX_SIZE](#ga5c0993b8bc21d47fa15f56acb313ac31)。

RFC 1034 第 3.1 节；RFC 6763 第 7.2 节。

<a id="r_gacc652552aa567206ab7a4d7d070d1fbc"></a>

```c
#define DNS_SD_SERVICE_MIN_SIZE 2
```

相关声明：[DNS_SD_SERVICE_MIN_SIZE](#gacc652552aa567206ab7a4d7d070d1fbc)。

RFC 6763 第 7.2 节，包含下划线（Underscore）。

<a id="r_gab4d208eac1491c45cb47e87c90a78c26"></a>

```c
#define DNS_SD_SERVICE_MAX_SIZE 16
```

相关声明：[DNS_SD_SERVICE_MAX_SIZE](#gab4d208eac1491c45cb47e87c90a78c26)。

RFC 6763 第 7.2 节，包含下划线（Underscore）。

<a id="r_ga81cac0a52e58142e492bad244ff97490"></a>

```c
#define DNS_SD_SERVICE_PREFIX '_'
```

相关声明：[DNS_SD_SERVICE_PREFIX](#ga81cac0a52e58142e492bad244ff97490)。

RFC 6763 第 4.1.2 节。

<a id="r_gafb686ae445f5bd640176f59d62df2bdc"></a>

```c
#define DNS_SD_PROTO_SIZE 4
```

相关声明：[DNS_SD_PROTO_SIZE](#gafb686ae445f5bd640176f59d62df2bdc)。

RFC 6763 第 4.1.2 节，为 `_tcp` 或 `_udp`，不区分大小写（Case-insensitive）。

<a id="r_ga19d655c1778143e2aed5d2d69a757422"></a>

```c
#define DNS_SD_DOMAIN_MIN_SIZE 2
```

相关声明：[DNS_SD_DOMAIN_MIN_SIZE](#ga19d655c1778143e2aed5d2d69a757422)。

ICANN 的顶级域（TLD）命名规则（Naming Rules）。

<a id="r_gaa93b197f2b9a3b13c7ed8f3c455f11cb"></a>

```c
#define DNS_SD_DOMAIN_MAX_SIZE 63
```

相关声明：[DNS_SD_DOMAIN_MAX_SIZE](#gaa93b197f2b9a3b13c7ed8f3c455f11cb)。

RFC 1034 第 3.1 节；RFC 6763 第 7.2 节。

<a id="r_gaeec792bc3111e1961eb2e21cd8bea80a"></a>

```c
#define DNS_SD_MIN_LABELS 3
```

相关声明：[DNS_SD_MIN_LABELS](#gaeec792bc3111e1961eb2e21cd8bea80a)。

完全限定名称（Fully-qualified Name）中的最少段数（Segments）。

<a id="r_ga269e2f3bbf15a5ccd81a444749faa384"></a>

```c
#define DNS_SD_MAX_LABELS 4
```

相关声明：[DNS_SD_MAX_LABELS](#ga269e2f3bbf15a5ccd81a444749faa384)。

完全限定名称（Fully-qualified Name）中的最多段数（Segments）。

<a id="r_ga0c0060a680d5c4fe56f2815c920c3627"></a>

```c
#define DNS_SD_REGISTER_SERVICE(_id, _instance, _service, _proto, _domain, _text, _port)
```

相关声明：[DNS_SD_REGISTER_SERVICE](#ga0c0060a680d5c4fe56f2815c920c3627)。

为 DNS 服务发现（DNS Service Discovery，DNS-SD）注册服务。

<a id="r_ga96abc525d755c138304f07cdd2d9e1c2"></a>

```c
#define DNS_SD_REGISTER_TCP_SERVICE(id, instance, service, domain, text, port)
```

相关声明：[DNS_SD_REGISTER_TCP_SERVICE](#ga96abc525d755c138304f07cdd2d9e1c2)。

为 DNS 服务发现（DNS-SD）注册 TCP 服务。

<a id="r_gaf8abe0968552213d46b49be16c1f21d6"></a>

```c
#define DNS_SD_REGISTER_UDP_SERVICE(id, instance, service, domain, text, port)
```

相关声明：[DNS_SD_REGISTER_UDP_SERVICE](#gaf8abe0968552213d46b49be16c1f21d6)。

为 DNS 服务发现（DNS-SD）注册 UDP 服务。

<a id="r_ga221216c5ffd142aa4c6cade4064d580f"></a>

```c
#define DNS_SD_EMPTY_TXT dns_sd_empty_txt
```

相关声明：[DNS_SD_EMPTY_TXT](#ga221216c5ffd142aa4c6cade4064d580f)。

空 DNS-SD TXT 说明符（Specifier）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.3\_函数（Functions）

<a id="r_ga6d68e785607089df42d534c2f876c6d5"></a>

```c
static size_t dns_sd_txt_size (const struct dns_sd_rec *rec)
```

相关声明：[dns_sd_txt_size](#ga6d68e785607089df42d534c2f876c6d5)、[dns_sd_rec](../network_application_model_reference/P025_dns_sd_rec_结构体.md)。

获取 DNS-SD TXT 数据大小（Data Size）。

<a id="r_gaeba098fa6d159067c70588cb60056277"></a>

```c
bool dns_sd_is_service_type_enumeration (const struct dns_sd_rec *rec)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[dns_sd_is_service_type_enumeration](#gaeba098fa6d159067c70588cb60056277)、[dns_sd_rec](../network_application_model_reference/P025_dns_sd_rec_结构体.md)。

检查 `rec` 是否为 DNS-SD 服务类型枚举（Service Type Enumeration）。

<a id="r_ga328d71e26411460b1b329db8f1ebd37b"></a>

```c
void dns_sd_create_wildcard_filter (struct dns_sd_rec *filter)
```

相关声明：[dns_sd_create_wildcard_filter](#ga328d71e26411460b1b329db8f1ebd37b)、[dns_sd_rec](../network_application_model_reference/P025_dns_sd_rec_结构体.md)。

创建 DNS-SD 记录的通配过滤器（Wildcard Filter）。

## 9.4\_详细说明（Detailed Documentation）

<a id="gaa93b197f2b9a3b13c7ed8f3c455f11cb"></a>

### `DNS_SD_DOMAIN_MAX_SIZE`

```c
#define DNS_SD_DOMAIN_MAX_SIZE 63
```

```c
#include <zephyr/net/dns_sd.h>
```

RFC 1034 第 3.1 节；RFC 6763 第 7.2 节。

<a id="ga19d655c1778143e2aed5d2d69a757422"></a>

### `DNS_SD_DOMAIN_MIN_SIZE`

```c
#define DNS_SD_DOMAIN_MIN_SIZE 2
```

```c
#include <zephyr/net/dns_sd.h>
```

ICANN 的顶级域（TLD）命名规则（Naming Rules）。

<a id="ga221216c5ffd142aa4c6cade4064d580f"></a>

### `DNS_SD_EMPTY_TXT`

```c
#define DNS_SD_EMPTY_TXT dns_sd_empty_txt
```

```c
#include <zephyr/net/dns_sd.h>
```

空 DNS-SD TXT 说明符（Specifier）。

<a id="ga5c0993b8bc21d47fa15f56acb313ac31"></a>

### `DNS_SD_INSTANCE_MAX_SIZE`

```c
#define DNS_SD_INSTANCE_MAX_SIZE 63
```

```c
#include <zephyr/net/dns_sd.h>
```

RFC 1034 第 3.1 节；RFC 6763 第 7.2 节。

<a id="ga4d1f5462555d6051bdeaa21b02e7aa6e"></a>

### `DNS_SD_INSTANCE_MIN_SIZE`

```c
#define DNS_SD_INSTANCE_MIN_SIZE 1
```

```c
#include <zephyr/net/dns_sd.h>
```

RFC 1034 第 3.1 节。

<a id="ga269e2f3bbf15a5ccd81a444749faa384"></a>

### `DNS_SD_MAX_LABELS`

```c
#define DNS_SD_MAX_LABELS 4
```

```c
#include <zephyr/net/dns_sd.h>
```

完全限定名称（Fully-qualified Name）中的最多段数（Segments）。

表示以下形式的完全限定名称（Fully Qualified Names，FQNs）：

原始示例（Example）：

```c
<instance>.<sn>._tcp.<domain>.
```

目前不支持子类型（Sub-types）和服务域（Service Domains），仅支持 local 域。具体而言，不支持以下情况：

原始示例（Example）：

```c
<sub>._sub.<sn>._tcp.<servicedomain>.<parentdomain>.
```

**参阅（See Also）**：另请参阅（See Also）：RFC 6763 第 7.2 节。

<a id="gaeec792bc3111e1961eb2e21cd8bea80a"></a>

### `DNS_SD_MIN_LABELS`

```c
#define DNS_SD_MIN_LABELS 3
```

```c
#include <zephyr/net/dns_sd.h>
```

完全限定名称（Fully-qualified Name）中的最少段数（Segments）。

表示以下形式的完全限定名称（Fully Qualified Names，FQNs）：

原始示例（Example）：

```c
<sn>._tcp.<domain>.
```

目前不支持子类型（Sub-types）和服务域（Service Domains），仅支持 local 域。具体而言，不支持以下情况：

原始示例（Example）：

```c
<sub>._sub.<sn>._tcp.<servicedomain>.<parentdomain>.
```

**参阅（See Also）**：另请参阅（See Also）：RFC 6763 第 7.2 节。

<a id="gafb686ae445f5bd640176f59d62df2bdc"></a>

### `DNS_SD_PROTO_SIZE`

```c
#define DNS_SD_PROTO_SIZE 4
```

```c
#include <zephyr/net/dns_sd.h>
```

RFC 6763 第 4.1.2 节，为 `_tcp` 或 `_udp`，不区分大小写（Case-insensitive）。

<a id="ga0c0060a680d5c4fe56f2815c920c3627"></a>

### `DNS_SD_REGISTER_SERVICE`

```c
#define DNS_SD_REGISTER_SERVICE ( _id, _instance, _service, _proto, _domain, _text, _port )
```

```c
#include <zephyr/net/dns_sd.h>
```

展开值（Value）：

```c
static const STRUCT_SECTION_ITERABLE(dns_sd_rec, _id) = {       \
        .instance = _instance,                                  \
        .service = _service,                                    \
        .proto = _proto,                                        \
        .domain = _domain,                                      \
        .text = (const char *)_text,                            \
        .text_size = sizeof(_text) - 1,                         \
        .port = _port,                                          \
}
```

为 DNS 服务发现（DNS Service Discovery，DNS-SD）注册服务。

此宏适用于高级用例。两个简单例子是需要自定义 _domain，或自定义的非标准 _proto。

另一个用例是端口号未预先分配。原因可能有多种，最常见的是使用临时端口（Ephemeral Port），即服务绑定到端口 0。此时 Zephyr 与其他操作系统一样，会选择未使用的端口。使用临时端口时，可让 _port 指向 IPv4 net_sockaddr_in 的 net_sockaddr_in::sin_port 字段，或 IPv6 net_sockaddr_in6 的 net_sockaddr_in6::sin6_port 字段。

可以通过 _id 变量引用此服务。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_id` | DNS-SD 服务记录（Service Record）的变量名 |
| `_instance` | 服务实例名称（Service Instance Name），例如 My HTTP Server |
| `_service` | 服务名称（Service Name），例如 _http |
| `_proto` | 服务使用的协议，为 _tcp 或 _udp |
| `_domain` | 服务的域（Domain），例如 local |
| `_text` | DNS TXT 记录（TXT Record）的信息 |
| `_port` | 指向此服务将使用的端口号的指针 |

<a id="ga96abc525d755c138304f07cdd2d9e1c2"></a>

### `DNS_SD_REGISTER_TCP_SERVICE`

```c
#define DNS_SD_REGISTER_TCP_SERVICE ( id, instance, service, domain, text, port )
```

```c
#include <zephyr/net/dns_sd.h>
```

展开值（Value）：

```c
static const uint16_t id ## _port = sys_cpu_to_be16(port); \
DNS_SD_REGISTER_SERVICE(id, instance, service, "_tcp", domain,   \
                        text, &id ## _port)
```

为 DNS 服务发现（DNS-SD）注册 TCP 服务。

此宏可通过 DNS-SD 通告服务（Service Advertisement）。

可以通过 id 变量引用此服务。

示例，包含 TXT：

原始示例（Example）：

```c
#include <zephyr/net/dns_sd.h>
static const char bar_txt[] = {
  "\x06" "path=/"
  "\x0f" "this=is the way"
  "\x0e" "foo or=foo not"
  "\x17" "this=has\0embedded\0nulls"
  "\x04" "true"
};
DNS_SD_REGISTER_TCP_SERVICE(bar, CONFIG_NET_HOSTNAME,
  "_bar", "local", bar_txt, 4242);
```

TXT 记录以单个长度字节（十六进制编码）开头，内容为 key=value 对，因此每个键值对（Key-value Pair）不得超过 255 字节。务必确保编码的长度值正确。

TXT 编码的其他规则参见 RFC 6763 第 6 节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | DNS-SD 服务记录（Service Record）的变量名 |
| `instance` | 服务实例名称（Service Instance Name），例如 My HTTP Server |
| `service` | 服务名称（Service Name），例如 _http |
| `domain` | 服务的域（Domain），例如 local |
| `text` | DNS TXT 记录（TXT Record）的信息 |
| `port` | 此服务将使用的端口号 |

**参阅（See Also）**：另请参阅（See Also）：RFC 6763。

<a id="gaf8abe0968552213d46b49be16c1f21d6"></a>

### `DNS_SD_REGISTER_UDP_SERVICE`

```c
#define DNS_SD_REGISTER_UDP_SERVICE ( id, instance, service, domain, text, port )
```

```c
#include <zephyr/net/dns_sd.h>
```

展开值（Value）：

```c
static const uint16_t id ## _port = sys_cpu_to_be16(port); \
DNS_SD_REGISTER_SERVICE(id, instance, service, "_udp", domain,   \
                        text, &id ## _port)
```

为 DNS 服务发现（DNS-SD）注册 UDP 服务。

此宏可通过 DNS-SD 通告服务（Service Advertisement）。

可以通过 id 变量引用此服务。

示例，不包含 TXT：

原始示例（Example）：

```c
#include <zephyr/net/dns_sd.h>
DNS_SD_REGISTER_UDP_SERVICE(foo, CONFIG_NET_HOSTNAME,
  "_foo", "local", DNS_SD_EMPTY_TXT, 4242);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | DNS-SD 服务记录（Service Record）的变量名 |
| `instance` | 服务实例名称（Service Instance Name），例如 My TFTP Server |
| `service` | 服务名称（Service Name），例如 _tftp |
| `domain` | 服务的域（Domain），例如 local 或 zephyrproject.org |
| `text` | DNS TXT 记录（TXT Record）的信息 |
| `port` | 此服务将使用的端口号 |

**参阅（See Also）**：另请参阅（See Also）：RFC 6763。

<a id="gab4d208eac1491c45cb47e87c90a78c26"></a>

### `DNS_SD_SERVICE_MAX_SIZE`

```c
#define DNS_SD_SERVICE_MAX_SIZE 16
```

```c
#include <zephyr/net/dns_sd.h>
```

RFC 6763 第 7.2 节，包含下划线（Underscore）。

<a id="gacc652552aa567206ab7a4d7d070d1fbc"></a>

### `DNS_SD_SERVICE_MIN_SIZE`

```c
#define DNS_SD_SERVICE_MIN_SIZE 2
```

```c
#include <zephyr/net/dns_sd.h>
```

RFC 6763 第 7.2 节，包含下划线（Underscore）。

<a id="ga81cac0a52e58142e492bad244ff97490"></a>

### `DNS_SD_SERVICE_PREFIX`

```c
#define DNS_SD_SERVICE_PREFIX '_'
```

```c
#include <zephyr/net/dns_sd.h>
```

RFC 6763 第 4.1.2 节。

<a id="ga328d71e26411460b1b329db8f1ebd37b"></a>

### `dns_sd_create_wildcard_filter()`

```c
void dns_sd_create_wildcard_filter ( struct dns_sd_rec * filter)
```

```c
#include <zephyr/net/dns_sd.h>
```

创建 DNS-SD 记录的通配过滤器（Wildcard Filter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `filter` | 指向要使用的过滤器（Filter）的指针 |

<a id="gaeba098fa6d159067c70588cb60056277"></a>

### `dns_sd_is_service_type_enumeration()`

```c
bool dns_sd_is_service_type_enumeration ( const struct dns_sd_rec * rec)
```

```c
#include <zephyr/net/dns_sd.h>
```

检查 `rec` 是否为 DNS-SD 服务类型枚举（Service Type Enumeration）。

网络工具使用 DNS-SD 服务类型枚举（Service Type Enumeration），获取特定域中某个主机通过 mDNS 通告的全部服务列表。

例如，对于 .local 域，相应查询为 _services._dns-sd._udp.local。

目前仅支持 .local 域。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rec` | 待检查的记录（Record） |

**参阅（See Also）**：另请参阅（See Also）：RFC 6763 第 9 节。

**返回（Returns）**：返回值（Returns）：rec 是 DNS-SD 服务类型枚举（Service Type Enumeration）时返回 true。

<a id="ga6d68e785607089df42d534c2f876c6d5"></a>

### `dns_sd_txt_size()`

```c
size_t dns_sd_txt_size ( const struct dns_sd_rec * rec)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/dns_sd.h>
```

获取 DNS-SD TXT 数据大小（Data Size）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rec` | 待检查的记录（Record） |

**返回（Returns）**：返回值（Returns）：文本字段（Text Field）的大小。


## 9.5\_原页交叉引用（Cross References）

- [dns_sd_rec](../network_application_model_reference/P025_dns_sd_rec_结构体.md)
- [RFC 1034 第 3.1 节。](https://datatracker.ietf.org/doc/html/rfc1034#section-3.1)
- [RFC 6763, section-7.2](https://datatracker.ietf.org/doc/html/rfc6763#section-7.2)
- [RFC 6763 第 4.1.2 节。](https://datatracker.ietf.org/doc/html/rfc6763#section-4.1.2)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [RFC 6763](https://datatracker.ietf.org/doc/html/rfc6763)
- [zephyr/net/dns_sd.h](../api_file_storage_event_reference/P006_zephyr__net__dns_sd.h_文件参考.md)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [net_sockaddr_in::sin_port](../network_core_model_reference/P119_net_sockaddr_in_结构体.md#a099706d7572442b073f9efffe3df7000)
- [net_sockaddr_in](../network_core_model_reference/P119_net_sockaddr_in_结构体.md)
- [net_sockaddr_in6::sin6_port](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md#abd547e6daf4a9dd86a5c8349c0b80b04)
- [net_sockaddr_in6](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [sys_cpu_to_be16](../byteorder_reference/P001_系统字节序头文件参考.md#a9e2c7b19bbba5343ee8c5f9740484a56)
- [RFC 6763, section-6](https://datatracker.ietf.org/doc/html/rfc6763#section-6)
- [RFC 6763, section-9](https://datatracker.ietf.org/doc/html/rfc6763#section-9)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructdns__sd__rec_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="asys_2byteorder_8h_html_a9e2c7b19bbba5343ee8c5f9740484a56"></a>
<a id="adns__sd_8h_html"></a>
<a id="agroup__dns__sd_html_ga96abc525d755c138304f07cdd2d9e1c2"></a>
<a id="agroup__dns__sd_html_ga221216c5ffd142aa4c6cade4064d580f"></a>
<a id="agroup__dns__sd_html_gaf8abe0968552213d46b49be16c1f21d6"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_英飞凌（Infineon）CAT1.md) · [返回大纲](大纲.md) · [下一章](P010_eSPI SAF API主题.md)
