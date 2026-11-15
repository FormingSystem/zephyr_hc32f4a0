---
id: learning.zephyr-docs.api-file-management-reference.page-1
title: zephyr__bluetooth__audio__ascs.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ascs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_bluetooth\_\_audio\_\_ascs.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ascs_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙音频流控制服务（Audio Stream Control Service，ASCS）的API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/audio/audio.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

蓝牙音频流控制服务（Audio Stream Control Service，ASCS）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

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

## 1.2\_宏定义（Macros）

<a id="r_ga8e5cd46a1428a315119e47c9cbbb9bfd"></a>

```c
#define BT_BAP_ASCS_RSP(c, r)
```

相关声明：[BT_BAP_ASCS_RSP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga8e5cd46a1428a315119e47c9cbbb9bfd)。

用于初始化保存音频流端点控制点（ASE Control Point）通知值的对象的宏。

<a id="r_ga7a3fc7cb21be45276cf50846c076101d"></a>

```c
#define BT_BAP_QOS_CFG_PREF(_unframed_supported, _phy, _rtn, _latency, _pd_min, _pd_max, _pref_pd_min, _pref_pd_max)
```

相关声明：[BT_BAP_QOS_CFG_PREF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga7a3fc7cb21be45276cf50846c076101d)。

用于声明 `bt_bap_qos_cfg_pref` 成员的辅助宏。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.3\_枚举（Enumerations）

<a id="r_ga9f7efa749c75edd32dc50503397ab9d1"></a>

```c
enum bt_bap_ascs_rsp_code { BT_BAP_ASCS_RSP_CODE_SUCCESS = 0x00U , BT_BAP_ASCS_RSP_CODE_NOT_SUPPORTED = 0x01U , BT_BAP_ASCS_RSP_CODE_INVALID_LENGTH = 0x02U , BT_BAP_ASCS_RSP_CODE_INVALID_ASE = 0x03U , BT_BAP_ASCS_RSP_CODE_INVALID_ASE_STATE = 0x04U , BT_BAP_ASCS_RSP_CODE_INVALID_DIR = 0x05U , BT_BAP_ASCS_RSP_CODE_CAP_UNSUPPORTED = 0x06U , BT_BAP_ASCS_RSP_CODE_CONF_UNSUPPORTED = 0x07U , BT_BAP_ASCS_RSP_CODE_CONF_REJECTED = 0x08U , BT_BAP_ASCS_RSP_CODE_CONF_INVALID = 0x09U , BT_BAP_ASCS_RSP_CODE_METADATA_UNSUPPORTED = 0x0AU , BT_BAP_ASCS_RSP_CODE_METADATA_REJECTED = 0x0BU , BT_BAP_ASCS_RSP_CODE_METADATA_INVALID = 0x0CU , BT_BAP_ASCS_RSP_CODE_NO_MEM = 0x0DU , BT_BAP_ASCS_RSP_CODE_UNSPECIFIED = 0x0EU }
```

相关声明：[bt_bap_ascs_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9f7efa749c75edd32dc50503397ab9d1)、[BT_BAP_ASCS_RSP_CODE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd)、[BT_BAP_ASCS_RSP_CODE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a54515d30244888af19711f153b942d2d)、[BT_BAP_ASCS_RSP_CODE_INVALID_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1ad43b45076cbb1ec36af8a4e5126d4bb9)、[BT_BAP_ASCS_RSP_CODE_INVALID_ASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a635bf6ad106e80e4e64ce3153fd668aa)、[BT_BAP_ASCS_RSP_CODE_INVALID_ASE_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a11bc72f67d626889c24cd54f412730b5)、[BT_BAP_ASCS_RSP_CODE_INVALID_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a64417c64d67fa73fa8430b6f4255e146)、[BT_BAP_ASCS_RSP_CODE_CAP_UNSUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a)、[BT_BAP_ASCS_RSP_CODE_CONF_UNSUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62)、[BT_BAP_ASCS_RSP_CODE_CONF_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21)、[BT_BAP_ASCS_RSP_CODE_CONF_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a7f2a361b595dad7bc0e7f354bf6a1219)、[BT_BAP_ASCS_RSP_CODE_METADATA_UNSUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7)、[BT_BAP_ASCS_RSP_CODE_METADATA_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06)、[BT_BAP_ASCS_RSP_CODE_METADATA_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a3ef9532dbd19abc90a89305d67f82e06)、[BT_BAP_ASCS_RSP_CODE_NO_MEM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb)、[BT_BAP_ASCS_RSP_CODE_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a)。

响应状态码（Response Status Code）。

<a id="r_ga9ca1630544a336b15af8a8e8934c5a45"></a>

```c
enum bt_bap_ascs_reason { BT_BAP_ASCS_REASON_NONE = 0x00U , BT_BAP_ASCS_REASON_CODEC = 0x01U , BT_BAP_ASCS_REASON_CODEC_DATA = 0x02U , BT_BAP_ASCS_REASON_INTERVAL = 0x03U , BT_BAP_ASCS_REASON_FRAMING = 0x04U , BT_BAP_ASCS_REASON_PHY = 0x05U , BT_BAP_ASCS_REASON_SDU = 0x06U , BT_BAP_ASCS_REASON_RTN = 0x07U , BT_BAP_ASCS_REASON_LATENCY = 0x08U , BT_BAP_ASCS_REASON_PD = 0x09U , BT_BAP_ASCS_REASON_CIS = 0x0AU }
```

