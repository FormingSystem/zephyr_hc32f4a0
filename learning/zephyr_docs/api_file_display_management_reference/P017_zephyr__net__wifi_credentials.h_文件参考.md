---
id: learning.zephyr-docs.api-file-display-management-reference.page-17
title: zephyr__net__wifi_credentials.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wifi__credentials_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_net\_\_wifi\_credentials.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/wifi__credentials_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于存储和加载Wi-Fi凭据（Credentials）的库。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/net/wifi.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

用于存储和加载Wi-Fi凭据（Credentials）的库。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 17.1\_数据结构（Data Structures）

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

## 17.2\_宏定义（Macros）

<a id="r_ga656bc737cf1bceffc1cf85d06419cec9"></a>

```c
#define WIFI_CREDENTIALS_FLAG_BSSID BIT(0)
```

相关声明：[WIFI_CREDENTIALS_FLAG_BSSID](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga656bc737cf1bceffc1cf85d06419cec9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此条目包含基本服务集标识符（BSSID）。

<a id="r_ga34c10ac642daf7ee05c1b940c01f8932"></a>

```c
#define WIFI_CREDENTIALS_FLAG_FAVORITE BIT(1)
```

相关声明：[WIFI_CREDENTIALS_FLAG_FAVORITE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga34c10ac642daf7ee05c1b940c01f8932)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

应优先选用此条目（Preferred Entry）。

<a id="r_ga179a3abf6a1a44b0bee0d2a9736ece0c"></a>

```c
#define WIFI_CREDENTIALS_FLAG_2_4GHz BIT(2)
```

相关声明：[WIFI_CREDENTIALS_FLAG_2_4GHz](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga179a3abf6a1a44b0bee0d2a9736ece0c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此条目可使用 2.4 GHz 频段（Band）。

<a id="r_ga22d0707e4e4d2fd082563f7c1ebf5308"></a>

```c
#define WIFI_CREDENTIALS_FLAG_5GHz BIT(3)
```

相关声明：[WIFI_CREDENTIALS_FLAG_5GHz](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga22d0707e4e4d2fd082563f7c1ebf5308)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此条目可使用 5 GHz 频段（Band）。

<a id="r_ga50b7c4fd09530f93a7632a03a9a12604"></a>

```c
#define WIFI_CREDENTIALS_FLAG_6GHz BIT(4)
```

相关声明：[WIFI_CREDENTIALS_FLAG_6GHz](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga50b7c4fd09530f93a7632a03a9a12604)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此条目可使用 6 GHz 频段（Band）。

<a id="r_gab9a8dd24857d6ddb22ae96096a3ee75c"></a>

```c
#define WIFI_CREDENTIALS_FLAG_MFP_REQUIRED BIT(5)
```

相关声明：[WIFI_CREDENTIALS_FLAG_MFP_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#gab9a8dd24857d6ddb22ae96096a3ee75c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此条目要求管理帧保护（Management Frame Protection）。

<a id="r_ga973e4e6faafa8f8b946d3164b1daf95d"></a>

```c
#define WIFI_CREDENTIALS_FLAG_MFP_DISABLED BIT(6)
```

相关声明：[WIFI_CREDENTIALS_FLAG_MFP_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga973e4e6faafa8f8b946d3164b1daf95d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此条目禁用管理帧保护（Management Frame Protection）。

<a id="r_gab7024a46e99dc304dd4741c45b13c846"></a>

```c
#define WIFI_CREDENTIALS_FLAG_ANONYMOUS_IDENTITY BIT(7)
```

相关声明：[WIFI_CREDENTIALS_FLAG_ANONYMOUS_IDENTITY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#gab7024a46e99dc304dd4741c45b13c846)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此条目已配置匿名身份（Anonymous Identity）。

<a id="r_ga9a411a277da97426aa190a8f911a4042"></a>

```c
#define WIFI_CREDENTIALS_FLAG_KEY_PASSWORD BIT(8)
```

相关声明：[WIFI_CREDENTIALS_FLAG_KEY_PASSWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga9a411a277da97426aa190a8f911a4042)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此条目已配置密钥口令（Key Password）。

<a id="r_gaf9d3ffe6c9120a7fbc248c3ee66f42fa"></a>

```c
#define WIFI_CREDENTIALS_MAX_PASSWORD_LEN MAX(WIFI_PSK_MAX_LEN, CONFIG_WIFI_CREDENTIALS_SAE_PASSWORD_LENGTH)
```

相关声明：[WIFI_CREDENTIALS_MAX_PASSWORD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#gaf9d3ffe6c9120a7fbc248c3ee66f42fa)、[MAX](../util_reference/P001_通用工具公共接口.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)、[WIFI_PSK_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad7c3b99c974b342935180a28fdc5ddfc)。

密码最大长度（Maximum Password Length）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 17.3\_类型定义（Typedefs）

<a id="r_ga30c9333f10e8e8d03f268fb5c9a69562"></a>

```c
typedef void(* wifi_credentials_ssid_cb) (void *cb_arg, const char *ssid, size_t ssid_len)
```

相关声明：[wifi_credentials_ssid_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga30c9333f10e8e8d03f268fb5c9a69562)。

`wifi_credentials_for_each_ssid` 的回调类型（Callback Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.4\_函数（Functions）

<a id="r_ga548522fbc6b5fdcff4585c34f3565c82"></a>

```c
int wifi_credentials_get_by_ssid_personal (const char *ssid, size_t ssid_len, enum wifi_security_type *type, uint8_t *bssid_buf, size_t bssid_buf_len, char *password_buf, size_t password_buf_len, size_t *password_len, uint32_t *flags, uint8_t *channel, uint32_t *timeout)
```

相关声明：[wifi_credentials_get_by_ssid_personal](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga548522fbc6b5fdcff4585c34f3565c82)、[wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取指定服务集标识符（SSID）的凭据（Credentials）。

<a id="r_ga28b13d11cca692921252e98788552957"></a>

```c
int wifi_credentials_set_personal (const char *ssid, size_t ssid_len, enum wifi_security_type type, const uint8_t *bssid, size_t bssid_len, const char *password, size_t password_len, uint32_t flags, uint8_t channel, uint32_t timeout)
```

相关声明：[wifi_credentials_set_personal](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga28b13d11cca692921252e98788552957)、[wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置指定服务集标识符（SSID）的凭据（Credentials）。

<a id="r_ga3d83001e713206ec07f94996137537d5"></a>

```c
int wifi_credentials_get_by_ssid_personal_struct (const char *ssid, size_t ssid_len, struct wifi_credentials_personal *buf)
```

相关声明：[wifi_credentials_get_by_ssid_personal_struct](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga3d83001e713206ec07f94996137537d5)、[wifi_credentials_personal](../network_core_model_reference/P170_wifi_credentials_personal_结构体.md)。

通过结构体获取指定服务集标识符（SSID）的凭据（Credentials）。

<a id="r_ga1b5525c7a6a7ca312236a2c674d94055"></a>

```c
int wifi_credentials_set_personal_struct (const struct wifi_credentials_personal *creds)
```

相关声明：[wifi_credentials_set_personal_struct](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga1b5525c7a6a7ca312236a2c674d94055)、[wifi_credentials_personal](../network_core_model_reference/P170_wifi_credentials_personal_结构体.md)。

通过结构体设置指定服务集标识符（SSID）的凭据（Credentials）。

<a id="r_ga644d29db8091512a977f8e27b245975e"></a>

```c
int wifi_credentials_delete_by_ssid (const char *ssid, size_t ssid_len)
```

相关声明：[wifi_credentials_delete_by_ssid](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga644d29db8091512a977f8e27b245975e)。

删除指定服务集标识符（SSID）的凭据（Credentials）。

<a id="r_ga467ef5e15a637c33cb1926a3548ffb9e"></a>

```c
bool wifi_credentials_is_empty (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[wifi_credentials_is_empty](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga467ef5e15a637c33cb1926a3548ffb9e)。

检查凭据存储（Credentials Storage）是否为空。

<a id="r_gade76c60899e42fc2af5f7e93143c21ad"></a>

```c
int wifi_credentials_delete_all (void)
```

相关声明：[wifi_credentials_delete_all](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#gade76c60899e42fc2af5f7e93143c21ad)。

删除全部已存储的 Wi-Fi 凭据（Credentials）。

<a id="r_ga3a5b20d07afc52cc452a9c55998ebcf7"></a>

```c
void wifi_credentials_for_each_ssid (wifi_credentials_ssid_cb cb, void *cb_arg)
```

相关声明：[wifi_credentials_for_each_ssid](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga3a5b20d07afc52cc452a9c55998ebcf7)、[wifi_credentials_ssid_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga30c9333f10e8e8d03f268fb5c9a69562)。

为每个已注册的服务集标识符（SSID）调用回调。


## 17.5\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/net/wifi.h](../api_source_runtime_reference/P067_wifi.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P918_wifi_credentials.h_源码浏览.md)
- [wifi_credentials_header](../network_core_model_reference/P169_wifi_credentials_header_结构体.md)
- [wifi_credentials_personal](../network_core_model_reference/P170_wifi_credentials_personal_结构体.md)
- [wifi_credentials_enterprise](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md)
- [WIFI_CREDENTIALS_FLAG_BSSID](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga656bc737cf1bceffc1cf85d06419cec9)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [WIFI_CREDENTIALS_FLAG_FAVORITE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga34c10ac642daf7ee05c1b940c01f8932)
- [WIFI_CREDENTIALS_FLAG_2_4GHz](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga179a3abf6a1a44b0bee0d2a9736ece0c)
- [WIFI_CREDENTIALS_FLAG_5GHz](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga22d0707e4e4d2fd082563f7c1ebf5308)
- [WIFI_CREDENTIALS_FLAG_6GHz](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga50b7c4fd09530f93a7632a03a9a12604)
- [WIFI_CREDENTIALS_FLAG_MFP_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#gab9a8dd24857d6ddb22ae96096a3ee75c)
- [WIFI_CREDENTIALS_FLAG_MFP_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga973e4e6faafa8f8b946d3164b1daf95d)
- [WIFI_CREDENTIALS_FLAG_ANONYMOUS_IDENTITY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#gab7024a46e99dc304dd4741c45b13c846)
- [WIFI_CREDENTIALS_FLAG_KEY_PASSWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga9a411a277da97426aa190a8f911a4042)
- [WIFI_CREDENTIALS_MAX_PASSWORD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#gaf9d3ffe6c9120a7fbc248c3ee66f42fa)
- [MAX](../util_reference/P001_通用工具公共接口.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)
- [WIFI_PSK_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad7c3b99c974b342935180a28fdc5ddfc)
- [wifi_credentials_ssid_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga30c9333f10e8e8d03f268fb5c9a69562)
- [wifi_credentials_get_by_ssid_personal](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga548522fbc6b5fdcff4585c34f3565c82)
- [wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [wifi_credentials_set_personal](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga28b13d11cca692921252e98788552957)
- [wifi_credentials_get_by_ssid_personal_struct](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga3d83001e713206ec07f94996137537d5)
- [wifi_credentials_set_personal_struct](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga1b5525c7a6a7ca312236a2c674d94055)
- [wifi_credentials_delete_by_ssid](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga644d29db8091512a977f8e27b245975e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [wifi_credentials_is_empty](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga467ef5e15a637c33cb1926a3548ffb9e)
- [wifi_credentials_delete_all](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#gade76c60899e42fc2af5f7e93143c21ad)
- [wifi_credentials_for_each_ssid](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga3a5b20d07afc52cc452a9c55998ebcf7)

<a id="header-details"></a>

---

[上一章](P016_zephyr__drivers__uaol.h_文件参考.md) · [返回大纲](大纲.md)
