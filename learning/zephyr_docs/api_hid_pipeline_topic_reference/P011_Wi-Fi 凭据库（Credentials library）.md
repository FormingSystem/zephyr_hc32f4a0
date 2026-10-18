---
id: learning.zephyr-docs.api-hid-pipeline-topic-reference.page-11
title: Wi-Fi 凭据库（Credentials library）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_Wi-Fi 凭据库（Credentials library）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

提供 Wi-Fi 凭据存储和加载方式的库。

<a id="details"></a>

提供 Wi-Fi 凭据（Credentials）存储与加载能力的库。自 4.0 起提供，版本 0.1.0。

<a id="header-files"></a>
<a id="files"></a>

## 11.1\_文件（Files）

<a id="r_wifi_5Fcredentials_2Eh"></a>

```c
file wifi_credentials.h
```

相关声明：[wifi_credentials.h](../api_file_display_management_reference/P017_zephyr__net__wifi_credentials.h_文件参考.md)。

用于存储和加载Wi-Fi凭据（Credentials）的库。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.2\_数据结构（Data Structures）

<a id="r_wifi_5Fcredentials_5Fheader"></a>

```c
struct wifi_credentials_header
```

相关声明：[wifi_credentials_header](../network_core_model_reference/P169_wifi_credentials_header_结构体.md)。

Wi-Fi凭据条目头部（Credentials Entry Header）。

<a id="r_wifi_5Fcredentials_5Fpersonal"></a>

```c
struct wifi_credentials_personal
```

相关声明：[wifi_credentials_personal](../network_core_model_reference/P170_wifi_credentials_personal_结构体.md)。

Wi-Fi个人模式凭据（Personal Credentials）的条目。

<a id="r_wifi_5Fcredentials_5Fenterprise"></a>

```c
struct wifi_credentials_enterprise
```

相关声明：[wifi_credentials_enterprise](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md)。

Wi-Fi企业模式凭据（Enterprise Credentials）的条目。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.3\_宏定义（Macros）

<a id="r_ga656bc737cf1bceffc1cf85d06419cec9"></a>

```c
#define WIFI_CREDENTIALS_FLAG_BSSID BIT(0)
```

