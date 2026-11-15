---
id: learning.zephyr-docs.api-file-storage-event-reference.page-6
title: zephyr__net__dns_sd.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dns__sd_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_net\_\_dns\_sd.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dns__sd_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DNS服务发现（Service Discovery）。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/sys/byteorder.h>
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

DNS服务发现（Service Discovery）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_dns_5Fsd_5Frec"></a>

```c
struct dns_sd_rec
```

相关声明：[dns_sd_rec](../network_application_model_reference/P025_dns_sd_rec_结构体.md)。

DNS服务发现（Service Discovery）记录。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_ga4d1f5462555d6051bdeaa21b02e7aa6e"></a>

```c
#define DNS_SD_INSTANCE_MIN_SIZE 1
```

相关声明：[DNS_SD_INSTANCE_MIN_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga4d1f5462555d6051bdeaa21b02e7aa6e)。

RFC 1034 第 3.1 节。

<a id="r_ga5c0993b8bc21d47fa15f56acb313ac31"></a>

```c
#define DNS_SD_INSTANCE_MAX_SIZE 63
```

相关声明：[DNS_SD_INSTANCE_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga5c0993b8bc21d47fa15f56acb313ac31)。

RFC 1034 第 3.1 节；RFC 6763 第 7.2 节。

<a id="r_gacc652552aa567206ab7a4d7d070d1fbc"></a>

```c
#define DNS_SD_SERVICE_MIN_SIZE 2
```

