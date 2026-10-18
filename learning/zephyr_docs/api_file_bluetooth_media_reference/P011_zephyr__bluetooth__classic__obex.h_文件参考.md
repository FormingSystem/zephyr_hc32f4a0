---
id: learning.zephyr-docs.api-file-bluetooth-media-reference.page-11
title: zephyr__bluetooth__classic__obex.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/obex_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_bluetooth\_\_classic\_\_obex.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/obex_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel.h>
#include <string.h>
#include <errno.h>
#include <stdbool.h>
#include <zephyr/bluetooth/uuid.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_bt_5Fobex_5Fserver_5Fops"></a>

```c
struct bt_obex_server_ops
```

相关声明：[bt_obex_server_ops](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md)。

对象交换协议（OBEX）的服务器操作结构。

<a id="r_bt_5Fobex_5Fclient_5Fops"></a>

```c
struct bt_obex_client_ops
```

相关声明：[bt_obex_client_ops](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md)。

对象交换协议（OBEX）的客户端操作结构。

<a id="r_bt_5Fobex_5Ftransport_5Fops"></a>

```c
struct bt_obex_transport_ops
```

相关声明：[bt_obex_transport_ops](../bluetooth_service_model_reference/P134_bt_obex_transport_ops_结构体.md)。

对象交换协议（OBEX）的传输操作结构。

<a id="r_bt_5Fobex_5Fuuid"></a>

```c
union bt_obex_uuid
```

相关声明：[bt_obex_uuid](../bluetooth_service_model_reference/P189_bt_obex_uuid_联合体.md)。

<a id="r_bt_5Fobex_5Fserver"></a>

```c
struct bt_obex_server
```

相关声明：[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)。

对象交换协议（OBEX）的服务器结构。

<a id="r_bt_5Fobex_5Fclient"></a>

```c
struct bt_obex_client
```

相关声明：[bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)。

对象交换协议（OBEX）的客户端结构。

<a id="r_bt_5Fobex"></a>

```c
struct bt_obex
```

相关声明：[bt_obex](../bluetooth_service_model_reference/P127_bt_obex_结构体.md)。

对象交换协议（OBEX）结构。

<a id="r_bt_5Fobex_5Ftlv"></a>

```c
struct bt_obex_tlv
```

相关声明：[bt_obex_tlv](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md)。

蓝牙对象交换协议（Bluetooth OBEX）的类型-长度-值（TLV）三元组。

<a id="r_bt_5Fobex_5Fhdr"></a>

```c
struct bt_obex_hdr
```

相关声明：[bt_obex_hdr](../bluetooth_service_model_reference/P130_bt_obex_hdr_结构体.md)。

对象交换协议（OBEX）的头部结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.2\_宏定义（Macros）

<a id="r_ga6206007c2c3e50d997ae5a644ceae783"></a>

```c
#define BT_OBEX_MIN_MTU 255
```

相关声明：[BT_OBEX_MIN_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6206007c2c3e50d997ae5a644ceae783)。

<a id="r_ga534e9ffa9f7ba93eda049fd9022df69a"></a>

```c
#define BT_OBEX_HDR_LEN 3
```

相关声明：[BT_OBEX_HDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga534e9ffa9f7ba93eda049fd9022df69a)。

PUT 和 GET 请求及响应的对象交换（OBEX）数据包报头长度。

<a id="r_ga500dcfab79831c5d640406cff8c54f01"></a>

```c
#define BT_OBEX_PDU_LEN(mopl)
```

相关声明：[BT_OBEX_PDU_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga500dcfab79831c5d640406cff8c54f01)。

对象交换（OBEX）数据包的 PDU 数据长度上限。

<a id="r_ga5571666538c43d8d71dd17dc58d19f45"></a>

```c
#define BT_OBEX_HDR_LEN_OF_HEADER_BODY 3
```

相关声明：[BT_OBEX_HDR_LEN_OF_HEADER_BODY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga5571666538c43d8d71dd17dc58d19f45)。

OBEX 主体／主体结束报头（Body / End Body Header）的长度。

<a id="r_gab3db35da4b3daf626e89223262273fb9"></a>

```c
#define BT_OBEX_DATA_LEN_OF_HEADER_BODY(len)
```

相关声明：[BT_OBEX_DATA_LEN_OF_HEADER_BODY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab3db35da4b3daf626e89223262273fb9)。

添加的报头为主体／主体结束（Body / End Body）时，缓冲区的最大剩余长度。

<a id="r_ga3d89a9c04baec0be2dd6b9f922a7c985"></a>

```c
#define BT_OBEX_SEND_BUF_RESERVE 7
```

相关声明：[BT_OBEX_SEND_BUF_RESERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga3d89a9c04baec0be2dd6b9f922a7c985)。

<a id="r_ga6c6bd723b6b7c84d53ea0d0bc9787fbc"></a>

```c
#define BT_OBEX_CHALLENGE_TAG_NONCE 0x00
```

相关声明：[BT_OBEX_CHALLENGE_TAG_NONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6c6bd723b6b7c84d53ea0d0bc9787fbc)。

OBEX 摘要质询标记（Digest-challenge Tag）：Nonce，以字节串表示的一次性随机数。

<a id="r_gaab47709ef621b63172fa54314bf3eff0"></a>

```c
#define BT_OBEX_CHALLENGE_TAG_NONCE_LEN 16
```

相关声明：[BT_OBEX_CHALLENGE_TAG_NONCE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaab47709ef621b63172fa54314bf3eff0)。

OBEX 摘要质询的一次性随机数长度（Nonce Length），16 字节。

<a id="r_gae48159128c97a6579c8cbf12b5c934e4"></a>

```c
#define BT_OBEX_CHALLENGE_TAG_OPTIONS 0x01
```

相关声明：[BT_OBEX_CHALLENGE_TAG_OPTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gae48159128c97a6579c8cbf12b5c934e4)。

OBEX 摘要质询标记（Digest-challenge Tag）：Options，可选质询信息（Optional Challenge Information）。

<a id="r_ga40725e7d1882cd9f793dc490a9ad8341"></a>

```c
#define BT_OBEX_CHALLENGE_TAG_OPTIONS_LEN 1
```

相关声明：[BT_OBEX_CHALLENGE_TAG_OPTIONS_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga40725e7d1882cd9f793dc490a9ad8341)。

OBEX 摘要质询的选项长度（Options Length），1 字节。

<a id="r_ga4d936864173fe0218e660df7b53d666e"></a>

```c
#define BT_OBEX_CHALLENGE_TAG_OPTION_REQ_USER_ID BIT(0)
```

