---
id: learning.zephyr-docs.api-file-audio-test-reference.page-1
title: zephyr__bluetooth__audio__aics.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/aics_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_bluetooth\_\_audio\_\_aics.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/aics_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙音频输入控制服务（Audio Input Control Service）的API。

<a id="details"></a>

```c
#include <stdint.h>
#include <stdbool.h>
#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/bluetooth.h>
```

查看此文件的源码。

蓝牙音频输入控制服务（Audio Input Control Service）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_bt_5Faics_5Fregister_5Fparam"></a>

```c
struct bt_aics_register_param
```

相关声明：[bt_aics_register_param](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md)。

用于初始化音频输入控制服务（AICS）实例的结构体。

<a id="r_bt_5Faics_5Fdiscover_5Fparam"></a>

```c
struct bt_aics_discover_param
```

相关声明：[bt_aics_discover_param](../bluetooth_le_audio_model_reference/P003_bt_aics_discover_param_结构体.md)。

用于发现音频输入控制服务（AICS）实例的结构体。

<a id="r_bt_5Faics_5Fcb"></a>

```c
struct bt_aics_cb
```

相关声明：[bt_aics_cb](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md)。

保存音频输入控制服务（AICS）回调的结构体。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="define-members-0"></a>

### 音频输入控制服务静音状态（Audio Input Control Service Mute States）

<a id="r_ga47436e2df23067ce86dc761d77ed14b7"></a>

```c
#define BT_AICS_STATE_UNMUTED 0x00U
```

相关声明：[BT_AICS_STATE_UNMUTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga47436e2df23067ce86dc761d77ed14b7)。

静音状态（Mute State）为未静音（Unmuted）。

<a id="r_ga1572eaaffea5412b496eb714d64aa981"></a>

```c
#define BT_AICS_STATE_MUTED 0x01U
```

相关声明：[BT_AICS_STATE_MUTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga1572eaaffea5412b496eb714d64aa981)。

静音状态（Mute State）为已静音（Muted）。

<a id="r_gad0063d0e0b622b4093607e5485897214"></a>

```c
#define BT_AICS_STATE_MUTE_DISABLED 0x02U
```

相关声明：[BT_AICS_STATE_MUTE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gad0063d0e0b622b4093607e5485897214)。

静音状态（Mute State）为已禁用（Disabled）。

<a id="define-members-1"></a>

### 音频输入控制服务输入模式（Audio Input Control Service Input Modes）

<a id="r_gaecb9365a5e390111311d1b415a2cee79"></a>

```c
#define BT_AICS_MODE_MANUAL_ONLY 0x00U
```

相关声明：[BT_AICS_MODE_MANUAL_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gaecb9365a5e390111311d1b415a2cee79)。

增益模式（Gain Mode）仅支持手动，不能改为自动。

<a id="r_ga6b536bdcab602ccaccfafe3b37258890"></a>

```c
#define BT_AICS_MODE_AUTO_ONLY 0x01U
```

相关声明：[BT_AICS_MODE_AUTO_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga6b536bdcab602ccaccfafe3b37258890)。

增益模式（Gain Mode）仅支持自动，不能改为手动。

<a id="r_ga7cf0508dd7407ec3bb92dec71cc00816"></a>

```c
#define BT_AICS_MODE_MANUAL 0x02U
```

相关声明：[BT_AICS_MODE_MANUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga7cf0508dd7407ec3bb92dec71cc00816)。

增益模式（Gain Mode）为手动（Manual）。

<a id="r_ga0ac3a583dd7ca58a0d356d9f60797517"></a>

```c
#define BT_AICS_MODE_AUTO 0x03U
```

相关声明：[BT_AICS_MODE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga0ac3a583dd7ca58a0d356d9f60797517)。

增益模式（Gain Mode）为自动（Automatic）。

<a id="define-members-2"></a>

### 音频输入控制服务输入类型（Audio Input Control Service Input Types）

<a id="r_ga2204f35b5f1aa41c27f62b8f0dcf74b6"></a>

```c
#define BT_AICS_INPUT_TYPE_UNSPECIFIED 0x00U
```

相关声明：[BT_AICS_INPUT_TYPE_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga2204f35b5f1aa41c27f62b8f0dcf74b6)。

输入（Input）未指定。

<a id="r_gac8ebf643f9a4101ea8da18827577bf5d"></a>