相关声明：[DNS_SD_SERVICE_MIN_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#gacc652552aa567206ab7a4d7d070d1fbc)。

RFC 6763 第 7.2 节，包含下划线（Underscore）。

<a id="r_gab4d208eac1491c45cb47e87c90a78c26"></a>

```c
#define DNS_SD_SERVICE_MAX_SIZE 16
```

相关声明：[DNS_SD_SERVICE_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#gab4d208eac1491c45cb47e87c90a78c26)。

RFC 6763 第 7.2 节，包含下划线（Underscore）。

<a id="r_ga81cac0a52e58142e492bad244ff97490"></a>

```c
#define DNS_SD_SERVICE_PREFIX '_'
```

相关声明：[DNS_SD_SERVICE_PREFIX](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga81cac0a52e58142e492bad244ff97490)。

RFC 6763 第 4.1.2 节。

<a id="r_gafb686ae445f5bd640176f59d62df2bdc"></a>

```c
#define DNS_SD_PROTO_SIZE 4
```

相关声明：[DNS_SD_PROTO_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#gafb686ae445f5bd640176f59d62df2bdc)。

RFC 6763 第 4.1.2 节，为 `_tcp` 或 `_udp`，不区分大小写（Case-insensitive）。

<a id="r_ga19d655c1778143e2aed5d2d69a757422"></a>

```c
#define DNS_SD_DOMAIN_MIN_SIZE 2
```

相关声明：[DNS_SD_DOMAIN_MIN_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga19d655c1778143e2aed5d2d69a757422)。

ICANN 的顶级域（TLD）命名规则（Naming Rules）。

<a id="r_gaa93b197f2b9a3b13c7ed8f3c455f11cb"></a>

```c
#define DNS_SD_DOMAIN_MAX_SIZE 63
```

相关声明：[DNS_SD_DOMAIN_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#gaa93b197f2b9a3b13c7ed8f3c455f11cb)。

RFC 1034 第 3.1 节；RFC 6763 第 7.2 节。

<a id="r_gaeec792bc3111e1961eb2e21cd8bea80a"></a>

```c
#define DNS_SD_MIN_LABELS 3
```

相关声明：[DNS_SD_MIN_LABELS](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#gaeec792bc3111e1961eb2e21cd8bea80a)。

完全限定名称（Fully-qualified Name）中的最少段数（Segments）。

<a id="r_ga269e2f3bbf15a5ccd81a444749faa384"></a>

```c
#define DNS_SD_MAX_LABELS 4
```

相关声明：[DNS_SD_MAX_LABELS](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga269e2f3bbf15a5ccd81a444749faa384)。

完全限定名称（Fully-qualified Name）中的最多段数（Segments）。

<a id="r_ga0c0060a680d5c4fe56f2815c920c3627"></a>

```c
#define DNS_SD_REGISTER_SERVICE(_id, _instance, _service, _proto, _domain, _text, _port)
```

相关声明：[DNS_SD_REGISTER_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga0c0060a680d5c4fe56f2815c920c3627)。

为 DNS 服务发现（DNS Service Discovery，DNS-SD）注册服务。

<a id="r_ga96abc525d755c138304f07cdd2d9e1c2"></a>

```c
#define DNS_SD_REGISTER_TCP_SERVICE(id, instance, service, domain, text, port)
```

相关声明：[DNS_SD_REGISTER_TCP_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga96abc525d755c138304f07cdd2d9e1c2)。

为 DNS 服务发现（DNS-SD）注册 TCP 服务。

<a id="r_gaf8abe0968552213d46b49be16c1f21d6"></a>

```c
#define DNS_SD_REGISTER_UDP_SERVICE(id, instance, service, domain, text, port)
```

相关声明：[DNS_SD_REGISTER_UDP_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#gaf8abe0968552213d46b49be16c1f21d6)。

为 DNS 服务发现（DNS-SD）注册 UDP 服务。

<a id="r_ga221216c5ffd142aa4c6cade4064d580f"></a>

```c
#define DNS_SD_EMPTY_TXT dns_sd_empty_txt
```

相关声明：[DNS_SD_EMPTY_TXT](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga221216c5ffd142aa4c6cade4064d580f)。

空 DNS-SD TXT 说明符（Specifier）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.3\_函数（Functions）

<a id="r_ga6d68e785607089df42d534c2f876c6d5"></a>

```c
static size_t dns_sd_txt_size (const struct dns_sd_rec *rec)
```

相关声明：[dns_sd_txt_size](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga6d68e785607089df42d534c2f876c6d5)、[dns_sd_rec](../network_application_model_reference/P025_dns_sd_rec_结构体.md)。

获取 DNS-SD TXT 数据大小（Data Size）。

<a id="r_gaeba098fa6d159067c70588cb60056277"></a>

```c
bool dns_sd_is_service_type_enumeration (const struct dns_sd_rec *rec)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[dns_sd_is_service_type_enumeration](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#gaeba098fa6d159067c70588cb60056277)、[dns_sd_rec](../network_application_model_reference/P025_dns_sd_rec_结构体.md)。

检查 `rec` 是否为 DNS-SD 服务类型枚举（Service Type Enumeration）。

<a id="r_ga328d71e26411460b1b329db8f1ebd37b"></a>

```c
void dns_sd_create_wildcard_filter (struct dns_sd_rec *filter)
```

相关声明：[dns_sd_create_wildcard_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga328d71e26411460b1b329db8f1ebd37b)、[dns_sd_rec](../network_application_model_reference/P025_dns_sd_rec_结构体.md)。

创建 DNS-SD 记录的通配过滤器（Wildcard Filter）。


## 6.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/sys/byteorder.h](../byteorder_reference/P002_系统字节序头文件源码.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P144_dns_sd.h_源码浏览.md)
- [dns_sd_rec](../network_application_model_reference/P025_dns_sd_rec_结构体.md)
- [DNS_SD_INSTANCE_MIN_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga4d1f5462555d6051bdeaa21b02e7aa6e)
- [RFC 1034 第 3.1 节。](https://datatracker.ietf.org/doc/html/rfc1034#section-3.1)
- [DNS_SD_INSTANCE_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga5c0993b8bc21d47fa15f56acb313ac31)
- [RFC 6763, section-7.2](https://datatracker.ietf.org/doc/html/rfc6763#section-7.2)
- [DNS_SD_SERVICE_MIN_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#gacc652552aa567206ab7a4d7d070d1fbc)
- [DNS_SD_SERVICE_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#gab4d208eac1491c45cb47e87c90a78c26)
- [DNS_SD_SERVICE_PREFIX](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga81cac0a52e58142e492bad244ff97490)
- [RFC 6763 第 4.1.2 节。](https://datatracker.ietf.org/doc/html/rfc6763#section-4.1.2)
- [DNS_SD_PROTO_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#gafb686ae445f5bd640176f59d62df2bdc)
- [DNS_SD_DOMAIN_MIN_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga19d655c1778143e2aed5d2d69a757422)
- [DNS_SD_DOMAIN_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#gaa93b197f2b9a3b13c7ed8f3c455f11cb)
- [DNS_SD_MIN_LABELS](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#gaeec792bc3111e1961eb2e21cd8bea80a)
- [DNS_SD_MAX_LABELS](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga269e2f3bbf15a5ccd81a444749faa384)
- [DNS_SD_REGISTER_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga0c0060a680d5c4fe56f2815c920c3627)
- [DNS_SD_REGISTER_TCP_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga96abc525d755c138304f07cdd2d9e1c2)
- [DNS_SD_REGISTER_UDP_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#gaf8abe0968552213d46b49be16c1f21d6)
- [DNS_SD_EMPTY_TXT](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga221216c5ffd142aa4c6cade4064d580f)
- [dns_sd_txt_size](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga6d68e785607089df42d534c2f876c6d5)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [dns_sd_is_service_type_enumeration](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#gaeba098fa6d159067c70588cb60056277)
- [dns_sd_create_wildcard_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga328d71e26411460b1b329db8f1ebd37b)

<a id="header-details"></a>

---

[上一章](P005_zephyr__bluetooth__mesh__dfu_cli.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__wifi__esp_wifi__esp_wifi_mesh.h_文件参考.md)