相关声明：[WIFI_CREDENTIALS_FLAG_BSSID](#ga656bc737cf1bceffc1cf85d06419cec9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此条目包含基本服务集标识符（BSSID）。

<a id="r_ga34c10ac642daf7ee05c1b940c01f8932"></a>

```c
#define WIFI_CREDENTIALS_FLAG_FAVORITE BIT(1)
```

相关声明：[WIFI_CREDENTIALS_FLAG_FAVORITE](#ga34c10ac642daf7ee05c1b940c01f8932)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

应优先选用此条目（Preferred Entry）。

<a id="r_ga179a3abf6a1a44b0bee0d2a9736ece0c"></a>

```c
#define WIFI_CREDENTIALS_FLAG_2_4GHz BIT(2)
```

相关声明：[WIFI_CREDENTIALS_FLAG_2_4GHz](#ga179a3abf6a1a44b0bee0d2a9736ece0c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此条目可使用 2.4 GHz 频段（Band）。

<a id="r_ga22d0707e4e4d2fd082563f7c1ebf5308"></a>

```c
#define WIFI_CREDENTIALS_FLAG_5GHz BIT(3)
```

相关声明：[WIFI_CREDENTIALS_FLAG_5GHz](#ga22d0707e4e4d2fd082563f7c1ebf5308)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此条目可使用 5 GHz 频段（Band）。

<a id="r_ga50b7c4fd09530f93a7632a03a9a12604"></a>

```c
#define WIFI_CREDENTIALS_FLAG_6GHz BIT(4)
```

相关声明：[WIFI_CREDENTIALS_FLAG_6GHz](#ga50b7c4fd09530f93a7632a03a9a12604)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此条目可使用 6 GHz 频段（Band）。

<a id="r_gab9a8dd24857d6ddb22ae96096a3ee75c"></a>

```c
#define WIFI_CREDENTIALS_FLAG_MFP_REQUIRED BIT(5)
```

相关声明：[WIFI_CREDENTIALS_FLAG_MFP_REQUIRED](#gab9a8dd24857d6ddb22ae96096a3ee75c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此条目要求管理帧保护（Management Frame Protection）。

<a id="r_ga973e4e6faafa8f8b946d3164b1daf95d"></a>

```c
#define WIFI_CREDENTIALS_FLAG_MFP_DISABLED BIT(6)
```

相关声明：[WIFI_CREDENTIALS_FLAG_MFP_DISABLED](#ga973e4e6faafa8f8b946d3164b1daf95d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此条目禁用管理帧保护（Management Frame Protection）。

<a id="r_gab7024a46e99dc304dd4741c45b13c846"></a>

```c
#define WIFI_CREDENTIALS_FLAG_ANONYMOUS_IDENTITY BIT(7)
```

相关声明：[WIFI_CREDENTIALS_FLAG_ANONYMOUS_IDENTITY](#gab7024a46e99dc304dd4741c45b13c846)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此条目已配置匿名身份（Anonymous Identity）。

<a id="r_ga9a411a277da97426aa190a8f911a4042"></a>

```c
#define WIFI_CREDENTIALS_FLAG_KEY_PASSWORD BIT(8)
```

相关声明：[WIFI_CREDENTIALS_FLAG_KEY_PASSWORD](#ga9a411a277da97426aa190a8f911a4042)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此条目已配置密钥口令（Key Password）。

<a id="r_gaf9d3ffe6c9120a7fbc248c3ee66f42fa"></a>

```c
#define WIFI_CREDENTIALS_MAX_PASSWORD_LEN MAX(WIFI_PSK_MAX_LEN, CONFIG_WIFI_CREDENTIALS_SAE_PASSWORD_LENGTH)
```

相关声明：[WIFI_CREDENTIALS_MAX_PASSWORD_LEN](#gaf9d3ffe6c9120a7fbc248c3ee66f42fa)、[MAX](../util_reference/P001_通用工具公共接口.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)、[WIFI_PSK_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad7c3b99c974b342935180a28fdc5ddfc)。

密码最大长度（Maximum Password Length）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 11.4\_类型定义（Typedefs）

<a id="r_ga30c9333f10e8e8d03f268fb5c9a69562"></a>

```c
typedef void(* wifi_credentials_ssid_cb) (void *cb_arg, const char *ssid, size_t ssid_len)
```

相关声明：[wifi_credentials_ssid_cb](#ga30c9333f10e8e8d03f268fb5c9a69562)。

`wifi_credentials_for_each_ssid` 的回调类型（Callback Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.5\_函数（Functions）

<a id="r_ga548522fbc6b5fdcff4585c34f3565c82"></a>

```c
int wifi_credentials_get_by_ssid_personal (const char *ssid, size_t ssid_len, enum wifi_security_type *type, uint8_t *bssid_buf, size_t bssid_buf_len, char *password_buf, size_t password_buf_len, size_t *password_len, uint32_t *flags, uint8_t *channel, uint32_t *timeout)
```

相关声明：[wifi_credentials_get_by_ssid_personal](#ga548522fbc6b5fdcff4585c34f3565c82)、[wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取指定服务集标识符（SSID）的凭据（Credentials）。

<a id="r_ga28b13d11cca692921252e98788552957"></a>

```c
int wifi_credentials_set_personal (const char *ssid, size_t ssid_len, enum wifi_security_type type, const uint8_t *bssid, size_t bssid_len, const char *password, size_t password_len, uint32_t flags, uint8_t channel, uint32_t timeout)
```

相关声明：[wifi_credentials_set_personal](#ga28b13d11cca692921252e98788552957)、[wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置指定服务集标识符（SSID）的凭据（Credentials）。

<a id="r_ga3d83001e713206ec07f94996137537d5"></a>

```c
int wifi_credentials_get_by_ssid_personal_struct (const char *ssid, size_t ssid_len, struct wifi_credentials_personal *buf)
```

相关声明：[wifi_credentials_get_by_ssid_personal_struct](#ga3d83001e713206ec07f94996137537d5)、[wifi_credentials_personal](../network_core_model_reference/P170_wifi_credentials_personal_结构体.md)。

通过结构体获取指定服务集标识符（SSID）的凭据（Credentials）。

<a id="r_ga1b5525c7a6a7ca312236a2c674d94055"></a>

```c
int wifi_credentials_set_personal_struct (const struct wifi_credentials_personal *creds)
```

相关声明：[wifi_credentials_set_personal_struct](#ga1b5525c7a6a7ca312236a2c674d94055)、[wifi_credentials_personal](../network_core_model_reference/P170_wifi_credentials_personal_结构体.md)。

通过结构体设置指定服务集标识符（SSID）的凭据（Credentials）。

<a id="r_ga644d29db8091512a977f8e27b245975e"></a>

```c
int wifi_credentials_delete_by_ssid (const char *ssid, size_t ssid_len)
```

相关声明：[wifi_credentials_delete_by_ssid](#ga644d29db8091512a977f8e27b245975e)。

删除指定服务集标识符（SSID）的凭据（Credentials）。

<a id="r_ga467ef5e15a637c33cb1926a3548ffb9e"></a>

```c
bool wifi_credentials_is_empty (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[wifi_credentials_is_empty](#ga467ef5e15a637c33cb1926a3548ffb9e)。

检查凭据存储（Credentials Storage）是否为空。

<a id="r_gade76c60899e42fc2af5f7e93143c21ad"></a>

```c
int wifi_credentials_delete_all (void)
```

相关声明：[wifi_credentials_delete_all](#gade76c60899e42fc2af5f7e93143c21ad)。

删除全部已存储的 Wi-Fi 凭据（Credentials）。

<a id="r_ga3a5b20d07afc52cc452a9c55998ebcf7"></a>

```c
void wifi_credentials_for_each_ssid (wifi_credentials_ssid_cb cb, void *cb_arg)
```

相关声明：[wifi_credentials_for_each_ssid](#ga3a5b20d07afc52cc452a9c55998ebcf7)、[wifi_credentials_ssid_cb](#ga30c9333f10e8e8d03f268fb5c9a69562)。

为每个已注册的服务集标识符（SSID）调用回调。

## 11.6\_详细说明（Detailed Documentation）

<a id="ga179a3abf6a1a44b0bee0d2a9736ece0c"></a>

### `WIFI_CREDENTIALS_FLAG_2_4GHz`

```c
#define WIFI_CREDENTIALS_FLAG_2_4GHz BIT(2)
```

```c
#include <zephyr/net/wifi_credentials.h>
```

此条目可使用 2.4 GHz 频段（Band）。

<a id="ga22d0707e4e4d2fd082563f7c1ebf5308"></a>

### `WIFI_CREDENTIALS_FLAG_5GHz`

```c
#define WIFI_CREDENTIALS_FLAG_5GHz BIT(3)
```

```c
#include <zephyr/net/wifi_credentials.h>
```

此条目可使用 5 GHz 频段（Band）。

<a id="ga50b7c4fd09530f93a7632a03a9a12604"></a>

### `WIFI_CREDENTIALS_FLAG_6GHz`

```c
#define WIFI_CREDENTIALS_FLAG_6GHz BIT(4)
```

```c
#include <zephyr/net/wifi_credentials.h>
```

此条目可使用 6 GHz 频段（Band）。

<a id="gab7024a46e99dc304dd4741c45b13c846"></a>

### `WIFI_CREDENTIALS_FLAG_ANONYMOUS_IDENTITY`

```c
#define WIFI_CREDENTIALS_FLAG_ANONYMOUS_IDENTITY BIT(7)
```

```c
#include <zephyr/net/wifi_credentials.h>
```

此条目已配置匿名身份（Anonymous Identity）。

<a id="ga656bc737cf1bceffc1cf85d06419cec9"></a>

### `WIFI_CREDENTIALS_FLAG_BSSID`

```c
#define WIFI_CREDENTIALS_FLAG_BSSID BIT(0)
```

```c
#include <zephyr/net/wifi_credentials.h>
```

此条目包含基本服务集标识符（BSSID）。

<a id="ga34c10ac642daf7ee05c1b940c01f8932"></a>

### `WIFI_CREDENTIALS_FLAG_FAVORITE`

```c
#define WIFI_CREDENTIALS_FLAG_FAVORITE BIT(1)
```

```c
#include <zephyr/net/wifi_credentials.h>
```

应优先选用此条目（Preferred Entry）。

<a id="ga9a411a277da97426aa190a8f911a4042"></a>

### `WIFI_CREDENTIALS_FLAG_KEY_PASSWORD`

```c
#define WIFI_CREDENTIALS_FLAG_KEY_PASSWORD BIT(8)
```

```c
#include <zephyr/net/wifi_credentials.h>
```

此条目已配置密钥口令（Key Password）。

<a id="ga973e4e6faafa8f8b946d3164b1daf95d"></a>

### `WIFI_CREDENTIALS_FLAG_MFP_DISABLED`

```c
#define WIFI_CREDENTIALS_FLAG_MFP_DISABLED BIT(6)
```

```c
#include <zephyr/net/wifi_credentials.h>
```

此条目禁用管理帧保护（Management Frame Protection）。

<a id="gab9a8dd24857d6ddb22ae96096a3ee75c"></a>

### `WIFI_CREDENTIALS_FLAG_MFP_REQUIRED`

```c
#define WIFI_CREDENTIALS_FLAG_MFP_REQUIRED BIT(5)
```

```c
#include <zephyr/net/wifi_credentials.h>
```

此条目要求管理帧保护（Management Frame Protection）。

<a id="gaf9d3ffe6c9120a7fbc248c3ee66f42fa"></a>

### `WIFI_CREDENTIALS_MAX_PASSWORD_LEN`

```c
#define WIFI_CREDENTIALS_MAX_PASSWORD_LEN MAX(WIFI_PSK_MAX_LEN, CONFIG_WIFI_CREDENTIALS_SAE_PASSWORD_LENGTH)
```

```c
#include <zephyr/net/wifi_credentials.h>
```

密码最大长度（Maximum Password Length）。

<a id="ga30c9333f10e8e8d03f268fb5c9a69562"></a>

### `wifi_credentials_ssid_cb`

```c
typedef void(* wifi_credentials_ssid_cb) (void *cb_arg, const char *ssid, size_t ssid_len)
```

```c
#include <zephyr/net/wifi_credentials.h>
```

`wifi_credentials_for_each_ssid` 的回调类型（Callback Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cb_arg` | 回调函数参数（Callback Arguments）。`wifi_credentials_for_each_ssid` 传递相应的 `cb_arg`。 |
| `[in] ssid` | 服务集标识符（SSID）。 |
| `[in] ssid_len` | 服务集标识符（SSID）长度。 |

<a id="gade76c60899e42fc2af5f7e93143c21ad"></a>

### `wifi_credentials_delete_all()`

```c
int wifi_credentials_delete_all ( void )
```

```c
#include <zephyr/net/wifi_credentials.h>
```

删除全部已存储的 Wi-Fi 凭据（Credentials）。

删除系统中已存储的全部 Wi-Fi 凭据（Credentials）。通常用于清除所有已保存网络。

**返回（Returns）**：返回值：成功返回 0，否则返回负错误码（Negative Error Code）。

<a id="ga644d29db8091512a977f8e27b245975e"></a>

### `wifi_credentials_delete_by_ssid()`

```c
int wifi_credentials_delete_by_ssid ( const char * ssid, size_t ssid_len )
```

```c
#include <zephyr/net/wifi_credentials.h>
```

删除指定服务集标识符（SSID）的凭据（Credentials）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ssid` | 要查找的服务集标识符（SSID）。 |
| `[in] ssid_len` | 服务集标识符（SSID）长度。 |

**返回（Returns）**：返回值：未找到此 SSID 的网络时返回 `-ENOENT`；成功返回 0，其他情况返回负错误码。

<a id="ga3a5b20d07afc52cc452a9c55998ebcf7"></a>

### `wifi_credentials_for_each_ssid()`

```c
void wifi_credentials_for_each_ssid ( wifi_credentials_ssid_cb cb, void * cb_arg )
```

```c
#include <zephyr/net/wifi_credentials.h>
```

为每个已注册的服务集标识符（SSID）调用回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调（Callback）。 |
| `cb_arg` | 回调函数参数（Callback Argument）。 |

<a id="ga548522fbc6b5fdcff4585c34f3565c82"></a>

### `wifi_credentials_get_by_ssid_personal()`

```c
int wifi_credentials_get_by_ssid_personal ( const char * ssid, size_t ssid_len, enum wifi_security_type * type, uint8_t * bssid_buf, size_t bssid_buf_len, char * password_buf, size_t password_buf_len, size_t * password_len, uint32_t * flags, uint8_t * channel, uint32_t * timeout )
```

```c
#include <zephyr/net/wifi_credentials.h>
```

获取指定服务集标识符（SSID）的凭据（Credentials）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ssid` | 要查找的服务集标识符（SSID）。 |
| `[in] ssid_len` | 服务集标识符（SSID）长度。 |
| `[out] type` | Wi‑Fi 安全类型（Wi-Fi security type）。 |
| `[out] bssid_buf` | 若固定了基本服务集标识符（BSSID），用于保存它的缓冲区。 |
| `[in] bssid_buf_len` | `bssid_buf` 的长度。 |
| `[out] password_buf` | 用于保存密码（Password）的缓冲区。 |
| `[in] password_buf_len` | `password_buf` 的长度。 |
| `[out] password_len` | 密码长度（Password Length）。 |
| `[out] flags` | 标志（Flags）。 |
| `[out] channel` | 信道（Channel）。 |
| `[out] timeout` | 超时（Timeout） |

**返回（Returns）**：返回值：0 表示成功；`-ENOENT` 表示未找到此 SSID 的网络；`-EINVAL` 表示必需缓冲区为 `NULL`，或 SSID 长度无效；`-EPROTO` 表示此 SSID 对应的网络不是个人网络（Personal Network）。

<a id="ga3d83001e713206ec07f94996137537d5"></a>

### `wifi_credentials_get_by_ssid_personal_struct()`

```c
int wifi_credentials_get_by_ssid_personal_struct ( const char * ssid, size_t ssid_len, struct wifi_credentials_personal * buf )
```

```c
#include <zephyr/net/wifi_credentials.h>
```

通过结构体获取指定服务集标识符（SSID）的凭据（Credentials）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ssid` | 要查找的服务集标识符（SSID）。 |
| `[in] ssid_len` | 服务集标识符（SSID）长度。 |
| `[out] buf` | `credentials`：指向保存凭据（Credentials）的结构体的指针。 |

**返回（Returns）**：返回值：0 表示成功；`-ENOENT` 表示未找到此 SSID 的网络；`-EINVAL` 表示必需缓冲区为 `NULL` 或过小；`-EPROTO` 表示此 SSID 对应的网络不是个人网络（Personal Network）。

<a id="ga467ef5e15a637c33cb1926a3548ffb9e"></a>

### `wifi_credentials_is_empty()`

```c
bool wifi_credentials_is_empty ( void )
```

```c
#include <zephyr/net/wifi_credentials.h>
```

检查凭据存储（Credentials Storage）是否为空。

**返回（Returns）**：返回值：凭据存储（Credential Storage）为空时返回 `true`，否则返回 `false`。

<a id="ga28b13d11cca692921252e98788552957"></a>

### `wifi_credentials_set_personal()`

```c
int wifi_credentials_set_personal ( const char * ssid, size_t ssid_len, enum wifi_security_type type, const uint8_t * bssid, size_t bssid_len, const char * password, size_t password_len, uint32_t flags, uint8_t channel, uint32_t timeout )
```

```c
#include <zephyr/net/wifi_credentials.h>
```

设置指定服务集标识符（SSID）的凭据（Credentials）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ssid` | 要查找的服务集标识符（SSID）。 |
| `[in] ssid_len` | 服务集标识符（SSID）长度。 |
| `[in] type` | Wi‑Fi 安全类型（Wi-Fi security type）。 |
| `[in] bssid` | 基本服务集标识符（BSSID），可为 `NULL`。 |
| `[in] bssid_len` | BSSID 缓冲区长度，必须为 0 或 `WIFI_MAC_ADDR_LEN`。 |
| `[in] password` | 密码（Password）。 |
| `[in] password_len` | 密码长度（Password Length）。 |
| `[in] flags` | 标志（Flags）。 |
| `[in] channel` | 信道（Channel）。 |
| `[in] timeout` | 超时（Timeout） |

**说明（Note）**：注意：为已存储的 SSID 保存凭据（Credentials）会覆盖已有条目，不会添加第二条。只有不同的 SSID 才会占用不同存储槽位（Storage Slots）。

**返回（Returns）**：返回值：0 表示成功，凭据已保存到持久存储（Persistent Storage）；`-EINVAL` 表示必需缓冲区为 `NULL`，或安全类型不受支持；`-ENOTSUP` 表示安全类型不受支持；`-ENOBUFS` 表示所有槽位均已占用。

<a id="ga1b5525c7a6a7ca312236a2c674d94055"></a>

### `wifi_credentials_set_personal_struct()`

```c
int wifi_credentials_set_personal_struct ( const struct wifi_credentials_personal * creds)
```

```c
#include <zephyr/net/wifi_credentials.h>
```

通过结构体设置指定服务集标识符（SSID）的凭据（Credentials）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] creds` | `credentials`：指向从中加载凭据（Credentials）的结构体的指针。 |

**说明（Note）**：注意：为已存储的 SSID 保存凭据（Credentials）会覆盖已有条目，不会添加第二条。只有不同的 SSID 才会占用不同存储槽位（Storage Slots）。

**返回（Returns）**：返回值：0 表示成功；`-ENOENT` 表示未找到此 SSID 的网络；`-EINVAL` 表示必需缓冲区为 `NULL` 或大小不正确；`-ENOBUFS` 表示所有槽位均已占用。


## 11.7\_原页交叉引用（Cross References）

- [wifi_credentials.h](../api_file_display_management_reference/P017_zephyr__net__wifi_credentials.h_文件参考.md)
- [wifi_credentials_header](../network_core_model_reference/P169_wifi_credentials_header_结构体.md)
- [wifi_credentials_personal](../network_core_model_reference/P170_wifi_credentials_personal_结构体.md)
- [wifi_credentials_enterprise](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [MAX](../util_reference/P001_通用工具公共接口.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)
- [WIFI_PSK_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad7c3b99c974b342935180a28fdc5ddfc)
- [wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_虚拟网络接口支持函数（Virtual Network Interface Support Functions）.md) · [返回大纲](大纲.md)