相关声明：[BT_OBEX_CHALLENGE_TAG_OPTION_REQ_USER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga4d936864173fe0218e660df7b53d666e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

选项位 0（BIT0）：设置时，必须在认证响应（Authenticate Response）中发送用户 ID（User Id）。

<a id="r_gad35d3b9c3a398b1f4bdba610c825aca3"></a>

```c
#define BT_OBEX_CHALLENGE_TAG_OPTION_ACCESS_MODE BIT(1)
```

相关声明：[BT_OBEX_CHALLENGE_TAG_OPTION_ACCESS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gad35d3b9c3a398b1f4bdba610c825aca3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

选项位 1（BIT1）：访问模式（Access Mode）；设置时为只读（Read Only），否则允许完全访问（Full Access）。

<a id="r_ga7957818ad49e8e406942dad698e2d089"></a>

```c
#define BT_OBEX_CHALLENGE_TAG_REALM 0x02
```

相关声明：[BT_OBEX_CHALLENGE_TAG_REALM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga7957818ad49e8e406942dad698e2d089)。

OBEX 摘要质询标记（Digest-challenge Tag）：Realm，一个可显示字符串，指示应使用哪个用户 ID 和／或密码。

<a id="r_ga69d4d1a8af96df807ab9f1ec5fc42503"></a>

```c
#define BT_OBEX_RESPONSE_TAG_REQ_DIGEST 0x00
```

相关声明：[BT_OBEX_RESPONSE_TAG_REQ_DIGEST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga69d4d1a8af96df807ab9f1ec5fc42503)。

OBEX 摘要响应标记（Digest-response Tag）：Request-digest，以字节串表示的请求摘要。

<a id="r_gacbae9ed1d18eaab7934258cbfe4fd62a"></a>

```c
#define BT_OBEX_RESPONSE_TAG_REQ_DIGEST_LEN 16
```

相关声明：[BT_OBEX_RESPONSE_TAG_REQ_DIGEST_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gacbae9ed1d18eaab7934258cbfe4fd62a)。

OBEX 摘要响应的请求摘要长度（Request-digest Length），16 字节。

<a id="r_gad466df7bba9c20ff47820121372193ec"></a>

```c
#define BT_OBEX_RESPONSE_TAG_USER_ID 0x01
```

相关声明：[BT_OBEX_RESPONSE_TAG_USER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gad466df7bba9c20ff47820121372193ec)。

OBEX 摘要响应标记（Digest-response Tag）：User Id，长度为 n 的用户 ID 字符串。

<a id="r_gacbdbc35907fcd1b5362fb108f7925412"></a>

```c
#define BT_OBEX_RESPONSE_TAG_NONCE 0x02
```

相关声明：[BT_OBEX_RESPONSE_TAG_NONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gacbdbc35907fcd1b5362fb108f7925412)。

OBEX 摘要响应标记（Digest-response Tag）：Nonce，即摘要质询字符串中发送的一次性随机数。

<a id="r_ga78897a868628d0dc9992ebb7d79e6dd5"></a>

```c
#define BT_OBEX_RESPONSE_TAG_NONCE_LEN 16
```

相关声明：[BT_OBEX_RESPONSE_TAG_NONCE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga78897a868628d0dc9992ebb7d79e6dd5)。

OBEX 摘要响应的一次性随机数长度（Nonce Length），16 字节。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.3\_枚举（Enumerations）

<a id="r_ga81b84c24a976c6c13d33eb23b0b10ae9"></a>

```c
enum bt_obex_rsp_code { BT_OBEX_RSP_CODE_CONTINUE = 0x90 , BT_OBEX_RSP_CODE_OK = 0xa0 , BT_OBEX_RSP_CODE_SUCCESS = 0xa0 , BT_OBEX_RSP_CODE_CREATED = 0xa1 , BT_OBEX_RSP_CODE_ACCEPTED = 0xa2 , BT_OBEX_RSP_CODE_NON_AUTH_INFO = 0xa3 , BT_OBEX_RSP_CODE_NO_CONTENT = 0xa4 , BT_OBEX_RSP_CODE_RESET_CONTENT = 0xa5 , BT_OBEX_RSP_CODE_PARTIAL_CONTENT = 0xa6 , BT_OBEX_RSP_CODE_MULTI_CHOICES = 0xb0 , BT_OBEX_RSP_CODE_MOVED_PERM = 0xb1 , BT_OBEX_RSP_CODE_MOVED_TEMP = 0xb2 , BT_OBEX_RSP_CODE_SEE_OTHER = 0xb3 , BT_OBEX_RSP_CODE_NOT_MODIFIED = 0xb4 , BT_OBEX_RSP_CODE_USE_PROXY = 0xb5 , BT_OBEX_RSP_CODE_BAD_REQ = 0xc0 , BT_OBEX_RSP_CODE_UNAUTH = 0xc1 , BT_OBEX_RSP_CODE_PAY_REQ = 0xc2 , BT_OBEX_RSP_CODE_FORBIDDEN = 0xc3 , BT_OBEX_RSP_CODE_NOT_FOUND = 0xc4 , BT_OBEX_RSP_CODE_NOT_ALLOW = 0xc5 , BT_OBEX_RSP_CODE_NOT_ACCEPT = 0xc6 , BT_OBEX_RSP_CODE_PROXY_AUTH_REQ = 0xc7 , BT_OBEX_RSP_CODE_REQ_TIMEOUT = 0xc8 , BT_OBEX_RSP_CODE_CONFLICT = 0xc9 , BT_OBEX_RSP_CODE_GONE = 0xca , BT_OBEX_RSP_CODE_LEN_REQ = 0xcb , BT_OBEX_RSP_CODE_PRECON_FAIL = 0xcc , BT_OBEX_RSP_CODE_ENTITY_TOO_LARGE = 0xcd , BT_OBEX_RSP_CODE_URL_TOO_LARGE = 0xce , BT_OBEX_RSP_CODE_UNSUPP_MEDIA_TYPE = 0xcf , BT_OBEX_RSP_CODE_INTER_ERROR = 0xd0 , BT_OBEX_RSP_CODE_NOT_IMPL = 0xd1 , BT_OBEX_RSP_CODE_BAD_GATEWAY = 0xd2 , BT_OBEX_RSP_CODE_UNAVAIL = 0xd3 , BT_OBEX_RSP_CODE_GATEWAY_TIMEOUT = 0xd4 , BT_OBEX_RSP_CODE_VER_UNSUPP = 0xd5 , BT_OBEX_RSP_CODE_DB_FULL = 0xe0 , BT_OBEX_RSP_CODE_DB_LOCK = 0xe1 }
```

相关声明：[bt_obex_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga81b84c24a976c6c13d33eb23b0b10ae9)、[BT_OBEX_RSP_CODE_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a7e38ca653283f53b62fa4b21f48d998a)、[BT_OBEX_RSP_CODE_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a881d3098a198dc1eced2150a213d1054)、[BT_OBEX_RSP_CODE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9af449d3c85fbec550c76e29287a626789)、[BT_OBEX_RSP_CODE_CREATED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a955b065ee2543e0bc31a03d9bd15900b)、[BT_OBEX_RSP_CODE_ACCEPTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aba13d60d30201bdb13f01c1ee2ff7916)、[BT_OBEX_RSP_CODE_NON_AUTH_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a2f88a5bf5bb9690d8db856bf02f305d8)、[BT_OBEX_RSP_CODE_NO_CONTENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a32d55bb3c73ecb8cdf5f76c6724c9884)、[BT_OBEX_RSP_CODE_RESET_CONTENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a4e8f5c004cf3ef6e9ad1b5be1d106a39)、[BT_OBEX_RSP_CODE_PARTIAL_CONTENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9afcf5fc7c81eed4d5b67def413535a46f)、[BT_OBEX_RSP_CODE_MULTI_CHOICES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a3b948c9bdf3bebd2b0e7cf34960c19b2)、[BT_OBEX_RSP_CODE_MOVED_PERM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aa5252b1eaa5fa7d41052d97af24fd4d7)、[BT_OBEX_RSP_CODE_MOVED_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9abf41a7e722e12bd71a93093e36bfc2bf)、[BT_OBEX_RSP_CODE_SEE_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ac25903e3a229ac50ecea485eca8c5236)、[BT_OBEX_RSP_CODE_NOT_MODIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ab33e506b470df404119976d5460b6bda)、[BT_OBEX_RSP_CODE_USE_PROXY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ac19ffb8b59a7cb1a3e0c1edfe91dd472)、[BT_OBEX_RSP_CODE_BAD_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a2d2ff2c6ec42d9e80dc4e841e19d31ee)、[BT_OBEX_RSP_CODE_UNAUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9acfbc9161dddf6859dd8e8ac70cf8d446)、[BT_OBEX_RSP_CODE_PAY_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a5fc2aa165ffea0caeb59e05ee951e3dc)、[BT_OBEX_RSP_CODE_FORBIDDEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a4b7a12b0e11747d1a470e8f559b55ea8)、[BT_OBEX_RSP_CODE_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a2b91abe9e010465f9514f37477b993e0)、[BT_OBEX_RSP_CODE_NOT_ALLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a3f510d3b203257a37d2ef005d4517a67)、[BT_OBEX_RSP_CODE_NOT_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a48f773daa7f2dabaadc37142ec32ffd1)、[BT_OBEX_RSP_CODE_PROXY_AUTH_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aeb2abeaf682a47a46291784c2b24b793)、[BT_OBEX_RSP_CODE_REQ_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a3f60fb4d3444570c9a73f43b7c9bdc1f)、[BT_OBEX_RSP_CODE_CONFLICT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aeca60f95428624932314fc8f3b4a1b79)、[BT_OBEX_RSP_CODE_GONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aa34ece6da3fe28ec3747ce8621da7e31)、[BT_OBEX_RSP_CODE_LEN_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ac0faf667c93a32293fbacca2e1696938)、[BT_OBEX_RSP_CODE_PRECON_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aacc05fd2528e29fbd53eb5ff940f9079)、[BT_OBEX_RSP_CODE_ENTITY_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a21783b5d9036d61304a7acb3b03d0913)、[BT_OBEX_RSP_CODE_URL_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9adc906b909c09a8a1cc421e8f4efc1444)、[BT_OBEX_RSP_CODE_UNSUPP_MEDIA_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a650312673ccc758b735bcead8f1009ef)、[BT_OBEX_RSP_CODE_INTER_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9add3501ba98c972e0e01a6fa898612bd4)、[BT_OBEX_RSP_CODE_NOT_IMPL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aba8108ac6b050d3dad845a5e8cb42eaf)、[BT_OBEX_RSP_CODE_BAD_GATEWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ac39d7d6fa1fcb0cc5be0ad25aa2574f9)、[BT_OBEX_RSP_CODE_UNAVAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a613e95b96eaba0522070b620b4b90953)、[BT_OBEX_RSP_CODE_GATEWAY_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a850bbc0fd1810e3a74f2a057e8358b48)、[BT_OBEX_RSP_CODE_VER_UNSUPP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ab41b31b5e85dcb2981b3f6e9bbba2dd9)、[BT_OBEX_RSP_CODE_DB_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ad65c4246d828770010748b1faa6af71c)、[BT_OBEX_RSP_CODE_DB_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a5c0692d0e3db45a898426b2751e682a0)。

OBEX 响应码（Response Code）。

<a id="r_ga3c893652eb9a5f0bf699d357caf40948"></a>

```c
enum bt_obex_header_id { BT_OBEX_HEADER_ID_COUNT = 0xC0 , BT_OBEX_HEADER_ID_NAME = 0x01 , BT_OBEX_HEADER_ID_TYPE = 0x42 , BT_OBEX_HEADER_ID_LEN = 0xC3 , BT_OBEX_HEADER_ID_TIME_ISO_8601 = 0x44 , BT_OBEX_HEADER_ID_TIME = 0xC4 , BT_OBEX_HEADER_ID_DES = 0x05 , BT_OBEX_HEADER_ID_TARGET = 0x46 , BT_OBEX_HEADER_ID_HTTP = 0x47 , BT_OBEX_HEADER_ID_BODY = 0x48 , BT_OBEX_HEADER_ID_END_BODY = 0x49 , BT_OBEX_HEADER_ID_WHO = 0x4A , BT_OBEX_HEADER_ID_CONN_ID = 0xCB , BT_OBEX_HEADER_ID_APP_PARAM = 0x4C , BT_OBEX_HEADER_ID_AUTH_CHALLENGE = 0x4D , BT_OBEX_HEADER_ID_AUTH_RSP = 0x4E , BT_OBEX_HEADER_ID_CREATE_ID = 0xCF , BT_OBEX_HEADER_ID_WAN_UUID = 0x50 , BT_OBEX_HEADER_ID_OBJECT_CLASS = 0x51 , BT_OBEX_HEADER_ID_SESSION_PARAM = 0x52 , BT_OBEX_HEADER_ID_SESSION_SEQ_NUM = 0x93 , BT_OBEX_HEADER_ID_ACTION_ID = 0x94 , BT_OBEX_HEADER_ID_DEST_NAME = 0x15 , BT_OBEX_HEADER_ID_PERM = 0xD6 , BT_OBEX_HEADER_ID_SRM = 0x97 , BT_OBEX_HEADER_ID_SRM_PARAM = 0x98 }
```

相关声明：[bt_obex_header_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga3c893652eb9a5f0bf699d357caf40948)、[BT_OBEX_HEADER_ID_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a6119d9faab405c63a25791edc9588889)、[BT_OBEX_HEADER_ID_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948adf199ff987c26bd8d6301c409fb5f6a4)、[BT_OBEX_HEADER_ID_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a8bfeff22eabea432eb5863a974adb745)、[BT_OBEX_HEADER_ID_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948ae075bf9dd7e57c66613ffb3de84f09bb)、[BT_OBEX_HEADER_ID_TIME_ISO_8601](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948ac2899a8dca76bfd88bb94d43a3c8a693)、[BT_OBEX_HEADER_ID_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a4fad7112257bd771e412eefd0c1e8bcc)、[BT_OBEX_HEADER_ID_DES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a0fb867c69fb0c8680170359a41f2a3b1)、[BT_OBEX_HEADER_ID_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a5929acc483779593b1b5c7b702b17976)、[BT_OBEX_HEADER_ID_HTTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a46735e651f7f378a3efb1be1a232e4ca)、[BT_OBEX_HEADER_ID_BODY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a3264aa53da0fd7ec6611b8a20a8745f4)、[BT_OBEX_HEADER_ID_END_BODY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948aaa78dab2eda48ebd5d594024b53bec6b)、[BT_OBEX_HEADER_ID_WHO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948ab28b3ee885c373ca83a745fcd019e2e4)、[BT_OBEX_HEADER_ID_CONN_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a3417001aed5d114492dcbe2c29496a1b)、[BT_OBEX_HEADER_ID_APP_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a6dac6844a5db11dbc0e43613a32c13a9)、[BT_OBEX_HEADER_ID_AUTH_CHALLENGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948aa48d582e278e748574d57818a7f5daf1)、[BT_OBEX_HEADER_ID_AUTH_RSP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a97c1dfb166ac549576d30cadd156365f)、[BT_OBEX_HEADER_ID_CREATE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a31bec44f1240f21545f917eedd31026e)、[BT_OBEX_HEADER_ID_WAN_UUID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a65e148b396f75cd55b992df84d5176ff)、[BT_OBEX_HEADER_ID_OBJECT_CLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a5b723fde52df0965299d2f79e433c0a2)、[BT_OBEX_HEADER_ID_SESSION_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948afe34bec1dba1d1fca717f3ffa7c20628)、[BT_OBEX_HEADER_ID_SESSION_SEQ_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a3d42ab8b6a28f9062a97e2b1a9fa7c16)、[BT_OBEX_HEADER_ID_ACTION_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a01e2d13304514242e954d45e74e3fcba)、[BT_OBEX_HEADER_ID_DEST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948ae5149b2da2cfb3c2e832f51282bc08d6)、[BT_OBEX_HEADER_ID_PERM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a6aad7cbbcbebe670d370919fbdc61c19)、[BT_OBEX_HEADER_ID_SRM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948aa722c75042f0db4fba5c6a90516494b1)、[BT_OBEX_HEADER_ID_SRM_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948adda0f643d1c2ebd20d4c9d5644ef6b2c)。

OBEX 报头 ID（Header ID）。

<a id="r_ga622610a779a2e050e9a05c7eae945b3e"></a>

```c
enum bt_obex_state { BT_OBEX_DISCONNECTED , BT_OBEX_CONNECTING , BT_OBEX_CONNECTED , BT_OBEX_DISCONNECTING }
```

相关声明：[bt_obex_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga622610a779a2e050e9a05c7eae945b3e)、[BT_OBEX_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga622610a779a2e050e9a05c7eae945b3ead7138e7373f5562faf13faa8bca424e6)、[BT_OBEX_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga622610a779a2e050e9a05c7eae945b3ea8743efcfd509ba7b156ac91a3c928614)、[BT_OBEX_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga622610a779a2e050e9a05c7eae945b3ea15ddd595c7832a8bfd382f87b938723b)、[BT_OBEX_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga622610a779a2e050e9a05c7eae945b3eae41568fe4c0d0db81ff60f41be6443a5)。

OBEX 生命周期状态（Life-span States）。

<a id="r_gab5f7e6a6c7503f97a851f48c70162483"></a>

```c
enum bt_obex_setpath_flags { BT_OBEX_SETPATH_FLAG_BACKUP = (1UL << (0U)) , BT_OBEX_SETPATH_FLAG_NO_CREATE = (1UL << (1U)) }
```

相关声明：[bt_obex_setpath_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab5f7e6a6c7503f97a851f48c70162483)、[BT_OBEX_SETPATH_FLAG_BACKUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ggab5f7e6a6c7503f97a851f48c70162483a9f89d8219783650a02e8ceb3faf6bd75)、[BT_OBEX_SETPATH_FLAG_NO_CREATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ggab5f7e6a6c7503f97a851f48c70162483ae47e6f7c5a8da44615e7245c5e1cd553)。

OBEX 设置路径操作标志（SetPath Operation Flags）。

<a id="r_ga12730d705667c2717c05a75cdfc07281"></a>

```c
enum bt_obex_action_id { BT_OBEX_ACTION_COPY = 0x00 , BT_OBEX_ACTION_MOVE_RENAME = 0x01 , BT_OBEX_ACTION_SET_PERM = 0x02 }
```

相关声明：[bt_obex_action_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga12730d705667c2717c05a75cdfc07281)、[BT_OBEX_ACTION_COPY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga12730d705667c2717c05a75cdfc07281abb151a8123c7e6826a052ab252455aee)、[BT_OBEX_ACTION_MOVE_RENAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga12730d705667c2717c05a75cdfc07281a7c57548121adf0afe43066070ef4b1fa)、[BT_OBEX_ACTION_SET_PERM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga12730d705667c2717c05a75cdfc07281a711263abb984488b8c7273052fb76ae0)。

OBEX 动作（Actions）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.4\_函数（Functions）

<a id="r_ga7cb42acb39c601375ef7c73f6be7e6af"></a>

```c
static const char * bt_obex_rsp_code_to_str (enum bt_obex_rsp_code rsp_code)
```

相关声明：[bt_obex_rsp_code_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga7cb42acb39c601375ef7c73f6be7e6af)、[bt_obex_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga81b84c24a976c6c13d33eb23b0b10ae9)。

将 OBEX 响应码（Response Code）转换为字符串。

<a id="r_ga1df3928a40f544ffb98b5eb1ceac62dd"></a>

```c
int bt_obex_server_register (struct bt_obex_server *server, const struct bt_uuid_128 *uuid)
```

相关声明：[bt_obex_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga1df3928a40f544ffb98b5eb1ceac62dd)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)。

注册 OBEX 服务器（Server）。

<a id="r_ga642bfabb90d6576f92c5b546a592ec17"></a>

```c
int bt_obex_server_unregister (struct bt_obex_server *server)
```

相关声明：[bt_obex_server_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga642bfabb90d6576f92c5b546a592ec17)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)。

