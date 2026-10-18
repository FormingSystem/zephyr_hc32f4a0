---
id: learning.zephyr-docs.api-memory-timer-topic-reference.page-1
title: 音频输入控制服务（Audio Input Control Service，AICS）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_音频输入控制服务（Audio Input Control Service，AICS）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

音频输入控制服务（Audio Input Control Service，AICS）

<a id="details"></a>

音频输入控制服务（Audio Input Control Service，AICS）。自 2.6 起提供（Since 2.6），版本（Version）0.8.0。AICS 是次级服务（Secondary Service），因此不应独立使用，而应在其他主服务（Primary Service）的上下文中使用。此 API 同时实现服务器和客户端功能。注意，API 封装了音频输入控制状态中的变更计数器（Change Counter），并自动处理其变化。如果计数器已过期，客户端实现在执行写请求时会自主读取其值。

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

<a id="r_bt_5Faics"></a>

```c
struct bt_aics
```

相关声明：[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

音频输入控制服务（Audio Input Control Service，AICS）的不透明实例（Opaque Instance）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.2\_类型定义（Typedefs）

<a id="r_ga36991fe1dee5168db618518d094d80ef"></a>

```c
typedef void(* bt_aics_write_cb) (struct bt_aics *inst, int err)
```

相关声明：[bt_aics_write_cb](#ga36991fe1dee5168db618518d094d80ef)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

写入操作的回调函数（Callback Function）。

<a id="r_ga2e851f49f9c7e71a18376468a13fdf4f"></a>

```c
typedef void(* bt_aics_state_cb) (struct bt_aics *inst, int err, int8_t gain, uint8_t mute, uint8_t mode)
```

相关声明：[bt_aics_state_cb](#ga2e851f49f9c7e71a18376468a13fdf4f)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

输入状态（Input State）的回调函数。

<a id="r_ga11da08c010f4aa849c2e3725dc5cbaeb"></a>

```c
typedef void(* bt_aics_gain_setting_cb) (struct bt_aics *inst, int err, uint8_t units, int8_t minimum, int8_t maximum)
```

相关声明：[bt_aics_gain_setting_cb](#ga11da08c010f4aa849c2e3725dc5cbaeb)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

增益设置（Gain Settings）的回调函数。

<a id="r_ga6e76b9f2de4cdbcd7539c76f6a347fa5"></a>

```c
typedef void(* bt_aics_type_cb) (struct bt_aics *inst, int err, uint8_t type)
```

相关声明：[bt_aics_type_cb](#ga6e76b9f2de4cdbcd7539c76f6a347fa5)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

输入类型（Input Type）的回调函数。

<a id="r_ga044d92a4273c6537a9cdf20922352ed6"></a>

```c
typedef void(* bt_aics_status_cb) (struct bt_aics *inst, int err, bool active)
```

相关声明：[bt_aics_status_cb](#ga044d92a4273c6537a9cdf20922352ed6)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

输入状态（Input Status）的回调函数。

<a id="r_ga98b142ea7a66de5577c44aa90d507930"></a>

```c
typedef void(* bt_aics_description_cb) (struct bt_aics *inst, int err, char *description)
```

相关声明：[bt_aics_description_cb](#ga98b142ea7a66de5577c44aa90d507930)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

用于描述（Description）的回调函数。

<a id="r_ga9fda39f8410308e05eb928eeb7267e83"></a>

```c
typedef void(* bt_aics_discover_cb) (struct bt_aics *inst, int err)
```

相关声明：[bt_aics_discover_cb](#ga9fda39f8410308e05eb928eeb7267e83)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

bt_aics_discover 的回调函数（Callback Function）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_ga4d511e81dd0f0a72fd502bc05dd85e91"></a>

```c
static const char * bt_aics_mode_to_str (uint8_t mode)
```

相关声明：[bt_aics_mode_to_str](#ga4d511e81dd0f0a72fd502bc05dd85e91)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将音频输入控制服务（AICS）的增益模式（Gain Mode）转换为便于阅读的字符串。

<a id="r_gab10ad3599f5b602cdf5504bc92508109"></a>

```c
struct bt_aics * bt_aics_free_instance_get (void)
```

相关声明：[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[bt_aics_free_instance_get](#gab10ad3599f5b602cdf5504bc92508109)。

从池中获取一个空闲的音频输入控制服务（Audio Input Control Service）实例。

<a id="r_ga8b415343e7ecf399ecfd0dcaa49bd1ee"></a>

```c
void * bt_aics_svc_decl_get (struct bt_aics *aics)
```

相关声明：[bt_aics_svc_decl_get](#ga8b415343e7ecf399ecfd0dcaa49bd1ee)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

获取服务声明属性（Service Declaration Attribute）。

<a id="r_ga0e088e26cf73f1f3b918660d4acdebb9"></a>

```c
int bt_aics_client_conn_get (const struct bt_aics *aics, struct bt_conn **conn)
```

相关声明：[bt_aics_client_conn_get](#ga0e088e26cf73f1f3b918660d4acdebb9)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取客户端实例的连接指针（Connection Pointer）。

<a id="r_ga008ef5cebfcb9b4a3084f411fa81238e"></a>

```c
int bt_aics_register (struct bt_aics *aics, struct bt_aics_register_param *param)
```

相关声明：[bt_aics_register](#ga008ef5cebfcb9b4a3084f411fa81238e)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[bt_aics_register_param](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md)。

初始化音频输入控制服务（Audio Input Control Service）实例。

<a id="r_gad16d296462af2f61a893bda8d25cc9de"></a>

```c
int bt_aics_discover (struct bt_conn *conn, struct bt_aics *inst, const struct bt_aics_discover_param *param)
```

相关声明：[bt_aics_discover](#gad16d296462af2f61a893bda8d25cc9de)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[bt_aics_discover_param](../bluetooth_le_audio_model_reference/P003_bt_aics_discover_param_结构体.md)。

发现音频输入控制服务（Audio Input Control Service）。

<a id="r_ga4be4c4e3c74aa55fbf599157aa1c2098"></a>

```c
int bt_aics_deactivate (struct bt_aics *inst)
```

相关声明：[bt_aics_deactivate](#ga4be4c4e3c74aa55fbf599157aa1c2098)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

停用音频输入控制服务（Audio Input Control Service）实例。

<a id="r_gac46268949fa7cbbb827d149a3a904daa"></a>

```c
int bt_aics_activate (struct bt_aics *inst)
```

相关声明：[bt_aics_activate](#gac46268949fa7cbbb827d149a3a904daa)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

激活音频输入控制服务（Audio Input Control Service）实例。

<a id="r_ga23bbc1393d21fe38f501813935b25b3d"></a>

```c
int bt_aics_state_get (struct bt_aics *inst)
```

相关声明：[bt_aics_state_get](#ga23bbc1393d21fe38f501813935b25b3d)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

读取音频输入控制服务（Audio Input Control Service）的输入状态（Input State）。

<a id="r_ga38d7131397d7762d3bd53e152a6c6130"></a>

```c
int bt_aics_gain_setting_get (struct bt_aics *inst)
```

相关声明：[bt_aics_gain_setting_get](#ga38d7131397d7762d3bd53e152a6c6130)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

读取音频输入控制服务（Audio Input Control Service）的增益设置（Gain Settings）。

<a id="r_gaf57896e2096a5e96ec46a56cdf216159"></a>

```c
int bt_aics_type_get (struct bt_aics *inst)
```

相关声明：[bt_aics_type_get](#gaf57896e2096a5e96ec46a56cdf216159)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

读取音频输入控制服务（Audio Input Control Service）的输入类型（Input Type）。

<a id="r_gade387c52d201ce10b39ef52157dae83d"></a>

```c
int bt_aics_status_get (struct bt_aics *inst)
```

相关声明：[bt_aics_status_get](#gade387c52d201ce10b39ef52157dae83d)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

读取音频输入控制服务（Audio Input Control Service）的输入状态（Input Status）。

<a id="r_ga5a1ad98afe45da9ffbb7247671385d40"></a>

```c
int bt_aics_disable_mute (struct bt_aics *inst)
```

相关声明：[bt_aics_disable_mute](#ga5a1ad98afe45da9ffbb7247671385d40)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

禁用音频输入控制服务（Audio Input Control Service）的静音功能（Mute）。

<a id="r_ga43396d2d4b3bd9cdd0c82275fafeadfc"></a>

```c
int bt_aics_unmute (struct bt_aics *inst)
```

相关声明：[bt_aics_unmute](#ga43396d2d4b3bd9cdd0c82275fafeadfc)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

取消音频输入控制服务（Audio Input Control Service）输入的静音（Unmute）。

<a id="r_ga5345254eaf099560e609d97044b39a97"></a>

```c
int bt_aics_mute (struct bt_aics *inst)
```

相关声明：[bt_aics_mute](#ga5345254eaf099560e609d97044b39a97)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

将音频输入控制服务（Audio Input Control Service）的输入静音（Mute）。

<a id="r_ga0460e82d4277a2c4b14964799ad5f2b0"></a>

```c
int bt_aics_gain_set_manual_only (struct bt_aics *inst)
```

相关声明：[bt_aics_gain_set_manual_only](#ga0460e82d4277a2c4b14964799ad5f2b0)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

在音频输入控制服务（Audio Input Control Service）中设置仅手动增益模式（Manual-only Gain Mode）。

<a id="r_ga22869d8a62eb59bc4aad25946da8f9cf"></a>

```c
int bt_aics_gain_set_auto_only (struct bt_aics *inst)
```

相关声明：[bt_aics_gain_set_auto_only](#ga22869d8a62eb59bc4aad25946da8f9cf)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

在音频输入控制服务（Audio Input Control Service）中设置仅自动增益模式（Automatic-only Gain Mode）。

<a id="r_ga7ddb93125f6275fc7c99fbf448e24f0c"></a>

```c
int bt_aics_manual_gain_set (struct bt_aics *inst)
```

相关声明：[bt_aics_manual_gain_set](#ga7ddb93125f6275fc7c99fbf448e24f0c)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

将输入增益（Input Gain）设为手动。

<a id="r_ga759712886cd3c4c025ea360dcb663c59"></a>

```c
int bt_aics_automatic_gain_set (struct bt_aics *inst)
```

相关声明：[bt_aics_automatic_gain_set](#ga759712886cd3c4c025ea360dcb663c59)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

将输入增益（Input Gain）设为自动。

<a id="r_ga20f3a178788ec6aef593034159793b94"></a>

```c
int bt_aics_gain_set (struct bt_aics *inst, int8_t gain)
```

相关声明：[bt_aics_gain_set](#ga20f3a178788ec6aef593034159793b94)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

设置输入增益（Input Gain）。

<a id="r_gaf0b659698aa6a6a79143d4f591f67e09"></a>

```c
int bt_aics_description_get (struct bt_aics *inst)
```

相关声明：[bt_aics_description_get](#gaf0b659698aa6a6a79143d4f591f67e09)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

读取音频输入控制服务（Audio Input Control Service）的描述（Description）。

<a id="r_ga7de5ffd2eb61ca562b9773b37470ebd9"></a>

```c
int bt_aics_description_set (struct bt_aics *inst, const char *description)
```

相关声明：[bt_aics_description_set](#ga7de5ffd2eb61ca562b9773b37470ebd9)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

设置音频输入控制服务（Audio Input Control Service）的描述（Description）。

<a id="r_ga913838aa0d5bff239c2faef4d8a8b36b"></a>

```c
struct bt_aics * bt_aics_client_free_instance_get (void)
```

相关声明：[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[bt_aics_client_free_instance_get](#ga913838aa0d5bff239c2faef4d8a8b36b)。

获取新的音频输入控制服务（Audio Input Control Service）客户端实例。

<a id="r_gab660d2d4603de3837a3b93ce11e4d0fd"></a>

```c
int bt_aics_client_free_instance (struct bt_aics *inst)
```

相关声明：[bt_aics_client_free_instance](#gab660d2d4603de3837a3b93ce11e4d0fd)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)。

释放从 bt_aics_client_free_instance_get() 获得的实例（Instance）。

<a id="r_gabd6bdcdad0dd5a4c509f9e7cabb3e601"></a>

```c
void bt_aics_client_cb_register (struct bt_aics *inst, struct bt_aics_cb *cb)
```

相关声明：[bt_aics_client_cb_register](#gabd6bdcdad0dd5a4c509f9e7cabb3e601)、[bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)、[bt_aics_cb](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md)。

注册音频输入控制服务（Audio Input Control Service）客户端的回调。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 1.4\_音频输入控制服务静音状态（Audio Input Control Service Mute States）

<a id="r_ga47436e2df23067ce86dc761d77ed14b7"></a>

```c
#define BT_AICS_STATE_UNMUTED 0x00U
```

相关声明：[BT_AICS_STATE_UNMUTED](#ga47436e2df23067ce86dc761d77ed14b7)。

静音状态（Mute State）为未静音（Unmuted）。

<a id="r_ga1572eaaffea5412b496eb714d64aa981"></a>

```c
#define BT_AICS_STATE_MUTED 0x01U
```

相关声明：[BT_AICS_STATE_MUTED](#ga1572eaaffea5412b496eb714d64aa981)。

静音状态（Mute State）为已静音（Muted）。

<a id="r_gad0063d0e0b622b4093607e5485897214"></a>

```c
#define BT_AICS_STATE_MUTE_DISABLED 0x02U
```

相关声明：[BT_AICS_STATE_MUTE_DISABLED](#gad0063d0e0b622b4093607e5485897214)。

静音状态（Mute State）为已禁用（Disabled）。

## 1.5\_音频输入控制服务输入模式（Audio Input Control Service Input Modes）

<a id="r_gaecb9365a5e390111311d1b415a2cee79"></a>

```c
#define BT_AICS_MODE_MANUAL_ONLY 0x00U
```

相关声明：[BT_AICS_MODE_MANUAL_ONLY](#gaecb9365a5e390111311d1b415a2cee79)。

增益模式（Gain Mode）仅支持手动，不能改为自动。

<a id="r_ga6b536bdcab602ccaccfafe3b37258890"></a>

```c
#define BT_AICS_MODE_AUTO_ONLY 0x01U
```

相关声明：[BT_AICS_MODE_AUTO_ONLY](#ga6b536bdcab602ccaccfafe3b37258890)。

增益模式（Gain Mode）仅支持自动，不能改为手动。

<a id="r_ga7cf0508dd7407ec3bb92dec71cc00816"></a>

```c
#define BT_AICS_MODE_MANUAL 0x02U
```

相关声明：[BT_AICS_MODE_MANUAL](#ga7cf0508dd7407ec3bb92dec71cc00816)。

增益模式（Gain Mode）为手动（Manual）。

<a id="r_ga0ac3a583dd7ca58a0d356d9f60797517"></a>

```c
#define BT_AICS_MODE_AUTO 0x03U
```

相关声明：[BT_AICS_MODE_AUTO](#ga0ac3a583dd7ca58a0d356d9f60797517)。

增益模式（Gain Mode）为自动（Automatic）。

## 1.6\_音频输入控制服务输入类型（Audio Input Control Service Input Types）

<a id="r_ga2204f35b5f1aa41c27f62b8f0dcf74b6"></a>

```c
#define BT_AICS_INPUT_TYPE_UNSPECIFIED 0x00U
```

相关声明：[BT_AICS_INPUT_TYPE_UNSPECIFIED](#ga2204f35b5f1aa41c27f62b8f0dcf74b6)。

输入（Input）未指定。

<a id="r_gac8ebf643f9a4101ea8da18827577bf5d"></a>

```c
#define BT_AICS_INPUT_TYPE_BLUETOOTH 0x01U
```

相关声明：[BT_AICS_INPUT_TYPE_BLUETOOTH](#gac8ebf643f9a4101ea8da18827577bf5d)。

输入为蓝牙音频流（Bluetooth Audio Stream）。

<a id="r_ga7fcb5aefacb641a8ef7db4e9a554a65d"></a>

```c
#define BT_AICS_INPUT_TYPE_MICROPHONE 0x02U
```

相关声明：[BT_AICS_INPUT_TYPE_MICROPHONE](#ga7fcb5aefacb641a8ef7db4e9a554a65d)。

输入为麦克风（Microphone）。

<a id="r_ga525b361d1d555f20d292cf1aded0d046"></a>

```c
#define BT_AICS_INPUT_TYPE_ANALOG 0x03U
```

相关声明：[BT_AICS_INPUT_TYPE_ANALOG](#ga525b361d1d555f20d292cf1aded0d046)。

输入为模拟信号（Analog）。

<a id="r_ga688605eb9eb5b27ca62fac9b85fde472"></a>

```c
#define BT_AICS_INPUT_TYPE_DIGITAL 0x04U
```

相关声明：[BT_AICS_INPUT_TYPE_DIGITAL](#ga688605eb9eb5b27ca62fac9b85fde472)。

输入为数字信号（Digital）。

<a id="r_ga3b878b41ab30067bceefc0cd72340376"></a>

```c
#define BT_AICS_INPUT_TYPE_RADIO 0x05U
```

相关声明：[BT_AICS_INPUT_TYPE_RADIO](#ga3b878b41ab30067bceefc0cd72340376)。

输入为无线电广播（Radio），例如 AM/FM/XM 等。

<a id="r_ga43a02e2025e3cb3e10bc2ee2128ee877"></a>

```c
#define BT_AICS_INPUT_TYPE_STREAMING 0x06U
```

相关声明：[BT_AICS_INPUT_TYPE_STREAMING](#ga43a02e2025e3cb3e10bc2ee2128ee877)。

输入为流式音频源（Streaming Audio Source）。

<a id="r_gaacf259f2bc3d341c8d2857de5d412219"></a>

```c
#define BT_AICS_INPUT_TYPE_AMBIENT 0x07U
```

相关声明：[BT_AICS_INPUT_TYPE_AMBIENT](#gaacf259f2bc3d341c8d2857de5d412219)。

输入采用透明／透传方式（Transparent/Pass-through）。

## 1.7\_音频输入控制服务错误码（Audio Input Control Service Error Codes）

<a id="r_gae54199f78ff7d7380353f3950bd03a39"></a>

```c
#define BT_AICS_ERR_INVALID_COUNTER 0x80U
```

相关声明：[BT_AICS_ERR_INVALID_COUNTER](#gae54199f78ff7d7380353f3950bd03a39)。

Change_Counter 操作数值与音频输入状态特征（Audio Input State Characteristic）的 Change_Counter 字段值不匹配。

<a id="r_ga00c0942dab2bf25c680278927aa49af8"></a>

```c
#define BT_AICS_ERR_OP_NOT_SUPPORTED 0x81U
```

相关声明：[BT_AICS_ERR_OP_NOT_SUPPORTED](#ga00c0942dab2bf25c680278927aa49af8)。

控制点过程（Control Point Procedure）使用了无效操作码（Opcode）。

<a id="r_ga1efb1f6a4c24c2a20fc7136928abac6b"></a>

```c
#define BT_AICS_ERR_MUTE_DISABLED 0x82U
```

相关声明：[BT_AICS_ERR_MUTE_DISABLED](#ga1efb1f6a4c24c2a20fc7136928abac6b)。

静音／取消静音命令（Mute/Unmute Commands）已禁用。

<a id="r_ga2f3806b8056ea8ed43b2a7cd52ffa4f3"></a>

```c
#define BT_AICS_ERR_OUT_OF_RANGE 0x83U
```

相关声明：[BT_AICS_ERR_OUT_OF_RANGE](#ga2f3806b8056ea8ed43b2a7cd52ffa4f3)。

控制点过程（Control Point Procedure）使用的操作数（Operand）值超出允许范围。

<a id="r_ga6673570f7679322bfa4719bf6e41e299"></a>

```c
#define BT_AICS_ERR_GAIN_MODE_NOT_ALLOWED 0x84U
```

相关声明：[BT_AICS_ERR_GAIN_MODE_NOT_ALLOWED](#ga6673570f7679322bfa4719bf6e41e299)。

不允许所请求的增益模式变更（Gain Mode Change）。

## 1.8\_详细说明（Detailed Documentation）

<a id="ga6673570f7679322bfa4719bf6e41e299"></a>

### `BT_AICS_ERR_GAIN_MODE_NOT_ALLOWED`

```c
#define BT_AICS_ERR_GAIN_MODE_NOT_ALLOWED 0x84U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

不允许所请求的增益模式变更（Gain Mode Change）。

<a id="gae54199f78ff7d7380353f3950bd03a39"></a>

### `BT_AICS_ERR_INVALID_COUNTER`

```c
#define BT_AICS_ERR_INVALID_COUNTER 0x80U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

Change_Counter 操作数值与音频输入状态特征（Audio Input State Characteristic）的 Change_Counter 字段值不匹配。

<a id="ga1efb1f6a4c24c2a20fc7136928abac6b"></a>

### `BT_AICS_ERR_MUTE_DISABLED`

```c
#define BT_AICS_ERR_MUTE_DISABLED 0x82U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

静音／取消静音命令（Mute/Unmute Commands）已禁用。

参见 BT_AICS_STATE_MUTE_DISABLED。

<a id="ga00c0942dab2bf25c680278927aa49af8"></a>

### `BT_AICS_ERR_OP_NOT_SUPPORTED`

```c
#define BT_AICS_ERR_OP_NOT_SUPPORTED 0x81U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

控制点过程（Control Point Procedure）使用了无效操作码（Opcode）。

<a id="ga2f3806b8056ea8ed43b2a7cd52ffa4f3"></a>

### `BT_AICS_ERR_OUT_OF_RANGE`

```c
#define BT_AICS_ERR_OUT_OF_RANGE 0x83U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

控制点过程（Control Point Procedure）使用的操作数（Operand）值超出允许范围。

<a id="gaacf259f2bc3d341c8d2857de5d412219"></a>

### `BT_AICS_INPUT_TYPE_AMBIENT`

```c
#define BT_AICS_INPUT_TYPE_AMBIENT 0x07U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

输入采用透明／透传方式（Transparent/Pass-through）。

<a id="ga525b361d1d555f20d292cf1aded0d046"></a>

### `BT_AICS_INPUT_TYPE_ANALOG`

```c
#define BT_AICS_INPUT_TYPE_ANALOG 0x03U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

输入为模拟信号（Analog）。

<a id="gac8ebf643f9a4101ea8da18827577bf5d"></a>

### `BT_AICS_INPUT_TYPE_BLUETOOTH`

```c
#define BT_AICS_INPUT_TYPE_BLUETOOTH 0x01U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

输入为蓝牙音频流（Bluetooth Audio Stream）。

<a id="ga688605eb9eb5b27ca62fac9b85fde472"></a>

### `BT_AICS_INPUT_TYPE_DIGITAL`

```c
#define BT_AICS_INPUT_TYPE_DIGITAL 0x04U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

输入为数字信号（Digital）。

<a id="ga7fcb5aefacb641a8ef7db4e9a554a65d"></a>

### `BT_AICS_INPUT_TYPE_MICROPHONE`

```c
#define BT_AICS_INPUT_TYPE_MICROPHONE 0x02U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

输入为麦克风（Microphone）。

<a id="ga3b878b41ab30067bceefc0cd72340376"></a>

### `BT_AICS_INPUT_TYPE_RADIO`

```c
#define BT_AICS_INPUT_TYPE_RADIO 0x05U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

输入为无线电广播（Radio），例如 AM/FM/XM 等。

<a id="ga43a02e2025e3cb3e10bc2ee2128ee877"></a>

### `BT_AICS_INPUT_TYPE_STREAMING`

```c
#define BT_AICS_INPUT_TYPE_STREAMING 0x06U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

输入为流式音频源（Streaming Audio Source）。

<a id="ga2204f35b5f1aa41c27f62b8f0dcf74b6"></a>

### `BT_AICS_INPUT_TYPE_UNSPECIFIED`

```c
#define BT_AICS_INPUT_TYPE_UNSPECIFIED 0x00U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

输入（Input）未指定。

<a id="ga0ac3a583dd7ca58a0d356d9f60797517"></a>

### `BT_AICS_MODE_AUTO`

```c
#define BT_AICS_MODE_AUTO 0x03U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

增益模式（Gain Mode）为自动（Automatic）。

客户端无法控制增益（Gain）。

<a id="ga6b536bdcab602ccaccfafe3b37258890"></a>

### `BT_AICS_MODE_AUTO_ONLY`

```c
#define BT_AICS_MODE_AUTO_ONLY 0x01U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

增益模式（Gain Mode）仅支持自动，不能改为手动。

客户端无法控制增益（Gain）。

<a id="ga7cf0508dd7407ec3bb92dec71cc00816"></a>

### `BT_AICS_MODE_MANUAL`

```c
#define BT_AICS_MODE_MANUAL 0x02U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

增益模式（Gain Mode）为手动（Manual）。

客户端可以控制增益（Gain）。

<a id="gaecb9365a5e390111311d1b415a2cee79"></a>

### `BT_AICS_MODE_MANUAL_ONLY`

```c
#define BT_AICS_MODE_MANUAL_ONLY 0x00U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

增益模式（Gain Mode）仅支持手动，不能改为自动。

客户端可以控制增益（Gain）。

<a id="gad0063d0e0b622b4093607e5485897214"></a>

### `BT_AICS_STATE_MUTE_DISABLED`

```c
#define BT_AICS_STATE_MUTE_DISABLED 0x02U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

静音状态（Mute State）为已禁用（Disabled）。

<a id="ga1572eaaffea5412b496eb714d64aa981"></a>

### `BT_AICS_STATE_MUTED`

```c
#define BT_AICS_STATE_MUTED 0x01U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

静音状态（Mute State）为已静音（Muted）。

<a id="ga47436e2df23067ce86dc761d77ed14b7"></a>

### `BT_AICS_STATE_UNMUTED`

```c
#define BT_AICS_STATE_UNMUTED 0x00U
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

静音状态（Mute State）为未静音（Unmuted）。

<a id="ga98b142ea7a66de5577c44aa90d507930"></a>

### `bt_aics_description_cb`

```c
typedef void(* bt_aics_description_cb) (struct bt_aics *inst, int err, char *description)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

用于描述（Description）的回调函数。

读取此值时，或服务器、客户端任一方更改此值时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |
| `err` | 错误值（Error Value）：0 表示成功；正值为 GATT 错误，负值为 errno 错误。对于通知（Notifications），始终为 0。 |
| `description` | 描述为 UTF-8 编码字符串（UTF-8 Encoded String），可能已被截短。 |

<a id="ga9fda39f8410308e05eb928eeb7267e83"></a>

### `bt_aics_discover_cb`

```c
typedef void(* bt_aics_discover_cb) (struct bt_aics *inst, int err)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

bt_aics_discover 的回调函数（Callback Function）。

此回调通常会被包含音频输入控制服务（Audio Input Control Service）客户端的主服务（Primary Service）覆盖。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |
| `err` | 错误值（Error Value）：0 表示成功；正值为 GATT 错误，负值为 errno 错误。对于通知（Notifications），始终为 0。 |

<a id="ga11da08c010f4aa849c2e3725dc5cbaeb"></a>

### `bt_aics_gain_setting_cb`

```c
typedef void(* bt_aics_gain_setting_cb) (struct bt_aics *inst, int err, uint8_t units, int8_t minimum, int8_t maximum)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

增益设置（Gain Settings）的回调函数。

读取此值时，或服务器、客户端任一方更改此值时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |
| `err` | 错误值（Error Value）：0 表示成功；正值为 GATT 错误，负值为 errno 错误。对于通知（Notifications），始终为 0。 |
| `units` | 表示增益设置值（Gain Setting Value）每次增加或减少一步的大小，以 0.1 分贝（Decibel）为单位。 |
| `minimum` | 增益设置允许的最小增益（Minimum Gain）。 |
| `maximum` | 增益设置允许的最大增益（Maximum Gain）。 |

<a id="ga2e851f49f9c7e71a18376468a13fdf4f"></a>

### `bt_aics_state_cb`

```c
typedef void(* bt_aics_state_cb) (struct bt_aics *inst, int err, int8_t gain, uint8_t mute, uint8_t mode)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

输入状态（Input State）的回调函数。

读取此值时，或服务器、客户端任一方更改此值时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |
| `err` | 错误值（Error Value）：0 表示成功；正值为 GATT 错误，负值为 errno 错误。对于通知（Notifications），始终为 0。 |
| `gain` | 增益设置值（Gain Setting Value）。 |
| `mute` | 静音值（Mute Value）。 |
| `mode` | 模式值（Mode Value）。 |

<a id="ga044d92a4273c6537a9cdf20922352ed6"></a>

### `bt_aics_status_cb`

```c
typedef void(* bt_aics_status_cb) (struct bt_aics *inst, int err, bool active)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

输入状态（Input Status）的回调函数。

读取此值时，或服务器、客户端任一方更改此值时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |
| `err` | 错误值（Error Value）：0 表示成功；正值为 GATT 错误，负值为 errno 错误。对于通知（Notifications），始终为 0。 |
| `active` | 实例是活动还是非活动（Active/Inactive）。 |

<a id="ga6e76b9f2de4cdbcd7539c76f6a347fa5"></a>

### `bt_aics_type_cb`

```c
typedef void(* bt_aics_type_cb) (struct bt_aics *inst, int err, uint8_t type)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

输入类型（Input Type）的回调函数。

读取此值时，或服务器、客户端任一方更改此值时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |
| `err` | 错误值（Error Value）：0 表示成功；正值为 GATT 错误，负值为 errno 错误。对于通知（Notifications），始终为 0。 |
| `type` | 输入类型（Input Type）。 |

<a id="ga36991fe1dee5168db618518d094d80ef"></a>

### `bt_aics_write_cb`

```c
typedef void(* bt_aics_write_cb) (struct bt_aics *inst, int err)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

写入操作的回调函数（Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |

<a id="gac46268949fa7cbbb827d149a3a904daa"></a>

### `bt_aics_activate()`

```c
int bt_aics_activate ( struct bt_aics * inst)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

激活音频输入控制服务（Audio Input Control Service）实例。

音频输入控制服务（Audio Input Control Service）默认处于活动状态；使用 bt_aics_deactivate 停用实例后，服务器可以通过此函数将其重新激活。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga759712886cd3c4c025ea360dcb663c59"></a>

### `bt_aics_automatic_gain_set()`

```c
int bt_aics_automatic_gain_set ( struct bt_aics * inst)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

将输入增益（Input Gain）设为自动。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="gabd6bdcdad0dd5a4c509f9e7cabb3e601"></a>

### `bt_aics_client_cb_register()`

```c
void bt_aics_client_cb_register ( struct bt_aics * inst, struct bt_aics_cb * cb )
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

注册音频输入控制服务（Audio Input Control Service）客户端的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |
| `cb` | 指向回调结构体（Callback Structure）的指针。 |

<a id="ga0e088e26cf73f1f3b918660d4acdebb9"></a>

### `bt_aics_client_conn_get()`

```c
int bt_aics_client_conn_get ( const struct bt_aics * aics, struct bt_conn ** conn )
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

获取客户端实例的连接指针（Connection Pointer）。

获取音频输入控制服务（Audio Input Control Service）客户端实例的蓝牙连接指针（Bluetooth Connection Pointer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `aics` | 音频输入控制服务（Audio Input Control Service）客户端实例指针。 |
| `conn` | 连接指针（Connection Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gab660d2d4603de3837a3b93ce11e4d0fd"></a>

### `bt_aics_client_free_instance()`

```c
int bt_aics_client_free_instance ( struct bt_aics * inst)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

释放从 bt_aics_client_free_instance_get() 获得的实例（Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 待释放的实例（Instance） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | inst 为 NULL 或不是客户端实例。 |
| `-EALREADY` | inst 已处于空闲状态。 |
| `-EBUSY` | inst 正忙。 |

<a id="ga913838aa0d5bff239c2faef4d8a8b36b"></a>

### `bt_aics_client_free_instance_get()`

```c
struct bt_aics * bt_aics_client_free_instance_get ( void )
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

获取新的音频输入控制服务（Audio Input Control Service）客户端实例。

**返回（Returns）**：返回值（Returns）：指向实例的指针；无剩余空闲实例时返回 NULL。

<a id="ga4be4c4e3c74aa55fbf599157aa1c2098"></a>

### `bt_aics_deactivate()`

```c
int bt_aics_deactivate ( struct bt_aics * inst)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

停用音频输入控制服务（Audio Input Control Service）实例。

音频输入控制服务（Audio Input Control Service）默认处于活动状态，此函数允许服务器将其停用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gaf0b659698aa6a6a79143d4f591f67e09"></a>

### `bt_aics_description_get()`

```c
int bt_aics_description_get ( struct bt_aics * inst)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

读取音频输入控制服务（Audio Input Control Service）的描述（Description）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga7de5ffd2eb61ca562b9773b37470ebd9"></a>

### `bt_aics_description_set()`

```c
int bt_aics_description_set ( struct bt_aics * inst, const char * description )
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

设置音频输入控制服务（Audio Input Control Service）的描述（Description）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |
| `description` | 描述（Description），以 UTF-8 编码字符串表示。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga5a1ad98afe45da9ffbb7247671385d40"></a>

### `bt_aics_disable_mute()`

```c
int bt_aics_disable_mute ( struct bt_aics * inst)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

禁用音频输入控制服务（Audio Input Control Service）的静音功能（Mute）。

调用 bt_aics_unmute() 或 bt_aics_mute() 会重新启用静音功能（Mute），并将静音状态设置为未静音（Unmuted）或已静音（Muted）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |

返回（Returns）：成功时为 0，失败时为 errno 值。

<a id="gad16d296462af2f61a893bda8d25cc9de"></a>

### `bt_aics_discover()`

```c
int bt_aics_discover ( struct bt_conn * conn, struct bt_aics * inst, const struct bt_aics_discover_param * param )
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

发现音频输入控制服务（Audio Input Control Service）。

根据 param 尝试发现服务器上的音频输入控制服务（Audio Input Control Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接到具有音频输入控制服务（Audio Input Control Service）的对端的连接。 |
| `inst` | 实例指针（Instance Pointer）。 |
| `param` | 指向参数（Parameters）的指针。 |

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回 errno。

<a id="gab10ad3599f5b602cdf5504bc92508109"></a>

### `bt_aics_free_instance_get()`

```c
struct bt_aics * bt_aics_free_instance_get ( void )
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

从池中获取一个空闲的音频输入控制服务（Audio Input Control Service）实例。

返回（Returns）：成功时为音频输入控制服务（Audio Input Control Service）实例，出错时为 NULL。

<a id="ga20f3a178788ec6aef593034159793b94"></a>

### `bt_aics_gain_set()`

```c
int bt_aics_gain_set ( struct bt_aics * inst, int8_t gain )
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

设置输入增益（Input Gain）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |
| `gain` | 要设置的增益（Gain），范围为 -128 至 127，以增益设置单位（Gain Setting Units）表示，参见 bt_aics_gain_setting_cb。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga22869d8a62eb59bc4aad25946da8f9cf"></a>

### `bt_aics_gain_set_auto_only()`

```c
int bt_aics_gain_set_auto_only ( struct bt_aics * inst)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

在音频输入控制服务（Audio Input Control Service）中设置仅自动增益模式（Automatic-only Gain Mode）。

使用此函数启用仅自动增益（Automatic-only Gain）后，将禁止通过 bt_aics_gain_set 设置增益。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |

返回（Returns）：成功时为 0，失败时为 errno 值。

<a id="ga0460e82d4277a2c4b14964799ad5f2b0"></a>

### `bt_aics_gain_set_manual_only()`

```c
int bt_aics_gain_set_manual_only ( struct bt_aics * inst)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

在音频输入控制服务（Audio Input Control Service）中设置仅手动增益模式（Manual-only Gain Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |

返回（Returns）：成功时为 0，失败时为 errno 值。

<a id="ga38d7131397d7762d3bd53e152a6c6130"></a>

### `bt_aics_gain_setting_get()`

```c
int bt_aics_gain_setting_get ( struct bt_aics * inst)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

读取音频输入控制服务（Audio Input Control Service）的增益设置（Gain Settings）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga7ddb93125f6275fc7c99fbf448e24f0c"></a>

### `bt_aics_manual_gain_set()`

```c
int bt_aics_manual_gain_set ( struct bt_aics * inst)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

将输入增益（Input Gain）设为手动。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga4d511e81dd0f0a72fd502bc05dd85e91"></a>

### `bt_aics_mode_to_str()`

```c
const char * bt_aics_mode_to_str ( uint8_t mode)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/audio/aics.h>
```

将音频输入控制服务（AICS）的增益模式（Gain Mode）转换为便于阅读的字符串。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mode` | 增益模式值（Gain Mode Value），即 `BT_AICS_MODE_*`。 |

返回（Returns）：增益模式（Gain Mode）的字符串表示。

<a id="ga5345254eaf099560e609d97044b39a97"></a>

### `bt_aics_mute()`

```c
int bt_aics_mute ( struct bt_aics * inst)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

将音频输入控制服务（Audio Input Control Service）的输入静音（Mute）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga008ef5cebfcb9b4a3084f411fa81238e"></a>

### `bt_aics_register()`

```c
int bt_aics_register ( struct bt_aics * aics, struct bt_aics_register_param * param )
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

初始化音频输入控制服务（Audio Input Control Service）实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `aics` | 音频输入控制服务（Audio Input Control Service）实例。 |
| `param` | 音频输入控制服务注册参数（Audio Input Control Service Register Parameters）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga23bbc1393d21fe38f501813935b25b3d"></a>

### `bt_aics_state_get()`

```c
int bt_aics_state_get ( struct bt_aics * inst)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

读取音频输入控制服务（Audio Input Control Service）的输入状态（Input State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="gade387c52d201ce10b39ef52157dae83d"></a>

### `bt_aics_status_get()`

```c
int bt_aics_status_get ( struct bt_aics * inst)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

读取音频输入控制服务（Audio Input Control Service）的输入状态（Input Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga8b415343e7ecf399ecfd0dcaa49bd1ee"></a>

### `bt_aics_svc_decl_get()`

```c
void * bt_aics_svc_decl_get ( struct bt_aics * aics)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

获取服务声明属性（Service Declaration Attribute）。

返回的首个服务属性（Service Attribute）可包含在其他任意 GATT 服务中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `aics` | 音频输入控制服务（Audio Input Control Service）实例。 |

**返回（Returns）**：返回值（Returns）：指向服务属性（Attributes）的指针。

<a id="gaf57896e2096a5e96ec46a56cdf216159"></a>

### `bt_aics_type_get()`

```c
int bt_aics_type_get ( struct bt_aics * inst)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

读取音频输入控制服务（Audio Input Control Service）的输入类型（Input Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga43396d2d4b3bd9cdd0c82275fafeadfc"></a>

### `bt_aics_unmute()`

```c
int bt_aics_unmute ( struct bt_aics * inst)
```

```c
#include <zephyr/bluetooth/audio/aics.h>
```

取消音频输入控制服务（Audio Input Control Service）输入的静音（Unmute）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。


## 1.9\_原页交叉引用（Cross References）

- [bt_aics_register_param](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md)
- [bt_aics_discover_param](../bluetooth_le_audio_model_reference/P003_bt_aics_discover_param_结构体.md)
- [bt_aics_cb](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md)
- [bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [zephyr/bluetooth/audio/aics.h](../api_file_audio_test_reference/P001_zephyr__bluetooth__audio__aics.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_BAP 单播客户端 API（Unicast Client APIs）.md)
