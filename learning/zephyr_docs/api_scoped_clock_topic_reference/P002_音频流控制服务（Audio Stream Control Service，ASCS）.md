---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-2
title: 音频流控制服务（Audio Stream Control Service，ASCS）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_音频流控制服务（Audio Stream Control Service，ASCS）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

音频流控制服务（Audio Stream Control Service，ASCS）

<a id="details"></a>

音频流控制服务（Audio Stream Control Service，ASCS）。自 4.5 起提供（Since 4.5），版本（Version）0.1.0。ASCS 提供音频流端点（Audio Stream Endpoints，ASEs），使客户端能够控制这些端点及其关联的单播音频流（Unicast Audio Streams）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fbap_5Fascs_5Frsp"></a>

```c
struct bt_bap_ascs_rsp
```

相关声明：[bt_bap_ascs_rsp](../bluetooth_le_audio_model_reference/P010_bt_bap_ascs_rsp_结构体.md)。

保存 ASE 控制点通知（ASE Control Point Notification）字段值的结构体。

<a id="r_bt_5Fbap_5Fqos_5Fcfg_5Fpref"></a>

```c
struct bt_bap_qos_cfg_pref
```

相关声明：[bt_bap_qos_cfg_pref](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md)。

音频流服务质量偏好（Audio Stream Quality of Service Preference）结构体。

<a id="r_bt_5Fascs_5Fcb"></a>

```c
struct bt_ascs_cb
```

相关声明：[bt_ascs_cb](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md)。

音频流控制服务（Audio Stream Control Service，ASCS）回调结构体。

<a id="r_bt_5Fascs_5Fregister_5Fparam"></a>

```c
struct bt_ascs_register_param
```

相关声明：[bt_ascs_register_param](../bluetooth_le_audio_model_reference/P006_bt_ascs_register_param_结构体.md)。

注册音频流控制服务（Audio Stream Control Service，ASCS）的参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga8e5cd46a1428a315119e47c9cbbb9bfd"></a>

```c
#define BT_BAP_ASCS_RSP(c, r)
```

