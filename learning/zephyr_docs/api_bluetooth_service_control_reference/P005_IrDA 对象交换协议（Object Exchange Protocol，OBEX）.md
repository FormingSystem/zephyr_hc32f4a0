---
id: learning.zephyr-docs.api-bluetooth-service-control-reference.page-5
title: IrDA 对象交换协议（Object Exchange Protocol，OBEX）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_IrDA 对象交换协议（Object Exchange Protocol，OBEX）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IrDA 对象交换协议（Object Exchange Protocol，OBEX）

<a id="details"></a>

IrDA 对象交换协议（Object Exchange Protocol，OBEX）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

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

## 5.2\_宏定义（Macros）

<a id="r_ga6206007c2c3e50d997ae5a644ceae783"></a>

```c
#define BT_OBEX_MIN_MTU 255
```

相关声明：[BT_OBEX_MIN_MTU](#ga6206007c2c3e50d997ae5a644ceae783)。

<a id="r_ga534e9ffa9f7ba93eda049fd9022df69a"></a>

```c
#define BT_OBEX_HDR_LEN 3
```

相关声明：[BT_OBEX_HDR_LEN](#ga534e9ffa9f7ba93eda049fd9022df69a)。

PUT 和 GET 请求及响应的对象交换（OBEX）数据包报头长度。

<a id="r_ga500dcfab79831c5d640406cff8c54f01"></a>

```c
#define BT_OBEX_PDU_LEN(mopl)
```

相关声明：[BT_OBEX_PDU_LEN](#ga500dcfab79831c5d640406cff8c54f01)。

对象交换（OBEX）数据包的 PDU 数据长度上限。

<a id="r_ga5571666538c43d8d71dd17dc58d19f45"></a>

```c
#define BT_OBEX_HDR_LEN_OF_HEADER_BODY 3
```

相关声明：[BT_OBEX_HDR_LEN_OF_HEADER_BODY](#ga5571666538c43d8d71dd17dc58d19f45)。

OBEX 主体／主体结束报头（Body / End Body Header）的长度。

<a id="r_gab3db35da4b3daf626e89223262273fb9"></a>

```c
#define BT_OBEX_DATA_LEN_OF_HEADER_BODY(len)
```

相关声明：[BT_OBEX_DATA_LEN_OF_HEADER_BODY](#gab3db35da4b3daf626e89223262273fb9)。

添加的报头为主体／主体结束（Body / End Body）时，缓冲区的最大剩余长度。

<a id="r_ga3d89a9c04baec0be2dd6b9f922a7c985"></a>

```c
#define BT_OBEX_SEND_BUF_RESERVE 7
```

相关声明：[BT_OBEX_SEND_BUF_RESERVE](#ga3d89a9c04baec0be2dd6b9f922a7c985)。

<a id="r_ga6c6bd723b6b7c84d53ea0d0bc9787fbc"></a>

```c
#define BT_OBEX_CHALLENGE_TAG_NONCE 0x00
```

相关声明：[BT_OBEX_CHALLENGE_TAG_NONCE](#ga6c6bd723b6b7c84d53ea0d0bc9787fbc)。

OBEX 摘要质询标记（Digest-challenge Tag）：Nonce，以字节串表示的一次性随机数。

<a id="r_gaab47709ef621b63172fa54314bf3eff0"></a>

```c
#define BT_OBEX_CHALLENGE_TAG_NONCE_LEN 16
```

相关声明：[BT_OBEX_CHALLENGE_TAG_NONCE_LEN](#gaab47709ef621b63172fa54314bf3eff0)。

OBEX 摘要质询的一次性随机数长度（Nonce Length），16 字节。

<a id="r_gae48159128c97a6579c8cbf12b5c934e4"></a>

```c
#define BT_OBEX_CHALLENGE_TAG_OPTIONS 0x01
```

相关声明：[BT_OBEX_CHALLENGE_TAG_OPTIONS](#gae48159128c97a6579c8cbf12b5c934e4)。

OBEX 摘要质询标记（Digest-challenge Tag）：Options，可选质询信息（Optional Challenge Information）。

<a id="r_ga40725e7d1882cd9f793dc490a9ad8341"></a>

```c
#define BT_OBEX_CHALLENGE_TAG_OPTIONS_LEN 1
```

相关声明：[BT_OBEX_CHALLENGE_TAG_OPTIONS_LEN](#ga40725e7d1882cd9f793dc490a9ad8341)。

OBEX 摘要质询的选项长度（Options Length），1 字节。

<a id="r_ga4d936864173fe0218e660df7b53d666e"></a>

```c
#define BT_OBEX_CHALLENGE_TAG_OPTION_REQ_USER_ID BIT(0)
```

相关声明：[BT_OBEX_CHALLENGE_TAG_OPTION_REQ_USER_ID](#ga4d936864173fe0218e660df7b53d666e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

选项位 0（BIT0）：设置时，必须在认证响应（Authenticate Response）中发送用户 ID（User Id）。

<a id="r_gad35d3b9c3a398b1f4bdba610c825aca3"></a>

```c
#define BT_OBEX_CHALLENGE_TAG_OPTION_ACCESS_MODE BIT(1)
```

相关声明：[BT_OBEX_CHALLENGE_TAG_OPTION_ACCESS_MODE](#gad35d3b9c3a398b1f4bdba610c825aca3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

选项位 1（BIT1）：访问模式（Access Mode）；设置时为只读（Read Only），否则允许完全访问（Full Access）。

<a id="r_ga7957818ad49e8e406942dad698e2d089"></a>

```c
#define BT_OBEX_CHALLENGE_TAG_REALM 0x02
```

相关声明：[BT_OBEX_CHALLENGE_TAG_REALM](#ga7957818ad49e8e406942dad698e2d089)。

OBEX 摘要质询标记（Digest-challenge Tag）：Realm，一个可显示字符串，指示应使用哪个用户 ID 和／或密码。

<a id="r_ga69d4d1a8af96df807ab9f1ec5fc42503"></a>

```c
#define BT_OBEX_RESPONSE_TAG_REQ_DIGEST 0x00
```

相关声明：[BT_OBEX_RESPONSE_TAG_REQ_DIGEST](#ga69d4d1a8af96df807ab9f1ec5fc42503)。

OBEX 摘要响应标记（Digest-response Tag）：Request-digest，以字节串表示的请求摘要。

<a id="r_gacbae9ed1d18eaab7934258cbfe4fd62a"></a>

```c
#define BT_OBEX_RESPONSE_TAG_REQ_DIGEST_LEN 16
```

相关声明：[BT_OBEX_RESPONSE_TAG_REQ_DIGEST_LEN](#gacbae9ed1d18eaab7934258cbfe4fd62a)。

OBEX 摘要响应的请求摘要长度（Request-digest Length），16 字节。

<a id="r_gad466df7bba9c20ff47820121372193ec"></a>

```c
#define BT_OBEX_RESPONSE_TAG_USER_ID 0x01
```

相关声明：[BT_OBEX_RESPONSE_TAG_USER_ID](#gad466df7bba9c20ff47820121372193ec)。

OBEX 摘要响应标记（Digest-response Tag）：User Id，长度为 n 的用户 ID 字符串。

<a id="r_gacbdbc35907fcd1b5362fb108f7925412"></a>

```c
#define BT_OBEX_RESPONSE_TAG_NONCE 0x02
```

相关声明：[BT_OBEX_RESPONSE_TAG_NONCE](#gacbdbc35907fcd1b5362fb108f7925412)。

OBEX 摘要响应标记（Digest-response Tag）：Nonce，即摘要质询字符串中发送的一次性随机数。

<a id="r_ga78897a868628d0dc9992ebb7d79e6dd5"></a>

```c
#define BT_OBEX_RESPONSE_TAG_NONCE_LEN 16
```

相关声明：[BT_OBEX_RESPONSE_TAG_NONCE_LEN](#ga78897a868628d0dc9992ebb7d79e6dd5)。

OBEX 摘要响应的一次性随机数长度（Nonce Length），16 字节。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.3\_枚举（Enumerations）

<a id="r_ga81b84c24a976c6c13d33eb23b0b10ae9"></a>

```c
enum bt_obex_rsp_code { BT_OBEX_RSP_CODE_CONTINUE = 0x90 , BT_OBEX_RSP_CODE_OK = 0xa0 , BT_OBEX_RSP_CODE_SUCCESS = 0xa0 , BT_OBEX_RSP_CODE_CREATED = 0xa1 , BT_OBEX_RSP_CODE_ACCEPTED = 0xa2 , BT_OBEX_RSP_CODE_NON_AUTH_INFO = 0xa3 , BT_OBEX_RSP_CODE_NO_CONTENT = 0xa4 , BT_OBEX_RSP_CODE_RESET_CONTENT = 0xa5 , BT_OBEX_RSP_CODE_PARTIAL_CONTENT = 0xa6 , BT_OBEX_RSP_CODE_MULTI_CHOICES = 0xb0 , BT_OBEX_RSP_CODE_MOVED_PERM = 0xb1 , BT_OBEX_RSP_CODE_MOVED_TEMP = 0xb2 , BT_OBEX_RSP_CODE_SEE_OTHER = 0xb3 , BT_OBEX_RSP_CODE_NOT_MODIFIED = 0xb4 , BT_OBEX_RSP_CODE_USE_PROXY = 0xb5 , BT_OBEX_RSP_CODE_BAD_REQ = 0xc0 , BT_OBEX_RSP_CODE_UNAUTH = 0xc1 , BT_OBEX_RSP_CODE_PAY_REQ = 0xc2 , BT_OBEX_RSP_CODE_FORBIDDEN = 0xc3 , BT_OBEX_RSP_CODE_NOT_FOUND = 0xc4 , BT_OBEX_RSP_CODE_NOT_ALLOW = 0xc5 , BT_OBEX_RSP_CODE_NOT_ACCEPT = 0xc6 , BT_OBEX_RSP_CODE_PROXY_AUTH_REQ = 0xc7 , BT_OBEX_RSP_CODE_REQ_TIMEOUT = 0xc8 , BT_OBEX_RSP_CODE_CONFLICT = 0xc9 , BT_OBEX_RSP_CODE_GONE = 0xca , BT_OBEX_RSP_CODE_LEN_REQ = 0xcb , BT_OBEX_RSP_CODE_PRECON_FAIL = 0xcc , BT_OBEX_RSP_CODE_ENTITY_TOO_LARGE = 0xcd , BT_OBEX_RSP_CODE_URL_TOO_LARGE = 0xce , BT_OBEX_RSP_CODE_UNSUPP_MEDIA_TYPE = 0xcf , BT_OBEX_RSP_CODE_INTER_ERROR = 0xd0 , BT_OBEX_RSP_CODE_NOT_IMPL = 0xd1 , BT_OBEX_RSP_CODE_BAD_GATEWAY = 0xd2 , BT_OBEX_RSP_CODE_UNAVAIL = 0xd3 , BT_OBEX_RSP_CODE_GATEWAY_TIMEOUT = 0xd4 , BT_OBEX_RSP_CODE_VER_UNSUPP = 0xd5 , BT_OBEX_RSP_CODE_DB_FULL = 0xe0 , BT_OBEX_RSP_CODE_DB_LOCK = 0xe1 }
```

相关声明：[bt_obex_rsp_code](#ga81b84c24a976c6c13d33eb23b0b10ae9)、[BT_OBEX_RSP_CODE_CONTINUE](#gga81b84c24a976c6c13d33eb23b0b10ae9a7e38ca653283f53b62fa4b21f48d998a)、[BT_OBEX_RSP_CODE_OK](#gga81b84c24a976c6c13d33eb23b0b10ae9a881d3098a198dc1eced2150a213d1054)、[BT_OBEX_RSP_CODE_SUCCESS](#gga81b84c24a976c6c13d33eb23b0b10ae9af449d3c85fbec550c76e29287a626789)、[BT_OBEX_RSP_CODE_CREATED](#gga81b84c24a976c6c13d33eb23b0b10ae9a955b065ee2543e0bc31a03d9bd15900b)、[BT_OBEX_RSP_CODE_ACCEPTED](#gga81b84c24a976c6c13d33eb23b0b10ae9aba13d60d30201bdb13f01c1ee2ff7916)、[BT_OBEX_RSP_CODE_NON_AUTH_INFO](#gga81b84c24a976c6c13d33eb23b0b10ae9a2f88a5bf5bb9690d8db856bf02f305d8)、[BT_OBEX_RSP_CODE_NO_CONTENT](#gga81b84c24a976c6c13d33eb23b0b10ae9a32d55bb3c73ecb8cdf5f76c6724c9884)、[BT_OBEX_RSP_CODE_RESET_CONTENT](#gga81b84c24a976c6c13d33eb23b0b10ae9a4e8f5c004cf3ef6e9ad1b5be1d106a39)、[BT_OBEX_RSP_CODE_PARTIAL_CONTENT](#gga81b84c24a976c6c13d33eb23b0b10ae9afcf5fc7c81eed4d5b67def413535a46f)、[BT_OBEX_RSP_CODE_MULTI_CHOICES](#gga81b84c24a976c6c13d33eb23b0b10ae9a3b948c9bdf3bebd2b0e7cf34960c19b2)、[BT_OBEX_RSP_CODE_MOVED_PERM](#gga81b84c24a976c6c13d33eb23b0b10ae9aa5252b1eaa5fa7d41052d97af24fd4d7)、[BT_OBEX_RSP_CODE_MOVED_TEMP](#gga81b84c24a976c6c13d33eb23b0b10ae9abf41a7e722e12bd71a93093e36bfc2bf)、[BT_OBEX_RSP_CODE_SEE_OTHER](#gga81b84c24a976c6c13d33eb23b0b10ae9ac25903e3a229ac50ecea485eca8c5236)、[BT_OBEX_RSP_CODE_NOT_MODIFIED](#gga81b84c24a976c6c13d33eb23b0b10ae9ab33e506b470df404119976d5460b6bda)、[BT_OBEX_RSP_CODE_USE_PROXY](#gga81b84c24a976c6c13d33eb23b0b10ae9ac19ffb8b59a7cb1a3e0c1edfe91dd472)、[BT_OBEX_RSP_CODE_BAD_REQ](#gga81b84c24a976c6c13d33eb23b0b10ae9a2d2ff2c6ec42d9e80dc4e841e19d31ee)、[BT_OBEX_RSP_CODE_UNAUTH](#gga81b84c24a976c6c13d33eb23b0b10ae9acfbc9161dddf6859dd8e8ac70cf8d446)、[BT_OBEX_RSP_CODE_PAY_REQ](#gga81b84c24a976c6c13d33eb23b0b10ae9a5fc2aa165ffea0caeb59e05ee951e3dc)、[BT_OBEX_RSP_CODE_FORBIDDEN](#gga81b84c24a976c6c13d33eb23b0b10ae9a4b7a12b0e11747d1a470e8f559b55ea8)、[BT_OBEX_RSP_CODE_NOT_FOUND](#gga81b84c24a976c6c13d33eb23b0b10ae9a2b91abe9e010465f9514f37477b993e0)、[BT_OBEX_RSP_CODE_NOT_ALLOW](#gga81b84c24a976c6c13d33eb23b0b10ae9a3f510d3b203257a37d2ef005d4517a67)、[BT_OBEX_RSP_CODE_NOT_ACCEPT](#gga81b84c24a976c6c13d33eb23b0b10ae9a48f773daa7f2dabaadc37142ec32ffd1)、[BT_OBEX_RSP_CODE_PROXY_AUTH_REQ](#gga81b84c24a976c6c13d33eb23b0b10ae9aeb2abeaf682a47a46291784c2b24b793)、[BT_OBEX_RSP_CODE_REQ_TIMEOUT](#gga81b84c24a976c6c13d33eb23b0b10ae9a3f60fb4d3444570c9a73f43b7c9bdc1f)、[BT_OBEX_RSP_CODE_CONFLICT](#gga81b84c24a976c6c13d33eb23b0b10ae9aeca60f95428624932314fc8f3b4a1b79)、[BT_OBEX_RSP_CODE_GONE](#gga81b84c24a976c6c13d33eb23b0b10ae9aa34ece6da3fe28ec3747ce8621da7e31)、[BT_OBEX_RSP_CODE_LEN_REQ](#gga81b84c24a976c6c13d33eb23b0b10ae9ac0faf667c93a32293fbacca2e1696938)、[BT_OBEX_RSP_CODE_PRECON_FAIL](#gga81b84c24a976c6c13d33eb23b0b10ae9aacc05fd2528e29fbd53eb5ff940f9079)、[BT_OBEX_RSP_CODE_ENTITY_TOO_LARGE](#gga81b84c24a976c6c13d33eb23b0b10ae9a21783b5d9036d61304a7acb3b03d0913)、[BT_OBEX_RSP_CODE_URL_TOO_LARGE](#gga81b84c24a976c6c13d33eb23b0b10ae9adc906b909c09a8a1cc421e8f4efc1444)、[BT_OBEX_RSP_CODE_UNSUPP_MEDIA_TYPE](#gga81b84c24a976c6c13d33eb23b0b10ae9a650312673ccc758b735bcead8f1009ef)、[BT_OBEX_RSP_CODE_INTER_ERROR](#gga81b84c24a976c6c13d33eb23b0b10ae9add3501ba98c972e0e01a6fa898612bd4)、[BT_OBEX_RSP_CODE_NOT_IMPL](#gga81b84c24a976c6c13d33eb23b0b10ae9aba8108ac6b050d3dad845a5e8cb42eaf)、[BT_OBEX_RSP_CODE_BAD_GATEWAY](#gga81b84c24a976c6c13d33eb23b0b10ae9ac39d7d6fa1fcb0cc5be0ad25aa2574f9)、[BT_OBEX_RSP_CODE_UNAVAIL](#gga81b84c24a976c6c13d33eb23b0b10ae9a613e95b96eaba0522070b620b4b90953)、[BT_OBEX_RSP_CODE_GATEWAY_TIMEOUT](#gga81b84c24a976c6c13d33eb23b0b10ae9a850bbc0fd1810e3a74f2a057e8358b48)、[BT_OBEX_RSP_CODE_VER_UNSUPP](#gga81b84c24a976c6c13d33eb23b0b10ae9ab41b31b5e85dcb2981b3f6e9bbba2dd9)、[BT_OBEX_RSP_CODE_DB_FULL](#gga81b84c24a976c6c13d33eb23b0b10ae9ad65c4246d828770010748b1faa6af71c)、[BT_OBEX_RSP_CODE_DB_LOCK](#gga81b84c24a976c6c13d33eb23b0b10ae9a5c0692d0e3db45a898426b2751e682a0)。

OBEX 响应码（Response Code）。

<a id="r_ga3c893652eb9a5f0bf699d357caf40948"></a>

```c
enum bt_obex_header_id { BT_OBEX_HEADER_ID_COUNT = 0xC0 , BT_OBEX_HEADER_ID_NAME = 0x01 , BT_OBEX_HEADER_ID_TYPE = 0x42 , BT_OBEX_HEADER_ID_LEN = 0xC3 , BT_OBEX_HEADER_ID_TIME_ISO_8601 = 0x44 , BT_OBEX_HEADER_ID_TIME = 0xC4 , BT_OBEX_HEADER_ID_DES = 0x05 , BT_OBEX_HEADER_ID_TARGET = 0x46 , BT_OBEX_HEADER_ID_HTTP = 0x47 , BT_OBEX_HEADER_ID_BODY = 0x48 , BT_OBEX_HEADER_ID_END_BODY = 0x49 , BT_OBEX_HEADER_ID_WHO = 0x4A , BT_OBEX_HEADER_ID_CONN_ID = 0xCB , BT_OBEX_HEADER_ID_APP_PARAM = 0x4C , BT_OBEX_HEADER_ID_AUTH_CHALLENGE = 0x4D , BT_OBEX_HEADER_ID_AUTH_RSP = 0x4E , BT_OBEX_HEADER_ID_CREATE_ID = 0xCF , BT_OBEX_HEADER_ID_WAN_UUID = 0x50 , BT_OBEX_HEADER_ID_OBJECT_CLASS = 0x51 , BT_OBEX_HEADER_ID_SESSION_PARAM = 0x52 , BT_OBEX_HEADER_ID_SESSION_SEQ_NUM = 0x93 , BT_OBEX_HEADER_ID_ACTION_ID = 0x94 , BT_OBEX_HEADER_ID_DEST_NAME = 0x15 , BT_OBEX_HEADER_ID_PERM = 0xD6 , BT_OBEX_HEADER_ID_SRM = 0x97 , BT_OBEX_HEADER_ID_SRM_PARAM = 0x98 }
```

相关声明：[bt_obex_header_id](#ga3c893652eb9a5f0bf699d357caf40948)、[BT_OBEX_HEADER_ID_COUNT](#gga3c893652eb9a5f0bf699d357caf40948a6119d9faab405c63a25791edc9588889)、[BT_OBEX_HEADER_ID_NAME](#gga3c893652eb9a5f0bf699d357caf40948adf199ff987c26bd8d6301c409fb5f6a4)、[BT_OBEX_HEADER_ID_TYPE](#gga3c893652eb9a5f0bf699d357caf40948a8bfeff22eabea432eb5863a974adb745)、[BT_OBEX_HEADER_ID_LEN](#gga3c893652eb9a5f0bf699d357caf40948ae075bf9dd7e57c66613ffb3de84f09bb)、[BT_OBEX_HEADER_ID_TIME_ISO_8601](#gga3c893652eb9a5f0bf699d357caf40948ac2899a8dca76bfd88bb94d43a3c8a693)、[BT_OBEX_HEADER_ID_TIME](#gga3c893652eb9a5f0bf699d357caf40948a4fad7112257bd771e412eefd0c1e8bcc)、[BT_OBEX_HEADER_ID_DES](#gga3c893652eb9a5f0bf699d357caf40948a0fb867c69fb0c8680170359a41f2a3b1)、[BT_OBEX_HEADER_ID_TARGET](#gga3c893652eb9a5f0bf699d357caf40948a5929acc483779593b1b5c7b702b17976)、[BT_OBEX_HEADER_ID_HTTP](#gga3c893652eb9a5f0bf699d357caf40948a46735e651f7f378a3efb1be1a232e4ca)、[BT_OBEX_HEADER_ID_BODY](#gga3c893652eb9a5f0bf699d357caf40948a3264aa53da0fd7ec6611b8a20a8745f4)、[BT_OBEX_HEADER_ID_END_BODY](#gga3c893652eb9a5f0bf699d357caf40948aaa78dab2eda48ebd5d594024b53bec6b)、[BT_OBEX_HEADER_ID_WHO](#gga3c893652eb9a5f0bf699d357caf40948ab28b3ee885c373ca83a745fcd019e2e4)、[BT_OBEX_HEADER_ID_CONN_ID](#gga3c893652eb9a5f0bf699d357caf40948a3417001aed5d114492dcbe2c29496a1b)、[BT_OBEX_HEADER_ID_APP_PARAM](#gga3c893652eb9a5f0bf699d357caf40948a6dac6844a5db11dbc0e43613a32c13a9)、[BT_OBEX_HEADER_ID_AUTH_CHALLENGE](#gga3c893652eb9a5f0bf699d357caf40948aa48d582e278e748574d57818a7f5daf1)、[BT_OBEX_HEADER_ID_AUTH_RSP](#gga3c893652eb9a5f0bf699d357caf40948a97c1dfb166ac549576d30cadd156365f)、[BT_OBEX_HEADER_ID_CREATE_ID](#gga3c893652eb9a5f0bf699d357caf40948a31bec44f1240f21545f917eedd31026e)、[BT_OBEX_HEADER_ID_WAN_UUID](#gga3c893652eb9a5f0bf699d357caf40948a65e148b396f75cd55b992df84d5176ff)、[BT_OBEX_HEADER_ID_OBJECT_CLASS](#gga3c893652eb9a5f0bf699d357caf40948a5b723fde52df0965299d2f79e433c0a2)、[BT_OBEX_HEADER_ID_SESSION_PARAM](#gga3c893652eb9a5f0bf699d357caf40948afe34bec1dba1d1fca717f3ffa7c20628)、[BT_OBEX_HEADER_ID_SESSION_SEQ_NUM](#gga3c893652eb9a5f0bf699d357caf40948a3d42ab8b6a28f9062a97e2b1a9fa7c16)、[BT_OBEX_HEADER_ID_ACTION_ID](#gga3c893652eb9a5f0bf699d357caf40948a01e2d13304514242e954d45e74e3fcba)、[BT_OBEX_HEADER_ID_DEST_NAME](#gga3c893652eb9a5f0bf699d357caf40948ae5149b2da2cfb3c2e832f51282bc08d6)、[BT_OBEX_HEADER_ID_PERM](#gga3c893652eb9a5f0bf699d357caf40948a6aad7cbbcbebe670d370919fbdc61c19)、[BT_OBEX_HEADER_ID_SRM](#gga3c893652eb9a5f0bf699d357caf40948aa722c75042f0db4fba5c6a90516494b1)、[BT_OBEX_HEADER_ID_SRM_PARAM](#gga3c893652eb9a5f0bf699d357caf40948adda0f643d1c2ebd20d4c9d5644ef6b2c)。

OBEX 报头 ID（Header ID）。

<a id="r_ga622610a779a2e050e9a05c7eae945b3e"></a>

```c
enum bt_obex_state { BT_OBEX_DISCONNECTED , BT_OBEX_CONNECTING , BT_OBEX_CONNECTED , BT_OBEX_DISCONNECTING }
```

相关声明：[bt_obex_state](#ga622610a779a2e050e9a05c7eae945b3e)、[BT_OBEX_DISCONNECTED](#gga622610a779a2e050e9a05c7eae945b3ead7138e7373f5562faf13faa8bca424e6)、[BT_OBEX_CONNECTING](#gga622610a779a2e050e9a05c7eae945b3ea8743efcfd509ba7b156ac91a3c928614)、[BT_OBEX_CONNECTED](#gga622610a779a2e050e9a05c7eae945b3ea15ddd595c7832a8bfd382f87b938723b)、[BT_OBEX_DISCONNECTING](#gga622610a779a2e050e9a05c7eae945b3eae41568fe4c0d0db81ff60f41be6443a5)。

OBEX 生命周期状态（Life-span States）。

<a id="r_gab5f7e6a6c7503f97a851f48c70162483"></a>

```c
enum bt_obex_setpath_flags { BT_OBEX_SETPATH_FLAG_BACKUP = (1UL << (0U)) , BT_OBEX_SETPATH_FLAG_NO_CREATE = (1UL << (1U)) }
```

相关声明：[bt_obex_setpath_flags](#gab5f7e6a6c7503f97a851f48c70162483)、[BT_OBEX_SETPATH_FLAG_BACKUP](#ggab5f7e6a6c7503f97a851f48c70162483a9f89d8219783650a02e8ceb3faf6bd75)、[BT_OBEX_SETPATH_FLAG_NO_CREATE](#ggab5f7e6a6c7503f97a851f48c70162483ae47e6f7c5a8da44615e7245c5e1cd553)。

OBEX 设置路径操作标志（SetPath Operation Flags）。

<a id="r_ga12730d705667c2717c05a75cdfc07281"></a>

```c
enum bt_obex_action_id { BT_OBEX_ACTION_COPY = 0x00 , BT_OBEX_ACTION_MOVE_RENAME = 0x01 , BT_OBEX_ACTION_SET_PERM = 0x02 }
```

相关声明：[bt_obex_action_id](#ga12730d705667c2717c05a75cdfc07281)、[BT_OBEX_ACTION_COPY](#gga12730d705667c2717c05a75cdfc07281abb151a8123c7e6826a052ab252455aee)、[BT_OBEX_ACTION_MOVE_RENAME](#gga12730d705667c2717c05a75cdfc07281a7c57548121adf0afe43066070ef4b1fa)、[BT_OBEX_ACTION_SET_PERM](#gga12730d705667c2717c05a75cdfc07281a711263abb984488b8c7273052fb76ae0)。

OBEX 动作（Actions）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.4\_函数（Functions）

<a id="r_ga7cb42acb39c601375ef7c73f6be7e6af"></a>

```c
static const char * bt_obex_rsp_code_to_str (enum bt_obex_rsp_code rsp_code)
```

相关声明：[bt_obex_rsp_code_to_str](#ga7cb42acb39c601375ef7c73f6be7e6af)、[bt_obex_rsp_code](#ga81b84c24a976c6c13d33eb23b0b10ae9)。

将 OBEX 响应码（Response Code）转换为字符串。

<a id="r_ga1df3928a40f544ffb98b5eb1ceac62dd"></a>

```c
int bt_obex_server_register (struct bt_obex_server *server, const struct bt_uuid_128 *uuid)
```

相关声明：[bt_obex_server_register](#ga1df3928a40f544ffb98b5eb1ceac62dd)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)。

注册 OBEX 服务器（Server）。

<a id="r_ga642bfabb90d6576f92c5b546a592ec17"></a>

```c
int bt_obex_server_unregister (struct bt_obex_server *server)
```

相关声明：[bt_obex_server_unregister](#ga642bfabb90d6576f92c5b546a592ec17)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)。

注销 OBEX 服务器（Server）。

<a id="r_ga21afebccbd592381fb1569feaff98511"></a>

```c
int bt_obex_connect (struct bt_obex_client *client, uint16_t mopl, struct net_buf *buf)
```

相关声明：[bt_obex_connect](#ga21afebccbd592381fb1569feaff98511)、[bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 连接请求（connect request）。

<a id="r_gad91f69ba1b6780501722221bc516db4b"></a>

```c
int bt_obex_connect_rsp (struct bt_obex_server *server, uint8_t rsp_code, uint16_t mopl, struct net_buf *buf)
```

相关声明：[bt_obex_connect_rsp](#gad91f69ba1b6780501722221bc516db4b)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 连接响应（connect response）。

<a id="r_ga107787f08e55bf2740cc14cb5614bdbf"></a>

```c
int bt_obex_disconnect (struct bt_obex_client *client, struct net_buf *buf)
```

相关声明：[bt_obex_disconnect](#ga107787f08e55bf2740cc14cb5614bdbf)、[bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 断开连接请求（disconnect request）。

<a id="r_gac7763a310a553b3ba3c6b8b06951f191"></a>

```c
int bt_obex_disconnect_rsp (struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_obex_disconnect_rsp](#gac7763a310a553b3ba3c6b8b06951f191)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 断开连接响应（disconnect response）。

<a id="r_ga1d8684307899b1bd3724cb3aa996c53e"></a>

```c
int bt_obex_put (struct bt_obex_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_obex_put](#ga1d8684307899b1bd3724cb3aa996c53e)、[bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 放入请求（put request）。

<a id="r_gab5dfc5988d17ef0b79b84fd4c96dc60a"></a>

```c
int bt_obex_put_rsp (struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_obex_put_rsp](#gab5dfc5988d17ef0b79b84fd4c96dc60a)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 放入响应（put response）。

<a id="r_gabd3ff76e8a39e5944daa944f38a63c5f"></a>

```c
int bt_obex_get (struct bt_obex_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_obex_get](#gabd3ff76e8a39e5944daa944f38a63c5f)、[bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 获取请求（get request）。

<a id="r_ga3e9415fa4595d17676ada6622c9fd475"></a>

```c
int bt_obex_get_rsp (struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_obex_get_rsp](#ga3e9415fa4595d17676ada6622c9fd475)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 获取响应（get response）。

<a id="r_gafa2e01166c3177fe3aea937632fb52b7"></a>

```c
int bt_obex_abort (struct bt_obex_client *client, struct net_buf *buf)
```

相关声明：[bt_obex_abort](#gafa2e01166c3177fe3aea937632fb52b7)、[bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 中止请求（abort request）。

<a id="r_ga6f9de12183c445557f952fe2b49e3029"></a>

```c
int bt_obex_abort_rsp (struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_obex_abort_rsp](#ga6f9de12183c445557f952fe2b49e3029)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 中止响应（abort response）。

<a id="r_ga6d61b4421ad1e56cc2ae611ec77e561e"></a>

```c
int bt_obex_setpath (struct bt_obex_client *client, uint8_t flags, struct net_buf *buf)
```

相关声明：[bt_obex_setpath](#ga6d61b4421ad1e56cc2ae611ec77e561e)、[bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 设置路径请求（setpath request）。

<a id="r_ga13836db790849b5ec6b52bcb97c84505"></a>

```c
int bt_obex_setpath_rsp (struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_obex_setpath_rsp](#ga13836db790849b5ec6b52bcb97c84505)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 设置路径响应（setpath response）。

<a id="r_gab4b0a3533c7ec044efbee05c852d4f09"></a>

```c
int bt_obex_action (struct bt_obex_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_obex_action](#gab4b0a3533c7ec044efbee05c852d4f09)、[bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 动作请求（action request）。

<a id="r_gae178bf14d0495ad1e1aa5f7b4d8e1652"></a>

```c
int bt_obex_action_rsp (struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_obex_action_rsp](#gae178bf14d0495ad1e1aa5f7b4d8e1652)、[bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 动作响应（action response）。

<a id="r_ga14c8efe9c8a99e2736552d59972e7b23"></a>

```c
int bt_obex_add_header_count (struct net_buf *buf, uint32_t count)
```

相关声明：[bt_obex_add_header_count](#ga14c8efe9c8a99e2736552d59972e7b23)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

添加报头（Add Header）：对象数量（Number of Objects），供 Connect 使用。

<a id="r_ga9cd4c8342f67b53a3c3177a51f8887cb"></a>

```c
int bt_obex_add_header_name (struct net_buf *buf, uint16_t len, const uint8_t *name)
```

相关声明：[bt_obex_add_header_name](#ga9cd4c8342f67b53a3c3177a51f8887cb)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：对象名称（Object Name），通常为文件名。

<a id="r_gadd9f9b4cb50eb51df05c60705223e53b"></a>

```c
int bt_obex_add_header_type (struct net_buf *buf, uint16_t len, const uint8_t *type)
```

相关声明：[bt_obex_add_header_type](#gadd9f9b4cb50eb51df05c60705223e53b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：对象类型（Object Type），例如（原文此处未列出示例）。

<a id="r_ga0d27f09e3b8ea5636f0a34cf8729abaf"></a>

```c
int bt_obex_add_header_len (struct net_buf *buf, uint32_t len)
```

相关声明：[bt_obex_add_header_len](#ga0d27f09e3b8ea5636f0a34cf8729abaf)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

添加报头（Add Header）：对象长度（Object Length），单位为字节。

<a id="r_ga877d67e0a4135cabf8b5fddab4d014c6"></a>

```c
int bt_obex_add_header_time_iso_8601 (struct net_buf *buf, uint16_t len, const uint8_t *t)
```

相关声明：[bt_obex_add_header_time_iso_8601](#ga877d67e0a4135cabf8b5fddab4d014c6)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：日期／时间戳（Date/Time Stamp），ISO 8601 版本，为首选形式。

<a id="r_ga249e8b35b98f564d57dc1d644228b8f2"></a>

```c
int bt_obex_add_header_time (struct net_buf *buf, uint32_t t)
```

相关声明：[bt_obex_add_header_time](#ga249e8b35b98f564d57dc1d644228b8f2)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

添加报头（Add Header）：日期／时间戳（Date/Time Stamp），4 字节版本，仅用于兼容。

<a id="r_gaedc6f39972a5414d085ce17b09ffd121"></a>

```c
int bt_obex_add_header_description (struct net_buf *buf, uint16_t len, const uint8_t *dec)
```

相关声明：[bt_obex_add_header_description](#gaedc6f39972a5414d085ce17b09ffd121)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：对象的文本描述（Text Description）。

<a id="r_gac778e8ff0ac7e74795b107750a4a6719"></a>

```c
int bt_obex_add_header_target (struct net_buf *buf, uint16_t len, const uint8_t *target)
```

相关声明：[bt_obex_add_header_target](#gac778e8ff0ac7e74795b107750a4a6719)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：操作目标服务的名称（Service Name）。

<a id="r_ga6392da7ce8009eb95ab8c8a4d45fcb40"></a>

```c
int bt_obex_add_header_http (struct net_buf *buf, uint16_t len, const uint8_t *http)
```

相关声明：[bt_obex_add_header_http](#ga6392da7ce8009eb95ab8c8a4d45fcb40)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：一个 HTTP 1.x 报头（Header）。

<a id="r_gad1b3c22eea0915b962d7ab1e27726fe2"></a>

```c
int bt_obex_add_header_body (struct net_buf *buf, uint16_t len, const uint8_t *body)
```

相关声明：[bt_obex_add_header_body](#gad1b3c22eea0915b962d7ab1e27726fe2)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：对象主体的一个块（Body Chunk）。

<a id="r_ga805f13b12c7ce23057cb983d7159c36b"></a>

```c
int bt_obex_add_header_end_body (struct net_buf *buf, uint16_t len, const uint8_t *body)
```

相关声明：[bt_obex_add_header_end_body](#ga805f13b12c7ce23057cb983d7159c36b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：对象主体的最后一个块（Final Body Chunk）。

<a id="r_gadf2d0b93618e0e29341bc21dfd44954f"></a>

```c
static int bt_obex_add_header_body_or_end_body (struct net_buf *buf, uint16_t mopl, uint16_t len, const uint8_t *body, uint16_t *added_len)
```

相关声明：[bt_obex_add_header_body_or_end_body](#gadf2d0b93618e0e29341bc21dfd44954f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

添加报头（Add Header）：对象主体的一个块（Body Chunk），可能是最后一个块。

<a id="r_ga56690794dc07dfa598ae2ac68bc90aa0"></a>

```c
int bt_obex_add_header_who (struct net_buf *buf, uint16_t len, const uint8_t *who)
```

相关声明：[bt_obex_add_header_who](#ga56690794dc07dfa598ae2ac68bc90aa0)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：标识 OBEX 应用，用于判断是否正在与对等端通信。

<a id="r_gadc92dff93ef2051ff8b3b277a1bc1f17"></a>

```c
int bt_obex_add_header_conn_id (struct net_buf *buf, uint32_t conn_id)
```

相关声明：[bt_obex_add_header_conn_id](#gadc92dff93ef2051ff8b3b277a1bc1f17)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

添加报头（Add Header）：用于 OBEX 连接复用（Connection Multiplexing）的标识符。

<a id="r_gaeacfe7cb654bf33e7b387358a19fd3d3"></a>

```c
int bt_obex_add_header_app_param (struct net_buf *buf, size_t count, const struct bt_obex_tlv data[])
```

相关声明：[bt_obex_add_header_app_param](#gaeacfe7cb654bf33e7b387358a19fd3d3)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_obex_tlv](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md)。

添加报头（Add Header）：扩展应用请求与响应信息（Extended Application Request & Response Information）。

<a id="r_gacfc897d66e8c14629fa4d94f3782c741"></a>

```c
int bt_obex_add_header_auth_challenge (struct net_buf *buf, size_t count, const struct bt_obex_tlv data[])
```

相关声明：[bt_obex_add_header_auth_challenge](#gacfc897d66e8c14629fa4d94f3782c741)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_obex_tlv](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md)。

添加报头（Add Header）：认证摘要质询（Authentication Digest-challenge）。

<a id="r_ga5433561f0e9bad6da2d94dccca1578de"></a>

```c
int bt_obex_add_header_auth_rsp (struct net_buf *buf, size_t count, const struct bt_obex_tlv data[])
```

相关声明：[bt_obex_add_header_auth_rsp](#ga5433561f0e9bad6da2d94dccca1578de)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_obex_tlv](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md)。

添加报头（Add Header）：认证摘要响应（Authentication Digest-response）。

<a id="r_ga14c619eef70addc01d13841eda2d8f89"></a>

```c
int bt_obex_add_header_creator_id (struct net_buf *buf, uint32_t creator_id)
```

相关声明：[bt_obex_add_header_creator_id](#ga14c619eef70addc01d13841eda2d8f89)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

添加报头（Add Header）：指示对象创建者（Object Creator）。

<a id="r_ga111cd19449aba6fd0e667551874af0cf"></a>

```c
int bt_obex_add_header_wan_uuid (struct net_buf *buf, uint16_t len, const uint8_t *uuid)
```

相关声明：[bt_obex_add_header_wan_uuid](#ga111cd19449aba6fd0e667551874af0cf)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)。

添加报头（Add Header）：唯一标识网络客户端（Network Client），即 OBEX 服务器。

<a id="r_ga7473f42bef1409100886f7812a71a1dc"></a>

```c
int bt_obex_add_header_obj_class (struct net_buf *buf, uint16_t len, const uint8_t *obj_class)
```

相关声明：[bt_obex_add_header_obj_class](#ga7473f42bef1409100886f7812a71a1dc)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：对象的 OBEX 对象类（Object Class）。

<a id="r_gac47ddfe8cfe1e595a1821f32415d14eb"></a>

```c
int bt_obex_add_header_session_param (struct net_buf *buf, uint16_t len, const uint8_t *session_param)
```

相关声明：[bt_obex_add_header_session_param](#gac47ddfe8cfe1e595a1821f32415d14eb)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：会话命令／响应（Session Commands/Responses）使用的参数。

<a id="r_gad4a84068ce8c7c37b5189d366b771235"></a>

```c
int bt_obex_add_header_session_seq_number (struct net_buf *buf, uint32_t session_seq_number)
```

相关声明：[bt_obex_add_header_session_seq_number](#gad4a84068ce8c7c37b5189d366b771235)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

添加报头（Add Header）：每个 OBEX 数据包中用于保证可靠性的序列号（Sequence Number）。

<a id="r_ga58034dc9ba274030eea5bc3980e2ff95"></a>

```c
int bt_obex_add_header_action_id (struct net_buf *buf, uint8_t action_id)
```

相关声明：[bt_obex_add_header_action_id](#ga58034dc9ba274030eea5bc3980e2ff95)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：指定要执行的动作（Action），供 ACTION 操作使用。

<a id="r_ga4463514cf369beb882fec9ab15904821"></a>

```c
int bt_obex_add_header_dest_name (struct net_buf *buf, uint16_t len, const uint8_t *dest_name)
```

相关声明：[bt_obex_add_header_dest_name](#ga4463514cf369beb882fec9ab15904821)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：目标对象名称（Destination Object Name），供某些 ACTION 操作使用。

<a id="r_ga4b7c08fd620fdc1ff28a4714c84b6e30"></a>

```c
int bt_obex_add_header_perm (struct net_buf *buf, uint32_t perm)
```

相关声明：[bt_obex_add_header_perm](#ga4b7c08fd620fdc1ff28a4714c84b6e30)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

添加报头（Add Header）：用于设置权限（Permissions）的 4 字节位掩码。

<a id="r_ga23ed862cc6149a71793d02d89fb98cdc"></a>

```c
int bt_obex_add_header_srm (struct net_buf *buf, uint8_t srm)
```

相关声明：[bt_obex_add_header_srm](#ga23ed862cc6149a71793d02d89fb98cdc)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：用于设置单响应模式（Single Response Mode，SRM）的 1 字节值。

<a id="r_gaaa8a9630b0bf5597ca620b864fdafa87"></a>

```c
int bt_obex_add_header_srm_param (struct net_buf *buf, uint8_t srm_param)
```

相关声明：[bt_obex_add_header_srm_param](#gaaa8a9630b0bf5597ca620b864fdafa87)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加报头（Add Header）：单响应模式参数（Single Response Mode Parameter，SRM）。

<a id="r_ga5c93e9786adfb45a60a911087f859757"></a>

```c
int bt_obex_header_parse (struct net_buf *buf, bool(*func)(struct bt_obex_hdr *hdr, void *user_data), void *user_data)
```

相关声明：[bt_obex_header_parse](#ga5c93e9786adfb45a60a911087f859757)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_obex_hdr](../bluetooth_service_model_reference/P130_bt_obex_hdr_结构体.md)。

解析 OBEX 报头（Header）的辅助函数。

<a id="r_ga1e9b6dd9a8816ce87235b6b3d723541c"></a>

```c
int bt_obex_get_header_count (struct net_buf *buf, uint32_t *count)
```

相关声明：[bt_obex_get_header_count](#ga1e9b6dd9a8816ce87235b6b3d723541c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取报头值（Get Header Value）：对象数量（Number of Objects），供 Connect 使用。

<a id="r_gabef4622fa48b493f6d6ad5d1ecb65726"></a>

```c
int bt_obex_get_header_name (struct net_buf *buf, uint16_t *len, const uint8_t **name)
```

相关声明：[bt_obex_get_header_name](#gabef4622fa48b493f6d6ad5d1ecb65726)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：对象名称（Object Name），通常为文件名。

<a id="r_gabcfa9b33c0f91fbcf787d58e1f1bba41"></a>

```c
int bt_obex_get_header_type (struct net_buf *buf, uint16_t *len, const uint8_t **type)
```

相关声明：[bt_obex_get_header_type](#gabcfa9b33c0f91fbcf787d58e1f1bba41)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：对象类型（Object Type），例如（原文此处未列出示例）。

<a id="r_ga18ce5303b138959481666c0b8101f59e"></a>

```c
int bt_obex_get_header_len (struct net_buf *buf, uint32_t *len)
```

相关声明：[bt_obex_get_header_len](#ga18ce5303b138959481666c0b8101f59e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取报头值（Get Header Value）：对象长度（Object Length），单位为字节。

<a id="r_gacee063f6b53b85bad52a519cd1c794c5"></a>

```c
int bt_obex_get_header_time_iso_8601 (struct net_buf *buf, uint16_t *len, const uint8_t **t)
```

相关声明：[bt_obex_get_header_time_iso_8601](#gacee063f6b53b85bad52a519cd1c794c5)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：日期／时间戳（Date/Time Stamp），ISO 8601 版本，为首选形式。

<a id="r_ga367337d0f002a046248e92f3578efbb6"></a>

```c
int bt_obex_get_header_time (struct net_buf *buf, uint32_t *t)
```

相关声明：[bt_obex_get_header_time](#ga367337d0f002a046248e92f3578efbb6)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取报头值（Get Header Value）：日期／时间戳（Date/Time Stamp），4 字节版本，仅用于兼容。

<a id="r_ga3d805f241fc507587445b3204070055e"></a>

```c
int bt_obex_get_header_description (struct net_buf *buf, uint16_t *len, const uint8_t **dec)
```

相关声明：[bt_obex_get_header_description](#ga3d805f241fc507587445b3204070055e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：对象的文本描述（Text Description）。

<a id="r_ga49265f0aec21d8c33f56eb44723dabba"></a>

```c
int bt_obex_get_header_target (struct net_buf *buf, uint16_t *len, const uint8_t **target)
```

相关声明：[bt_obex_get_header_target](#ga49265f0aec21d8c33f56eb44723dabba)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：操作目标服务的名称（Service Name）。

<a id="r_ga5a181f7779df1ed2919ba3a94a630df4"></a>

```c
int bt_obex_get_header_http (struct net_buf *buf, uint16_t *len, const uint8_t **http)
```

相关声明：[bt_obex_get_header_http](#ga5a181f7779df1ed2919ba3a94a630df4)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：一个 HTTP 1.x 报头（Header）。

<a id="r_gaba71a8b3b8adc251a5a87fa60848bb3c"></a>

```c
int bt_obex_get_header_body (struct net_buf *buf, uint16_t *len, const uint8_t **body)
```

相关声明：[bt_obex_get_header_body](#gaba71a8b3b8adc251a5a87fa60848bb3c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：对象主体的一个块（Body Chunk）。

<a id="r_gaf8ff29ef3413492d2ec67fba278c2f82"></a>

```c
int bt_obex_get_header_end_body (struct net_buf *buf, uint16_t *len, const uint8_t **body)
```

相关声明：[bt_obex_get_header_end_body](#gaf8ff29ef3413492d2ec67fba278c2f82)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：对象主体的最后一个块（Final Body Chunk）。

<a id="r_gab551b01deed2c5a31f9a7a4b99045c9c"></a>

```c
int bt_obex_get_header_who (struct net_buf *buf, uint16_t *len, const uint8_t **who)
```

相关声明：[bt_obex_get_header_who](#gab551b01deed2c5a31f9a7a4b99045c9c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：标识 OBEX 应用，用于判断是否正在与对等端通信。

<a id="r_ga225ac4953da5e56a07865c8ab6ee0591"></a>

```c
int bt_obex_get_header_conn_id (struct net_buf *buf, uint32_t *conn_id)
```

相关声明：[bt_obex_get_header_conn_id](#ga225ac4953da5e56a07865c8ab6ee0591)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取报头值（Get Header Value）：用于 OBEX 连接复用（Connection Multiplexing）的标识符。

<a id="r_gaccecf00dc6209d1701ac0a6985f38257"></a>

```c
int bt_obex_tlv_parse (uint16_t len, const uint8_t *data, bool(*func)(struct bt_obex_tlv *tlv, void *user_data), void *user_data)
```

相关声明：[bt_obex_tlv_parse](#gaccecf00dc6209d1701ac0a6985f38257)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_obex_tlv](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md)。

解析 OBEX 类型－长度－值三元组（TLV Triplet）的辅助函数。

<a id="r_ga96981ef9187406efbd374fd623a14eaa"></a>

```c
int bt_obex_get_header_app_param (struct net_buf *buf, uint16_t *len, const uint8_t **app_param)
```

相关声明：[bt_obex_get_header_app_param](#ga96981ef9187406efbd374fd623a14eaa)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：扩展应用请求与响应信息（Extended Application Request & Response Information）。

<a id="r_ga6ee576eecea3947f1832d4859f16e1db"></a>

```c
int bt_obex_get_header_auth_challenge (struct net_buf *buf, uint16_t *len, const uint8_t **auth)
```

相关声明：[bt_obex_get_header_auth_challenge](#ga6ee576eecea3947f1832d4859f16e1db)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：认证摘要质询（Authentication Digest-challenge）。

<a id="r_gad9bae471db418e0a50c1b234e37b5d9d"></a>

```c
int bt_obex_get_header_auth_rsp (struct net_buf *buf, uint16_t *len, const uint8_t **auth)
```

相关声明：[bt_obex_get_header_auth_rsp](#gad9bae471db418e0a50c1b234e37b5d9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：认证摘要响应（Authentication Digest-response）。

<a id="r_ga9e08bf74bfbf001a80f40ee2d1b1ef82"></a>

```c
int bt_obex_get_header_creator_id (struct net_buf *buf, uint32_t *creator_id)
```

相关声明：[bt_obex_get_header_creator_id](#ga9e08bf74bfbf001a80f40ee2d1b1ef82)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取报头值（Get Header Value）：指示对象创建者（Object Creator）。

<a id="r_gaf9ffc19ef06a2773d664c0b15b2b8857"></a>

```c
int bt_obex_get_header_wan_uuid (struct net_buf *buf, uint16_t *len, const uint8_t **uuid)
```

相关声明：[bt_obex_get_header_wan_uuid](#gaf9ffc19ef06a2773d664c0b15b2b8857)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)。

获取报头值（Get Header Value）：唯一标识网络客户端（Network Client），即 OBEX 服务器。

<a id="r_ga49d1988eae4165f1cec624812cfe5f36"></a>

```c
int bt_obex_get_header_obj_class (struct net_buf *buf, uint16_t *len, const uint8_t **obj_class)
```

相关声明：[bt_obex_get_header_obj_class](#ga49d1988eae4165f1cec624812cfe5f36)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：对象的 OBEX 对象类（Object Class，原文写作 oBEX）。

<a id="r_ga560c8f0cb92b769a0716b2bc163c38e1"></a>

```c
int bt_obex_get_header_session_param (struct net_buf *buf, uint16_t *len, const uint8_t **session_param)
```

相关声明：[bt_obex_get_header_session_param](#ga560c8f0cb92b769a0716b2bc163c38e1)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：会话命令／响应（Session Commands/Responses）使用的参数。

<a id="r_gaaa33502f3ae9f97767bd0e5e660f021f"></a>

```c
int bt_obex_get_header_session_seq_number (struct net_buf *buf, uint32_t *session_seq_number)
```

相关声明：[bt_obex_get_header_session_seq_number](#gaaa33502f3ae9f97767bd0e5e660f021f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取报头值（Get Header Value）：每个 OBEX 数据包中用于保证可靠性的序列号（Sequence Number）。

<a id="r_gacc1673746737e4163165b5f379c8105f"></a>

```c
int bt_obex_get_header_action_id (struct net_buf *buf, uint8_t *action_id)
```

相关声明：[bt_obex_get_header_action_id](#gacc1673746737e4163165b5f379c8105f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：指定要执行的动作（Action），供 ACTION 操作使用。

<a id="r_ga945c0865edef9f34e2cf1e817a3b45c1"></a>

```c
int bt_obex_get_header_dest_name (struct net_buf *buf, uint16_t *len, const uint8_t **dest_name)
```

相关声明：[bt_obex_get_header_dest_name](#ga945c0865edef9f34e2cf1e817a3b45c1)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：目标对象名称（Destination Object Name），供某些 ACTION 操作使用。

<a id="r_gab234af4e944a3e97e3459613078005a1"></a>

```c
int bt_obex_get_header_perm (struct net_buf *buf, uint32_t *perm)
```

相关声明：[bt_obex_get_header_perm](#gab234af4e944a3e97e3459613078005a1)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取报头值（Get Header Value）：用于设置权限（Permissions）的 4 字节位掩码。

<a id="r_gae0865eea3d8db09023cfc77b2118bad5"></a>

```c
int bt_obex_get_header_srm (struct net_buf *buf, uint8_t *srm)
```

相关声明：[bt_obex_get_header_srm](#gae0865eea3d8db09023cfc77b2118bad5)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：用于设置单响应模式（Single Response Mode，SRM）的 1 字节值。

<a id="r_ga7501193240498e7a9da0034b2e434ffc"></a>

```c
int bt_obex_get_header_srm_param (struct net_buf *buf, uint8_t *srm_param)
```

相关声明：[bt_obex_get_header_srm_param](#ga7501193240498e7a9da0034b2e434ffc)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取报头值（Get Header Value）：单响应模式参数（Single Response Mode Parameter，SRM）。

<a id="r_gafadd6e44ae19786617b5e60608fa4651"></a>

```c
int bt_obex_make_uuid (union bt_obex_uuid *uuid, const uint8_t *data, uint16_t len)
```

相关声明：[bt_obex_make_uuid](#gafadd6e44ae19786617b5e60608fa4651)、[bt_obex_uuid](../bluetooth_service_model_reference/P189_bt_obex_uuid_联合体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

使用指定数据和长度构造通用唯一标识符（UUID）。

<a id="r_ga170456d806c0ff494b0c1d7fad763051"></a>

```c
bool bt_obex_string_is_valid (uint8_t id, uint16_t len, const uint8_t *str)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_obex_string_is_valid](#ga170456d806c0ff494b0c1d7fad763051)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

检查字符串（String）是否有效。

<a id="r_ga296af3d5a15684e4aa3846cc24203fef"></a>

```c
bool bt_obex_has_header (struct net_buf *buf, uint8_t id)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_obex_has_header](#ga296af3d5a15684e4aa3846cc24203fef)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

检查 buf 是否包含指定报头（Header）。

<a id="r_ga5ae88dad0e7c97d0f20c7e4ceeeb3ce8"></a>

```c
bool bt_obex_has_app_param (struct net_buf *buf, uint8_t id)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_obex_has_app_param](#ga5ae88dad0e7c97d0f20c7e4ceeeb3ce8)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

检查 buf 是否包含指定应用参数（Application Parameter）。

<a id="r_ga3708c17f9c23fdeb5ceda376787cebbd"></a>

```c
int bt_obex_generate_nonce (const uint8_t *pwd, size_t pwd_len, uint8_t nonce[16])
```

相关声明：[bt_obex_generate_nonce](#ga3708c17f9c23fdeb5ceda376787cebbd)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为 OBEX 认证质询（Authentication Challenge）生成一次性随机数（Nonce）。

<a id="r_ga51baeae9280bb50e34b6608f620498fa"></a>

```c
int bt_obex_calculate_request_digest (const uint8_t *pwd, size_t pwd_len, const uint8_t nonce[16], uint8_t digest[16])
```

相关声明：[bt_obex_calculate_request_digest](#ga51baeae9280bb50e34b6608f620498fa)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为 OBEX 认证响应（Authentication Response）计算请求摘要（Request Digest）。

<a id="r_gae31398502c9d237d7afd47d70315be3f"></a>

```c
int bt_obex_verify_auth_response (const uint8_t *pwd, size_t pwd_len, const uint8_t nonce[16], const uint8_t digest[16])
```

相关声明：[bt_obex_verify_auth_response](#gae31398502c9d237d7afd47d70315be3f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

验证 OBEX 认证响应（Authentication Response）。

## 5.5\_详细说明（Detailed Documentation）

<a id="ga6c6bd723b6b7c84d53ea0d0bc9787fbc"></a>

### `BT_OBEX_CHALLENGE_TAG_NONCE`

```c
#define BT_OBEX_CHALLENGE_TAG_NONCE 0x00
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 摘要质询标记（Digest-challenge Tag）：Nonce，以字节串表示的一次性随机数。

<a id="gaab47709ef621b63172fa54314bf3eff0"></a>

### `BT_OBEX_CHALLENGE_TAG_NONCE_LEN`

```c
#define BT_OBEX_CHALLENGE_TAG_NONCE_LEN 16
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 摘要质询的一次性随机数长度（Nonce Length），16 字节。

<a id="gad35d3b9c3a398b1f4bdba610c825aca3"></a>

### `BT_OBEX_CHALLENGE_TAG_OPTION_ACCESS_MODE`

```c
#define BT_OBEX_CHALLENGE_TAG_OPTION_ACCESS_MODE BIT(1)
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

选项位 1（BIT1）：访问模式（Access Mode）；设置时为只读（Read Only），否则允许完全访问（Full Access）。

<a id="ga4d936864173fe0218e660df7b53d666e"></a>

### `BT_OBEX_CHALLENGE_TAG_OPTION_REQ_USER_ID`

```c
#define BT_OBEX_CHALLENGE_TAG_OPTION_REQ_USER_ID BIT(0)
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

选项位 0（BIT0）：设置时，必须在认证响应（Authenticate Response）中发送用户 ID（User Id）。

<a id="gae48159128c97a6579c8cbf12b5c934e4"></a>

### `BT_OBEX_CHALLENGE_TAG_OPTIONS`

```c
#define BT_OBEX_CHALLENGE_TAG_OPTIONS 0x01
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 摘要质询标记（Digest-challenge Tag）：Options，可选质询信息（Optional Challenge Information）。

<a id="ga40725e7d1882cd9f793dc490a9ad8341"></a>

### `BT_OBEX_CHALLENGE_TAG_OPTIONS_LEN`

```c
#define BT_OBEX_CHALLENGE_TAG_OPTIONS_LEN 1
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 摘要质询的选项长度（Options Length），1 字节。

<a id="ga7957818ad49e8e406942dad698e2d089"></a>

### `BT_OBEX_CHALLENGE_TAG_REALM`

```c
#define BT_OBEX_CHALLENGE_TAG_REALM 0x02
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 摘要质询标记（Digest-challenge Tag）：Realm，一个可显示字符串，指示应使用哪个用户 ID 和／或密码。

字符串的第一个字节指定要使用的字符集（Character Set），其取值与 IrLMP 为昵称（Nickname）定义的字符集取值相同。

<a id="gab3db35da4b3daf626e89223262273fb9"></a>

### `BT_OBEX_DATA_LEN_OF_HEADER_BODY`

```c
#define BT_OBEX_DATA_LEN_OF_HEADER_BODY ( len)
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

展开值（Value）：

```c
((len) - BT_OBEX_HDR_LEN_OF_HEADER_BODY)
```

添加的报头为主体／主体结束（Body / End Body）时，缓冲区的最大剩余长度。

用于在添加正文头（Body Header）数据时计算最大发送长度。

原始示例（Example）：

```c
uint16_t len = BT_OBEX_PDU_LEN(mopl);

len = MIN(len - buf->len, net_buf_tailroom(buf));
if (len > BT_OBEX_HDR_LEN_OF_HEADER_BODY) {
        len = BT_OBEX_DATA_LEN_OF_HEADER_BODY(len);
        Calling bt_obex_add_header_body() or bt_obex_add_header_end_body()
        ...
}
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `len` | 最大剩余长度（Maximum Remaining Length）。 |

<a id="ga534e9ffa9f7ba93eda049fd9022df69a"></a>

### `BT_OBEX_HDR_LEN`

```c
#define BT_OBEX_HDR_LEN 3
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

PUT 和 GET 请求及响应的对象交换（OBEX）数据包报头长度。

<a id="ga5571666538c43d8d71dd17dc58d19f45"></a>

### `BT_OBEX_HDR_LEN_OF_HEADER_BODY`

```c
#define BT_OBEX_HDR_LEN_OF_HEADER_BODY 3
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 主体／主体结束报头（Body / End Body Header）的长度。

<a id="ga6206007c2c3e50d997ae5a644ceae783"></a>

### `BT_OBEX_MIN_MTU`

```c
#define BT_OBEX_MIN_MTU 255
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

<a id="ga500dcfab79831c5d640406cff8c54f01"></a>

### `BT_OBEX_PDU_LEN`

```c
#define BT_OBEX_PDU_LEN ( mopl)
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

展开值（Value）：

```c
((mopl) - BT_OBEX_HDR_LEN)
```

对象交换（OBEX）数据包的 PDU 数据长度上限。

<a id="gacbdbc35907fcd1b5362fb108f7925412"></a>

### `BT_OBEX_RESPONSE_TAG_NONCE`

```c
#define BT_OBEX_RESPONSE_TAG_NONCE 0x02
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 摘要响应标记（Digest-response Tag）：Nonce，即摘要质询字符串中发送的一次性随机数。

<a id="ga78897a868628d0dc9992ebb7d79e6dd5"></a>

### `BT_OBEX_RESPONSE_TAG_NONCE_LEN`

```c
#define BT_OBEX_RESPONSE_TAG_NONCE_LEN 16
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 摘要响应的一次性随机数长度（Nonce Length），16 字节。

<a id="ga69d4d1a8af96df807ab9f1ec5fc42503"></a>

### `BT_OBEX_RESPONSE_TAG_REQ_DIGEST`

```c
#define BT_OBEX_RESPONSE_TAG_REQ_DIGEST 0x00
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 摘要响应标记（Digest-response Tag）：Request-digest，以字节串表示的请求摘要。

<a id="gacbae9ed1d18eaab7934258cbfe4fd62a"></a>

### `BT_OBEX_RESPONSE_TAG_REQ_DIGEST_LEN`

```c
#define BT_OBEX_RESPONSE_TAG_REQ_DIGEST_LEN 16
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 摘要响应的请求摘要长度（Request-digest Length），16 字节。

<a id="gad466df7bba9c20ff47820121372193ec"></a>

### `BT_OBEX_RESPONSE_TAG_USER_ID`

```c
#define BT_OBEX_RESPONSE_TAG_USER_ID 0x01
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 摘要响应标记（Digest-response Tag）：User Id，长度为 n 的用户 ID 字符串。

最大大小为 20 字节。

<a id="ga3d89a9c04baec0be2dd6b9f922a7c985"></a>

### `BT_OBEX_SEND_BUF_RESERVE`

```c
#define BT_OBEX_SEND_BUF_RESERVE 7
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

<a id="ga12730d705667c2717c05a75cdfc07281"></a>

### `bt_obex_action_id`

```c
enum bt_obex_action_id
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 动作（Actions）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_OBEX_ACTION_COPY` | 复制对象操作（Copy Object Action）。 |
| `BT_OBEX_ACTION_MOVE_RENAME` | 移动／重命名对象操作（Move/Rename Object Action）。 |
| `BT_OBEX_ACTION_SET_PERM` | 设置对象权限操作（Set Object Permissions Action）。 |

<a id="ga3c893652eb9a5f0bf699d357caf40948"></a>

### `bt_obex_header_id`

```c
enum bt_obex_header_id
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 报头 ID（Header ID）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_OBEX_HEADER_ID_COUNT` | 对象数量（Number of Objects），用于连接（Connect）操作。 |
| `BT_OBEX_HEADER_ID_NAME` | 对象名称（Name），通常是文件名。 |
| `BT_OBEX_HEADER_ID_TYPE` | 对象类型（Type），例如文本（Text）、HTML、二进制（Binary）或厂商专用类型（Manufacturer Specific）。 |
| `BT_OBEX_HEADER_ID_LEN` | 对象长度（Length），单位为字节。 |
| `BT_OBEX_HEADER_ID_TIME_ISO_8601` | 日期／时间戳（Date/Time Stamp），ISO 8601 版本，推荐使用。 |
| `BT_OBEX_HEADER_ID_TIME` | 日期／时间戳（Date/Time Stamp），4 字节版本，仅用于兼容。 |
| `BT_OBEX_HEADER_ID_DES` | 对象的文本描述（Text Description）。 |
| `BT_OBEX_HEADER_ID_TARGET` | 操作所针对的服务名称（Service Name）。 |
| `BT_OBEX_HEADER_ID_HTTP` | 一个 HTTP 1.x 头（Header）。 |
| `BT_OBEX_HEADER_ID_BODY` | 对象正文（Object Body）的一个分块。 |
| `BT_OBEX_HEADER_ID_END_BODY` | 对象正文（Object Body）的最后一个分块。 |
| `BT_OBEX_HEADER_ID_WHO` | 标识 OBEX 应用程序，用于判断是否在与相应对端通信。 |
| `BT_OBEX_HEADER_ID_CONN_ID` | 用于 OBEX 连接复用（Connection Multiplexing）的标识符。 |
| `BT_OBEX_HEADER_ID_APP_PARAM` | 扩展应用请求与响应信息（Extended Application Request & Response Information）。 |
| `BT_OBEX_HEADER_ID_AUTH_CHALLENGE` | 认证摘要质询（Authentication Digest-challenge）。 |
| `BT_OBEX_HEADER_ID_AUTH_RSP` | 认证摘要响应（Authentication Digest-response）。 |
| `BT_OBEX_HEADER_ID_CREATE_ID` | 指示对象的创建者（Creator）。 |
| `BT_OBEX_HEADER_ID_WAN_UUID` | 唯一标识网络客户端（Network Client），即 OBEX 服务器。 |
| `BT_OBEX_HEADER_ID_OBJECT_CLASS` | 对象的 OBEX 对象类（Object Class）。 |
| `BT_OBEX_HEADER_ID_SESSION_PARAM` | 会话命令／响应（Session Commands/Responses）中使用的参数。 |
| `BT_OBEX_HEADER_ID_SESSION_SEQ_NUM` | 各个 OBEX 数据包中用于保证可靠性的序列号（Sequence Number）。 |
| `BT_OBEX_HEADER_ID_ACTION_ID` | 指定要执行的操作（Action），用于 `ACTION` 操作。 |
| `BT_OBEX_HEADER_ID_DEST_NAME` | 目标对象名称（Destination Object Name），用于某些 `ACTION` 操作。 |
| `BT_OBEX_HEADER_ID_PERM` | 用于设置权限（Permissions）的 4 字节位掩码。 |
| `BT_OBEX_HEADER_ID_SRM` | 用于设置单响应模式（Single Response Mode，SRM）的 1 字节值。 |
| `BT_OBEX_HEADER_ID_SRM_PARAM` | 用于设置单响应模式（Single Response Mode，SRM）期间所用参数的 1 字节值。 |

<a id="ga81b84c24a976c6c13d33eb23b0b10ae9"></a>

### `bt_obex_rsp_code`

```c
enum bt_obex_rsp_code
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 响应码（Response Code）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_OBEX_RSP_CODE_CONTINUE` | 继续（Continue）。 |
| `BT_OBEX_RSP_CODE_OK` | 成功（OK）。 |
| `BT_OBEX_RSP_CODE_SUCCESS` | 成功。 |
| `BT_OBEX_RSP_CODE_CREATED` | 已创建（Created）。 |
| `BT_OBEX_RSP_CODE_ACCEPTED` | 已接受（Accepted）。 |
| `BT_OBEX_RSP_CODE_NON_AUTH_INFO` | 非权威信息（Non-Authoritative Information）。 |
| `BT_OBEX_RSP_CODE_NO_CONTENT` | 无内容（No Content）。 |
| `BT_OBEX_RSP_CODE_RESET_CONTENT` | 重置内容（Reset Content）。 |
| `BT_OBEX_RSP_CODE_PARTIAL_CONTENT` | 部分内容（Partial Content）。 |
| `BT_OBEX_RSP_CODE_MULTI_CHOICES` | 多种选择（Multiple Choices）。 |
| `BT_OBEX_RSP_CODE_MOVED_PERM` | 永久移动（Moved Permanently）。 |
| `BT_OBEX_RSP_CODE_MOVED_TEMP` | 临时移动（Moved Temporarily）。 |
| `BT_OBEX_RSP_CODE_SEE_OTHER` | 查看其他资源（See Other）。 |
| `BT_OBEX_RSP_CODE_NOT_MODIFIED` | 未修改（Not Modified）。 |
| `BT_OBEX_RSP_CODE_USE_PROXY` | 使用代理（Use Proxy）。 |
| `BT_OBEX_RSP_CODE_BAD_REQ` | 错误请求（Bad Request）：服务器无法理解请求。 |
| `BT_OBEX_RSP_CODE_UNAUTH` | 未经授权（Unauthorized）。 |
| `BT_OBEX_RSP_CODE_PAY_REQ` | 需要付费（Payment Required）。 |
| `BT_OBEX_RSP_CODE_FORBIDDEN` | 禁止（Forbidden）：理解该操作，但拒绝执行。 |
| `BT_OBEX_RSP_CODE_NOT_FOUND` | 未找到（Not Found）。 |
| `BT_OBEX_RSP_CODE_NOT_ALLOW` | 方法不允许（Method Not Allowed）。 |
| `BT_OBEX_RSP_CODE_NOT_ACCEPT` | 不可接受（Not Acceptable）。 |
| `BT_OBEX_RSP_CODE_PROXY_AUTH_REQ` | 需要代理身份验证（Proxy Authentication Required）。 |
| `BT_OBEX_RSP_CODE_REQ_TIMEOUT` | 请求超时（Request Time Out）。 |
| `BT_OBEX_RSP_CODE_CONFLICT` | 冲突（Conflict）。 |
| `BT_OBEX_RSP_CODE_GONE` | 资源已永久移除（Gone）。 |
| `BT_OBEX_RSP_CODE_LEN_REQ` | 需要长度（Length Required）。 |
| `BT_OBEX_RSP_CODE_PRECON_FAIL` | 前置条件失败（Precondition Failed）。 |
| `BT_OBEX_RSP_CODE_ENTITY_TOO_LARGE` | 请求实体过大（Requested Entity Too Large）。 |
| `BT_OBEX_RSP_CODE_URL_TOO_LARGE` | 请求 URL 过长（Requested URL Too Large）。 |
| `BT_OBEX_RSP_CODE_UNSUPP_MEDIA_TYPE` | 不支持的媒体类型（Unsupported Media Type）。 |
| `BT_OBEX_RSP_CODE_INTER_ERROR` | 服务器内部错误（Internal Server Error）。 |
| `BT_OBEX_RSP_CODE_NOT_IMPL` | 未实现（Not Implemented）。 |
| `BT_OBEX_RSP_CODE_BAD_GATEWAY` | 网关错误（Bad Gateway）。 |
| `BT_OBEX_RSP_CODE_UNAVAIL` | 服务不可用（Service Unavailable）。 |
| `BT_OBEX_RSP_CODE_GATEWAY_TIMEOUT` | 网关超时（Gateway Timeout）。 |
| `BT_OBEX_RSP_CODE_VER_UNSUPP` | 不支持的 HTTP 版本（HTTP Version Not Supported）。 |
| `BT_OBEX_RSP_CODE_DB_FULL` | 数据库已满（Database Full）。 |
| `BT_OBEX_RSP_CODE_DB_LOCK` | 数据库已锁定（Database Locked）。 |

<a id="gab5f7e6a6c7503f97a851f48c70162483"></a>

### `bt_obex_setpath_flags`

```c
enum bt_obex_setpath_flags
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 设置路径操作标志（SetPath Operation Flags）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_OBEX_SETPATH_FLAG_BACKUP` | 应用名称（Name）之前返回上一级，等同于许多系统中的 `../`。 |
| `BT_OBEX_SETPATH_FLAG_NO_CREATE` | 如果文件夹不存在，不创建文件夹，而是返回错误。 |

<a id="ga622610a779a2e050e9a05c7eae945b3e"></a>

### `bt_obex_state`

```c
enum bt_obex_state
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 生命周期状态（Life-span States）。

仅供内部 API 使用，用于根据操作上下文（Operational Context）将 OBEX 设置为适当状态。

调用 `bt_obex_connect` 时，或从 `bt_obex_server_ops::connect` 返回时，OBEX 进入 `BT_OBEX_CONNECTING` 状态。

当 OBEX 离开 `BT_OBEX_CONNECTING` 状态并进入 `BT_OBEX_CONNECTED` 时，会调用 `bt_obex_connect_rsp` 或 `bt_obex_client_ops::connect`，响应码为 `BT_OBEX_RSP_CODE_SUCCESS`。

当 OBEX 从其他状态进入 `BT_OBEX_DISCONNECTED` 时，会调用 `bt_obex_client_ops::disconnect` 或 `bt_obex_connect_rsp`，响应码为 `BT_OBEX_RSP_CODE_SUCCESS`；或者 OBEX 传输（Transport）从其他传输状态进入已断开状态。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_OBEX_DISCONNECTED` | OBEX 已断开连接（Disconnected）。 |
| `BT_OBEX_CONNECTING` | OBEX 正在连接（Connecting）。 |
| `BT_OBEX_CONNECTED` | OBEX 已准备好承载上层通信（Upper Layer Traffic）。 |
| `BT_OBEX_DISCONNECTING` | OBEX 正在断开连接（Disconnecting）。 |

<a id="gafa2e01166c3177fe3aea937632fb52b7"></a>

### `bt_obex_abort()`

```c
int bt_obex_abort ( struct bt_obex_client * client, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 中止请求（abort request）。

当客户端决定在多包操作（Multi-packet Operation，例如 Put）正常结束前终止它时，使用中止请求（Abort Request）。中止请求始终装入一个 OBEX 数据包，并设置 `Final` 位。参数 `buf` 保存中止请求的数据包数据，即头序列（Sequence of Headers）。所有头均通过 `bt_obex_add_header_*` 函数打包，例如描述头（Description Header）通过 `bt_obex_add_header_description` 打包。如果没有需要发送的数据，`buf` 可以为 `NULL`。译注：原文先称 `buf` 为第二个参数，随后又写成第三个参数，存在不一致；具体位置以本项函数声明为准。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | OBEX 客户端对象（Client Object）。 |
| `buf` | 要发送的头序列（Sequence of Headers）。 |

**说明（Note）**：注意：成功时，缓冲区所有权（Buffer Ownership）转交给协议栈；发生错误时，调用者保留缓冲区所有权。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga6f9de12183c445557f952fe2b49e3029"></a>

### `bt_obex_abort_rsp()`

```c
int bt_obex_abort_rsp ( struct bt_obex_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 中止响应（abort response）。

中止响应（Abort Response）用于确认中止请求数据包，由服务器发送给客户端。中止响应始终装入一个 OBEX 数据包，并设置 `Final` 位。

第二个参数 `rsp_code` 用于传递 `bt_obex_rsp_code` 响应码，典型成功值为 `BT_OBEX_RSP_CODE_SUCCESS`。第三个参数 `buf` 保存中止响应的数据包数据，即头序列（Sequence of Headers）。所有头均通过 `bt_obex_add_header_*` 函数打包。如果没有需要发送的数据，`buf` 可以为 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | OBEX 服务器对象（Server Object）。 |
| `rsp_code` | 响应码（Response Code）。 |
| `buf` | 要发送的头序列（Sequence of Headers）。 |

**说明（Note）**：注意：成功时，缓冲区所有权（Buffer Ownership）转交给协议栈；发生错误时，调用者保留缓冲区所有权。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gab4b0a3533c7ec044efbee05c852d4f09"></a>

### `bt_obex_action()`

```c
int bt_obex_action ( struct bt_obex_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 动作请求（action request）。

动作操作（Action Operation）用于满足常见动作的需求。其中使用动作 ID 头 `BT_OBEX_HEADER_ID_ACTION_ID`，该头包含一个动作标识符（Action Identifier），用于定义要执行的动作。所有动作均为可选，是否支持取决于服务器实现。

`bt_obex_action_id` 定义了三种动作（Actions）：

`BT_OBEX_ACTION_COPY` 用于将对象从一个位置复制到另一个位置。名称头（Name）`BT_OBEX_HEADER_ID_NAME` 指定源文件名，目标名称头（Dest Name）`BT_OBEX_HEADER_ID_DEST_NAME` 指定目标文件名。此动作必须提供这两个头。

`BT_OBEX_ACTION_MOVE_RENAME` 用于将对象从一个位置移动到另一个位置，也可用于重命名对象。名称头（Name）`BT_OBEX_HEADER_ID_NAME` 指定源文件名，目标名称头（Dest Name）`BT_OBEX_HEADER_ID_DEST_NAME` 指定目标文件名。此动作必须提供这两个头。

`BT_OBEX_ACTION_SET_PERM` 用于设置对象或文件夹的访问权限（Access Permissions）。名称头（Name）`BT_OBEX_HEADER_ID_NAME` 指定源文件名，权限头（Permissions）`BT_OBEX_HEADER_ID_PERM` 指定此对象的新权限。此动作必须提供这两个头。

动作操作（Action Operation）由一个或多个请求数据包组成；最后一个请求包应设置第二个参数 `final`。第三个参数 `buf` 保存动作请求的数据包数据，即头序列（Sequence of Headers）。所有头均通过 `bt_obex_add_header_*` 函数打包，例如名称头（Name）通过 `bt_obex_add_header_name` 打包。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | OBEX 客户端对象（Client Object）。 |
| `final` | 操作码（Opcode）的最终位（Final Bit）。 |
| `buf` | 要发送的头序列（Sequence of Headers）。 |

**说明（Note）**：注意：成功时，缓冲区所有权（Buffer Ownership）转交给协议栈；发生错误时，调用者保留缓冲区所有权。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gae178bf14d0495ad1e1aa5f7b4d8e1652"></a>

### `bt_obex_action_rsp()`

```c
int bt_obex_action_rsp ( struct bt_obex_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 动作响应（action response）。

动作响应（Action Response）用于确认动作请求数据包，由服务器发送给客户端。第二个参数 `rsp_code` 用于传递 `bt_obex_rsp_code` 响应码，典型成功值为 `BT_OBEX_RSP_CODE_SUCCESS`。

`bt_obex_action_id` 定义了三种动作（Actions）。每种动作请求都有相应的失败响应码（Failure Response Codes）。

对于 `BT_OBEX_ACTION_COPY` 动作：`BT_OBEX_RSP_CODE_NOT_FOUND` 表示源对象或目标文件夹不存在；`BT_OBEX_RSP_CODE_FORBIDDEN` 表示无法修改目标对象／文件夹的权限，访问被拒绝；`BT_OBEX_RSP_CODE_DB_FULL` 表示内存不足，无法在目标文件夹中创建对象；`BT_OBEX_RSP_CODE_CONFLICT` 表示无法修改权限，发生共享冲突，或对象／设置对象权限操作忙；`BT_OBEX_RSP_CODE_NOT_IMPL` 表示不支持设置对象权限操作；`BT_OBEX_RSP_CODE_NOT_MODIFIED` 表示目标文件夹／文件已存在，无法创建。译注：此处有关设置权限的措辞来自官方原文，虽列在复制动作下，仍按原文保留。

对于 `BT_OBEX_ACTION_MOVE_RENAME` 动作：`BT_OBEX_RSP_CODE_NOT_FOUND` 表示源对象或目标文件夹不存在；`BT_OBEX_RSP_CODE_FORBIDDEN` 表示无法修改目标对象／文件夹的权限，访问被拒绝；`BT_OBEX_RSP_CODE_DB_FULL` 表示内存不足，无法在目标文件夹中创建对象；`BT_OBEX_RSP_CODE_CONFLICT` 表示无法修改权限，发生共享冲突，或对象／设置对象权限操作忙；`BT_OBEX_RSP_CODE_NOT_IMPL` 表示不支持设置对象权限操作；`BT_OBEX_RSP_CODE_NOT_MODIFIED` 表示目标文件夹／文件已存在，无法创建。译注：此处有关设置权限的措辞来自官方原文，虽列在移动／重命名动作下，仍按原文保留。

对于 `BT_OBEX_ACTION_SET_PERM` 动作：`BT_OBEX_RSP_CODE_NOT_FOUND` 表示源对象或目标文件夹不存在；`BT_OBEX_RSP_CODE_FORBIDDEN` 表示无法修改目标对象／文件夹的权限，访问被拒绝；`BT_OBEX_RSP_CODE_NOT_IMPL` 表示不支持设置对象权限操作；`BT_OBEX_RSP_CODE_CONFLICT` 表示无法修改权限，发生共享冲突，或对象／设置对象权限操作忙。

第三个参数 `buf` 保存动作响应（Action Response）的数据包数据，即头序列（Sequence of Headers）。所有头均通过 `bt_obex_add_header_*` 函数打包。如果没有需要发送的数据，`buf` 可以为 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | OBEX 服务器对象（Server Object）。 |
| `rsp_code` | 响应码（Response Code）。 |
| `buf` | 要发送的头序列（Sequence of Headers）。 |

**说明（Note）**：注意：成功时，缓冲区所有权（Buffer Ownership）转交给协议栈；发生错误时，调用者保留缓冲区所有权。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga58034dc9ba274030eea5bc3980e2ff95"></a>

### `bt_obex_add_header_action_id()`

```c
int bt_obex_add_header_action_id ( struct net_buf * buf, uint8_t action_id )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：指定要执行的动作（Action），供 ACTION 操作使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `action_id` | 动作 ID（Action Id），参见 `bt_obex_action_id`。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaeacfe7cb654bf33e7b387358a19fd3d3"></a>

### `bt_obex_add_header_app_param()`

```c
int bt_obex_add_header_app_param ( struct net_buf * buf, size_t count, const struct bt_obex_tlv data[] )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：扩展应用请求与响应信息（Extended Application Request & Response Information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `count` | `data` 中 `bt_obex_tlv` 结构的数量。 |
| `data` | `bt_obex_tlv` 结构数组。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gacfc897d66e8c14629fa4d94f3782c741"></a>

### `bt_obex_add_header_auth_challenge()`

```c
int bt_obex_add_header_auth_challenge ( struct net_buf * buf, size_t count, const struct bt_obex_tlv data[] )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：认证摘要质询（Authentication Digest-challenge）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `count` | `data` 中 `bt_obex_tlv` 结构的数量。 |
| `data` | `bt_obex_tlv` 结构数组。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga5433561f0e9bad6da2d94dccca1578de"></a>

### `bt_obex_add_header_auth_rsp()`

```c
int bt_obex_add_header_auth_rsp ( struct net_buf * buf, size_t count, const struct bt_obex_tlv data[] )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：认证摘要响应（Authentication Digest-response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `count` | `data` 中 `bt_obex_tlv` 结构的数量。 |
| `data` | `bt_obex_tlv` 结构数组。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gad1b3c22eea0915b962d7ab1e27726fe2"></a>

### `bt_obex_add_header_body()`

```c
int bt_obex_add_header_body ( struct net_buf * buf, uint16_t len, const uint8_t * body )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：对象主体的一个块（Body Chunk）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 正文（Body）的长度。 |
| `body` | 对象正文（Object Body）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gadf2d0b93618e0e29341bc21dfd44954f"></a>

### `bt_obex_add_header_body_or_end_body()`

```c
int bt_obex_add_header_body_or_end_body ( struct net_buf * buf, uint16_t mopl, uint16_t len, const uint8_t * body, uint16_t * added_len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：对象主体的一个块（Body Chunk），可能是最后一个块。

此函数帮助上层添加正文／正文结束头（Body/End-of-Body Header）。如果缓冲区尾部空间（Tailroom）大于传入的正文空间，并且添加正文后缓冲区总长度不超过 `mopl`，则添加正文结束头；否则添加正文头。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `mopl` | OBEX 连接的最大 OBEX 数据包长度（Maximum OBEX Packet Length，MOPL）。 |
| `len` | 正文（Body）的长度。 |
| `body` | 对象正文（Object Body）。 |
| `added_len` | 添加的长度（Added Length）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gadc92dff93ef2051ff8b3b277a1bc1f17"></a>

### `bt_obex_add_header_conn_id()`

```c
int bt_obex_add_header_conn_id ( struct net_buf * buf, uint32_t conn_id )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：用于 OBEX 连接复用（Connection Multiplexing）的标识符。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `conn_id` | 连接 ID（Connection Id）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga14c8efe9c8a99e2736552d59972e7b23"></a>

### `bt_obex_add_header_count()`

```c
int bt_obex_add_header_count ( struct net_buf * buf, uint32_t count )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：对象数量（Number of Objects），供 Connect 使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `count` | 对象数量（Number of Objects）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga14c619eef70addc01d13841eda2d8f89"></a>

### `bt_obex_add_header_creator_id()`

```c
int bt_obex_add_header_creator_id ( struct net_buf * buf, uint32_t creator_id )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：指示对象创建者（Object Creator）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `creator_id` | 创建者 ID（Creator Id）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaedc6f39972a5414d085ce17b09ffd121"></a>

### `bt_obex_add_header_description()`

```c
int bt_obex_add_header_description ( struct net_buf * buf, uint16_t len, const uint8_t * dec )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：对象的文本描述（Text Description）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 描述（Description）的长度。 |
| `dec` | 对象描述（Description）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga4463514cf369beb882fec9ab15904821"></a>

### `bt_obex_add_header_dest_name()`

```c
int bt_obex_add_header_dest_name ( struct net_buf * buf, uint16_t len, const uint8_t * dest_name )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：目标对象名称（Destination Object Name），供某些 ACTION 操作使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 目标名称（Destination Name）的长度。 |
| `dest_name` | 目标名称（Destination Name）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga805f13b12c7ce23057cb983d7159c36b"></a>

### `bt_obex_add_header_end_body()`

```c
int bt_obex_add_header_end_body ( struct net_buf * buf, uint16_t len, const uint8_t * body )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：对象主体的最后一个块（Final Body Chunk）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 正文（Body）的长度。 |
| `body` | 对象正文（Object Body）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga6392da7ce8009eb95ab8c8a4d45fcb40"></a>

### `bt_obex_add_header_http()`

```c
int bt_obex_add_header_http ( struct net_buf * buf, uint16_t len, const uint8_t * http )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：一个 HTTP 1.x 报头（Header）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | HTTP 1.x 头（Header）的长度。 |
| `http` | HTTP 1.x 头（Header）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga0d27f09e3b8ea5636f0a34cf8729abaf"></a>

### `bt_obex_add_header_len()`

```c
int bt_obex_add_header_len ( struct net_buf * buf, uint32_t len )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：对象长度（Object Length），单位为字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 对象长度（Length），单位为字节。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga9cd4c8342f67b53a3c3177a51f8887cb"></a>

### `bt_obex_add_header_name()`

```c
int bt_obex_add_header_name ( struct net_buf * buf, uint16_t len, const uint8_t * name )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：对象名称（Object Name），通常为文件名。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 名称（Name）的长度。 |
| `name` | 对象名称（Name）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga7473f42bef1409100886f7812a71a1dc"></a>

### `bt_obex_add_header_obj_class()`

```c
int bt_obex_add_header_obj_class ( struct net_buf * buf, uint16_t len, const uint8_t * obj_class )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：对象的 OBEX 对象类（Object Class）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 对象类（Object Class）的长度。 |
| `obj_class` | 对象类（Object Class）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga4b7c08fd620fdc1ff28a4714c84b6e30"></a>

### `bt_obex_add_header_perm()`

```c
int bt_obex_add_header_perm ( struct net_buf * buf, uint32_t perm )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：用于设置权限（Permissions）的 4 字节位掩码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `perm` | 权限（Permissions）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gac47ddfe8cfe1e595a1821f32415d14eb"></a>

### `bt_obex_add_header_session_param()`

```c
int bt_obex_add_header_session_param ( struct net_buf * buf, uint16_t len, const uint8_t * session_param )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：会话命令／响应（Session Commands/Responses）使用的参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 会话参数（Session Parameter）的长度。 |
| `session_param` | 会话参数（Session Parameter）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gad4a84068ce8c7c37b5189d366b771235"></a>

### `bt_obex_add_header_session_seq_number()`

```c
int bt_obex_add_header_session_seq_number ( struct net_buf * buf, uint32_t session_seq_number )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：每个 OBEX 数据包中用于保证可靠性的序列号（Sequence Number）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `session_seq_number` | 会话序列参数（Session Sequence Parameter）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga23ed862cc6149a71793d02d89fb98cdc"></a>

### `bt_obex_add_header_srm()`

```c
int bt_obex_add_header_srm ( struct net_buf * buf, uint8_t srm )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：用于设置单响应模式（Single Response Mode，SRM）的 1 字节值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `srm` | 单响应模式（Single Response Mode，SRM）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaaa8a9630b0bf5597ca620b864fdafa87"></a>

### `bt_obex_add_header_srm_param()`

```c
int bt_obex_add_header_srm_param ( struct net_buf * buf, uint8_t srm_param )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：单响应模式参数（Single Response Mode Parameter，SRM）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `srm_param` | 单响应模式（SRM）参数。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gac778e8ff0ac7e74795b107750a4a6719"></a>

### `bt_obex_add_header_target()`

```c
int bt_obex_add_header_target ( struct net_buf * buf, uint16_t len, const uint8_t * target )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：操作目标服务的名称（Service Name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 目标名称（Target Name）的长度。 |
| `target` | 目标名称（Target Name）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga249e8b35b98f564d57dc1d644228b8f2"></a>

### `bt_obex_add_header_time()`

```c
int bt_obex_add_header_time ( struct net_buf * buf, uint32_t t )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：日期／时间戳（Date/Time Stamp），4 字节版本，仅用于兼容。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `t` | 日期／时间戳（Date/Time Stamp）。译注：原文 `Data/time` 中的 `Data` 按上下文译为日期。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga877d67e0a4135cabf8b5fddab4d014c6"></a>

### `bt_obex_add_header_time_iso_8601()`

```c
int bt_obex_add_header_time_iso_8601 ( struct net_buf * buf, uint16_t len, const uint8_t * t )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：日期／时间戳（Date/Time Stamp），ISO 8601 版本，为首选形式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 日期／时间戳（Date/Time Stamp）的长度。译注：原文 `data/time` 中的 `data` 按上下文译为日期。 |
| `t` | 日期／时间戳（Date/Time Stamp）。译注：原文 `Data/time` 中的 `Data` 按上下文译为日期。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gadd9f9b4cb50eb51df05c60705223e53b"></a>

### `bt_obex_add_header_type()`

```c
int bt_obex_add_header_type ( struct net_buf * buf, uint16_t len, const uint8_t * type )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：对象类型（Object Type），例如（原文此处未列出示例）。

文本（Text）、HTML、二进制（Binary）或厂商专用类型（Manufacturer Specific）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 类型（Type）的长度。 |
| `type` | 对象类型（Type）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga111cd19449aba6fd0e667551874af0cf"></a>

### `bt_obex_add_header_wan_uuid()`

```c
int bt_obex_add_header_wan_uuid ( struct net_buf * buf, uint16_t len, const uint8_t * uuid )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：唯一标识网络客户端（Network Client），即 OBEX 服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | UUID 的长度。 |
| `uuid` | 通用唯一标识符（UUID）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga56690794dc07dfa598ae2ac68bc90aa0"></a>

### `bt_obex_add_header_who()`

```c
int bt_obex_add_header_who ( struct net_buf * buf, uint16_t len, const uint8_t * who )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

添加报头（Add Header）：标识 OBEX 应用，用于判断是否正在与对等端通信。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | `Who` 头值的长度。 |
| `who` | `Who` 头。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga51baeae9280bb50e34b6608f620498fa"></a>

### `bt_obex_calculate_request_digest()`

```c
int bt_obex_calculate_request_digest ( const uint8_t * pwd, size_t pwd_len, const uint8_t nonce[16], uint8_t digest[16] )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

为 OBEX 认证响应（Authentication Response）计算请求摘要（Request Digest）。

根据密码（Password）和收到的随机数（Nonce）计算认证响应（Authentication Response）的 MD5 摘要。发送该摘要可以证明掌握密码，而无需传输密码本身。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pwd` | 用于认证（Authentication）的密码字节。 |
| `pwd_len` | `pwd` 的长度，单位为字节。 |
| `nonce` | 认证质询（Authentication Challenge）中收到的随机数（Nonce），长度为 `BT_OBEX_CHALLENGE_TAG_NONCE_LEN` 字节。 |
| `digest` | 存放计算所得请求摘要（Request Digest）的输出缓冲区，长度为 `BT_OBEX_RESPONSE_TAG_REQ_DIGEST_LEN` 字节。 |

返回（Returns）：成功时为0，失败时为负错误码。

**警告（Warning）**：警告：OBEX 认证使用 MD5，其密码学强度较弱，只能提供有限的安全性。

<a id="ga21afebccbd592381fb1569feaff98511"></a>

### `bt_obex_connect()`

```c
int bt_obex_connect ( struct bt_obex_client * client, uint16_t mopl, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 连接请求（connect request）。

连接操作（Connect Operation）发起连接，并建立链路双方的基本预期。连接请求必须装入一个数据包。第三个参数 `buf` 保存连接请求的数据包数据，即头序列（Sequence of Headers）。所有头均通过 `bt_obex_add_header_*` 函数打包，例如认证质询头（Authenticate Challenge）通过 `bt_obex_add_header_auth_challenge` 打包。调用此函数之前，应设置客户端的 OBEX 对象；将 `bt_obex_client::ops` 初始化为有效的 `bt_obex_client_ops` 对象地址，并将 `bt_obex_client::obex` 初始化为有效的 IrDA 对象交换协议（IrDA Object Exchange Protocol，OBEX）对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | OBEX 客户端对象（Client Object）。 |
| `mopl` | OBEX 数据包的最大长度。 |
| `buf` | 要发送的头序列（Sequence of Headers）。 |

**说明（Note）**：注意：成功时，缓冲区所有权（Buffer Ownership）转交给协议栈；发生错误时，调用者保留缓冲区所有权。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gad91f69ba1b6780501722221bc516db4b"></a>

### `bt_obex_connect_rsp()`

```c
int bt_obex_connect_rsp ( struct bt_obex_server * server, uint8_t rsp_code, uint16_t mopl, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 连接响应（connect response）。

连接响应（Connect Response）用于确认连接请求数据包，必须装入一个数据包。

第二个参数 `rsp_code` 用于传递 `bt_obex_rsp_code` 响应码，典型成功值为 `BT_OBEX_RSP_CODE_SUCCESS`。参数 `buf` 保存连接响应的数据包数据，即头序列（Sequence of Headers）。所有头均通过 `bt_obex_add_header_*` 函数打包，例如认证响应头（Authenticate Response）通过 `bt_obex_add_header_auth_rsp` 打包。译注：原文将 `buf` 先称为第四个参数，又称为第三个参数，存在不一致；具体位置以本项函数声明为准。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | OBEX 服务器对象（Server Object）。 |
| `rsp_code` | 响应码（Response Code）。 |
| `mopl` | OBEX 数据包的最大长度。 |
| `buf` | 要发送的头序列（Sequence of Headers）。 |

**说明（Note）**：注意：成功时，缓冲区所有权（Buffer Ownership）转交给协议栈；发生错误时，调用者保留缓冲区所有权。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga107787f08e55bf2740cc14cb5614bdbf"></a>

### `bt_obex_disconnect()`

```c
int bt_obex_disconnect ( struct bt_obex_client * client, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 断开连接请求（disconnect request）。

断开连接操作（Disconnect Operation）由客户端发出 OBEX 连接结束的信号。断开连接请求必须装入一个数据包。

第二个参数 `buf` 保存断开连接请求（Disconnect Request）的数据包数据，即头序列（Sequence of Headers）。所有头均通过 `bt_obex_add_header_*` 函数打包，例如连接 ID 头（Connection Id）通过 `bt_obex_add_header_conn_id` 打包。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | OBEX 客户端对象（Client Object）。 |
| `buf` | 要发送的头序列（Sequence of Headers）。 |

**说明（Note）**：注意：成功时，缓冲区所有权（Buffer Ownership）转交给协议栈；发生错误时，调用者保留缓冲区所有权。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gac7763a310a553b3ba3c6b8b06951f191"></a>

### `bt_obex_disconnect_rsp()`

```c
int bt_obex_disconnect_rsp ( struct bt_obex_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 断开连接响应（disconnect response）。

断开连接响应（Disconnect Response）用于确认断开连接请求数据包，必须装入一个数据包。

第二个参数 `rsp_code` 用于传递 `bt_obex_rsp_code` 响应码。典型值为：成功时使用 `BT_OBEX_RSP_CODE_SUCCESS`；连接 ID 头（Connection Id）无效、服务不可用时使用 `BT_OBEX_RSP_CODE_UNAVAIL`。第三个参数 `buf` 保存响应的数据包数据，即头序列（Sequence of Headers）。所有头均通过 `bt_obex_add_header_*` 函数打包。译注：原文在断开连接响应说明中将该缓冲区写为“连接响应（Connect Response）”，此处按所在操作理解为断开连接响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | OBEX 服务器对象（Server Object）。 |
| `rsp_code` | 响应码（Response Code）。 |
| `buf` | 要发送的头序列（Sequence of Headers）。 |

**说明（Note）**：注意：成功时，缓冲区所有权（Buffer Ownership）转交给协议栈；发生错误时，调用者保留缓冲区所有权。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga3708c17f9c23fdeb5ceda376787cebbd"></a>

### `bt_obex_generate_nonce()`

```c
int bt_obex_generate_nonce ( const uint8_t * pwd, size_t pwd_len, uint8_t nonce[16] )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

为 OBEX 认证质询（Authentication Challenge）生成一次性随机数（Nonce）。

生成用于 OBEX 认证质询（Authentication Challenge）的随机数（Nonce）。随机数用于在认证期间防止重放攻击（Replay Attacks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pwd` | 用于生成随机数（Nonce）的密码字节。 |
| `pwd_len` | `pwd` 的长度，单位为字节。 |
| `nonce` | 存放生成的随机数（Nonce）的输出缓冲区，长度为 `BT_OBEX_CHALLENGE_TAG_NONCE_LEN` 字节。 |

返回（Returns）：成功时为0，失败时为负错误码。

**警告（Warning）**：警告：OBEX 认证使用 MD5，其密码学强度较弱，只能提供有限的安全性。

<a id="gabd3ff76e8a39e5944daa944f38a63c5f"></a>

### `bt_obex_get()`

```c
int bt_obex_get ( struct bt_obex_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 获取请求（get request）。

获取操作（Get Operation）请求服务器向客户端返回一个对象。它由一个或多个请求数据包组成；最后一个请求包应设置第二个参数 `final`，表示 Get 的请求阶段完成。一旦发送了设置最终位（Final Bit）的 Get 请求，直到操作完成前，所有后续 Get 请求包都必须设置该位。第三个参数 `buf` 保存 Get 请求的数据包数据，即头序列（Sequence of Headers）。所有头均通过 `bt_obex_add_header_*` 函数打包，例如名称头（Name）通过 `bt_obex_add_header_name` 打包。如果没有需要发送的数据，`buf` 可以为 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | OBEX 客户端对象（Client Object）。 |
| `final` | 操作码（Opcode）的最终位（Final Bit）。 |
| `buf` | 要发送的头序列（Sequence of Headers）。 |

**说明（Note）**：注意：成功时，缓冲区所有权（Buffer Ownership）转交给协议栈；发生错误时，调用者保留缓冲区所有权。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gacc1673746737e4163165b5f379c8105f"></a>

### `bt_obex_get_header_action_id()`

```c
int bt_obex_get_header_action_id ( struct net_buf * buf, uint8_t * action_id )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：指定要执行的动作（Action），供 ACTION 操作使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `action_id` | 动作 ID（Action Id），参见 `bt_obex_action_id`。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga96981ef9187406efbd374fd623a14eaa"></a>

### `bt_obex_get_header_app_param()`

```c
int bt_obex_get_header_app_param ( struct net_buf * buf, uint16_t * len, const uint8_t ** app_param )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：扩展应用请求与响应信息（Extended Application Request & Response Information）。

可调用 `bt_obex_tlv_parse` 解析该参数（Parameter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | `app_param` 的长度。 |
| `app_param` | 应用参数（Application Parameter）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga6ee576eecea3947f1832d4859f16e1db"></a>

### `bt_obex_get_header_auth_challenge()`

```c
int bt_obex_get_header_auth_challenge ( struct net_buf * buf, uint16_t * len, const uint8_t ** auth )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：认证摘要质询（Authentication Digest-challenge）。

可调用 `bt_obex_tlv_parse` 解析这些选项（Options）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | `auth_challenge` 的长度。 |
| `auth` | 认证质询（Authentication Challenge）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gad9bae471db418e0a50c1b234e37b5d9d"></a>

### `bt_obex_get_header_auth_rsp()`

```c
int bt_obex_get_header_auth_rsp ( struct net_buf * buf, uint16_t * len, const uint8_t ** auth )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：认证摘要响应（Authentication Digest-response）。

可调用 `bt_obex_tlv_parse` 解析这些选项（Options）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 认证响应（Authentication Response）的长度。 |
| `auth` | 认证响应（Authentication Response）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaba71a8b3b8adc251a5a87fa60848bb3c"></a>

### `bt_obex_get_header_body()`

```c
int bt_obex_get_header_body ( struct net_buf * buf, uint16_t * len, const uint8_t ** body )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：对象主体的一个块（Body Chunk）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 正文（Body）的长度。 |
| `body` | 对象正文（Object Body）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga225ac4953da5e56a07865c8ab6ee0591"></a>

### `bt_obex_get_header_conn_id()`

```c
int bt_obex_get_header_conn_id ( struct net_buf * buf, uint32_t * conn_id )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：用于 OBEX 连接复用（Connection Multiplexing）的标识符。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `conn_id` | 连接 ID（Connection Id）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga1e9b6dd9a8816ce87235b6b3d723541c"></a>

### `bt_obex_get_header_count()`

```c
int bt_obex_get_header_count ( struct net_buf * buf, uint32_t * count )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：对象数量（Number of Objects），供 Connect 使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `count` | 对象数量（Number of Objects）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga9e08bf74bfbf001a80f40ee2d1b1ef82"></a>

### `bt_obex_get_header_creator_id()`

```c
int bt_obex_get_header_creator_id ( struct net_buf * buf, uint32_t * creator_id )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：指示对象创建者（Object Creator）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `creator_id` | 创建者 ID（Creator Id）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga3d805f241fc507587445b3204070055e"></a>

### `bt_obex_get_header_description()`

```c
int bt_obex_get_header_description ( struct net_buf * buf, uint16_t * len, const uint8_t ** dec )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：对象的文本描述（Text Description）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 描述（Description）的长度。 |
| `dec` | 对象描述（Description）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga945c0865edef9f34e2cf1e817a3b45c1"></a>

### `bt_obex_get_header_dest_name()`

```c
int bt_obex_get_header_dest_name ( struct net_buf * buf, uint16_t * len, const uint8_t ** dest_name )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：目标对象名称（Destination Object Name），供某些 ACTION 操作使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 目标名称（Destination Name）的长度。 |
| `dest_name` | 目标名称（Destination Name）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaf8ff29ef3413492d2ec67fba278c2f82"></a>

### `bt_obex_get_header_end_body()`

```c
int bt_obex_get_header_end_body ( struct net_buf * buf, uint16_t * len, const uint8_t ** body )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：对象主体的最后一个块（Final Body Chunk）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 正文（Body）的长度。 |
| `body` | 对象正文（Object Body）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga5a181f7779df1ed2919ba3a94a630df4"></a>

### `bt_obex_get_header_http()`

```c
int bt_obex_get_header_http ( struct net_buf * buf, uint16_t * len, const uint8_t ** http )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：一个 HTTP 1.x 报头（Header）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | HTTP 1.x 头（Header）的长度。 |
| `http` | HTTP 1.x 头（Header）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga18ce5303b138959481666c0b8101f59e"></a>

### `bt_obex_get_header_len()`

```c
int bt_obex_get_header_len ( struct net_buf * buf, uint32_t * len )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：对象长度（Object Length），单位为字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 对象长度（Length），单位为字节。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gabef4622fa48b493f6d6ad5d1ecb65726"></a>

### `bt_obex_get_header_name()`

```c
int bt_obex_get_header_name ( struct net_buf * buf, uint16_t * len, const uint8_t ** name )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：对象名称（Object Name），通常为文件名。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 名称（Name）的长度。 |
| `name` | 对象名称（Name）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga49d1988eae4165f1cec624812cfe5f36"></a>

### `bt_obex_get_header_obj_class()`

```c
int bt_obex_get_header_obj_class ( struct net_buf * buf, uint16_t * len, const uint8_t ** obj_class )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：对象的 OBEX 对象类（Object Class，原文写作 oBEX）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 对象类（Object Class）的长度。 |
| `obj_class` | 对象类（Object Class）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gab234af4e944a3e97e3459613078005a1"></a>

### `bt_obex_get_header_perm()`

```c
int bt_obex_get_header_perm ( struct net_buf * buf, uint32_t * perm )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：用于设置权限（Permissions）的 4 字节位掩码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `perm` | 权限（Permissions）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga560c8f0cb92b769a0716b2bc163c38e1"></a>

### `bt_obex_get_header_session_param()`

```c
int bt_obex_get_header_session_param ( struct net_buf * buf, uint16_t * len, const uint8_t ** session_param )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：会话命令／响应（Session Commands/Responses）使用的参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 会话参数（Session Parameter）的长度。 |
| `session_param` | 会话参数（Session Parameter）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaaa33502f3ae9f97767bd0e5e660f021f"></a>

### `bt_obex_get_header_session_seq_number()`

```c
int bt_obex_get_header_session_seq_number ( struct net_buf * buf, uint32_t * session_seq_number )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：每个 OBEX 数据包中用于保证可靠性的序列号（Sequence Number）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `session_seq_number` | 会话序列参数（Session Sequence Parameter）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gae0865eea3d8db09023cfc77b2118bad5"></a>

### `bt_obex_get_header_srm()`

```c
int bt_obex_get_header_srm ( struct net_buf * buf, uint8_t * srm )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：用于设置单响应模式（Single Response Mode，SRM）的 1 字节值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `srm` | 单响应模式（Single Response Mode，SRM）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga7501193240498e7a9da0034b2e434ffc"></a>

### `bt_obex_get_header_srm_param()`

```c
int bt_obex_get_header_srm_param ( struct net_buf * buf, uint8_t * srm_param )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：单响应模式参数（Single Response Mode Parameter，SRM）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `srm_param` | 单响应模式（SRM）参数。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga49265f0aec21d8c33f56eb44723dabba"></a>

### `bt_obex_get_header_target()`

```c
int bt_obex_get_header_target ( struct net_buf * buf, uint16_t * len, const uint8_t ** target )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：操作目标服务的名称（Service Name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 目标名称（Target Name）的长度。 |
| `target` | 目标名称（Target Name）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga367337d0f002a046248e92f3578efbb6"></a>

### `bt_obex_get_header_time()`

```c
int bt_obex_get_header_time ( struct net_buf * buf, uint32_t * t )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：日期／时间戳（Date/Time Stamp），4 字节版本，仅用于兼容。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `t` | 日期／时间戳（Date/Time Stamp）。译注：原文 `Data/time` 中的 `Data` 按上下文译为日期。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gacee063f6b53b85bad52a519cd1c794c5"></a>

### `bt_obex_get_header_time_iso_8601()`

```c
int bt_obex_get_header_time_iso_8601 ( struct net_buf * buf, uint16_t * len, const uint8_t ** t )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：日期／时间戳（Date/Time Stamp），ISO 8601 版本，为首选形式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 日期／时间戳（Date/Time Stamp）的长度。译注：原文 `data/time` 中的 `data` 按上下文译为日期。 |
| `t` | 日期／时间戳（Date/Time Stamp）。译注：原文 `Data/time` 中的 `Data` 按上下文译为日期。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gabcfa9b33c0f91fbcf787d58e1f1bba41"></a>

### `bt_obex_get_header_type()`

```c
int bt_obex_get_header_type ( struct net_buf * buf, uint16_t * len, const uint8_t ** type )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：对象类型（Object Type），例如（原文此处未列出示例）。

文本（Text）、HTML、二进制（Binary）或厂商专用类型（Manufacturer Specific）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | 类型（Type）的长度。 |
| `type` | 对象类型（Type）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaf9ffc19ef06a2773d664c0b15b2b8857"></a>

### `bt_obex_get_header_wan_uuid()`

```c
int bt_obex_get_header_wan_uuid ( struct net_buf * buf, uint16_t * len, const uint8_t ** uuid )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：唯一标识网络客户端（Network Client），即 OBEX 服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | UUID 的长度。 |
| `uuid` | 通用唯一标识符（UUID）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gab551b01deed2c5a31f9a7a4b99045c9c"></a>

### `bt_obex_get_header_who()`

```c
int bt_obex_get_header_who ( struct net_buf * buf, uint16_t * len, const uint8_t ** who )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

获取报头值（Get Header Value）：标识 OBEX 应用，用于判断是否正在与对等端通信。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `len` | `Who` 头值的长度。 |
| `who` | `Who` 头。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga3e9415fa4595d17676ada6622c9fd475"></a>

### `bt_obex_get_rsp()`

```c
int bt_obex_get_rsp ( struct bt_obex_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 获取响应（get response）。

获取响应（Get Response）用于确认 Get 请求数据包，由服务器发送给客户端。如果服务器中有多个对象符合请求，具体行为取决于系统。不过，在请求阶段完成前，服务器设备不得开始发送对象正文分块（Object Body Chunks）。

第二个参数 `rsp_code` 用于传递 `bt_obex_rsp_code` 响应码。典型值为：`BT_OBEX_RSP_CODE_CONTINUE` 表示继续，`BT_OBEX_RSP_CODE_SUCCESS` 表示成功。如果整个对象能装入一个响应包，成功响应使用 `BT_OBEX_RSP_CODE_SUCCESS`，即成功且设置最终位（Final Bit），后接对象正文。如果响应较大，需要多个 GET 响应，则只有最后一个响应使用 `BT_OBEX_RSP_CODE_SUCCESS`，其他响应均使用 `BT_OBEX_RSP_CODE_CONTINUE`。对象以头序列（Sequence of Headers）的形式返回，与 Put 操作相同。其他任何 `bt_obex_rsp_code` 响应码均表示失败；典型失败码包括 `BT_OBEX_RSP_CODE_BAD_REQ`，表示错误请求、服务器无法理解请求，以及 `BT_OBEX_RSP_CODE_FORBIDDEN`，表示理解操作但拒绝执行。第三个参数 `buf` 保存 Get 响应的数据包数据，即头序列。所有头均通过 `bt_obex_add_header_*` 函数打包，例如 SRM 头通过 `bt_obex_add_header_srm` 打包。如果没有需要发送的数据，`buf` 可以为 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | OBEX 服务器对象（Server Object）。 |
| `rsp_code` | 响应码（Response Code）。 |
| `buf` | 要发送的头序列（Sequence of Headers）。 |

**说明（Note）**：注意：成功时，缓冲区所有权（Buffer Ownership）转交给协议栈；发生错误时，调用者保留缓冲区所有权。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga5ae88dad0e7c97d0f20c7e4ceeeb3ce8"></a>

### `bt_obex_has_app_param()`

```c
bool bt_obex_has_app_param ( struct net_buf * buf, uint8_t id )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

检查 buf 是否包含指定应用参数（Application Parameter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `id` | 应用参数（Application Parameter）的标签 ID（Tag ID）。 |

**返回（Returns）**：返回值：找到标签（Tag）时为 `true`，否则为 `false`。

<a id="ga296af3d5a15684e4aa3846cc24203fef"></a>

### `bt_obex_has_header()`

```c
bool bt_obex_has_header ( struct net_buf * buf, uint8_t id )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

检查 buf 是否包含指定报头（Header）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 需要发送的缓冲区（Buffer）。 |
| `id` | 头的 ID（Header ID）。 |

**返回（Returns）**：返回值：找到头（Header）时为 `true`，否则为 `false`。

<a id="ga5c93e9786adfb45a60a911087f859757"></a>

### `bt_obex_header_parse()`

```c
int bt_obex_header_parse ( struct net_buf * buf, bool(* func )(struct bt_obex_hdr *hdr, void *user_data), void * user_data )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

解析 OBEX 报头（Header）的辅助函数。

用于解析 OBEX 数据包头结构（Header Structure）的辅助函数。最常见的用法是在 OBEX 服务器和客户端的回调中调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 传递给 OBEX 服务器和客户端回调的 OBEX 数据包（Packet）。 |
| `func` | 每找到一个数据元素（Element）便调用一次的回调函数。回调应返回 `true` 继续解析，或返回 `false` 停止解析。 |
| `user_data` | 要传递给回调（Callback）的用户数据（User Data）。 |

**警告（Warning）**：警告：此辅助函数会在解析时消耗 `buf` 中的数据。如果之后还需要使用原始数据，用户应先制作副本（Copy）。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gafadd6e44ae19786617b5e60608fa4651"></a>

### `bt_obex_make_uuid()`

```c
int bt_obex_make_uuid ( union bt_obex_uuid * uuid, const uint8_t * data, uint16_t len )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

使用指定数据和长度构造通用唯一标识符（UUID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `uuid` | OBEX 的 UUID。 |
| `data` | UUID 数据。 |
| `len` | UUID 数据长度。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga1d8684307899b1bd3724cb3aa996c53e"></a>

### `bt_obex_put()`

```c
int bt_obex_put ( struct bt_obex_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 放入请求（put request）。

放置操作（Put Operation）将一个对象从客户端发送到服务器。它由一个或多个请求数据包组成；最后一个请求包应设置第二个参数 `final`。第三个参数 `buf` 保存 Put 请求的数据包数据，即头序列（Sequence of Headers）。所有头均通过 `bt_obex_add_header_*` 函数打包，例如名称头（Name）通过 `bt_obex_add_header_name` 打包。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | OBEX 客户端对象（Client Object）。 |
| `final` | 操作码（Opcode）的最终位（Final Bit）。 |
| `buf` | 要发送的头序列（Sequence of Headers）。 |

**说明（Note）**：注意：完全不带正文头（Body Header）或正文结束头（End-of-Body Header）的 Put 操作应视为删除请求。类似地，带有空正文结束头的 Put 操作请求接收方创建空对象。此定义未必适用于所有实现；换言之，设备并不一定要支持删除操作或空对象。成功时，缓冲区所有权（Buffer Ownership）移交给协议栈；出错时，调用者保留缓冲区所有权。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gab5dfc5988d17ef0b79b84fd4c96dc60a"></a>

### `bt_obex_put_rsp()`

```c
int bt_obex_put_rsp ( struct bt_obex_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 放入响应（put response）。

放置响应（Put Response）用于确认每个 Put 请求数据包，由服务器发送给客户端。第二个参数 `rsp_code` 用于传递 `bt_obex_rsp_code` 响应码；典型值 `BT_OBEX_RSP_CODE_CONTINUE` 表示继续，`BT_OBEX_RSP_CODE_SUCCESS` 表示成功。第三个参数 `buf` 保存 Put 响应的数据包数据，即头序列（Sequence of Headers）。所有头均通过 `bt_obex_add_header_*` 函数打包，例如 SRM 头通过 `bt_obex_add_header_srm` 打包。如果没有需要发送的数据，`buf` 可以为 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | OBEX 服务器对象（Server Object）。 |
| `rsp_code` | 响应码（Response Code）。 |
| `buf` | 要发送的头序列（Sequence of Headers）。 |

**说明（Note）**：注意：成功时，缓冲区所有权（Buffer Ownership）转交给协议栈；发生错误时，调用者保留缓冲区所有权。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga7cb42acb39c601375ef7c73f6be7e6af"></a>

### `bt_obex_rsp_code_to_str()`

```c
const char * bt_obex_rsp_code_to_str ( enum bt_obex_rsp_code rsp_code)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/obex.h>
```

将 OBEX 响应码（Response Code）转换为字符串。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rsp_code` | 响应码（Response Code）。 |

**返回（Returns）**：返回值：响应码（Response Code）的字符串表示。如果未启用 `CONFIG_BT_OEBX_RSP_CODE_TO_STR`，则仅返回空字符串。译注：配置符号按官方本句原样保留，其中 `OEBX` 的拼写应与实际源码核对。

<a id="ga1df3928a40f544ffb98b5eb1ceac62dd"></a>

### `bt_obex_server_register()`

```c
int bt_obex_server_register ( struct bt_obex_server * server, const struct bt_uuid_128 * uuid )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

注册 OBEX 服务器（Server）。

使用指定 UUID 注册 OBEX 服务器（Server）。

调用此函数之前，应设置服务器的 OBEX 对象。如果 UUID 为 `NULL`，则接受任何连接请求；否则必须保留 UUID 的存储空间。调用此 API 之前，应将 `bt_obex_server::ops` 初始化为有效的 `bt_obex_server_ops` 对象地址，并将 `bt_obex_server::obex` 初始化为有效的 IrDA 对象交换协议（IrDA Object Exchange Protocol，OBEX）对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | OBEX 服务器对象。 |
| `uuid` | 服务（Service）的 UUID。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga642bfabb90d6576f92c5b546a592ec17"></a>

### `bt_obex_server_unregister()`

```c
int bt_obex_server_unregister ( struct bt_obex_server * server)
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

注销 OBEX 服务器（Server）。

注销已注册的 OBEX 服务器（Server）。

调用此函数时，服务器应处于已断开连接（Disconnected）状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | OBEX 服务器对象。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga6d61b4421ad1e56cc2ae611ec77e561e"></a>

### `bt_obex_setpath()`

```c
int bt_obex_setpath ( struct bt_obex_client * client, uint8_t flags, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 设置路径请求（setpath request）。

设置路径请求（Setpath Request）用于设置接收方的“当前文件夹（Current Folder）”，以支持需要附加路径信息的传输。路径名称包含在名称头（Name Header）中。Setpath 请求始终装入一个 OBEX 数据包，并设置最终位（Final Bit）。

第二个参数 `flags` 是 Setpath 操作标志位图（Flags Bitmap）。位 0 表示在应用名称之前返回上一级，等同于许多系统中的 `../`；位 1 表示文件夹不存在时不创建它，而是返回错误。其他位必须由发送方置零，并由接收方忽略。第三个参数 `buf` 保存 Setpath 请求的数据包数据，即头序列（Sequence of Headers）。所有头均通过 `bt_obex_add_header_*` 函数打包，例如名称头（Name）通过 `bt_obex_add_header_name` 打包。如果添加名称头，表示客户端希望从当前文件夹向下进入该名称指定的下一级文件夹；或者在 `flags` 未设置任何位时，客户端希望返回默认文件夹。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | OBEX 客户端对象（Client Object）。 |
| `flags` | Setpath 请求标志（Flags），参见 `bt_obex_setpath_flags`。 |
| `buf` | 要发送的头序列（Sequence of Headers）。 |

**说明（Note）**：注意：当标志（Flags）或常量（Constants）足以表达整个请求操作时，可以省略名称头（Name Header）。例如，返回上一级时设置 `flags` 的位 0，等同于某些系统中的 `cd ..`。成功时，缓冲区所有权（Buffer Ownership）移交给协议栈；出错时，调用者保留缓冲区所有权。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga13836db790849b5ec6b52bcb97c84505"></a>

### `bt_obex_setpath_rsp()`

```c
int bt_obex_setpath_rsp ( struct bt_obex_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

OBEX 设置路径响应（setpath response）。

设置路径响应（Setpath Response）用于确认 Setpath 请求数据包，由服务器发送给客户端。它始终装入一个 OBEX 数据包，并设置最终位（Final Bit）。

第二个参数 `rsp_code` 用于传递 `bt_obex_rsp_code` 响应码，典型成功值为 `BT_OBEX_RSP_CODE_SUCCESS`。其他任何 `bt_obex_rsp_code` 响应码均表示失败；典型失败码包括 `BT_OBEX_RSP_CODE_BAD_REQ`，表示错误请求、服务器无法理解请求，以及 `BT_OBEX_RSP_CODE_FORBIDDEN`，表示理解操作但拒绝执行。第三个参数 `buf` 保存 Setpath 响应的数据包数据，即头序列（Sequence of Headers）。所有头均通过 `bt_obex_add_header_*` 函数打包。如果没有需要发送的数据，`buf` 可以为 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | OBEX 服务器对象（Server Object）。 |
| `rsp_code` | 响应码（Response Code）。 |
| `buf` | 要发送的头序列（Sequence of Headers）。 |

**说明（Note）**：注意：成功时，缓冲区所有权（Buffer Ownership）转交给协议栈；发生错误时，调用者保留缓冲区所有权。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga170456d806c0ff494b0c1d7fad763051"></a>

### `bt_obex_string_is_valid()`

```c
bool bt_obex_string_is_valid ( uint8_t id, uint16_t len, const uint8_t * str )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

检查字符串（String）是否有效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 头 ID（Header ID）。 |
| `len` | 字符串（String）的长度。 |
| `str` | 字符串（String）的地址。 |

**返回（Returns）**：返回值：字符串有效时为 `true`，否则为 `false`。

<a id="gaccecf00dc6209d1701ac0a6985f38257"></a>

### `bt_obex_tlv_parse()`

```c
int bt_obex_tlv_parse ( uint16_t len, const uint8_t * data, bool(* func )(struct bt_obex_tlv *tlv, void *user_data), void * user_data )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

解析 OBEX 类型－长度－值三元组（TLV Triplet）的辅助函数。

用于解析 OBEX 数据包中标签—长度—值（Tag-Length-Value，TLV）三元组结构的辅助函数。最常见的用法是在 OBEX 服务器和客户端的回调中调用它。数据采用 TLV 编码方案，通常是应用请求—响应参数（Application Request-Response Parameters）、认证质询（Authenticate Challenge）和认证响应（Authenticate Response）这些头的头值；也就是 `bt_obex_get_header_app_param`、`bt_obex_get_header_auth_challenge` 或 `bt_obex_get_header_auth_rsp` 的输出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `len` | 数据（Data）的长度。 |
| `data` | 传递给 OBEX 服务器和客户端回调的数据（Data）。 |
| `func` | 每从数据中找到一个 TLV 三元组（Triplet）便调用一次的回调函数。回调应返回 `true` 继续解析，或返回 `false` 停止解析。 |
| `user_data` | 要传递给回调（Callback）的用户数据（User Data）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gae31398502c9d237d7afd47d70315be3f"></a>

### `bt_obex_verify_auth_response()`

```c
int bt_obex_verify_auth_response ( const uint8_t * pwd, size_t pwd_len, const uint8_t nonce[16], const uint8_t digest[16] )
```

```c
#include <zephyr/bluetooth/classic/obex.h>
```

验证 OBEX 认证响应（Authentication Response）。

验证收到的请求摘要（Request Digest）是否与根据密码和随机数（Nonce）计算出的预期值匹配。认证方使用此函数验证对端的认证响应（Authentication Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pwd` | 用于认证（Authentication）的密码字节。 |
| `pwd_len` | `pwd` 的长度，单位为字节。 |
| `nonce` | 认证质询（Authentication Challenge）中发送的随机数（Nonce），长度为 `BT_OBEX_CHALLENGE_TAG_NONCE_LEN` 字节。 |
| `digest` | 从对端收到的请求摘要（Request Digest），长度为 `BT_OBEX_RESPONSE_TAG_REQ_DIGEST_LEN` 字节。 |

**返回（Returns）**：返回值：认证成功时为 0，失败时为负错误码（Negative Error Code）。

**警告（Warning）**：警告：OBEX 认证使用 MD5，其密码学强度较弱，只能提供有限的安全性。


## 5.6\_原页交叉引用（Cross References）

- [bt_obex_server_ops](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md)
- [bt_obex_client_ops](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md)
- [bt_obex_transport_ops](../bluetooth_service_model_reference/P134_bt_obex_transport_ops_结构体.md)
- [bt_obex_uuid](../bluetooth_service_model_reference/P189_bt_obex_uuid_联合体.md)
- [bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)
- [bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)
- [bt_obex](../bluetooth_service_model_reference/P127_bt_obex_结构体.md)
- [bt_obex_tlv](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md)
- [bt_obex_hdr](../bluetooth_service_model_reference/P130_bt_obex_hdr_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/bluetooth/classic/obex.h](../api_file_bluetooth_media_reference/P011_zephyr__bluetooth__classic__obex.h_文件参考.md)
- [MIN](../util_reference/P001_通用工具公共接口.md#ga3acffbd305ee72dcd4593c0d8af64a4f)
- [net_buf_tailroom](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaecbc6adf16469e3366c88445ea7a553a)
- [bt_obex_server_ops::connect](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md#a0449e9ab3018796818460f95dd2df13e)
- [bt_obex_client_ops::connect](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md#ac47ffc1353bef9d4d3725e05b75461f2)
- [bt_obex_client_ops::disconnect](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md#a1e7227232515d875123e6f8ed2bfd993)
- [bt_obex_client::ops](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md#a4b9a3f84253936e7babbfc0077da994a)
- [bt_obex_client::obex](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md#a271142fde25a5622e25404e3a1f469ad)
- [IrDA 对象交换协议（Object Exchange Protocol，OBEX）](P005_IrDA 对象交换协议（Object Exchange Protocol，OBEX）.md)
- [CONFIG_BT_OEBX_RSP_CODE_TO_STR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OEBX_RSP_CODE_TO_STR)
- [bt_obex_server::ops](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md#aefe5b0dbed43308a4881643b5705f033)
- [bt_obex_server::obex](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md#ac96bcf45b1753cacb8a797c5f7c29eed)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__obex_html_ga5571666538c43d8d71dd17dc58d19f45"></a>
<a id="agroup__bt__obex_html_ga500dcfab79831c5d640406cff8c54f01"></a>
<a id="agroup__bt__obex_html_ga805f13b12c7ce23057cb983d7159c36b"></a>
<a id="agroup__bt__obex_html_gab3db35da4b3daf626e89223262273fb9"></a>
<a id="agroup__bt__obex_html_gad1b3c22eea0915b962d7ab1e27726fe2"></a>
<a id="agroup__net__buf_html_gaecbc6adf16469e3366c88445ea7a553a"></a>
<a id="agroup__sys-util_html_ga3acffbd305ee72dcd4593c0d8af64a4f"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="agroup__bt__obex_html_ga534e9ffa9f7ba93eda049fd9022df69a"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga12730d705667c2717c05a75cdfc07281abb151a8123c7e6826a052ab252455aee"></a>
<a id="gga12730d705667c2717c05a75cdfc07281a7c57548121adf0afe43066070ef4b1fa"></a>
<a id="gga12730d705667c2717c05a75cdfc07281a711263abb984488b8c7273052fb76ae0"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948a6119d9faab405c63a25791edc9588889"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948adf199ff987c26bd8d6301c409fb5f6a4"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948a8bfeff22eabea432eb5863a974adb745"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948ae075bf9dd7e57c66613ffb3de84f09bb"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948ac2899a8dca76bfd88bb94d43a3c8a693"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948a4fad7112257bd771e412eefd0c1e8bcc"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948a0fb867c69fb0c8680170359a41f2a3b1"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948a5929acc483779593b1b5c7b702b17976"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948a46735e651f7f378a3efb1be1a232e4ca"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948a3264aa53da0fd7ec6611b8a20a8745f4"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948aaa78dab2eda48ebd5d594024b53bec6b"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948ab28b3ee885c373ca83a745fcd019e2e4"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948a3417001aed5d114492dcbe2c29496a1b"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948a6dac6844a5db11dbc0e43613a32c13a9"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948aa48d582e278e748574d57818a7f5daf1"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948a97c1dfb166ac549576d30cadd156365f"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948a31bec44f1240f21545f917eedd31026e"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948a65e148b396f75cd55b992df84d5176ff"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948a5b723fde52df0965299d2f79e433c0a2"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948afe34bec1dba1d1fca717f3ffa7c20628"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948a3d42ab8b6a28f9062a97e2b1a9fa7c16"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948a01e2d13304514242e954d45e74e3fcba"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948ae5149b2da2cfb3c2e832f51282bc08d6"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948a6aad7cbbcbebe670d370919fbdc61c19"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948aa722c75042f0db4fba5c6a90516494b1"></a>
<a id="gga3c893652eb9a5f0bf699d357caf40948adda0f643d1c2ebd20d4c9d5644ef6b2c"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a7e38ca653283f53b62fa4b21f48d998a"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a881d3098a198dc1eced2150a213d1054"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9af449d3c85fbec550c76e29287a626789"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a955b065ee2543e0bc31a03d9bd15900b"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9aba13d60d30201bdb13f01c1ee2ff7916"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a2f88a5bf5bb9690d8db856bf02f305d8"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a32d55bb3c73ecb8cdf5f76c6724c9884"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a4e8f5c004cf3ef6e9ad1b5be1d106a39"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9afcf5fc7c81eed4d5b67def413535a46f"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a3b948c9bdf3bebd2b0e7cf34960c19b2"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9aa5252b1eaa5fa7d41052d97af24fd4d7"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9abf41a7e722e12bd71a93093e36bfc2bf"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9ac25903e3a229ac50ecea485eca8c5236"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9ab33e506b470df404119976d5460b6bda"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9ac19ffb8b59a7cb1a3e0c1edfe91dd472"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a2d2ff2c6ec42d9e80dc4e841e19d31ee"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9acfbc9161dddf6859dd8e8ac70cf8d446"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a5fc2aa165ffea0caeb59e05ee951e3dc"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a4b7a12b0e11747d1a470e8f559b55ea8"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a2b91abe9e010465f9514f37477b993e0"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a3f510d3b203257a37d2ef005d4517a67"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a48f773daa7f2dabaadc37142ec32ffd1"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9aeb2abeaf682a47a46291784c2b24b793"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a3f60fb4d3444570c9a73f43b7c9bdc1f"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9aeca60f95428624932314fc8f3b4a1b79"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9aa34ece6da3fe28ec3747ce8621da7e31"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9ac0faf667c93a32293fbacca2e1696938"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9aacc05fd2528e29fbd53eb5ff940f9079"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a21783b5d9036d61304a7acb3b03d0913"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9adc906b909c09a8a1cc421e8f4efc1444"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a650312673ccc758b735bcead8f1009ef"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9add3501ba98c972e0e01a6fa898612bd4"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9aba8108ac6b050d3dad845a5e8cb42eaf"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9ac39d7d6fa1fcb0cc5be0ad25aa2574f9"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a613e95b96eaba0522070b620b4b90953"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a850bbc0fd1810e3a74f2a057e8358b48"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9ab41b31b5e85dcb2981b3f6e9bbba2dd9"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9ad65c4246d828770010748b1faa6af71c"></a>
<a id="gga81b84c24a976c6c13d33eb23b0b10ae9a5c0692d0e3db45a898426b2751e682a0"></a>
<a id="ggab5f7e6a6c7503f97a851f48c70162483a9f89d8219783650a02e8ceb3faf6bd75"></a>
<a id="ggab5f7e6a6c7503f97a851f48c70162483ae47e6f7c5a8da44615e7245c5e1cd553"></a>
<a id="gga622610a779a2e050e9a05c7eae945b3ead7138e7373f5562faf13faa8bca424e6"></a>
<a id="gga622610a779a2e050e9a05c7eae945b3ea8743efcfd509ba7b156ac91a3c928614"></a>
<a id="gga622610a779a2e050e9a05c7eae945b3ea15ddd595c7832a8bfd382f87b938723b"></a>
<a id="gga622610a779a2e050e9a05c7eae945b3eae41568fe4c0d0db81ff60f41be6443a5"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_消息访问配置文件（Message Access Profile，MAP）.md) · [返回大纲](大纲.md) · [下一章](P006_电话簿访问配置文件（Phone Book Access Profile，PBAP）.md)