```c
#define BT_AICS_INPUT_TYPE_BLUETOOTH 0x01U
```

相关声明：[BT_AICS_INPUT_TYPE_BLUETOOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gac8ebf643f9a4101ea8da18827577bf5d)。

输入为蓝牙音频流（Bluetooth Audio Stream）。

<a id="r_ga7fcb5aefacb641a8ef7db4e9a554a65d"></a>

```c
#define BT_AICS_INPUT_TYPE_MICROPHONE 0x02U
```

相关声明：[BT_AICS_INPUT_TYPE_MICROPHONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga7fcb5aefacb641a8ef7db4e9a554a65d)。

输入为麦克风（Microphone）。

<a id="r_ga525b361d1d555f20d292cf1aded0d046"></a>

```c
#define BT_AICS_INPUT_TYPE_ANALOG 0x03U
```

相关声明：[BT_AICS_INPUT_TYPE_ANALOG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga525b361d1d555f20d292cf1aded0d046)。

输入为模拟信号（Analog）。

<a id="r_ga688605eb9eb5b27ca62fac9b85fde472"></a>

```c
#define BT_AICS_INPUT_TYPE_DIGITAL 0x04U
```

相关声明：[BT_AICS_INPUT_TYPE_DIGITAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga688605eb9eb5b27ca62fac9b85fde472)。

输入为数字信号（Digital）。

<a id="r_ga3b878b41ab30067bceefc0cd72340376"></a>

```c
#define BT_AICS_INPUT_TYPE_RADIO 0x05U
```

相关声明：[BT_AICS_INPUT_TYPE_RADIO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga3b878b41ab30067bceefc0cd72340376)。

输入为无线电广播（Radio），例如 AM/FM/XM 等。

<a id="r_ga43a02e2025e3cb3e10bc2ee2128ee877"></a>

```c
#define BT_AICS_INPUT_TYPE_STREAMING 0x06U
```

相关声明：[BT_AICS_INPUT_TYPE_STREAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga43a02e2025e3cb3e10bc2ee2128ee877)。

输入为流式音频源（Streaming Audio Source）。

<a id="r_gaacf259f2bc3d341c8d2857de5d412219"></a>

```c
#define BT_AICS_INPUT_TYPE_AMBIENT 0x07U
```

相关声明：[BT_AICS_INPUT_TYPE_AMBIENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gaacf259f2bc3d341c8d2857de5d412219)。

输入采用透明／透传方式（Transparent/Pass-through）。

<a id="define-members-3"></a>

### 音频输入控制服务错误码（Audio Input Control Service Error Codes）

<a id="r_gae54199f78ff7d7380353f3950bd03a39"></a>

```c
#define BT_AICS_ERR_INVALID_COUNTER 0x80U
```

相关声明：[BT_AICS_ERR_INVALID_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gae54199f78ff7d7380353f3950bd03a39)。

Change_Counter 操作数值与音频输入状态特征（Audio Input State Characteristic）的 Change_Counter 字段值不匹配。

<a id="r_ga00c0942dab2bf25c680278927aa49af8"></a>

```c
#define BT_AICS_ERR_OP_NOT_SUPPORTED 0x81U
```

相关声明：[BT_AICS_ERR_OP_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga00c0942dab2bf25c680278927aa49af8)。

控制点过程（Control Point Procedure）使用了无效操作码（Opcode）。

<a id="r_ga1efb1f6a4c24c2a20fc7136928abac6b"></a>

```c
#define BT_AICS_ERR_MUTE_DISABLED 0x82U
```

相关声明：[BT_AICS_ERR_MUTE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga1efb1f6a4c24c2a20fc7136928abac6b)。

静音／取消静音命令（Mute/Unmute Commands）已禁用。

<a id="r_ga2f3806b8056ea8ed43b2a7cd52ffa4f3"></a>

```c
#define BT_AICS_ERR_OUT_OF_RANGE 0x83U
```

相关声明：[BT_AICS_ERR_OUT_OF_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga2f3806b8056ea8ed43b2a7cd52ffa4f3)。

控制点过程（Control Point Procedure）使用的操作数（Operand）值超出允许范围。

<a id="r_ga6673570f7679322bfa4719bf6e41e299"></a>

```c
#define BT_AICS_ERR_GAIN_MODE_NOT_ALLOWED 0x84U
```