相关声明：[bt_bap_ascs_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9ca1630544a336b15af8a8e8934c5a45)、[BT_BAP_ASCS_REASON_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd)、[BT_BAP_ASCS_REASON_CODEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a8923f9c27858f27fd3799367cf525aea)、[BT_BAP_ASCS_REASON_CODEC_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a69c9d998626ccb2a6963dd2dfd68cbb0)、[BT_BAP_ASCS_REASON_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45ae297b097cc8fbb5f161c0d8c44c6623c)、[BT_BAP_ASCS_REASON_FRAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a458cd637ba37015e2598990f9f248539)、[BT_BAP_ASCS_REASON_PHY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a8eda92a6782649f2a42f0021095a54a8)、[BT_BAP_ASCS_REASON_SDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a731ac5962c8a8685c3f40884c1b67d0b)、[BT_BAP_ASCS_REASON_RTN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45acc839aadf0d60ce8eb086271397b94cf)、[BT_BAP_ASCS_REASON_LATENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a904156d246f97189820c9de93fb90942)、[BT_BAP_ASCS_REASON_PD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a1fdcf3a40ed30b7aa63e1df573a2d557)、[BT_BAP_ASCS_REASON_CIS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a93bc6ab73f6088bceea03c6f8e71854c)。

响应原因（Response Reasons）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.4\_函数（Functions）

<a id="r_ga04eddf75bc1f2deafee5d6b234dd5b07"></a>

```c
int bt_ascs_register (const struct bt_ascs_register_param *param)
```

相关声明：[bt_ascs_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga04eddf75bc1f2deafee5d6b234dd5b07)、[bt_ascs_register_param](../bluetooth_le_audio_model_reference/P006_bt_ascs_register_param_结构体.md)。

注册音频流控制服务（Audio Stream Control Service，ASCS）。

<a id="r_ga2a87430dd2b2a04985c2faffb0b033a3"></a>

```c
int bt_ascs_unregister (void)
```

相关声明：[bt_ascs_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga2a87430dd2b2a04985c2faffb0b033a3)。

注销音频流控制服务（ASCS）。


## 1.5\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h_source.html)
- [zephyr/bluetooth/audio/audio.h](../api_source_compiler_device_reference/P002_audio.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P017_ascs.h_源码浏览.md)
- [bt_bap_ascs_rsp](../bluetooth_le_audio_model_reference/P010_bt_bap_ascs_rsp_结构体.md)
- [bt_bap_qos_cfg_pref](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md)
- [bt_ascs_cb](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md)
- [bt_ascs_register_param](../bluetooth_le_audio_model_reference/P006_bt_ascs_register_param_结构体.md)
- [BT_BAP_ASCS_RSP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga8e5cd46a1428a315119e47c9cbbb9bfd)
- [BT_BAP_QOS_CFG_PREF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga7a3fc7cb21be45276cf50846c076101d)
- [bt_bap_ascs_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9f7efa749c75edd32dc50503397ab9d1)
- [BT_BAP_ASCS_RSP_CODE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd)
- [BT_BAP_ASCS_RSP_CODE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a54515d30244888af19711f153b942d2d)
- [BT_BAP_ASCS_RSP_CODE_INVALID_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1ad43b45076cbb1ec36af8a4e5126d4bb9)
- [BT_BAP_ASCS_RSP_CODE_INVALID_ASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a635bf6ad106e80e4e64ce3153fd668aa)
- [BT_BAP_ASCS_RSP_CODE_INVALID_ASE_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a11bc72f67d626889c24cd54f412730b5)
- [BT_BAP_ASCS_RSP_CODE_INVALID_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a64417c64d67fa73fa8430b6f4255e146)
- [BT_BAP_ASCS_RSP_CODE_CAP_UNSUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a)
- [BT_BAP_ASCS_RSP_CODE_CONF_UNSUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62)
- [BT_BAP_ASCS_RSP_CODE_CONF_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21)
- [BT_BAP_ASCS_RSP_CODE_CONF_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a7f2a361b595dad7bc0e7f354bf6a1219)
- [BT_BAP_ASCS_RSP_CODE_METADATA_UNSUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7)
- [BT_BAP_ASCS_RSP_CODE_METADATA_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06)
- [BT_BAP_ASCS_RSP_CODE_METADATA_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a3ef9532dbd19abc90a89305d67f82e06)
- [BT_BAP_ASCS_RSP_CODE_NO_MEM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb)
- [BT_BAP_ASCS_RSP_CODE_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a)
- [bt_bap_ascs_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9ca1630544a336b15af8a8e8934c5a45)
- [BT_BAP_ASCS_REASON_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd)
- [BT_BAP_ASCS_REASON_CODEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a8923f9c27858f27fd3799367cf525aea)
- [BT_BAP_ASCS_REASON_CODEC_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a69c9d998626ccb2a6963dd2dfd68cbb0)
- [BT_BAP_ASCS_REASON_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45ae297b097cc8fbb5f161c0d8c44c6623c)
- [BT_BAP_ASCS_REASON_FRAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a458cd637ba37015e2598990f9f248539)
- [BT_BAP_ASCS_REASON_PHY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a8eda92a6782649f2a42f0021095a54a8)
- [BT_BAP_ASCS_REASON_SDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a731ac5962c8a8685c3f40884c1b67d0b)
- [BT_BAP_ASCS_REASON_RTN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45acc839aadf0d60ce8eb086271397b94cf)
- [BT_BAP_ASCS_REASON_LATENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a904156d246f97189820c9de93fb90942)
- [BT_BAP_ASCS_REASON_PD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a1fdcf3a40ed30b7aa63e1df573a2d557)
- [BT_BAP_ASCS_REASON_CIS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a93bc6ab73f6088bceea03c6f8e71854c)
- [bt_ascs_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga04eddf75bc1f2deafee5d6b234dd5b07)
- [bt_ascs_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga2a87430dd2b2a04985c2faffb0b033a3)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__bluetooth__mesh__blob_srv.h_文件参考.md)