注销 OBEX 服务器（Server）。

<a id="r_ga21afebccbd592381fb1569feaff98511"></a>

```c
int bt_obex_connect (struct bt_obex_client *client, uint16_t mopl, struct net_buf *buf)
```

相关声明：[bt_obex_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga21afebccbd592381fb1569feaff98511)、[bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 连接请求（connect request）。

<a id="r_gad91f69ba1b6780501722221bc516db4b"></a>

```c
int bt_obex_connect_rsp (struct bt_obex_server *server, uint8_t rsp_code, uint16_t mopl, struct net_buf *buf)
```

相关声明：[bt_obex_connect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gad91f69ba1b6780501722221bc516db4b)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 连接响应（connect response）。

<a id="r_ga107787f08e55bf2740cc14cb5614bdbf"></a>

```c
int bt_obex_disconnect (struct bt_obex_client *client, struct net_buf *buf)
```

相关声明：[bt_obex_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga107787f08e55bf2740cc14cb5614bdbf)、[bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 断开连接请求（disconnect request）。

<a id="r_gac7763a310a553b3ba3c6b8b06951f191"></a>

```c
int bt_obex_disconnect_rsp (struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_obex_disconnect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gac7763a310a553b3ba3c6b8b06951f191)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 断开连接响应（disconnect response）。

<a id="r_ga1d8684307899b1bd3724cb3aa996c53e"></a>

```c
int bt_obex_put (struct bt_obex_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_obex_put](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga1d8684307899b1bd3724cb3aa996c53e)、[bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 放入请求（put request）。

<a id="r_gab5dfc5988d17ef0b79b84fd4c96dc60a"></a>

```c
int bt_obex_put_rsp (struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_obex_put_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab5dfc5988d17ef0b79b84fd4c96dc60a)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 放入响应（put response）。

<a id="r_gabd3ff76e8a39e5944daa944f38a63c5f"></a>

```c
int bt_obex_get (struct bt_obex_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_obex_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gabd3ff76e8a39e5944daa944f38a63c5f)、[bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 获取请求（get request）。

<a id="r_ga3e9415fa4595d17676ada6622c9fd475"></a>

```c
int bt_obex_get_rsp (struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_obex_get_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga3e9415fa4595d17676ada6622c9fd475)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 获取响应（get response）。

<a id="r_gafa2e01166c3177fe3aea937632fb52b7"></a>

```c
int bt_obex_abort (struct bt_obex_client *client, struct net_buf *buf)
```

相关声明：[bt_obex_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gafa2e01166c3177fe3aea937632fb52b7)、[bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 中止请求（abort request）。

<a id="r_ga6f9de12183c445557f952fe2b49e3029"></a>

```c
int bt_obex_abort_rsp (struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_obex_abort_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6f9de12183c445557f952fe2b49e3029)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 中止响应（abort response）。

<a id="r_ga6d61b4421ad1e56cc2ae611ec77e561e"></a>

```c
int bt_obex_setpath (struct bt_obex_client *client, uint8_t flags, struct net_buf *buf)
```

相关声明：[bt_obex_setpath](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6d61b4421ad1e56cc2ae611ec77e561e)、[bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 设置路径请求（setpath request）。

<a id="r_ga13836db790849b5ec6b52bcb97c84505"></a>

```c
int bt_obex_setpath_rsp (struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_obex_setpath_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga13836db790849b5ec6b52bcb97c84505)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 设置路径响应（setpath response）。

<a id="r_gab4b0a3533c7ec044efbee05c852d4f09"></a>

```c
int bt_obex_action (struct bt_obex_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_obex_action](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab4b0a3533c7ec044efbee05c852d4f09)、[bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 动作请求（action request）。

<a id="r_gae178bf14d0495ad1e1aa5f7b4d8e1652"></a>

```c
int bt_obex_action_rsp (struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_obex_action_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gae178bf14d0495ad1e1aa5f7b4d8e1652)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 动作响应（action response）。

<a id="r_ga14c8efe9c8a99e2736552d59972e7b23"></a>

```c
int bt_obex_add_header_count (struct net_buf *buf, uint32_t count)
```

相关声明：[bt_obex_add_header_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga14c8efe9c8a99e2736552d59972e7b23)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

添加报头（Add Header）：对象数量（Number of Objects），供 Connect 使用。

<a id="r_ga9cd4c8342f67b53a3c3177a51f8887cb"></a>

```c
int bt_obex_add_header_name (struct net_buf *buf, uint16_t len, const uint8_t *name)
```

相关声明：[bt_obex_add_header_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga9cd4c8342f67b53a3c3177a51f8887cb)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：对象名称（Object Name），通常为文件名。

<a id="r_gadd9f9b4cb50eb51df05c60705223e53b"></a>

```c
int bt_obex_add_header_type (struct net_buf *buf, uint16_t len, const uint8_t *type)
```

相关声明：[bt_obex_add_header_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gadd9f9b4cb50eb51df05c60705223e53b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：对象类型（Object Type），例如（原文此处未列出示例）。

<a id="r_ga0d27f09e3b8ea5636f0a34cf8729abaf"></a>

```c
int bt_obex_add_header_len (struct net_buf *buf, uint32_t len)
```

相关声明：[bt_obex_add_header_len](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga0d27f09e3b8ea5636f0a34cf8729abaf)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

添加报头（Add Header）：对象长度（Object Length），单位为字节。

<a id="r_ga877d67e0a4135cabf8b5fddab4d014c6"></a>

```c
int bt_obex_add_header_time_iso_8601 (struct net_buf *buf, uint16_t len, const uint8_t *t)
```

相关声明：[bt_obex_add_header_time_iso_8601](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga877d67e0a4135cabf8b5fddab4d014c6)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：日期／时间戳（Date/Time Stamp），ISO 8601 版本，为首选形式。

<a id="r_ga249e8b35b98f564d57dc1d644228b8f2"></a>

```c
int bt_obex_add_header_time (struct net_buf *buf, uint32_t t)
```

相关声明：[bt_obex_add_header_time](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga249e8b35b98f564d57dc1d644228b8f2)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

添加报头（Add Header）：日期／时间戳（Date/Time Stamp），4 字节版本，仅用于兼容。

<a id="r_gaedc6f39972a5414d085ce17b09ffd121"></a>

```c
int bt_obex_add_header_description (struct net_buf *buf, uint16_t len, const uint8_t *dec)
```

相关声明：[bt_obex_add_header_description](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaedc6f39972a5414d085ce17b09ffd121)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：对象的文本描述（Text Description）。

<a id="r_gac778e8ff0ac7e74795b107750a4a6719"></a>

```c
int bt_obex_add_header_target (struct net_buf *buf, uint16_t len, const uint8_t *target)
```

相关声明：[bt_obex_add_header_target](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gac778e8ff0ac7e74795b107750a4a6719)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：操作目标服务的名称（Service Name）。

<a id="r_ga6392da7ce8009eb95ab8c8a4d45fcb40"></a>

```c
int bt_obex_add_header_http (struct net_buf *buf, uint16_t len, const uint8_t *http)
```

相关声明：[bt_obex_add_header_http](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6392da7ce8009eb95ab8c8a4d45fcb40)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：一个 HTTP 1.x 报头（Header）。

<a id="r_gad1b3c22eea0915b962d7ab1e27726fe2"></a>

```c
int bt_obex_add_header_body (struct net_buf *buf, uint16_t len, const uint8_t *body)
```

相关声明：[bt_obex_add_header_body](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gad1b3c22eea0915b962d7ab1e27726fe2)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：对象主体的一个块（Body Chunk）。

<a id="r_ga805f13b12c7ce23057cb983d7159c36b"></a>

```c
int bt_obex_add_header_end_body (struct net_buf *buf, uint16_t len, const uint8_t *body)
```

相关声明：[bt_obex_add_header_end_body](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga805f13b12c7ce23057cb983d7159c36b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：对象主体的最后一个块（Final Body Chunk）。

<a id="r_gadf2d0b93618e0e29341bc21dfd44954f"></a>

```c
static int bt_obex_add_header_body_or_end_body (struct net_buf *buf, uint16_t mopl, uint16_t len, const uint8_t *body, uint16_t *added_len)
```

相关声明：[bt_obex_add_header_body_or_end_body](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gadf2d0b93618e0e29341bc21dfd44954f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

添加报头（Add Header）：对象主体的一个块（Body Chunk），可能是最后一个块。

<a id="r_ga56690794dc07dfa598ae2ac68bc90aa0"></a>

```c
int bt_obex_add_header_who (struct net_buf *buf, uint16_t len, const uint8_t *who)
```

相关声明：[bt_obex_add_header_who](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga56690794dc07dfa598ae2ac68bc90aa0)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：标识 OBEX 应用，用于判断是否正在与对等端通信。

<a id="r_gadc92dff93ef2051ff8b3b277a1bc1f17"></a>

```c
int bt_obex_add_header_conn_id (struct net_buf *buf, uint32_t conn_id)
```

相关声明：[bt_obex_add_header_conn_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gadc92dff93ef2051ff8b3b277a1bc1f17)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

添加报头（Add Header）：用于 OBEX 连接复用（Connection Multiplexing）的标识符。

<a id="r_gaeacfe7cb654bf33e7b387358a19fd3d3"></a>

```c
int bt_obex_add_header_app_param (struct net_buf *buf, size_t count, const struct bt_obex_tlv data[])
```

相关声明：[bt_obex_add_header_app_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaeacfe7cb654bf33e7b387358a19fd3d3)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_obex_tlv](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md)。

添加报头（Add Header）：扩展应用请求与响应信息（Extended Application Request & Response Information）。

<a id="r_gacfc897d66e8c14629fa4d94f3782c741"></a>

```c
int bt_obex_add_header_auth_challenge (struct net_buf *buf, size_t count, const struct bt_obex_tlv data[])
```

相关声明：[bt_obex_add_header_auth_challenge](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gacfc897d66e8c14629fa4d94f3782c741)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_obex_tlv](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md)。

添加报头（Add Header）：认证摘要质询（Authentication Digest-challenge）。

<a id="r_ga5433561f0e9bad6da2d94dccca1578de"></a>

```c
int bt_obex_add_header_auth_rsp (struct net_buf *buf, size_t count, const struct bt_obex_tlv data[])
```

相关声明：[bt_obex_add_header_auth_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga5433561f0e9bad6da2d94dccca1578de)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_obex_tlv](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md)。

添加报头（Add Header）：认证摘要响应（Authentication Digest-response）。

<a id="r_ga14c619eef70addc01d13841eda2d8f89"></a>

```c
int bt_obex_add_header_creator_id (struct net_buf *buf, uint32_t creator_id)
```

相关声明：[bt_obex_add_header_creator_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga14c619eef70addc01d13841eda2d8f89)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

添加报头（Add Header）：指示对象创建者（Object Creator）。

<a id="r_ga111cd19449aba6fd0e667551874af0cf"></a>

```c
int bt_obex_add_header_wan_uuid (struct net_buf *buf, uint16_t len, const uint8_t *uuid)
```

相关声明：[bt_obex_add_header_wan_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga111cd19449aba6fd0e667551874af0cf)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)。

添加报头（Add Header）：唯一标识网络客户端（Network Client），即 OBEX 服务器。

<a id="r_ga7473f42bef1409100886f7812a71a1dc"></a>

```c
int bt_obex_add_header_obj_class (struct net_buf *buf, uint16_t len, const uint8_t *obj_class)
```

相关声明：[bt_obex_add_header_obj_class](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga7473f42bef1409100886f7812a71a1dc)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：对象的 OBEX 对象类（Object Class）。

<a id="r_gac47ddfe8cfe1e595a1821f32415d14eb"></a>

```c
int bt_obex_add_header_session_param (struct net_buf *buf, uint16_t len, const uint8_t *session_param)
```

相关声明：[bt_obex_add_header_session_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gac47ddfe8cfe1e595a1821f32415d14eb)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：会话命令／响应（Session Commands/Responses）使用的参数。

<a id="r_gad4a84068ce8c7c37b5189d366b771235"></a>

```c
int bt_obex_add_header_session_seq_number (struct net_buf *buf, uint32_t session_seq_number)
```

相关声明：[bt_obex_add_header_session_seq_number](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gad4a84068ce8c7c37b5189d366b771235)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

添加报头（Add Header）：每个 OBEX 数据包中用于保证可靠性的序列号（Sequence Number）。

<a id="r_ga58034dc9ba274030eea5bc3980e2ff95"></a>

```c
int bt_obex_add_header_action_id (struct net_buf *buf, uint8_t action_id)
```

相关声明：[bt_obex_add_header_action_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga58034dc9ba274030eea5bc3980e2ff95)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：指定要执行的动作（Action），供 ACTION 操作使用。

<a id="r_ga4463514cf369beb882fec9ab15904821"></a>

```c
int bt_obex_add_header_dest_name (struct net_buf *buf, uint16_t len, const uint8_t *dest_name)
```

相关声明：[bt_obex_add_header_dest_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga4463514cf369beb882fec9ab15904821)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：目标对象名称（Destination Object Name），供某些 ACTION 操作使用。

<a id="r_ga4b7c08fd620fdc1ff28a4714c84b6e30"></a>

```c
int bt_obex_add_header_perm (struct net_buf *buf, uint32_t perm)
```

相关声明：[bt_obex_add_header_perm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga4b7c08fd620fdc1ff28a4714c84b6e30)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

添加报头（Add Header）：用于设置权限（Permissions）的 4 字节位掩码。

<a id="r_ga23ed862cc6149a71793d02d89fb98cdc"></a>

```c
int bt_obex_add_header_srm (struct net_buf *buf, uint8_t srm)
```

相关声明：[bt_obex_add_header_srm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga23ed862cc6149a71793d02d89fb98cdc)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：用于设置单响应模式（Single Response Mode，SRM）的 1 字节值。

<a id="r_gaaa8a9630b0bf5597ca620b864fdafa87"></a>

```c
int bt_obex_add_header_srm_param (struct net_buf *buf, uint8_t srm_param)
```

相关声明：[bt_obex_add_header_srm_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaaa8a9630b0bf5597ca620b864fdafa87)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：单响应模式参数（Single Response Mode Parameter，SRM）。

<a id="r_ga5c93e9786adfb45a60a911087f859757"></a>

```c
int bt_obex_header_parse (struct net_buf *buf, bool(*func)(struct bt_obex_hdr *hdr, void *user_data), void *user_data)
```

相关声明：[bt_obex_header_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga5c93e9786adfb45a60a911087f859757)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_obex_hdr](../bluetooth_service_model_reference/P130_bt_obex_hdr_结构体.md)。

解析 OBEX 报头（Header）的辅助函数。

<a id="r_ga1e9b6dd9a8816ce87235b6b3d723541c"></a>

```c
int bt_obex_get_header_count (struct net_buf *buf, uint32_t *count)
```

相关声明：[bt_obex_get_header_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga1e9b6dd9a8816ce87235b6b3d723541c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取报头值（Get Header Value）：对象数量（Number of Objects），供 Connect 使用。

<a id="r_gabef4622fa48b493f6d6ad5d1ecb65726"></a>

```c
int bt_obex_get_header_name (struct net_buf *buf, uint16_t *len, const uint8_t **name)
```

相关声明：[bt_obex_get_header_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gabef4622fa48b493f6d6ad5d1ecb65726)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：对象名称（Object Name），通常为文件名。

<a id="r_gabcfa9b33c0f91fbcf787d58e1f1bba41"></a>

```c
int bt_obex_get_header_type (struct net_buf *buf, uint16_t *len, const uint8_t **type)
```

相关声明：[bt_obex_get_header_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gabcfa9b33c0f91fbcf787d58e1f1bba41)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：对象类型（Object Type），例如（原文此处未列出示例）。

<a id="r_ga18ce5303b138959481666c0b8101f59e"></a>

```c
int bt_obex_get_header_len (struct net_buf *buf, uint32_t *len)
```

相关声明：[bt_obex_get_header_len](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga18ce5303b138959481666c0b8101f59e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取报头值（Get Header Value）：对象长度（Object Length），单位为字节。

<a id="r_gacee063f6b53b85bad52a519cd1c794c5"></a>

```c
int bt_obex_get_header_time_iso_8601 (struct net_buf *buf, uint16_t *len, const uint8_t **t)
```

相关声明：[bt_obex_get_header_time_iso_8601](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gacee063f6b53b85bad52a519cd1c794c5)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：日期／时间戳（Date/Time Stamp），ISO 8601 版本，为首选形式。

<a id="r_ga367337d0f002a046248e92f3578efbb6"></a>

```c
int bt_obex_get_header_time (struct net_buf *buf, uint32_t *t)
```

相关声明：[bt_obex_get_header_time](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga367337d0f002a046248e92f3578efbb6)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取报头值（Get Header Value）：日期／时间戳（Date/Time Stamp），4 字节版本，仅用于兼容。

<a id="r_ga3d805f241fc507587445b3204070055e"></a>

```c
int bt_obex_get_header_description (struct net_buf *buf, uint16_t *len, const uint8_t **dec)
```

相关声明：[bt_obex_get_header_description](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga3d805f241fc507587445b3204070055e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：对象的文本描述（Text Description）。

<a id="r_ga49265f0aec21d8c33f56eb44723dabba"></a>

```c
int bt_obex_get_header_target (struct net_buf *buf, uint16_t *len, const uint8_t **target)
```

相关声明：[bt_obex_get_header_target](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga49265f0aec21d8c33f56eb44723dabba)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：操作目标服务的名称（Service Name）。

<a id="r_ga5a181f7779df1ed2919ba3a94a630df4"></a>

```c
int bt_obex_get_header_http (struct net_buf *buf, uint16_t *len, const uint8_t **http)
```

相关声明：[bt_obex_get_header_http](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga5a181f7779df1ed2919ba3a94a630df4)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：一个 HTTP 1.x 报头（Header）。

<a id="r_gaba71a8b3b8adc251a5a87fa60848bb3c"></a>

```c
int bt_obex_get_header_body (struct net_buf *buf, uint16_t *len, const uint8_t **body)
```

相关声明：[bt_obex_get_header_body](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaba71a8b3b8adc251a5a87fa60848bb3c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：对象主体的一个块（Body Chunk）。

<a id="r_gaf8ff29ef3413492d2ec67fba278c2f82"></a>

```c
int bt_obex_get_header_end_body (struct net_buf *buf, uint16_t *len, const uint8_t **body)
```

相关声明：[bt_obex_get_header_end_body](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaf8ff29ef3413492d2ec67fba278c2f82)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：对象主体的最后一个块（Final Body Chunk）。

<a id="r_gab551b01deed2c5a31f9a7a4b99045c9c"></a>

```c
int bt_obex_get_header_who (struct net_buf *buf, uint16_t *len, const uint8_t **who)
```

相关声明：[bt_obex_get_header_who](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab551b01deed2c5a31f9a7a4b99045c9c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：标识 OBEX 应用，用于判断是否正在与对等端通信。

<a id="r_ga225ac4953da5e56a07865c8ab6ee0591"></a>

```c
int bt_obex_get_header_conn_id (struct net_buf *buf, uint32_t *conn_id)
```

相关声明：[bt_obex_get_header_conn_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga225ac4953da5e56a07865c8ab6ee0591)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取报头值（Get Header Value）：用于 OBEX 连接复用（Connection Multiplexing）的标识符。

<a id="r_gaccecf00dc6209d1701ac0a6985f38257"></a>

```c
int bt_obex_tlv_parse (uint16_t len, const uint8_t *data, bool(*func)(struct bt_obex_tlv *tlv, void *user_data), void *user_data)
```

相关声明：[bt_obex_tlv_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaccecf00dc6209d1701ac0a6985f38257)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_obex_tlv](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md)。

解析 OBEX 类型－长度－值三元组（TLV Triplet）的辅助函数。

<a id="r_ga96981ef9187406efbd374fd623a14eaa"></a>

```c
int bt_obex_get_header_app_param (struct net_buf *buf, uint16_t *len, const uint8_t **app_param)
```

相关声明：[bt_obex_get_header_app_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga96981ef9187406efbd374fd623a14eaa)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：扩展应用请求与响应信息（Extended Application Request & Response Information）。

<a id="r_ga6ee576eecea3947f1832d4859f16e1db"></a>

```c
int bt_obex_get_header_auth_challenge (struct net_buf *buf, uint16_t *len, const uint8_t **auth)
```

相关声明：[bt_obex_get_header_auth_challenge](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6ee576eecea3947f1832d4859f16e1db)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：认证摘要质询（Authentication Digest-challenge）。

<a id="r_gad9bae471db418e0a50c1b234e37b5d9d"></a>

```c
int bt_obex_get_header_auth_rsp (struct net_buf *buf, uint16_t *len, const uint8_t **auth)
```

相关声明：[bt_obex_get_header_auth_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gad9bae471db418e0a50c1b234e37b5d9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：认证摘要响应（Authentication Digest-response）。

<a id="r_ga9e08bf74bfbf001a80f40ee2d1b1ef82"></a>

```c
int bt_obex_get_header_creator_id (struct net_buf *buf, uint32_t *creator_id)
```

相关声明：[bt_obex_get_header_creator_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga9e08bf74bfbf001a80f40ee2d1b1ef82)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取报头值（Get Header Value）：指示对象创建者（Object Creator）。

<a id="r_gaf9ffc19ef06a2773d664c0b15b2b8857"></a>

```c
int bt_obex_get_header_wan_uuid (struct net_buf *buf, uint16_t *len, const uint8_t **uuid)
```

相关声明：[bt_obex_get_header_wan_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaf9ffc19ef06a2773d664c0b15b2b8857)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)。

获取报头值（Get Header Value）：唯一标识网络客户端（Network Client），即 OBEX 服务器。

<a id="r_ga49d1988eae4165f1cec624812cfe5f36"></a>

```c
int bt_obex_get_header_obj_class (struct net_buf *buf, uint16_t *len, const uint8_t **obj_class)
```

相关声明：[bt_obex_get_header_obj_class](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga49d1988eae4165f1cec624812cfe5f36)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：对象的 OBEX 对象类（Object Class，原文写作 oBEX）。

<a id="r_ga560c8f0cb92b769a0716b2bc163c38e1"></a>

```c
int bt_obex_get_header_session_param (struct net_buf *buf, uint16_t *len, const uint8_t **session_param)
```

相关声明：[bt_obex_get_header_session_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga560c8f0cb92b769a0716b2bc163c38e1)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：会话命令／响应（Session Commands/Responses）使用的参数。

<a id="r_gaaa33502f3ae9f97767bd0e5e660f021f"></a>

```c
int bt_obex_get_header_session_seq_number (struct net_buf *buf, uint32_t *session_seq_number)
```

相关声明：[bt_obex_get_header_session_seq_number](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaaa33502f3ae9f97767bd0e5e660f021f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取报头值（Get Header Value）：每个 OBEX 数据包中用于保证可靠性的序列号（Sequence Number）。

<a id="r_gacc1673746737e4163165b5f379c8105f"></a>

```c
int bt_obex_get_header_action_id (struct net_buf *buf, uint8_t *action_id)
```

相关声明：[bt_obex_get_header_action_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gacc1673746737e4163165b5f379c8105f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：指定要执行的动作（Action），供 ACTION 操作使用。

<a id="r_ga945c0865edef9f34e2cf1e817a3b45c1"></a>

```c
int bt_obex_get_header_dest_name (struct net_buf *buf, uint16_t *len, const uint8_t **dest_name)
```

相关声明：[bt_obex_get_header_dest_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga945c0865edef9f34e2cf1e817a3b45c1)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：目标对象名称（Destination Object Name），供某些 ACTION 操作使用。

<a id="r_gab234af4e944a3e97e3459613078005a1"></a>

```c
int bt_obex_get_header_perm (struct net_buf *buf, uint32_t *perm)
```

相关声明：[bt_obex_get_header_perm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab234af4e944a3e97e3459613078005a1)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取报头值（Get Header Value）：用于设置权限（Permissions）的 4 字节位掩码。

<a id="r_gae0865eea3d8db09023cfc77b2118bad5"></a>

```c
int bt_obex_get_header_srm (struct net_buf *buf, uint8_t *srm)
```

相关声明：[bt_obex_get_header_srm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gae0865eea3d8db09023cfc77b2118bad5)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：用于设置单响应模式（Single Response Mode，SRM）的 1 字节值。

<a id="r_ga7501193240498e7a9da0034b2e434ffc"></a>

```c
int bt_obex_get_header_srm_param (struct net_buf *buf, uint8_t *srm_param)
```

相关声明：[bt_obex_get_header_srm_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga7501193240498e7a9da0034b2e434ffc)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：单响应模式参数（Single Response Mode Parameter，SRM）。

<a id="r_gafadd6e44ae19786617b5e60608fa4651"></a>

```c
int bt_obex_make_uuid (union bt_obex_uuid *uuid, const uint8_t *data, uint16_t len)
```

相关声明：[bt_obex_make_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gafadd6e44ae19786617b5e60608fa4651)、[bt_obex_uuid](../bluetooth_service_model_reference/P189_bt_obex_uuid_联合体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

使用指定数据和长度构造通用唯一标识符（UUID）。

<a id="r_ga170456d806c0ff494b0c1d7fad763051"></a>

```c
bool bt_obex_string_is_valid (uint8_t id, uint16_t len, const uint8_t *str)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_obex_string_is_valid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga170456d806c0ff494b0c1d7fad763051)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

检查字符串（String）是否有效。

<a id="r_ga296af3d5a15684e4aa3846cc24203fef"></a>

```c
bool bt_obex_has_header (struct net_buf *buf, uint8_t id)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_obex_has_header](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga296af3d5a15684e4aa3846cc24203fef)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

检查 buf 是否包含指定报头（Header）。

<a id="r_ga5ae88dad0e7c97d0f20c7e4ceeeb3ce8"></a>

```c
bool bt_obex_has_app_param (struct net_buf *buf, uint8_t id)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_obex_has_app_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga5ae88dad0e7c97d0f20c7e4ceeeb3ce8)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

检查 buf 是否包含指定应用参数（Application Parameter）。

<a id="r_ga3708c17f9c23fdeb5ceda376787cebbd"></a>

```c
int bt_obex_generate_nonce (const uint8_t *pwd, size_t pwd_len, uint8_t nonce[16])
```

相关声明：[bt_obex_generate_nonce](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga3708c17f9c23fdeb5ceda376787cebbd)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为 OBEX 认证质询（Authentication Challenge）生成一次性随机数（Nonce）。

<a id="r_ga51baeae9280bb50e34b6608f620498fa"></a>

```c
int bt_obex_calculate_request_digest (const uint8_t *pwd, size_t pwd_len, const uint8_t nonce[16], uint8_t digest[16])
```

相关声明：[bt_obex_calculate_request_digest](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga51baeae9280bb50e34b6608f620498fa)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为 OBEX 认证响应（Authentication Response）计算请求摘要（Request Digest）。

<a id="r_gae31398502c9d237d7afd47d70315be3f"></a>

```c
int bt_obex_verify_auth_response (const uint8_t *pwd, size_t pwd_len, const uint8_t nonce[16], const uint8_t digest[16])
```

相关声明：[bt_obex_verify_auth_response](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gae31398502c9d237d7afd47d70315be3f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

验证 OBEX 认证响应（Authentication Response）。


## 11.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [string.h](../api_source_supplement_reference/P216_string.h_源码浏览.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/bluetooth/uuid.h](../api_source_supplement_reference/P020_uuid.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P062_obex.h_源码浏览.md)
- [bt_obex_server_ops](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md)
- [bt_obex_client_ops](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md)
- [bt_obex_transport_ops](../bluetooth_service_model_reference/P134_bt_obex_transport_ops_结构体.md)
- [bt_obex_uuid](../bluetooth_service_model_reference/P189_bt_obex_uuid_联合体.md)
- [bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)
- [bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)
- [bt_obex](../bluetooth_service_model_reference/P127_bt_obex_结构体.md)
- [bt_obex_tlv](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md)
- [bt_obex_hdr](../bluetooth_service_model_reference/P130_bt_obex_hdr_结构体.md)
- [BT_OBEX_MIN_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6206007c2c3e50d997ae5a644ceae783)
- [BT_OBEX_HDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga534e9ffa9f7ba93eda049fd9022df69a)
- [BT_OBEX_PDU_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga500dcfab79831c5d640406cff8c54f01)
- [BT_OBEX_HDR_LEN_OF_HEADER_BODY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga5571666538c43d8d71dd17dc58d19f45)
- [BT_OBEX_DATA_LEN_OF_HEADER_BODY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab3db35da4b3daf626e89223262273fb9)
- [BT_OBEX_SEND_BUF_RESERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga3d89a9c04baec0be2dd6b9f922a7c985)
- [BT_OBEX_CHALLENGE_TAG_NONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6c6bd723b6b7c84d53ea0d0bc9787fbc)
- [BT_OBEX_CHALLENGE_TAG_NONCE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaab47709ef621b63172fa54314bf3eff0)
- [BT_OBEX_CHALLENGE_TAG_OPTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gae48159128c97a6579c8cbf12b5c934e4)
- [BT_OBEX_CHALLENGE_TAG_OPTIONS_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga40725e7d1882cd9f793dc490a9ad8341)
- [BT_OBEX_CHALLENGE_TAG_OPTION_REQ_USER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga4d936864173fe0218e660df7b53d666e)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_OBEX_CHALLENGE_TAG_OPTION_ACCESS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gad35d3b9c3a398b1f4bdba610c825aca3)
- [BT_OBEX_CHALLENGE_TAG_REALM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga7957818ad49e8e406942dad698e2d089)
- [BT_OBEX_RESPONSE_TAG_REQ_DIGEST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga69d4d1a8af96df807ab9f1ec5fc42503)
- [BT_OBEX_RESPONSE_TAG_REQ_DIGEST_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gacbae9ed1d18eaab7934258cbfe4fd62a)
- [BT_OBEX_RESPONSE_TAG_USER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gad466df7bba9c20ff47820121372193ec)
- [BT_OBEX_RESPONSE_TAG_NONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gacbdbc35907fcd1b5362fb108f7925412)
- [BT_OBEX_RESPONSE_TAG_NONCE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga78897a868628d0dc9992ebb7d79e6dd5)
- [bt_obex_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga81b84c24a976c6c13d33eb23b0b10ae9)
- [BT_OBEX_RSP_CODE_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a7e38ca653283f53b62fa4b21f48d998a)
- [BT_OBEX_RSP_CODE_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a881d3098a198dc1eced2150a213d1054)
- [BT_OBEX_RSP_CODE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9af449d3c85fbec550c76e29287a626789)
- [BT_OBEX_RSP_CODE_CREATED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a955b065ee2543e0bc31a03d9bd15900b)
- [BT_OBEX_RSP_CODE_ACCEPTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aba13d60d30201bdb13f01c1ee2ff7916)
- [BT_OBEX_RSP_CODE_NON_AUTH_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a2f88a5bf5bb9690d8db856bf02f305d8)
- [BT_OBEX_RSP_CODE_NO_CONTENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a32d55bb3c73ecb8cdf5f76c6724c9884)
- [BT_OBEX_RSP_CODE_RESET_CONTENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a4e8f5c004cf3ef6e9ad1b5be1d106a39)
- [BT_OBEX_RSP_CODE_PARTIAL_CONTENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9afcf5fc7c81eed4d5b67def413535a46f)
- [BT_OBEX_RSP_CODE_MULTI_CHOICES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a3b948c9bdf3bebd2b0e7cf34960c19b2)
- [BT_OBEX_RSP_CODE_MOVED_PERM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aa5252b1eaa5fa7d41052d97af24fd4d7)
- [BT_OBEX_RSP_CODE_MOVED_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9abf41a7e722e12bd71a93093e36bfc2bf)
- [BT_OBEX_RSP_CODE_SEE_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ac25903e3a229ac50ecea485eca8c5236)
- [BT_OBEX_RSP_CODE_NOT_MODIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ab33e506b470df404119976d5460b6bda)
- [BT_OBEX_RSP_CODE_USE_PROXY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ac19ffb8b59a7cb1a3e0c1edfe91dd472)
- [BT_OBEX_RSP_CODE_BAD_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a2d2ff2c6ec42d9e80dc4e841e19d31ee)
- [BT_OBEX_RSP_CODE_UNAUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9acfbc9161dddf6859dd8e8ac70cf8d446)
- [BT_OBEX_RSP_CODE_PAY_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a5fc2aa165ffea0caeb59e05ee951e3dc)
- [BT_OBEX_RSP_CODE_FORBIDDEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a4b7a12b0e11747d1a470e8f559b55ea8)
- [BT_OBEX_RSP_CODE_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a2b91abe9e010465f9514f37477b993e0)
- [BT_OBEX_RSP_CODE_NOT_ALLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a3f510d3b203257a37d2ef005d4517a67)
- [BT_OBEX_RSP_CODE_NOT_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a48f773daa7f2dabaadc37142ec32ffd1)
- [BT_OBEX_RSP_CODE_PROXY_AUTH_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aeb2abeaf682a47a46291784c2b24b793)
- [BT_OBEX_RSP_CODE_REQ_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a3f60fb4d3444570c9a73f43b7c9bdc1f)
- [BT_OBEX_RSP_CODE_CONFLICT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aeca60f95428624932314fc8f3b4a1b79)
- [BT_OBEX_RSP_CODE_GONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aa34ece6da3fe28ec3747ce8621da7e31)
- [BT_OBEX_RSP_CODE_LEN_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ac0faf667c93a32293fbacca2e1696938)
- [BT_OBEX_RSP_CODE_PRECON_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aacc05fd2528e29fbd53eb5ff940f9079)
- [BT_OBEX_RSP_CODE_ENTITY_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a21783b5d9036d61304a7acb3b03d0913)
- [BT_OBEX_RSP_CODE_URL_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9adc906b909c09a8a1cc421e8f4efc1444)
- [BT_OBEX_RSP_CODE_UNSUPP_MEDIA_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a650312673ccc758b735bcead8f1009ef)
- [BT_OBEX_RSP_CODE_INTER_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9add3501ba98c972e0e01a6fa898612bd4)
- [BT_OBEX_RSP_CODE_NOT_IMPL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aba8108ac6b050d3dad845a5e8cb42eaf)
- [BT_OBEX_RSP_CODE_BAD_GATEWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ac39d7d6fa1fcb0cc5be0ad25aa2574f9)
- [BT_OBEX_RSP_CODE_UNAVAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a613e95b96eaba0522070b620b4b90953)
- [BT_OBEX_RSP_CODE_GATEWAY_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a850bbc0fd1810e3a74f2a057e8358b48)
- [BT_OBEX_RSP_CODE_VER_UNSUPP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ab41b31b5e85dcb2981b3f6e9bbba2dd9)
- [BT_OBEX_RSP_CODE_DB_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ad65c4246d828770010748b1faa6af71c)
- [BT_OBEX_RSP_CODE_DB_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a5c0692d0e3db45a898426b2751e682a0)
- [bt_obex_header_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga3c893652eb9a5f0bf699d357caf40948)
- [BT_OBEX_HEADER_ID_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a6119d9faab405c63a25791edc9588889)
- [BT_OBEX_HEADER_ID_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948adf199ff987c26bd8d6301c409fb5f6a4)
- [BT_OBEX_HEADER_ID_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a8bfeff22eabea432eb5863a974adb745)
- [BT_OBEX_HEADER_ID_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948ae075bf9dd7e57c66613ffb3de84f09bb)
- [BT_OBEX_HEADER_ID_TIME_ISO_8601](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948ac2899a8dca76bfd88bb94d43a3c8a693)
- [BT_OBEX_HEADER_ID_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a4fad7112257bd771e412eefd0c1e8bcc)
- [BT_OBEX_HEADER_ID_DES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a0fb867c69fb0c8680170359a41f2a3b1)
- [BT_OBEX_HEADER_ID_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a5929acc483779593b1b5c7b702b17976)
- [BT_OBEX_HEADER_ID_HTTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a46735e651f7f378a3efb1be1a232e4ca)
- [BT_OBEX_HEADER_ID_BODY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a3264aa53da0fd7ec6611b8a20a8745f4)
- [BT_OBEX_HEADER_ID_END_BODY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948aaa78dab2eda48ebd5d594024b53bec6b)
- [BT_OBEX_HEADER_ID_WHO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948ab28b3ee885c373ca83a745fcd019e2e4)
- [BT_OBEX_HEADER_ID_CONN_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a3417001aed5d114492dcbe2c29496a1b)
- [BT_OBEX_HEADER_ID_APP_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a6dac6844a5db11dbc0e43613a32c13a9)
- [BT_OBEX_HEADER_ID_AUTH_CHALLENGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948aa48d582e278e748574d57818a7f5daf1)
- [BT_OBEX_HEADER_ID_AUTH_RSP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a97c1dfb166ac549576d30cadd156365f)
- [BT_OBEX_HEADER_ID_CREATE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a31bec44f1240f21545f917eedd31026e)
- [BT_OBEX_HEADER_ID_WAN_UUID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a65e148b396f75cd55b992df84d5176ff)
- [BT_OBEX_HEADER_ID_OBJECT_CLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a5b723fde52df0965299d2f79e433c0a2)
- [BT_OBEX_HEADER_ID_SESSION_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948afe34bec1dba1d1fca717f3ffa7c20628)
- [BT_OBEX_HEADER_ID_SESSION_SEQ_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a3d42ab8b6a28f9062a97e2b1a9fa7c16)
- [BT_OBEX_HEADER_ID_ACTION_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a01e2d13304514242e954d45e74e3fcba)
- [BT_OBEX_HEADER_ID_DEST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948ae5149b2da2cfb3c2e832f51282bc08d6)
- [BT_OBEX_HEADER_ID_PERM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a6aad7cbbcbebe670d370919fbdc61c19)
- [BT_OBEX_HEADER_ID_SRM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948aa722c75042f0db4fba5c6a90516494b1)
- [BT_OBEX_HEADER_ID_SRM_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948adda0f643d1c2ebd20d4c9d5644ef6b2c)
- [bt_obex_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga622610a779a2e050e9a05c7eae945b3e)
- [BT_OBEX_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga622610a779a2e050e9a05c7eae945b3ead7138e7373f5562faf13faa8bca424e6)
- [BT_OBEX_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga622610a779a2e050e9a05c7eae945b3ea8743efcfd509ba7b156ac91a3c928614)
- [BT_OBEX_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga622610a779a2e050e9a05c7eae945b3ea15ddd595c7832a8bfd382f87b938723b)
- [BT_OBEX_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga622610a779a2e050e9a05c7eae945b3eae41568fe4c0d0db81ff60f41be6443a5)
- [bt_obex_setpath_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab5f7e6a6c7503f97a851f48c70162483)
- [BT_OBEX_SETPATH_FLAG_BACKUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ggab5f7e6a6c7503f97a851f48c70162483a9f89d8219783650a02e8ceb3faf6bd75)
- [BT_OBEX_SETPATH_FLAG_NO_CREATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ggab5f7e6a6c7503f97a851f48c70162483ae47e6f7c5a8da44615e7245c5e1cd553)
- [bt_obex_action_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga12730d705667c2717c05a75cdfc07281)
- [BT_OBEX_ACTION_COPY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga12730d705667c2717c05a75cdfc07281abb151a8123c7e6826a052ab252455aee)
- [BT_OBEX_ACTION_MOVE_RENAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga12730d705667c2717c05a75cdfc07281a7c57548121adf0afe43066070ef4b1fa)
- [BT_OBEX_ACTION_SET_PERM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga12730d705667c2717c05a75cdfc07281a711263abb984488b8c7273052fb76ae0)
- [bt_obex_rsp_code_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga7cb42acb39c601375ef7c73f6be7e6af)
- [bt_obex_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga1df3928a40f544ffb98b5eb1ceac62dd)
- [bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [bt_obex_server_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga642bfabb90d6576f92c5b546a592ec17)
- [bt_obex_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga21afebccbd592381fb1569feaff98511)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_obex_connect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gad91f69ba1b6780501722221bc516db4b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_obex_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga107787f08e55bf2740cc14cb5614bdbf)
- [bt_obex_disconnect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gac7763a310a553b3ba3c6b8b06951f191)
- [bt_obex_put](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga1d8684307899b1bd3724cb3aa996c53e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_obex_put_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab5dfc5988d17ef0b79b84fd4c96dc60a)
- [bt_obex_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gabd3ff76e8a39e5944daa944f38a63c5f)
- [bt_obex_get_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga3e9415fa4595d17676ada6622c9fd475)
- [bt_obex_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gafa2e01166c3177fe3aea937632fb52b7)
- [bt_obex_abort_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6f9de12183c445557f952fe2b49e3029)
- [bt_obex_setpath](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6d61b4421ad1e56cc2ae611ec77e561e)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bt_obex_setpath_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga13836db790849b5ec6b52bcb97c84505)
- [bt_obex_action](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab4b0a3533c7ec044efbee05c852d4f09)
- [bt_obex_action_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gae178bf14d0495ad1e1aa5f7b4d8e1652)
- [bt_obex_add_header_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga14c8efe9c8a99e2736552d59972e7b23)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_obex_add_header_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga9cd4c8342f67b53a3c3177a51f8887cb)
- [bt_obex_add_header_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gadd9f9b4cb50eb51df05c60705223e53b)
- [bt_obex_add_header_len](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga0d27f09e3b8ea5636f0a34cf8729abaf)
- [bt_obex_add_header_time_iso_8601](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga877d67e0a4135cabf8b5fddab4d014c6)
- [bt_obex_add_header_time](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga249e8b35b98f564d57dc1d644228b8f2)
- [bt_obex_add_header_description](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaedc6f39972a5414d085ce17b09ffd121)
- [bt_obex_add_header_target](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gac778e8ff0ac7e74795b107750a4a6719)
- [bt_obex_add_header_http](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6392da7ce8009eb95ab8c8a4d45fcb40)
- [bt_obex_add_header_body](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gad1b3c22eea0915b962d7ab1e27726fe2)
- [bt_obex_add_header_end_body](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga805f13b12c7ce23057cb983d7159c36b)
- [bt_obex_add_header_body_or_end_body](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gadf2d0b93618e0e29341bc21dfd44954f)
- [bt_obex_add_header_who](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga56690794dc07dfa598ae2ac68bc90aa0)
- [bt_obex_add_header_conn_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gadc92dff93ef2051ff8b3b277a1bc1f17)
- [bt_obex_add_header_app_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaeacfe7cb654bf33e7b387358a19fd3d3)
- [bt_obex_add_header_auth_challenge](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gacfc897d66e8c14629fa4d94f3782c741)
- [bt_obex_add_header_auth_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga5433561f0e9bad6da2d94dccca1578de)
- [bt_obex_add_header_creator_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga14c619eef70addc01d13841eda2d8f89)
- [bt_obex_add_header_wan_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga111cd19449aba6fd0e667551874af0cf)
- [bt_obex_add_header_obj_class](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga7473f42bef1409100886f7812a71a1dc)
- [bt_obex_add_header_session_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gac47ddfe8cfe1e595a1821f32415d14eb)
- [bt_obex_add_header_session_seq_number](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gad4a84068ce8c7c37b5189d366b771235)
- [bt_obex_add_header_action_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga58034dc9ba274030eea5bc3980e2ff95)
- [bt_obex_add_header_dest_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga4463514cf369beb882fec9ab15904821)
- [bt_obex_add_header_perm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga4b7c08fd620fdc1ff28a4714c84b6e30)
- [bt_obex_add_header_srm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga23ed862cc6149a71793d02d89fb98cdc)
- [bt_obex_add_header_srm_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaaa8a9630b0bf5597ca620b864fdafa87)
- [bt_obex_header_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga5c93e9786adfb45a60a911087f859757)
- [bt_obex_get_header_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga1e9b6dd9a8816ce87235b6b3d723541c)
- [bt_obex_get_header_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gabef4622fa48b493f6d6ad5d1ecb65726)
- [bt_obex_get_header_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gabcfa9b33c0f91fbcf787d58e1f1bba41)
- [bt_obex_get_header_len](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga18ce5303b138959481666c0b8101f59e)
- [bt_obex_get_header_time_iso_8601](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gacee063f6b53b85bad52a519cd1c794c5)
- [bt_obex_get_header_time](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga367337d0f002a046248e92f3578efbb6)
- [bt_obex_get_header_description](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga3d805f241fc507587445b3204070055e)
- [bt_obex_get_header_target](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga49265f0aec21d8c33f56eb44723dabba)
- [bt_obex_get_header_http](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga5a181f7779df1ed2919ba3a94a630df4)
- [bt_obex_get_header_body](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaba71a8b3b8adc251a5a87fa60848bb3c)
- [bt_obex_get_header_end_body](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaf8ff29ef3413492d2ec67fba278c2f82)
- [bt_obex_get_header_who](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab551b01deed2c5a31f9a7a4b99045c9c)
- [bt_obex_get_header_conn_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga225ac4953da5e56a07865c8ab6ee0591)
- [bt_obex_tlv_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaccecf00dc6209d1701ac0a6985f38257)
- [bt_obex_get_header_app_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga96981ef9187406efbd374fd623a14eaa)
- [bt_obex_get_header_auth_challenge](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6ee576eecea3947f1832d4859f16e1db)
- [bt_obex_get_header_auth_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gad9bae471db418e0a50c1b234e37b5d9d)
- [bt_obex_get_header_creator_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga9e08bf74bfbf001a80f40ee2d1b1ef82)
- [bt_obex_get_header_wan_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaf9ffc19ef06a2773d664c0b15b2b8857)
- [bt_obex_get_header_obj_class](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga49d1988eae4165f1cec624812cfe5f36)
- [bt_obex_get_header_session_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga560c8f0cb92b769a0716b2bc163c38e1)
- [bt_obex_get_header_session_seq_number](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaaa33502f3ae9f97767bd0e5e660f021f)
- [bt_obex_get_header_action_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gacc1673746737e4163165b5f379c8105f)
- [bt_obex_get_header_dest_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga945c0865edef9f34e2cf1e817a3b45c1)
- [bt_obex_get_header_perm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab234af4e944a3e97e3459613078005a1)
- [bt_obex_get_header_srm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gae0865eea3d8db09023cfc77b2118bad5)
- [bt_obex_get_header_srm_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga7501193240498e7a9da0034b2e434ffc)
- [bt_obex_make_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gafadd6e44ae19786617b5e60608fa4651)
- [bt_obex_string_is_valid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga170456d806c0ff494b0c1d7fad763051)
- [bt_obex_has_header](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga296af3d5a15684e4aa3846cc24203fef)
- [bt_obex_has_app_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga5ae88dad0e7c97d0f20c7e4ceeeb3ce8)
- [bt_obex_generate_nonce](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga3708c17f9c23fdeb5ceda376787cebbd)
- [bt_obex_calculate_request_digest](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga51baeae9280bb50e34b6608f620498fa)
- [bt_obex_verify_auth_response](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gae31398502c9d237d7afd47d70315be3f)

---

[上一章](P010_zephyr__dt-bindings__clock-monitor__nxp-freqme.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__bluetooth__audio__tbs.h_文件参考.md)