相关声明：[BT_BAP_ASCS_RSP](#ga8e5cd46a1428a315119e47c9cbbb9bfd)。

用于初始化保存音频流端点控制点（ASE Control Point）通知值的对象的宏。

<a id="r_ga7a3fc7cb21be45276cf50846c076101d"></a>

```c
#define BT_BAP_QOS_CFG_PREF(_unframed_supported, _phy, _rtn, _latency, _pd_min, _pd_max, _pref_pd_min, _pref_pd_max)
```

相关声明：[BT_BAP_QOS_CFG_PREF](#ga7a3fc7cb21be45276cf50846c076101d)。

用于声明 `bt_bap_qos_cfg_pref` 成员的辅助宏。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.3\_枚举（Enumerations）

<a id="r_ga9f7efa749c75edd32dc50503397ab9d1"></a>

```c
enum bt_bap_ascs_rsp_code { BT_BAP_ASCS_RSP_CODE_SUCCESS = 0x00U , BT_BAP_ASCS_RSP_CODE_NOT_SUPPORTED = 0x01U , BT_BAP_ASCS_RSP_CODE_INVALID_LENGTH = 0x02U , BT_BAP_ASCS_RSP_CODE_INVALID_ASE = 0x03U , BT_BAP_ASCS_RSP_CODE_INVALID_ASE_STATE = 0x04U , BT_BAP_ASCS_RSP_CODE_INVALID_DIR = 0x05U , BT_BAP_ASCS_RSP_CODE_CAP_UNSUPPORTED = 0x06U , BT_BAP_ASCS_RSP_CODE_CONF_UNSUPPORTED = 0x07U , BT_BAP_ASCS_RSP_CODE_CONF_REJECTED = 0x08U , BT_BAP_ASCS_RSP_CODE_CONF_INVALID = 0x09U , BT_BAP_ASCS_RSP_CODE_METADATA_UNSUPPORTED = 0x0AU , BT_BAP_ASCS_RSP_CODE_METADATA_REJECTED = 0x0BU , BT_BAP_ASCS_RSP_CODE_METADATA_INVALID = 0x0CU , BT_BAP_ASCS_RSP_CODE_NO_MEM = 0x0DU , BT_BAP_ASCS_RSP_CODE_UNSPECIFIED = 0x0EU }
```

相关声明：[bt_bap_ascs_rsp_code](#ga9f7efa749c75edd32dc50503397ab9d1)、[BT_BAP_ASCS_RSP_CODE_SUCCESS](#gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd)、[BT_BAP_ASCS_RSP_CODE_NOT_SUPPORTED](#gga9f7efa749c75edd32dc50503397ab9d1a54515d30244888af19711f153b942d2d)、[BT_BAP_ASCS_RSP_CODE_INVALID_LENGTH](#gga9f7efa749c75edd32dc50503397ab9d1ad43b45076cbb1ec36af8a4e5126d4bb9)、[BT_BAP_ASCS_RSP_CODE_INVALID_ASE](#gga9f7efa749c75edd32dc50503397ab9d1a635bf6ad106e80e4e64ce3153fd668aa)、[BT_BAP_ASCS_RSP_CODE_INVALID_ASE_STATE](#gga9f7efa749c75edd32dc50503397ab9d1a11bc72f67d626889c24cd54f412730b5)、[BT_BAP_ASCS_RSP_CODE_INVALID_DIR](#gga9f7efa749c75edd32dc50503397ab9d1a64417c64d67fa73fa8430b6f4255e146)、[BT_BAP_ASCS_RSP_CODE_CAP_UNSUPPORTED](#gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a)、[BT_BAP_ASCS_RSP_CODE_CONF_UNSUPPORTED](#gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62)、[BT_BAP_ASCS_RSP_CODE_CONF_REJECTED](#gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21)、[BT_BAP_ASCS_RSP_CODE_CONF_INVALID](#gga9f7efa749c75edd32dc50503397ab9d1a7f2a361b595dad7bc0e7f354bf6a1219)、[BT_BAP_ASCS_RSP_CODE_METADATA_UNSUPPORTED](#gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7)、[BT_BAP_ASCS_RSP_CODE_METADATA_REJECTED](#gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06)、[BT_BAP_ASCS_RSP_CODE_METADATA_INVALID](#gga9f7efa749c75edd32dc50503397ab9d1a3ef9532dbd19abc90a89305d67f82e06)、[BT_BAP_ASCS_RSP_CODE_NO_MEM](#gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb)、[BT_BAP_ASCS_RSP_CODE_UNSPECIFIED](#gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a)。

响应状态码（Response Status Code）。

<a id="r_ga9ca1630544a336b15af8a8e8934c5a45"></a>

```c
enum bt_bap_ascs_reason { BT_BAP_ASCS_REASON_NONE = 0x00U , BT_BAP_ASCS_REASON_CODEC = 0x01U , BT_BAP_ASCS_REASON_CODEC_DATA = 0x02U , BT_BAP_ASCS_REASON_INTERVAL = 0x03U , BT_BAP_ASCS_REASON_FRAMING = 0x04U , BT_BAP_ASCS_REASON_PHY = 0x05U , BT_BAP_ASCS_REASON_SDU = 0x06U , BT_BAP_ASCS_REASON_RTN = 0x07U , BT_BAP_ASCS_REASON_LATENCY = 0x08U , BT_BAP_ASCS_REASON_PD = 0x09U , BT_BAP_ASCS_REASON_CIS = 0x0AU }
```

相关声明：[bt_bap_ascs_reason](#ga9ca1630544a336b15af8a8e8934c5a45)、[BT_BAP_ASCS_REASON_NONE](#gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd)、[BT_BAP_ASCS_REASON_CODEC](#gga9ca1630544a336b15af8a8e8934c5a45a8923f9c27858f27fd3799367cf525aea)、[BT_BAP_ASCS_REASON_CODEC_DATA](#gga9ca1630544a336b15af8a8e8934c5a45a69c9d998626ccb2a6963dd2dfd68cbb0)、[BT_BAP_ASCS_REASON_INTERVAL](#gga9ca1630544a336b15af8a8e8934c5a45ae297b097cc8fbb5f161c0d8c44c6623c)、[BT_BAP_ASCS_REASON_FRAMING](#gga9ca1630544a336b15af8a8e8934c5a45a458cd637ba37015e2598990f9f248539)、[BT_BAP_ASCS_REASON_PHY](#gga9ca1630544a336b15af8a8e8934c5a45a8eda92a6782649f2a42f0021095a54a8)、[BT_BAP_ASCS_REASON_SDU](#gga9ca1630544a336b15af8a8e8934c5a45a731ac5962c8a8685c3f40884c1b67d0b)、[BT_BAP_ASCS_REASON_RTN](#gga9ca1630544a336b15af8a8e8934c5a45acc839aadf0d60ce8eb086271397b94cf)、[BT_BAP_ASCS_REASON_LATENCY](#gga9ca1630544a336b15af8a8e8934c5a45a904156d246f97189820c9de93fb90942)、[BT_BAP_ASCS_REASON_PD](#gga9ca1630544a336b15af8a8e8934c5a45a1fdcf3a40ed30b7aa63e1df573a2d557)、[BT_BAP_ASCS_REASON_CIS](#gga9ca1630544a336b15af8a8e8934c5a45a93bc6ab73f6088bceea03c6f8e71854c)。

响应原因（Response Reasons）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.4\_函数（Functions）

<a id="r_ga04eddf75bc1f2deafee5d6b234dd5b07"></a>

```c
int bt_ascs_register (const struct bt_ascs_register_param *param)
```

相关声明：[bt_ascs_register](#ga04eddf75bc1f2deafee5d6b234dd5b07)、[bt_ascs_register_param](../bluetooth_le_audio_model_reference/P006_bt_ascs_register_param_结构体.md)。

注册音频流控制服务（Audio Stream Control Service，ASCS）。

<a id="r_ga2a87430dd2b2a04985c2faffb0b033a3"></a>

```c
int bt_ascs_unregister (void)
```

相关声明：[bt_ascs_unregister](#ga2a87430dd2b2a04985c2faffb0b033a3)。

注销音频流控制服务（ASCS）。

## 2.5\_详细说明（Detailed Documentation）

<a id="ga8e5cd46a1428a315119e47c9cbbb9bfd"></a>

### `BT_BAP_ASCS_RSP`

```c
#define BT_BAP_ASCS_RSP ( c, r )
```

```c
#include <zephyr/bluetooth/audio/ascs.h>
```

展开值（Value）：

```c
(struct bt_bap_ascs_rsp)                                                                   \
{                                                                                          \
        .code = c, .reason = r                                                             \
}
```

用于初始化保存音频流端点控制点（ASE Control Point）通知值的对象的宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `c` | 响应码字段（Response Code Field）。 |
| `r` | 原因字段（Reason Field），为 bt_bap_ascs_reason 或 bt_audio_metadata_type，参见 bt_bap_ascs_rsp 中的说明。 |

<a id="ga7a3fc7cb21be45276cf50846c076101d"></a>

### `BT_BAP_QOS_CFG_PREF`

```c
#define BT_BAP_QOS_CFG_PREF ( _unframed_supported, _phy, _rtn, _latency, _pd_min, _pd_max, _pref_pd_min, _pref_pd_max )
```

```c
#include <zephyr/bluetooth/audio/ascs.h>
```

展开值（Value）：

```c
{                                                                                          \
        .unframed_supported = _unframed_supported,                                         \
        .phy = _phy,                                                                       \
        .rtn = _rtn,                                                                       \
        .latency = _latency,                                                               \
        .pd_min = _pd_min,                                                                 \
        .pd_max = _pd_max,                                                                 \
        .pref_pd_min = _pref_pd_min,                                                       \
        .pref_pd_max = _pref_pd_max,                                                       \
}
```

用于声明 `bt_bap_qos_cfg_pref` 成员的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_unframed_supported` | 是否支持未成帧的 PDU（Unframed PDUs）。 |
| `_phy` | 首选目标物理层（Preferred Target PHY）。 |
| `_rtn` | 首选重传次数（Preferred Retransmission Number）。 |
| `_latency` | 首选最大传输延迟（Preferred Maximum Transport Latency），单位为毫秒。 |
| `_pd_min` | 最小呈现延迟（Minimum Presentation Delay），单位为微秒。 |
| `_pd_max` | 最大呈现延迟（Maximum Presentation Delay），单位为微秒。 |
| `_pref_pd_min` | 首选最小呈现延迟（Preferred Minimum Presentation Delay），单位为微秒。 |
| `_pref_pd_max` | 首选最大呈现延迟（Preferred Maximum Presentation Delay），单位为微秒。 |

<a id="ga9ca1630544a336b15af8a8e8934c5a45"></a>

### `bt_bap_ascs_reason`

```c
enum bt_bap_ascs_reason
```

```c
#include <zephyr/bluetooth/audio/ascs.h>
```

响应原因（Response Reasons）。

bt_bap_ascs_rsp_code 值为 BT_BAP_ASCS_RSP_CODE_CONF_UNSUPPORTED、BT_BAP_ASCS_RSP_CODE_CONF_REJECTED 或 BT_BAP_ASCS_RSP_CODE_CONF_INVALID 时使用这些值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAP_ASCS_REASON_NONE` | 无原因（No Reason）。 |
| `BT_BAP_ASCS_REASON_CODEC` | 编解码器 ID（Codec ID）。 |
| `BT_BAP_ASCS_REASON_CODEC_DATA` | 编解码器配置（Codec Configuration）。 |
| `BT_BAP_ASCS_REASON_INTERVAL` | 服务数据单元间隔（SDU Interval）。 |
| `BT_BAP_ASCS_REASON_FRAMING` | 成帧（Framing）。 |
| `BT_BAP_ASCS_REASON_PHY` | 物理层（PHY）。 |
| `BT_BAP_ASCS_REASON_SDU` | 服务数据单元（SDU）的最大大小。 |
| `BT_BAP_ASCS_REASON_RTN` | 重传次数（Retransmission Number）。 |
| `BT_BAP_ASCS_REASON_LATENCY` | 最大传输延迟（Max Transport Latency）。 |
| `BT_BAP_ASCS_REASON_PD` | 呈现延迟（Presentation Delay）。 |
| `BT_BAP_ASCS_REASON_CIS` | 无效的连接等时流映射（CIS Mapping）。 |

<a id="ga9f7efa749c75edd32dc50503397ab9d1"></a>

### `bt_bap_ascs_rsp_code`

```c
enum bt_bap_ascs_rsp_code
```

```c
#include <zephyr/bluetooth/audio/ascs.h>
```

响应状态码（Response Status Code）。

请求流操作（Stream Operation）时，由服务器将这些值发送给客户端。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAP_ASCS_RSP_CODE_SUCCESS` | 服务器成功完成操作（Operation）。 |
| `BT_BAP_ASCS_RSP_CODE_NOT_SUPPORTED` | 服务器不支持客户端请求的操作（Operation）。 |
| `BT_BAP_ASCS_RSP_CODE_INVALID_LENGTH` | 服务器因操作长度无效（Invalid Operation Length）而拒绝。 |
| `BT_BAP_ASCS_RSP_CODE_INVALID_ASE` | 无效的音频流端点标识符（ASE ID）。 |
| `BT_BAP_ASCS_RSP_CODE_INVALID_ASE_STATE` | 无效的音频流端点状态（ASE State）。 |
| `BT_BAP_ASCS_RSP_CODE_INVALID_DIR` | 此方向上的操作无效（Invalid Operation for Direction）。 |
| `BT_BAP_ASCS_RSP_CODE_CAP_UNSUPPORTED` | 服务器不支持这些能力（Capabilities）。 |
| `BT_BAP_ASCS_RSP_CODE_CONF_UNSUPPORTED` | 服务器不支持这些配置参数（Configuration Parameters）。 |
| `BT_BAP_ASCS_RSP_CODE_CONF_REJECTED` | 服务器拒绝了配置参数（Configuration Parameters）。 |
| `BT_BAP_ASCS_RSP_CODE_CONF_INVALID` | 无效的配置参数（Configuration Parameters）。 |
| `BT_BAP_ASCS_RSP_CODE_METADATA_UNSUPPORTED` | 不支持的元数据（Metadata）。 |
| `BT_BAP_ASCS_RSP_CODE_METADATA_REJECTED` | 服务器拒绝了元数据（Metadata）。 |
| `BT_BAP_ASCS_RSP_CODE_METADATA_INVALID` | 无效的元数据（Metadata）。 |
| `BT_BAP_ASCS_RSP_CODE_NO_MEM` | 服务器资源不足（Insufficient Resources）。 |
| `BT_BAP_ASCS_RSP_CODE_UNSPECIFIED` | 未指定的错误（Unspecified Error）。 |

<a id="ga04eddf75bc1f2deafee5d6b234dd5b07"></a>

### `bt_ascs_register()`

```c
int bt_ascs_register ( const struct bt_ascs_register_param * param)
```

```c
#include <zephyr/bluetooth/audio/ascs.h>
```

注册音频流控制服务（Audio Stream Control Service，ASCS）。

初始化此服务并在 GATT 数据库中公开它，同时公开所指定数量的接收端（Sink）和源端（Source）ASE 特征（Characteristics）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 服务参数（Service Parameters）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | param 为 NULL 或包含无效值，或 bt_gatt_service_register() 失败。 |
| `-EALREADY` | ASCS 已注册（Already Registered）。 |
| `-EADDRINUSE` | 等时传输服务器（ISO Server）已通过 bt_iso_server_register() 注册。 |
| `-ENOTSUP` | 控制器不支持等时传输（ISO）。 |

<a id="ga2a87430dd2b2a04985c2faffb0b033a3"></a>

### `bt_ascs_unregister()`

```c
int bt_ascs_unregister ( void )
```

```c
#include <zephyr/bluetooth/audio/ascs.h>
```

注销音频流控制服务（ASCS）。

释放所有流（Streams），并从 GATT 数据库移除此服务。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOENT` | bt_gatt_service_unregister() 注销服务失败时。 |
| `-EALREADY` | ASCS 已注销（Already Unregistered）。 |


## 2.6\_原页交叉引用（Cross References）

- [bt_bap_ascs_rsp](../bluetooth_le_audio_model_reference/P010_bt_bap_ascs_rsp_结构体.md)
- [bt_bap_qos_cfg_pref](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md)
- [bt_ascs_cb](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md)
- [bt_ascs_register_param](../bluetooth_le_audio_model_reference/P006_bt_ascs_register_param_结构体.md)
- [zephyr/bluetooth/audio/ascs.h](../api_file_management_reference/P001_zephyr__bluetooth__audio__ascs.h_文件参考.md)
- [bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)
- [bt_gatt_service_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gab4d9cfea04e44445d5dc30ad52842b64)
- [bt_iso_server_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaff0e52777b2140519c63b54b9618bca8)
- [bt_gatt_service_unregister()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaf5bf0205fad5f7ad187b764d23deba6b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astructbt__bap__ascs__rsp_html"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd"></a>
<a id="gga9ca1630544a336b15af8a8e8934c5a45a8923f9c27858f27fd3799367cf525aea"></a>
<a id="gga9ca1630544a336b15af8a8e8934c5a45a69c9d998626ccb2a6963dd2dfd68cbb0"></a>
<a id="gga9ca1630544a336b15af8a8e8934c5a45ae297b097cc8fbb5f161c0d8c44c6623c"></a>
<a id="gga9ca1630544a336b15af8a8e8934c5a45a458cd637ba37015e2598990f9f248539"></a>
<a id="gga9ca1630544a336b15af8a8e8934c5a45a8eda92a6782649f2a42f0021095a54a8"></a>
<a id="gga9ca1630544a336b15af8a8e8934c5a45a731ac5962c8a8685c3f40884c1b67d0b"></a>
<a id="gga9ca1630544a336b15af8a8e8934c5a45acc839aadf0d60ce8eb086271397b94cf"></a>
<a id="gga9ca1630544a336b15af8a8e8934c5a45a904156d246f97189820c9de93fb90942"></a>
<a id="gga9ca1630544a336b15af8a8e8934c5a45a1fdcf3a40ed30b7aa63e1df573a2d557"></a>
<a id="gga9ca1630544a336b15af8a8e8934c5a45a93bc6ab73f6088bceea03c6f8e71854c"></a>
<a id="gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd"></a>
<a id="gga9f7efa749c75edd32dc50503397ab9d1a54515d30244888af19711f153b942d2d"></a>
<a id="gga9f7efa749c75edd32dc50503397ab9d1ad43b45076cbb1ec36af8a4e5126d4bb9"></a>
<a id="gga9f7efa749c75edd32dc50503397ab9d1a635bf6ad106e80e4e64ce3153fd668aa"></a>
<a id="gga9f7efa749c75edd32dc50503397ab9d1a11bc72f67d626889c24cd54f412730b5"></a>
<a id="gga9f7efa749c75edd32dc50503397ab9d1a64417c64d67fa73fa8430b6f4255e146"></a>
<a id="gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a"></a>
<a id="gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62"></a>
<a id="gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21"></a>
<a id="gga9f7efa749c75edd32dc50503397ab9d1a7f2a361b595dad7bc0e7f354bf6a1219"></a>
<a id="gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7"></a>
<a id="gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06"></a>
<a id="gga9f7efa749c75edd32dc50503397ab9d1a3ef9532dbd19abc90a89305d67f82e06"></a>
<a id="gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb"></a>
<a id="gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_辅助文本显示器（Auxiliary Text Display）.md) · [返回大纲](大纲.md) · [下一章](P003_CCP 呼叫控制服务器 API.md)
