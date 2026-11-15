---
id: learning.zephyr-docs.api-file-service-interface-reference.page-51
title: zephyr__net__tls_credentials.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tls__credentials_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_zephyr\_\_net\_\_tls\_credentials.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tls__credentials_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传输层安全（TLS）的凭据管理。

<a id="details"></a>

```c
#include <stddef.h>
#include <time.h>
```

查看此文件的源码。

传输层安全（TLS）凭据管理（Credentials Management），为应用程序提供配置 TLS 凭据的 API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 51.1\_宏定义（Macros）

<a id="r_ga79f3eea68c2706edd3320822968bd696"></a>

```c
#define SEC_TAG_TLS_INVALID (-1)
```

相关声明：[SEC_TAG_TLS_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga79f3eea68c2706edd3320822968bd696)。

无效的安全标签（Secure Tag）值。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 51.2\_类型定义（Typedefs）

<a id="r_gaadfe9694309e473f7be74ed98dfb36d3"></a>

```c
typedef int sec_tag_t
```

相关声明：[sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)。

安全标签（Secure Tag），用于引用 TLS 凭据（Credential）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 51.3\_枚举（Enumerations）

<a id="r_ga3a754894d0162634b59d60e319f37cd5"></a>

```c
enum tls_credential_type { TLS_CREDENTIAL_NONE , TLS_CREDENTIAL_CA_CERTIFICATE , TLS_CREDENTIAL_PUBLIC_CERTIFICATE , TLS_CREDENTIAL_PRIVATE_KEY , TLS_CREDENTIAL_PSK , TLS_CREDENTIAL_PSK_ID , TLS_CREDENTIAL_PRIVATE_KEY_PSA }
```

相关声明：[tls_credential_type](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga3a754894d0162634b59d60e319f37cd5)、[TLS_CREDENTIAL_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5a7009a9f266011529e64ec4e4c6692315)、[TLS_CREDENTIAL_CA_CERTIFICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5adcf949c1422f4d3b38795ae40d2321d5)、[TLS_CREDENTIAL_PUBLIC_CERTIFICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5acd8b96102765f7f2a83582eab80df3d8)、[TLS_CREDENTIAL_PRIVATE_KEY](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5a406e8bb1f992af5a72921f47b140840e)、[TLS_CREDENTIAL_PSK](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5accc6ad916ee6c6badafcc4c23e2a47df)、[TLS_CREDENTIAL_PSK_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5a1edcd43ba510558e4b1315e1bb86560d)、[TLS_CREDENTIAL_PRIVATE_KEY_PSA](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5ae7f4b9f4ed9865678d7cbdb741ca19e1)。

TLS 凭据类型（Credential Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 51.4\_函数（Functions）

<a id="r_ga640ff6dd3eb4d5017feaab6fab2bb2f7"></a>

```c
int tls_credential_add (sec_tag_t tag, enum tls_credential_type type, const void *cred, size_t credlen)
```

相关声明：[tls_credential_add](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga640ff6dd3eb4d5017feaab6fab2bb2f7)、[sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)、[tls_credential_type](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga3a754894d0162634b59d60e319f37cd5)。

添加 TLS 凭据（Credential）。

<a id="r_gac3ac4ca887faf6c1f2ae60c6a08f8795"></a>

```c
int tls_credential_get (sec_tag_t tag, enum tls_credential_type type, void *cred, size_t *credlen)
```

相关声明：[tls_credential_get](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gac3ac4ca887faf6c1f2ae60c6a08f8795)、[sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)、[tls_credential_type](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga3a754894d0162634b59d60e319f37cd5)。

获取 TLS 凭据（Credential）。

<a id="r_ga9d8b47a7a2675fb3b3c6ee346e925aca"></a>

```c
int tls_credential_delete (sec_tag_t tag, enum tls_credential_type type)
```

相关声明：[tls_credential_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga9d8b47a7a2675fb3b3c6ee346e925aca)、[sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)、[tls_credential_type](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga3a754894d0162634b59d60e319f37cd5)。

删除 TLS 凭据（Credential）。

<a id="r_ga7508492d623044d33406de5abdf29216"></a>

```c
int tls_credential_expiry (sec_tag_t tag, enum tls_credential_type type, time_t *expiry)
```

相关声明：[tls_credential_expiry](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga7508492d623044d33406de5abdf29216)、[sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)、[tls_credential_type](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga3a754894d0162634b59d60e319f37cd5)、[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)。

获取 TLS 凭据的到期时间（Expiry Time）。


## 51.5\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P870_tls_credentials.h_源码浏览.md)
- [SEC_TAG_TLS_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga79f3eea68c2706edd3320822968bd696)
- [sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)
- [tls_credential_type](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga3a754894d0162634b59d60e319f37cd5)
- [TLS_CREDENTIAL_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5a7009a9f266011529e64ec4e4c6692315)
- [TLS_CREDENTIAL_CA_CERTIFICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5adcf949c1422f4d3b38795ae40d2321d5)
- [TLS_CREDENTIAL_PUBLIC_CERTIFICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5acd8b96102765f7f2a83582eab80df3d8)
- [TLS_CREDENTIAL_PRIVATE_KEY](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5a406e8bb1f992af5a72921f47b140840e)
- [TLS_CREDENTIAL_PSK](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5accc6ad916ee6c6badafcc4c23e2a47df)
- [TLS_CREDENTIAL_PSK_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5a1edcd43ba510558e4b1315e1bb86560d)
- [TLS_CREDENTIAL_PRIVATE_KEY_PSA](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5ae7f4b9f4ed9865678d7cbdb741ca19e1)
- [tls_credential_add](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga640ff6dd3eb4d5017feaab6fab2bb2f7)
- [tls_credential_get](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gac3ac4ca887faf6c1f2ae60c6a08f8795)
- [tls_credential_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga9d8b47a7a2675fb3b3c6ee346e925aca)
- [tls_credential_expiry](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga7508492d623044d33406de5abdf29216)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)

<a id="header-details"></a>

---

[上一章](P050_zephyr__drivers__mfd__tla2528.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P052_zephyr__drivers__misc__tmc6460__tmc6460.h_文件参考.md)
