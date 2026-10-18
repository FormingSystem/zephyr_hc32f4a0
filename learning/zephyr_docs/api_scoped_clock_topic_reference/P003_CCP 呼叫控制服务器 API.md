---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-3
title: CCP 呼叫控制服务器 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_CCP 呼叫控制服务器 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_bt_5Fccp_5Fcall_5Fcontrol_5Fserver_5Fbearer"></a>

```c
struct bt_ccp_call_control_server_bearer
```

相关声明：[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)。

抽象呼叫控制服务器电话承载（Telephone Bearer）结构体。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.2\_函数（Functions）

<a id="r_ga5e5acb90cc39b5f8a4e25d8ab8a11b10"></a>

```c
int bt_ccp_call_control_server_register_bearer (const struct bt_tbs_register_param *param, struct bt_ccp_call_control_server_bearer **bearer)
```

相关声明：[bt_ccp_call_control_server_register_bearer](#ga5e5acb90cc39b5f8a4e25d8ab8a11b10)、[bt_tbs_register_param](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)。

注册电话承载（Telephone Bearer）。

<a id="r_gaa2486dec8a47bd7f4cd4076477e8ac4a"></a>

```c
int bt_ccp_call_control_server_unregister_bearer (struct bt_ccp_call_control_server_bearer *bearer)
```

相关声明：[bt_ccp_call_control_server_unregister_bearer](#gaa2486dec8a47bd7f4cd4076477e8ac4a)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)。

注销电话承载（Telephone Bearer）。

<a id="r_gaae263e42d76d99d950ac535c22fe64c2"></a>

```c
int bt_ccp_call_control_server_set_bearer_provider_name (struct bt_ccp_call_control_server_bearer *bearer, const char *name)
```

相关声明：[bt_ccp_call_control_server_set_bearer_provider_name](#gaae263e42d76d99d950ac535c22fe64c2)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)。

设置新的承载提供方名称（Bearer Provider Name）。

<a id="r_ga0b775c233dcfd08f57322afaf6fa9bcf"></a>

```c
int bt_ccp_call_control_server_get_bearer_provider_name (struct bt_ccp_call_control_server_bearer *bearer, char *name, size_t name_size)
```

相关声明：[bt_ccp_call_control_server_get_bearer_provider_name](#ga0b775c233dcfd08f57322afaf6fa9bcf)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)。

获取承载提供方名称（Bearer Provider Name）。

<a id="r_ga4c250633e8a9ff479952f9300c8eeddd"></a>

```c
int bt_ccp_call_control_server_get_bearer_uci (struct bt_ccp_call_control_server_bearer *bearer, char uci[6U])
```

相关声明：[bt_ccp_call_control_server_get_bearer_uci](#ga4c250633e8a9ff479952f9300c8eeddd)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)。

获取承载的统一呼叫者标识符（UCI）。

<a id="r_gac670cf57d2f02df44ea0d82a58524242"></a>

```c
int bt_ccp_call_control_server_set_bearer_tech (struct bt_ccp_call_control_server_bearer *bearer, enum bt_bearer_tech tech)
```

相关声明：[bt_ccp_call_control_server_set_bearer_tech](#gac670cf57d2f02df44ea0d82a58524242)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)、[bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)。

设置新的承载技术（Bearer Technology）。

<a id="r_ga84efc07e1703536ad6a005b5c5d9fb16"></a>

```c
int bt_ccp_call_control_server_get_bearer_tech (const struct bt_ccp_call_control_server_bearer *bearer, enum bt_bearer_tech *tech)
```

相关声明：[bt_ccp_call_control_server_get_bearer_tech](#ga84efc07e1703536ad6a005b5c5d9fb16)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)、[bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)。

获取承载技术（Bearer Technology）。

<a id="r_gaf7880d2e467b0931d894231312b7ed9b"></a>

```c
int bt_ccp_call_control_server_set_bearer_uri_schemes (struct bt_ccp_call_control_server_bearer *bearer, const char *uri_schemes)
```

相关声明：[bt_ccp_call_control_server_set_bearer_uri_schemes](#gaf7880d2e467b0931d894231312b7ed9b)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)。

设置新的承载所支持 URI 方案列表（URI Schemes Supported List）。

<a id="r_gad8525ac242806efd70d6adbd0148a0ba"></a>

```c
int bt_ccp_call_control_server_get_bearer_uri_schemes (struct bt_ccp_call_control_server_bearer *bearer, char *uri_schemes, size_t uri_schemes_size)
```

相关声明：[bt_ccp_call_control_server_get_bearer_uri_schemes](#gad8525ac242806efd70d6adbd0148a0ba)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)。

获取承载所支持 URI 方案列表（URI Schemes Supported List）。

## 3.3\_详细说明（Detailed Documentation）

<a id="ga0b775c233dcfd08f57322afaf6fa9bcf"></a>

### `bt_ccp_call_control_server_get_bearer_provider_name()`

```c
int bt_ccp_call_control_server_get_bearer_provider_name ( struct bt_ccp_call_control_server_bearer * bearer, char * name, size_t name_size )
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

获取承载提供方名称（Bearer Provider Name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] bearer` | 要获取名称的承载（Bearer）。 |
| `[out] name` | 指向缓冲区的指针，将在其中写入承载提供方名称（Bearer Provider Name）。 |
| ` name_size` | 名称缓冲区大小（Name Buffer Size）。建议使用 CONFIG_BT_CCP_CALL_CONTROL_SERVER_PROVIDER_NAME_MAX_LENGTH + 1，确保始终能够容纳名称。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | bearer 或 name 为 NULL。 |
| `-EFAULT` | bearer 未注册（Not Registered）。 |
| `-ENOMEM` | name_size 不足以容纳承载名称（Bearer Name），包括空字符终止符（Null Terminator）。 |

<a id="ga84efc07e1703536ad6a005b5c5d9fb16"></a>

### `bt_ccp_call_control_server_get_bearer_tech()`

```c
int bt_ccp_call_control_server_get_bearer_tech ( const struct bt_ccp_call_control_server_bearer * bearer, enum bt_bearer_tech * tech )
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

获取承载技术（Bearer Technology）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] bearer` | 要获取技术类型的承载（Bearer）。 |
| `[out] tech` | 指针，其指向的值将更新为承载技术类型（Bearer Technology）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | bearer 或 tech 为 NULL。 |
| `-EFAULT` | bearer 未注册（Not Registered）。 |

<a id="ga4c250633e8a9ff479952f9300c8eeddd"></a>

### `bt_ccp_call_control_server_get_bearer_uci()`

```c
int bt_ccp_call_control_server_get_bearer_uci ( struct bt_ccp_call_control_server_bearer * bearer, char uci[6U] )
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

获取承载的统一呼叫者标识符（UCI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] bearer` | 要获取 UCI 的承载（Bearer）。 |
| `[out] uci` | 指向大小为 BT_TBS_MAX_UCI_SIZE 的缓冲区的指针，将在其中写入承载 UCI。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | bearer 或 uci 为 NULL。 |
| `-EFAULT` | bearer 未注册（Not Registered）。 |

<a id="gad8525ac242806efd70d6adbd0148a0ba"></a>

### `bt_ccp_call_control_server_get_bearer_uri_schemes()`

```c
int bt_ccp_call_control_server_get_bearer_uri_schemes ( struct bt_ccp_call_control_server_bearer * bearer, char * uri_schemes, size_t uri_schemes_size )
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

获取承载所支持 URI 方案列表（URI Schemes Supported List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] bearer` | 要获取所支持 URI 方案列表（URI Schemes Supported List）的承载（Bearer）。 |
| `[out] uri_schemes` | 指针，其指向的值将更新为承载所支持的 URI 方案列表（URI Schemes Supported List）。 |
| ` uri_schemes_size` | uri_schemes 缓冲区大小。建议使用 CONFIG_BT_CCP_CALL_CONTROL_SERVER_URI_SCHEMES_MAX_LENGTH + 1，确保始终能够容纳所支持的 URI 方案列表。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | bearer 或 uri_schemes 为 NULL。 |
| `-EFAULT` | bearer 未注册（Not Registered）。 |
| `-ENOMEM` | uri_schemes_size 不足以容纳承载所支持的 URI 方案列表，包括空字符终止符（Null Terminator）。 |

<a id="ga5e5acb90cc39b5f8a4e25d8ab8a11b10"></a>

### `bt_ccp_call_control_server_register_bearer()`

```c
int bt_ccp_call_control_server_register_bearer ( const struct bt_tbs_register_param * param, struct bt_ccp_call_control_server_bearer ** bearer )
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

注册电话承载（Telephone Bearer）。

使用提供的参数注册电话承载服务（Telephone Bearer Service，TBS）或通用电话承载服务（Generic Telephone Bearer Service，GTBS）。

按照 TBS 规范，必须为此特性实例化 GTBS，因此注册任何 TBS 之前，都必须先注册 GTBS。同样，必须先注销全部 TBS，才能通过 bt_ccp_call_control_server_unregister_bearer() 注销 GTBS。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] param` | 用于初始化承载（Bearer）的参数。 |
| `[out] bearer` | 指向已初始化承载（Bearer）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | param 包含无效数据（Invalid Data）。 |
| `-EALREADY` | param.gtbs 为 true，且 GTBS 已注册。 |
| `-EAGAIN` | param.gtbs 为 false，且 GTBS 尚未注册。 |
| `-ENOMEM` | param.gtbs 为 false，且无法再注册更多 TBS（参见 CONFIG_BT_TBS_BEARER_COUNT）；或者 param.uri_schemes 的长度超过 CONFIG_BT_CCP_CALL_CONTROL_SERVER_URI_SCHEMES_MAX_LENGTH。 |
| `-ENOEXEC` | 服务注册（Register Service）失败。 |

<a id="gaae263e42d76d99d950ac535c22fe64c2"></a>

### `bt_ccp_call_control_server_set_bearer_provider_name()`

```c
int bt_ccp_call_control_server_set_bearer_provider_name ( struct bt_ccp_call_control_server_bearer * bearer, const char * name )
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

设置新的承载提供方名称（Bearer Provider Name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer` | 要设置名称的承载（Bearer）。 |
| `name` | 新的承载提供方名称（Bearer Provider Name）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | bearer 或 name 为 NULL，或 name 为空字符串，或 name 的长度超过 CONFIG_BT_CCP_CALL_CONTROL_SERVER_PROVIDER_NAME_MAX_LENGTH。 |
| `-EFAULT` | bearer 未注册（Not Registered）。 |
| `-EBUSY` | bearer 对应的 TBS 实例忙碌（Busy）。 |
| `-ENOEXEC` | bearer 对应的 TBS 实例返回了非预期错误（Unexpected Error）。 |

<a id="gac670cf57d2f02df44ea0d82a58524242"></a>

### `bt_ccp_call_control_server_set_bearer_tech()`

```c
int bt_ccp_call_control_server_set_bearer_tech ( struct bt_ccp_call_control_server_bearer * bearer, enum bt_bearer_tech tech )
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

设置新的承载技术（Bearer Technology）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] bearer` | 要设置名称的承载（Bearer）。 |
| ` tech` | 新的承载技术类型（Bearer Technology）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | bearer 为 NULL，或 tech 无效。 |
| `-EFAULT` | bearer 未注册（Not Registered）。 |

<a id="gaf7880d2e467b0931d894231312b7ed9b"></a>

### `bt_ccp_call_control_server_set_bearer_uri_schemes()`

```c
int bt_ccp_call_control_server_set_bearer_uri_schemes ( struct bt_ccp_call_control_server_bearer * bearer, const char * uri_schemes )
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

设置新的承载所支持 URI 方案列表（URI Schemes Supported List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer` | 要设置所支持 URI 方案列表（URI Schemes Supported List）的承载（Bearer）。 |
| `uri_schemes` | 新的承载所支持 URI 方案列表（URI Schemes Supported List）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已设置新的 URI 方案支持列表，或列表没有变化。 |
| `-EINVAL` | bearer 或 uri_schemes 为 NULL，或 uri_schemes 为空字符串，或 uri_schemes 含有 URI 方案不允许的字符。 |
| `-EFAULT` | bearer 未注册（Not Registered）。 |
| `-ENOMEM` | uri_schemes 的长度超过 CONFIG_BT_CCP_CALL_CONTROL_SERVER_URI_SCHEMES_MAX_LENGTH。 |

<a id="gaa2486dec8a47bd7f4cd4076477e8ac4a"></a>

### `bt_ccp_call_control_server_unregister_bearer()`

```c
int bt_ccp_call_control_server_unregister_bearer ( struct bt_ccp_call_control_server_bearer * bearer)
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

注销电话承载（Telephone Bearer）。

使用提供的参数注销电话承载服务（TBS）或通用电话承载服务（GTBS）。承载必须先通过 bt_ccp_call_control_server_register_bearer() 注册，之后才能注销。

注销 GTBS 之前，必须先注销全部 TBS。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer` | 要注销的承载（Bearer）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | bearer 为 NULL。 |
| `-EALREADY` | 承载（Bearer）未注册。 |
| `-ENOEXEC` | 服务注销（Unregister Service）失败。 |


## 3.4\_原页交叉引用（Cross References）

- [bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)
- [bt_tbs_register_param](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md)
- [bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)
- [zephyr/bluetooth/audio/ccp.h](../api_file_signal_device_reference/P002_zephyr__bluetooth__audio__ccp.h_文件参考.md)
- [CONFIG_BT_CCP_CALL_CONTROL_SERVER_PROVIDER_NAME_MAX_LENGTH](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CCP_CALL_CONTROL_SERVER_PROVIDER_NAME_MAX_LENGTH)
- [BT_TBS_MAX_UCI_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga42b72d7aef36cc7ea0d5dd4ec3d7a717)
- [CONFIG_BT_CCP_CALL_CONTROL_SERVER_URI_SCHEMES_MAX_LENGTH](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CCP_CALL_CONTROL_SERVER_URI_SCHEMES_MAX_LENGTH)
- [CONFIG_BT_TBS_BEARER_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_BEARER_COUNT)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_音频流控制服务（Audio Stream Control Service，ASCS）.md) · [返回大纲](大纲.md) · [下一章](P004_助听接入服务（Hearing Access Service，HAS）.md)