相关声明：[BT_AICS_ERR_GAIN_MODE_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga6673570f7679322bfa4719bf6e41e299)。

不允许所请求的增益模式变更（Gain Mode Change）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_ga36991fe1dee5168db618518d094d80ef"></a>

```c
typedef void(* bt_aics_write_cb) (struct bt_aics *inst, int err)
```

相关声明：[bt_aics_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga36991fe1dee5168db618518d094d80ef)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

写入操作的回调函数（Callback Function）。

<a id="r_ga2e851f49f9c7e71a18376468a13fdf4f"></a>

```c
typedef void(* bt_aics_state_cb) (struct bt_aics *inst, int err, int8_t gain, uint8_t mute, uint8_t mode)
```

相关声明：[bt_aics_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga2e851f49f9c7e71a18376468a13fdf4f)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

输入状态（Input State）的回调函数。

<a id="r_ga11da08c010f4aa849c2e3725dc5cbaeb"></a>

```c
typedef void(* bt_aics_gain_setting_cb) (struct bt_aics *inst, int err, uint8_t units, int8_t minimum, int8_t maximum)
```

相关声明：[bt_aics_gain_setting_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga11da08c010f4aa849c2e3725dc5cbaeb)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

增益设置（Gain Settings）的回调函数。

<a id="r_ga6e76b9f2de4cdbcd7539c76f6a347fa5"></a>

```c
typedef void(* bt_aics_type_cb) (struct bt_aics *inst, int err, uint8_t type)
```

相关声明：[bt_aics_type_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga6e76b9f2de4cdbcd7539c76f6a347fa5)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

输入类型（Input Type）的回调函数。

<a id="r_ga044d92a4273c6537a9cdf20922352ed6"></a>

```c
typedef void(* bt_aics_status_cb) (struct bt_aics *inst, int err, bool active)
```

相关声明：[bt_aics_status_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga044d92a4273c6537a9cdf20922352ed6)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

输入状态（Input Status）的回调函数。

<a id="r_ga98b142ea7a66de5577c44aa90d507930"></a>

```c
typedef void(* bt_aics_description_cb) (struct bt_aics *inst, int err, char *description)
```

相关声明：[bt_aics_description_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga98b142ea7a66de5577c44aa90d507930)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

用于描述（Description）的回调函数。

<a id="r_ga9fda39f8410308e05eb928eeb7267e83"></a>

```c
typedef void(* bt_aics_discover_cb) (struct bt_aics *inst, int err)
```

相关声明：[bt_aics_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga9fda39f8410308e05eb928eeb7267e83)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

bt_aics_discover 的回调函数（Callback Function）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.4\_函数（Functions）

<a id="r_ga4d511e81dd0f0a72fd502bc05dd85e91"></a>

```c
static const char * bt_aics_mode_to_str (uint8_t mode)
```

相关声明：[bt_aics_mode_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga4d511e81dd0f0a72fd502bc05dd85e91)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将音频输入控制服务（AICS）的增益模式（Gain Mode）转换为便于阅读的字符串。

<a id="r_gab10ad3599f5b602cdf5504bc92508109"></a>

```c
struct bt_aics * bt_aics_free_instance_get (void)
```

相关声明：[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[bt_aics_free_instance_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gab10ad3599f5b602cdf5504bc92508109)。

从池中获取一个空闲的音频输入控制服务（Audio Input Control Service）实例。

<a id="r_ga8b415343e7ecf399ecfd0dcaa49bd1ee"></a>

```c
void * bt_aics_svc_decl_get (struct bt_aics *aics)
```

相关声明：[bt_aics_svc_decl_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga8b415343e7ecf399ecfd0dcaa49bd1ee)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

获取服务声明属性（Service Declaration Attribute）。

<a id="r_ga0e088e26cf73f1f3b918660d4acdebb9"></a>

```c
int bt_aics_client_conn_get (const struct bt_aics *aics, struct bt_conn **conn)
```

相关声明：[bt_aics_client_conn_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga0e088e26cf73f1f3b918660d4acdebb9)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取客户端实例的连接指针（Connection Pointer）。

<a id="r_ga008ef5cebfcb9b4a3084f411fa81238e"></a>

```c
int bt_aics_register (struct bt_aics *aics, struct bt_aics_register_param *param)
```

相关声明：[bt_aics_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga008ef5cebfcb9b4a3084f411fa81238e)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[bt_aics_register_param](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md)。

初始化音频输入控制服务（Audio Input Control Service）实例。

<a id="r_gad16d296462af2f61a893bda8d25cc9de"></a>

```c
int bt_aics_discover (struct bt_conn *conn, struct bt_aics *inst, const struct bt_aics_discover_param *param)
```

相关声明：[bt_aics_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gad16d296462af2f61a893bda8d25cc9de)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[bt_aics_discover_param](../bluetooth_le_audio_model_reference/P003_bt_aics_discover_param_结构体.md)。

发现音频输入控制服务（Audio Input Control Service）。

<a id="r_ga4be4c4e3c74aa55fbf599157aa1c2098"></a>

```c
int bt_aics_deactivate (struct bt_aics *inst)
```

相关声明：[bt_aics_deactivate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga4be4c4e3c74aa55fbf599157aa1c2098)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

停用音频输入控制服务（Audio Input Control Service）实例。

<a id="r_gac46268949fa7cbbb827d149a3a904daa"></a>

```c
int bt_aics_activate (struct bt_aics *inst)
```

相关声明：[bt_aics_activate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gac46268949fa7cbbb827d149a3a904daa)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

激活音频输入控制服务（Audio Input Control Service）实例。

<a id="r_ga23bbc1393d21fe38f501813935b25b3d"></a>

```c
int bt_aics_state_get (struct bt_aics *inst)
```

相关声明：[bt_aics_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga23bbc1393d21fe38f501813935b25b3d)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

读取音频输入控制服务（Audio Input Control Service）的输入状态（Input State）。

<a id="r_ga38d7131397d7762d3bd53e152a6c6130"></a>

```c
int bt_aics_gain_setting_get (struct bt_aics *inst)
```

相关声明：[bt_aics_gain_setting_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga38d7131397d7762d3bd53e152a6c6130)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

读取音频输入控制服务（Audio Input Control Service）的增益设置（Gain Settings）。

<a id="r_gaf57896e2096a5e96ec46a56cdf216159"></a>

```c
int bt_aics_type_get (struct bt_aics *inst)
```

相关声明：[bt_aics_type_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gaf57896e2096a5e96ec46a56cdf216159)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

读取音频输入控制服务（Audio Input Control Service）的输入类型（Input Type）。

<a id="r_gade387c52d201ce10b39ef52157dae83d"></a>

```c
int bt_aics_status_get (struct bt_aics *inst)
```

相关声明：[bt_aics_status_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gade387c52d201ce10b39ef52157dae83d)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

读取音频输入控制服务（Audio Input Control Service）的输入状态（Input Status）。

<a id="r_ga5a1ad98afe45da9ffbb7247671385d40"></a>

```c
int bt_aics_disable_mute (struct bt_aics *inst)
```

相关声明：[bt_aics_disable_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga5a1ad98afe45da9ffbb7247671385d40)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

禁用音频输入控制服务（Audio Input Control Service）的静音功能（Mute）。

<a id="r_ga43396d2d4b3bd9cdd0c82275fafeadfc"></a>

```c
int bt_aics_unmute (struct bt_aics *inst)
```

相关声明：[bt_aics_unmute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga43396d2d4b3bd9cdd0c82275fafeadfc)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

取消音频输入控制服务（Audio Input Control Service）输入的静音（Unmute）。

<a id="r_ga5345254eaf099560e609d97044b39a97"></a>

```c
int bt_aics_mute (struct bt_aics *inst)
```

相关声明：[bt_aics_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga5345254eaf099560e609d97044b39a97)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

将音频输入控制服务（Audio Input Control Service）的输入静音（Mute）。

<a id="r_ga0460e82d4277a2c4b14964799ad5f2b0"></a>

```c
int bt_aics_gain_set_manual_only (struct bt_aics *inst)
```

相关声明：[bt_aics_gain_set_manual_only](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga0460e82d4277a2c4b14964799ad5f2b0)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

在音频输入控制服务（Audio Input Control Service）中设置仅手动增益模式（Manual-only Gain Mode）。

<a id="r_ga22869d8a62eb59bc4aad25946da8f9cf"></a>

```c
int bt_aics_gain_set_auto_only (struct bt_aics *inst)
```

相关声明：[bt_aics_gain_set_auto_only](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga22869d8a62eb59bc4aad25946da8f9cf)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

在音频输入控制服务（Audio Input Control Service）中设置仅自动增益模式（Automatic-only Gain Mode）。

<a id="r_ga7ddb93125f6275fc7c99fbf448e24f0c"></a>

```c
int bt_aics_manual_gain_set (struct bt_aics *inst)
```

相关声明：[bt_aics_manual_gain_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga7ddb93125f6275fc7c99fbf448e24f0c)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

将输入增益（Input Gain）设为手动。

<a id="r_ga759712886cd3c4c025ea360dcb663c59"></a>

```c
int bt_aics_automatic_gain_set (struct bt_aics *inst)
```

相关声明：[bt_aics_automatic_gain_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga759712886cd3c4c025ea360dcb663c59)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

将输入增益（Input Gain）设为自动。

<a id="r_ga20f3a178788ec6aef593034159793b94"></a>

```c
int bt_aics_gain_set (struct bt_aics *inst, int8_t gain)
```

相关声明：[bt_aics_gain_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga20f3a178788ec6aef593034159793b94)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

设置输入增益（Input Gain）。

<a id="r_gaf0b659698aa6a6a79143d4f591f67e09"></a>

```c
int bt_aics_description_get (struct bt_aics *inst)
```

相关声明：[bt_aics_description_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gaf0b659698aa6a6a79143d4f591f67e09)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

读取音频输入控制服务（Audio Input Control Service）的描述（Description）。

<a id="r_ga7de5ffd2eb61ca562b9773b37470ebd9"></a>

```c
int bt_aics_description_set (struct bt_aics *inst, const char *description)
```

相关声明：[bt_aics_description_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga7de5ffd2eb61ca562b9773b37470ebd9)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

设置音频输入控制服务（Audio Input Control Service）的描述（Description）。

<a id="r_ga913838aa0d5bff239c2faef4d8a8b36b"></a>

```c
struct bt_aics * bt_aics_client_free_instance_get (void)
```

相关声明：[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[bt_aics_client_free_instance_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga913838aa0d5bff239c2faef4d8a8b36b)。

获取新的音频输入控制服务（Audio Input Control Service）客户端实例。

<a id="r_gab660d2d4603de3837a3b93ce11e4d0fd"></a>

```c
int bt_aics_client_free_instance (struct bt_aics *inst)
```

相关声明：[bt_aics_client_free_instance](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gab660d2d4603de3837a3b93ce11e4d0fd)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

释放从 bt_aics_client_free_instance_get() 获得的实例（Instance）。

<a id="r_gabd6bdcdad0dd5a4c509f9e7cabb3e601"></a>

```c
void bt_aics_client_cb_register (struct bt_aics *inst, struct bt_aics_cb *cb)
```

相关声明：[bt_aics_client_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gabd6bdcdad0dd5a4c509f9e7cabb3e601)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[bt_aics_cb](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md)。

注册音频输入控制服务（Audio Input Control Service）客户端的回调。


## 1.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P018_aics.h_源码浏览.md)
- [bt_aics_register_param](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md)
- [bt_aics_discover_param](../bluetooth_le_audio_model_reference/P003_bt_aics_discover_param_结构体.md)
- [bt_aics_cb](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md)
- [BT_AICS_STATE_UNMUTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga47436e2df23067ce86dc761d77ed14b7)
- [BT_AICS_STATE_MUTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga1572eaaffea5412b496eb714d64aa981)
- [BT_AICS_STATE_MUTE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gad0063d0e0b622b4093607e5485897214)
- [BT_AICS_MODE_MANUAL_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gaecb9365a5e390111311d1b415a2cee79)
- [BT_AICS_MODE_AUTO_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga6b536bdcab602ccaccfafe3b37258890)
- [BT_AICS_MODE_MANUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga7cf0508dd7407ec3bb92dec71cc00816)
- [BT_AICS_MODE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga0ac3a583dd7ca58a0d356d9f60797517)
- [BT_AICS_INPUT_TYPE_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga2204f35b5f1aa41c27f62b8f0dcf74b6)
- [BT_AICS_INPUT_TYPE_BLUETOOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gac8ebf643f9a4101ea8da18827577bf5d)
- [BT_AICS_INPUT_TYPE_MICROPHONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga7fcb5aefacb641a8ef7db4e9a554a65d)
- [BT_AICS_INPUT_TYPE_ANALOG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga525b361d1d555f20d292cf1aded0d046)
- [BT_AICS_INPUT_TYPE_DIGITAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga688605eb9eb5b27ca62fac9b85fde472)
- [BT_AICS_INPUT_TYPE_RADIO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga3b878b41ab30067bceefc0cd72340376)
- [BT_AICS_INPUT_TYPE_STREAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga43a02e2025e3cb3e10bc2ee2128ee877)
- [BT_AICS_INPUT_TYPE_AMBIENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gaacf259f2bc3d341c8d2857de5d412219)
- [BT_AICS_ERR_INVALID_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gae54199f78ff7d7380353f3950bd03a39)
- [BT_AICS_ERR_OP_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga00c0942dab2bf25c680278927aa49af8)
- [BT_AICS_ERR_MUTE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga1efb1f6a4c24c2a20fc7136928abac6b)
- [BT_AICS_ERR_OUT_OF_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga2f3806b8056ea8ed43b2a7cd52ffa4f3)
- [BT_AICS_ERR_GAIN_MODE_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga6673570f7679322bfa4719bf6e41e299)
- [bt_aics_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga36991fe1dee5168db618518d094d80ef)
- [bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)
- [bt_aics_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga2e851f49f9c7e71a18376468a13fdf4f)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_aics_gain_setting_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga11da08c010f4aa849c2e3725dc5cbaeb)
- [bt_aics_type_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga6e76b9f2de4cdbcd7539c76f6a347fa5)
- [bt_aics_status_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga044d92a4273c6537a9cdf20922352ed6)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_aics_description_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga98b142ea7a66de5577c44aa90d507930)
- [bt_aics_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga9fda39f8410308e05eb928eeb7267e83)
- [bt_aics_mode_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga4d511e81dd0f0a72fd502bc05dd85e91)
- [bt_aics_free_instance_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gab10ad3599f5b602cdf5504bc92508109)
- [bt_aics_svc_decl_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga8b415343e7ecf399ecfd0dcaa49bd1ee)
- [bt_aics_client_conn_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga0e088e26cf73f1f3b918660d4acdebb9)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_aics_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga008ef5cebfcb9b4a3084f411fa81238e)
- [bt_aics_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gad16d296462af2f61a893bda8d25cc9de)
- [bt_aics_deactivate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga4be4c4e3c74aa55fbf599157aa1c2098)
- [bt_aics_activate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gac46268949fa7cbbb827d149a3a904daa)
- [bt_aics_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga23bbc1393d21fe38f501813935b25b3d)
- [bt_aics_gain_setting_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga38d7131397d7762d3bd53e152a6c6130)
- [bt_aics_type_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gaf57896e2096a5e96ec46a56cdf216159)
- [bt_aics_status_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gade387c52d201ce10b39ef52157dae83d)
- [bt_aics_disable_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga5a1ad98afe45da9ffbb7247671385d40)
- [bt_aics_unmute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga43396d2d4b3bd9cdd0c82275fafeadfc)
- [bt_aics_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga5345254eaf099560e609d97044b39a97)
- [bt_aics_gain_set_manual_only](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga0460e82d4277a2c4b14964799ad5f2b0)
- [bt_aics_gain_set_auto_only](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga22869d8a62eb59bc4aad25946da8f9cf)
- [bt_aics_manual_gain_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga7ddb93125f6275fc7c99fbf448e24f0c)
- [bt_aics_automatic_gain_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga759712886cd3c4c025ea360dcb663c59)
- [bt_aics_gain_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga20f3a178788ec6aef593034159793b94)
- [bt_aics_description_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gaf0b659698aa6a6a79143d4f591f67e09)
- [bt_aics_description_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga7de5ffd2eb61ca562b9773b37470ebd9)
- [bt_aics_client_free_instance_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga913838aa0d5bff239c2faef4d8a8b36b)
- [bt_aics_client_free_instance](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gab660d2d4603de3837a3b93ce11e4d0fd)
- [bt_aics_client_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gabd6bdcdad0dd5a4c509f9e7cabb3e601)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__dt-bindings__dma__ameba_dma.h_文件参考.md)
