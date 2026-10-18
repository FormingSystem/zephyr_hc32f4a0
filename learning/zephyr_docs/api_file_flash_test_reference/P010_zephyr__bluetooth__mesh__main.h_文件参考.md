---
id: learning.zephyr-docs.api-file-flash-test-reference.page-10
title: zephyr__bluetooth__mesh__main.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/main_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_bluetooth\_\_mesh\_\_main.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/main_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh协议（Protocol）的API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

蓝牙Mesh协议（Protocol）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fdev_5Fcapabilities"></a>

```c
struct bt_mesh_dev_capabilities
```

相关声明：[bt_mesh_dev_capabilities](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md)。

设备能力（Device Capabilities）。

<a id="r_bt_5Fmesh_5Fprov"></a>

```c
struct bt_mesh_prov
```

相关声明：[bt_mesh_prov](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md)。

配网（Provisioning）的属性与能力。

<a id="r_bt_5Fmesh_5Flpn_5Fcb"></a>

```c
struct bt_mesh_lpn_cb
```

相关声明：[bt_mesh_lpn_cb](../bluetooth_mesh_model_reference/P072_bt_mesh_lpn_cb_结构体.md)。

低功耗节点（Low Power Node，LPN）的回调函数。

<a id="r_bt_5Fmesh_5Ffriend_5Fcb"></a>

```c
struct bt_mesh_friend_cb
```

相关声明：[bt_mesh_friend_cb](../bluetooth_mesh_model_reference/P061_bt_mesh_friend_cb_结构体.md)。

好友节点（Friend Node）的回调函数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.2\_宏定义（Macros）

<a id="r_ga0d6985da3c7be76732ee103458b77121"></a>

```c
#define BT_MESH_NET_PRIMARY 0x000
```

相关声明：[BT_MESH_NET_PRIMARY](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga0d6985da3c7be76732ee103458b77121)。

主网络密钥索引（Primary Network Key Index）。

<a id="r_gac588eefe83db94784a420ce063f02b55"></a>

```c
#define BT_MESH_FEAT_RELAY BIT(0)
```

相关声明：[BT_MESH_FEAT_RELAY](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#gac588eefe83db94784a420ce063f02b55)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

中继特性（Relay Feature）。

<a id="r_gaee648ce202316c56d4d588cb0ad5aeb4"></a>

```c
#define BT_MESH_FEAT_PROXY BIT(1)
```

相关声明：[BT_MESH_FEAT_PROXY](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#gaee648ce202316c56d4d588cb0ad5aeb4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

GATT 代理特性（GATT Proxy Feature）。

<a id="r_ga8f27086b3bc3c4a6e14621836f9f8e80"></a>

```c
#define BT_MESH_FEAT_FRIEND BIT(2)
```

相关声明：[BT_MESH_FEAT_FRIEND](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga8f27086b3bc3c4a6e14621836f9f8e80)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

朋友特性（Friend Feature）。

<a id="r_gaad71a36c82b4e4d3fa334ecff5cc0171"></a>

```c
#define BT_MESH_FEAT_LOW_POWER BIT(3)
```

相关声明：[BT_MESH_FEAT_LOW_POWER](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#gaad71a36c82b4e4d3fa334ecff5cc0171)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

低功耗节点特性（Low Power Node Feature）。

<a id="r_gac337fd8688d70e862974e010ad42a11b"></a>

```c
#define BT_MESH_FEAT_SUPPORTED
```

相关声明：[BT_MESH_FEAT_SUPPORTED](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#gac337fd8688d70e862974e010ad42a11b)。

支持的心跳发布特性（Heartbeat Publication Features）。

<a id="r_gac18d4ce09495a8ade098a6320bb26ec2"></a>

```c
#define BT_MESH_LPN_CB_DEFINE(_name)
```

相关声明：[BT_MESH_LPN_CB_DEFINE](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#gac18d4ce09495a8ade098a6320bb26ec2)。

注册用于友谊关系事件（Friendship Events）的回调结构体。

<a id="r_ga4f00fa03af86b39e24140eb09c51ca4c"></a>

```c
#define BT_MESH_FRIEND_CB_DEFINE(_name)
```

相关声明：[BT_MESH_FRIEND_CB_DEFINE](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga4f00fa03af86b39e24140eb09c51ca4c)。

注册用于友谊关系事件（Friendship Events）的回调结构体。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.3\_枚举（Enumerations）

<a id="r_gabe5586cff0697e137730a52728978681"></a>

```c
enum { BT_MESH_PROV_AUTH_CMAC_AES128_AES_CCM , BT_MESH_PROV_AUTH_HMAC_SHA256_AES_CCM }
```

相关声明：[BT_MESH_PROV_AUTH_CMAC_AES128_AES_CCM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggabe5586cff0697e137730a52728978681affa8679d8be1a12714a34ed09c3b05dd)、[BT_MESH_PROV_AUTH_HMAC_SHA256_AES_CCM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggabe5586cff0697e137730a52728978681a292bf2e4d29f0bd0d746bbb871f2ee5a)。

可用的认证算法（Authentication Algorithms）。

<a id="r_gabec90bd95082b9dc8fa3ca27a9d7bc66"></a>

```c
enum { BT_MESH_STATIC_OOB_AVAILABLE = (1UL << (0)) , BT_MESH_OOB_AUTH_REQUIRED = (1UL << (1)) }
```

相关声明：[BT_MESH_STATIC_OOB_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggabec90bd95082b9dc8fa3ca27a9d7bc66a30e46fe23e508029b570e1f107b38d40)、[BT_MESH_OOB_AUTH_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggabec90bd95082b9dc8fa3ca27a9d7bc66a61f859a15fabc8d9fd278dabe5a86a37)。

带外类型字段值（OOB Type Field Values）。

<a id="r_ga5512b81ef7eeb45b0a12ef62234c8795"></a>

```c
enum bt_mesh_output_action_t { BT_MESH_NO_OUTPUT = 0 , BT_MESH_BLINK = (1UL << (0)) , BT_MESH_BEEP = (1UL << (1)) , BT_MESH_VIBRATE = (1UL << (2)) , BT_MESH_DISPLAY_NUMBER = (1UL << (3)) , BT_MESH_DISPLAY_STRING = (1UL << (4)) }
```

相关声明：[bt_mesh_output_action_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga5512b81ef7eeb45b0a12ef62234c8795)、[BT_MESH_NO_OUTPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795ad009060fd1f501c8362a63e6c020b113)、[BT_MESH_BLINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795ac38333011b4f76b036a04e41f1f71e83)、[BT_MESH_BEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795ae50031a39d19181df17ee6de1a12272c)、[BT_MESH_VIBRATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795ab45021af96db0465f5edc6e0ea7b6079)、[BT_MESH_DISPLAY_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795a3586ffa3e36247e0d90b83c3f075e591)、[BT_MESH_DISPLAY_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795aa07d600f2afe278729bb4e35d41bf29b)。

可用的配网输出认证动作（Provisioning Output Authentication Actions）。

<a id="r_gaf71f3dbdef6b8c085e9a4f068e1f60c5"></a>

```c
enum bt_mesh_input_action_t { BT_MESH_NO_INPUT = 0 , BT_MESH_PUSH = (1UL << (0)) , BT_MESH_TWIST = (1UL << (1)) , BT_MESH_ENTER_NUMBER = (1UL << (2)) , BT_MESH_ENTER_STRING = (1UL << (3)) }
```

相关声明：[bt_mesh_input_action_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf71f3dbdef6b8c085e9a4f068e1f60c5)、[BT_MESH_NO_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ac721b070cad51f1cd9aa1f0b60e59056)、[BT_MESH_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ae4902ce51142fa49d2d5e97165d6f51c)、[BT_MESH_TWIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ad6f22211d09614181cb5b0f42300a9ee)、[BT_MESH_ENTER_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf71f3dbdef6b8c085e9a4f068e1f60c5aa0de3817e863d1f06888100de24fb4b0)、[BT_MESH_ENTER_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf71f3dbdef6b8c085e9a4f068e1f60c5a5d6bd8e6110c8f53245840aead4201c2)。

可用的配网输入认证动作（Provisioning Input Authentication Actions）。

<a id="r_gaa157eb0fee30c28092a11993872b8fdd"></a>

```c
enum bt_mesh_prov_bearer_t { BT_MESH_PROV_ADV = (1UL << (0)) , BT_MESH_PROV_GATT = (1UL << (1)) , BT_MESH_PROV_REMOTE = (1UL << (2)) }
```

相关声明：[bt_mesh_prov_bearer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaa157eb0fee30c28092a11993872b8fdd)、[BT_MESH_PROV_ADV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaa157eb0fee30c28092a11993872b8fdda5142f018a5426a047688c6507b3af4f8)、[BT_MESH_PROV_GATT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaa157eb0fee30c28092a11993872b8fdda27c9c1278acc887214a4a30294bf52d8)、[BT_MESH_PROV_REMOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaa157eb0fee30c28092a11993872b8fdda4222d03b09ba43b6ea772738b8987501)。

可用的配网承载（Provisioning Bearers）。

<a id="r_gaf93f7b49dada5c3f7accc54663648e48"></a>

```c
enum bt_mesh_prov_oob_info_t { BT_MESH_PROV_OOB_OTHER = (1UL << (0)) , BT_MESH_PROV_OOB_URI = (1UL << (1)) , BT_MESH_PROV_OOB_2D_CODE = (1UL << (2)) , BT_MESH_PROV_OOB_BAR_CODE = (1UL << (3)) , BT_MESH_PROV_OOB_NFC = (1UL << (4)) , BT_MESH_PROV_OOB_NUMBER = (1UL << (5)) , BT_MESH_PROV_OOB_STRING = (1UL << (6)) , BT_MESH_PROV_OOB_CERTIFICATE = (1UL << (7)) , BT_MESH_PROV_OOB_RECORDS = (1UL << (8)) , BT_MESH_PROV_OOB_ON_BOX = (1UL << (11)) , BT_MESH_PROV_OOB_IN_BOX = (1UL << (12)) , BT_MESH_PROV_OOB_ON_PAPER = (1UL << (13)) , BT_MESH_PROV_OOB_IN_MANUAL = (1UL << (14)) , BT_MESH_PROV_OOB_ON_DEV = (1UL << (15)) }
```

相关声明：[bt_mesh_prov_oob_info_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf93f7b49dada5c3f7accc54663648e48)、[BT_MESH_PROV_OOB_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a487ffb56c8c15a37b69fa1699fff301a)、[BT_MESH_PROV_OOB_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48ad861e8de3c1fbc1658a6d0fba38785dd)、[BT_MESH_PROV_OOB_2D_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a34d005022a75446a386006f7690a473e)、[BT_MESH_PROV_OOB_BAR_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48abe8fd10b49a7bb6c7499eb73ae3876d3)、[BT_MESH_PROV_OOB_NFC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48ad9b4089a740d47950c02b4389d29df56)、[BT_MESH_PROV_OOB_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48ac5d40459453afebc841f32e1f0b33fbc)、[BT_MESH_PROV_OOB_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a8553379d579a418a6453669323b18088)、[BT_MESH_PROV_OOB_CERTIFICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a00eb3ba6b7940b02d2fe3892100f497e)、[BT_MESH_PROV_OOB_RECORDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48aa10724108397ab8d48a3aac2817992f2)、[BT_MESH_PROV_OOB_ON_BOX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48adbbc3c3829bb7caf1a4a5fd2066f3b4a)、[BT_MESH_PROV_OOB_IN_BOX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48ae855a27a18bfb6ea03f0ff6165e4a291)、[BT_MESH_PROV_OOB_ON_PAPER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a137946e3d53b996b77bebeda5fa930cb)、[BT_MESH_PROV_OOB_IN_MANUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a4a8a7e4ab87cf360abdb167076349072)、[BT_MESH_PROV_OOB_ON_DEV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48aa73dd9517eec86e51b48d256fc9660da)。

带外信息位置（Out of Band Information Location）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.4\_函数（Functions）

<a id="r_ga2592abf429b40ef9242bce26f5bd085e"></a>

```c
int bt_mesh_input_string (const char *str)
```

相关声明：[bt_mesh_input_string](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga2592abf429b40ef9242bce26f5bd085e)。

提供配网输入带外字符串（Provisioning Input OOB String）。

<a id="r_gabc9d68157928c2b343eddd08ef314d27"></a>

```c
int bt_mesh_input_numeric (uint8_t *numeric, size_t size)
```

相关声明：[bt_mesh_input_numeric](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gabc9d68157928c2b343eddd08ef314d27)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提供配网输入带外数值（Provisioning Input OOB Numeric Value）。

<a id="r_gae33b5b6e9650b49d46494b4a81b18674"></a>

```c
int bt_mesh_prov_remote_pub_key_set (const uint8_t public_key[64])
```

相关声明：[bt_mesh_prov_remote_pub_key_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gae33b5b6e9650b49d46494b4a81b18674)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提供设备公钥（Device Public Key）。

<a id="r_ga80be35bf7287e62cb47d8fba99d648a9"></a>

```c
int bt_mesh_auth_method_set_input (bt_mesh_input_action_t action, uint8_t size)
```

相关声明：[bt_mesh_auth_method_set_input](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga80be35bf7287e62cb47d8fba99d648a9)、[bt_mesh_input_action_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf71f3dbdef6b8c085e9a4f068e1f60c5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用输入带外认证（Input OOB Authentication）。

<a id="r_gad66ccc725a1cfdf2b79076f22f853f84"></a>

```c
int bt_mesh_auth_method_set_output (bt_mesh_output_action_t action, uint8_t size)
```

相关声明：[bt_mesh_auth_method_set_output](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gad66ccc725a1cfdf2b79076f22f853f84)、[bt_mesh_output_action_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga5512b81ef7eeb45b0a12ef62234c8795)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用输出带外认证（Output OOB Authentication）。

<a id="r_ga7b6024dc32f6ec7f26cbf91545911084"></a>

```c
int bt_mesh_auth_method_set_static (const uint8_t *static_val, uint8_t size)
```

相关声明：[bt_mesh_auth_method_set_static](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga7b6024dc32f6ec7f26cbf91545911084)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用静态带外认证（Static OOB Authentication）。

<a id="r_gabab41ebdcae2eaa109e03cb2d8fa78c6"></a>

```c
int bt_mesh_auth_method_set_none (void)
```

相关声明：[bt_mesh_auth_method_set_none](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gabab41ebdcae2eaa109e03cb2d8fa78c6)。

不使用带外认证（OOB Authentication）。

<a id="r_ga6c8dc1b09d4cde8738be83c992b860a9"></a>

```c
int bt_mesh_prov_enable (bt_mesh_prov_bearer_t bearers)
```

相关声明：[bt_mesh_prov_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga6c8dc1b09d4cde8738be83c992b860a9)、[bt_mesh_prov_bearer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaa157eb0fee30c28092a11993872b8fdd)。

启用指定配网承载（Provisioning Bearers）。

<a id="r_gac7e084e7d12a93377d49b1c3d6313399"></a>

```c
int bt_mesh_prov_disable (bt_mesh_prov_bearer_t bearers)
```

相关声明：[bt_mesh_prov_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gac7e084e7d12a93377d49b1c3d6313399)、[bt_mesh_prov_bearer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaa157eb0fee30c28092a11993872b8fdd)。

禁用指定配网承载（Provisioning Bearers）。

<a id="r_ga4ed6e078c1c0f197758c8dbb23db30f6"></a>

```c
int bt_mesh_provision (const uint8_t net_key[16], uint16_t net_idx, uint8_t flags, uint32_t iv_index, uint16_t addr, const uint8_t dev_key[16])
```

相关声明：[bt_mesh_provision](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga4ed6e078c1c0f197758c8dbb23db30f6)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为本地 Mesh 节点配网（Provision）。

<a id="r_ga0bfae4ebda53052cfa027c3a7ae51ec8"></a>

```c
int bt_mesh_provision_adv (const uint8_t uuid[16], uint16_t net_idx, uint16_t addr, uint8_t attention_duration)
```

相关声明：[bt_mesh_provision_adv](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga0bfae4ebda53052cfa027c3a7ae51ec8)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用 PB-ADV 为 Mesh 节点配网（Provision）。

<a id="r_ga60666e0d7629caf36026974621bae664"></a>

```c
int bt_mesh_provision_gatt (const uint8_t uuid[16], uint16_t net_idx, uint16_t addr, uint8_t attention_duration)
```

相关声明：[bt_mesh_provision_gatt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga60666e0d7629caf36026974621bae664)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用 PB-GATT 为 Mesh 节点配网（Provision）。

<a id="r_ga9fc414e4e15d6b3ab0dae5483ed62982"></a>

```c
int bt_mesh_provision_remote (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, const uint8_t uuid[16], uint16_t net_idx, uint16_t addr)
```

相关声明：[bt_mesh_provision_remote](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga9fc414e4e15d6b3ab0dae5483ed62982)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

使用 PB-Remote 为 Mesh 节点配网（Provision）。

<a id="r_gaa02583390f635ac251d22ed9ff953974"></a>

```c
int bt_mesh_reprovision_remote (struct bt_mesh_rpr_cli *cli, struct bt_mesh_rpr_node *srv, uint16_t addr, bool comp_change)
```

相关声明：[bt_mesh_reprovision_remote](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaa02583390f635ac251d22ed9ff953974)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

使用 PB-Remote 为 Mesh 节点重新配网（Reprovision）。

<a id="r_ga0307e62001ba7fa303ed311ebc47f116"></a>

```c
bool bt_mesh_is_provisioned (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_is_provisioned](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga0307e62001ba7fa303ed311ebc47f116)。

检查本地节点是否已配网（Provisioned）。

<a id="r_ga521def6f74467a9bd3f2757c6aabd405"></a>

```c
int bt_mesh_init (const struct bt_mesh_prov *prov, const struct bt_mesh_comp *comp)
```

相关声明：[bt_mesh_init](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga521def6f74467a9bd3f2757c6aabd405)、[bt_mesh_prov](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md)、[bt_mesh_comp](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md)。

初始化 Mesh 支持。

<a id="r_ga69fc65f4e07e6007388473f139e5d8d8"></a>

```c
void bt_mesh_reset (void)
```

相关声明：[bt_mesh_reset](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga69fc65f4e07e6007388473f139e5d8d8)。

重置本地 Mesh 节点（Local Mesh Node）的状态。

<a id="r_ga6c209dbad6881f1e9634d9b7d42f2c34"></a>

```c
int bt_mesh_suspend (void)
```

相关声明：[bt_mesh_suspend](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga6c209dbad6881f1e9634d9b7d42f2c34)。

临时挂起 Mesh 网络（Suspend Mesh Network）。

<a id="r_gaa9114ce8941e641dbb23828d7c0451fd"></a>

```c
int bt_mesh_resume (void)
```

相关声明：[bt_mesh_resume](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#gaa9114ce8941e641dbb23828d7c0451fd)。

恢复已挂起的 Mesh 网络（Resume Mesh Network）。

<a id="r_ga3fdc601bd036477f6bdf212667c6b0c9"></a>

```c
void bt_mesh_iv_update_test (bool enable)
```

相关声明：[bt_mesh_iv_update_test](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga3fdc601bd036477f6bdf212667c6b0c9)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

切换 IV 更新测试模式（IV Update Test Mode）。

<a id="r_gacdf00423b03057fdf3a4207ee579eb74"></a>

```c
bool bt_mesh_iv_update (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_iv_update](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#gacdf00423b03057fdf3a4207ee579eb74)。

切换 IV 更新状态（IV Update State）。

<a id="r_ga7964f5b1abb7b12728e4ec224c95c849"></a>

```c
int bt_mesh_lpn_set (bool enable)
```

相关声明：[bt_mesh_lpn_set](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga7964f5b1abb7b12728e4ec224c95c849)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

切换本地设备的低功耗特性（Low Power Feature）。

<a id="r_ga3fd66605950a55e299ca3a7cc697d453"></a>

```c
int bt_mesh_lpn_poll (void)
```

相关声明：[bt_mesh_lpn_poll](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga3fd66605950a55e299ca3a7cc697d453)。

发送朋友轮询消息（Friend Poll Message）。

<a id="r_ga28b9b1d7d732e300be8d4bbffdbad391"></a>

```c
int bt_mesh_friend_terminate (uint16_t lpn_addr)
```

相关声明：[bt_mesh_friend_terminate](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga28b9b1d7d732e300be8d4bbffdbad391)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

终止友谊关系（Friendship）。

<a id="r_ga62f9a72c4e9dc5e4f3f42bd4df4fe452"></a>

```c
void bt_mesh_rpl_pending_store (uint16_t addr)
```

相关声明：[bt_mesh_rpl_pending_store](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga62f9a72c4e9dc5e4f3f42bd4df4fe452)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将待存储的重放保护列表条目（RPL Entries）写入持久化存储（Persistent Storage）。

<a id="r_ga20fe74e33e6a35c452cd076c78aa4f05"></a>

```c
const uint8_t * bt_mesh_va_uuid_get (uint16_t addr, const uint8_t *uuid, uint16_t *retaddr)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_va_uuid_get](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga20fe74e33e6a35c452cd076c78aa4f05)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

遍历存储的标签 UUID（Label UUIDs）。


## 10.5\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P102_main.h_源码浏览.md)
- [bt_mesh_dev_capabilities](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md)
- [bt_mesh_prov](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md)
- [bt_mesh_lpn_cb](../bluetooth_mesh_model_reference/P072_bt_mesh_lpn_cb_结构体.md)
- [bt_mesh_friend_cb](../bluetooth_mesh_model_reference/P061_bt_mesh_friend_cb_结构体.md)
- [BT_MESH_NET_PRIMARY](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga0d6985da3c7be76732ee103458b77121)
- [BT_MESH_FEAT_RELAY](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#gac588eefe83db94784a420ce063f02b55)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_MESH_FEAT_PROXY](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#gaee648ce202316c56d4d588cb0ad5aeb4)
- [BT_MESH_FEAT_FRIEND](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga8f27086b3bc3c4a6e14621836f9f8e80)
- [BT_MESH_FEAT_LOW_POWER](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#gaad71a36c82b4e4d3fa334ecff5cc0171)
- [BT_MESH_FEAT_SUPPORTED](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#gac337fd8688d70e862974e010ad42a11b)
- [BT_MESH_LPN_CB_DEFINE](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#gac18d4ce09495a8ade098a6320bb26ec2)
- [BT_MESH_FRIEND_CB_DEFINE](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga4f00fa03af86b39e24140eb09c51ca4c)
- [BT_MESH_PROV_AUTH_CMAC_AES128_AES_CCM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggabe5586cff0697e137730a52728978681affa8679d8be1a12714a34ed09c3b05dd)
- [BT_MESH_PROV_AUTH_HMAC_SHA256_AES_CCM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggabe5586cff0697e137730a52728978681a292bf2e4d29f0bd0d746bbb871f2ee5a)
- [BT_MESH_STATIC_OOB_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggabec90bd95082b9dc8fa3ca27a9d7bc66a30e46fe23e508029b570e1f107b38d40)
- [BT_MESH_OOB_AUTH_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggabec90bd95082b9dc8fa3ca27a9d7bc66a61f859a15fabc8d9fd278dabe5a86a37)
- [bt_mesh_output_action_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga5512b81ef7eeb45b0a12ef62234c8795)
- [BT_MESH_NO_OUTPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795ad009060fd1f501c8362a63e6c020b113)
- [BT_MESH_BLINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795ac38333011b4f76b036a04e41f1f71e83)
- [BT_MESH_BEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795ae50031a39d19181df17ee6de1a12272c)
- [BT_MESH_VIBRATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795ab45021af96db0465f5edc6e0ea7b6079)
- [BT_MESH_DISPLAY_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795a3586ffa3e36247e0d90b83c3f075e591)
- [BT_MESH_DISPLAY_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795aa07d600f2afe278729bb4e35d41bf29b)
- [bt_mesh_input_action_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf71f3dbdef6b8c085e9a4f068e1f60c5)
- [BT_MESH_NO_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ac721b070cad51f1cd9aa1f0b60e59056)
- [BT_MESH_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ae4902ce51142fa49d2d5e97165d6f51c)
- [BT_MESH_TWIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ad6f22211d09614181cb5b0f42300a9ee)
- [BT_MESH_ENTER_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf71f3dbdef6b8c085e9a4f068e1f60c5aa0de3817e863d1f06888100de24fb4b0)
- [BT_MESH_ENTER_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf71f3dbdef6b8c085e9a4f068e1f60c5a5d6bd8e6110c8f53245840aead4201c2)
- [bt_mesh_prov_bearer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaa157eb0fee30c28092a11993872b8fdd)
- [BT_MESH_PROV_ADV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaa157eb0fee30c28092a11993872b8fdda5142f018a5426a047688c6507b3af4f8)
- [BT_MESH_PROV_GATT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaa157eb0fee30c28092a11993872b8fdda27c9c1278acc887214a4a30294bf52d8)
- [BT_MESH_PROV_REMOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaa157eb0fee30c28092a11993872b8fdda4222d03b09ba43b6ea772738b8987501)
- [bt_mesh_prov_oob_info_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf93f7b49dada5c3f7accc54663648e48)
- [BT_MESH_PROV_OOB_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a487ffb56c8c15a37b69fa1699fff301a)
- [BT_MESH_PROV_OOB_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48ad861e8de3c1fbc1658a6d0fba38785dd)
- [BT_MESH_PROV_OOB_2D_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a34d005022a75446a386006f7690a473e)
- [BT_MESH_PROV_OOB_BAR_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48abe8fd10b49a7bb6c7499eb73ae3876d3)
- [BT_MESH_PROV_OOB_NFC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48ad9b4089a740d47950c02b4389d29df56)
- [BT_MESH_PROV_OOB_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48ac5d40459453afebc841f32e1f0b33fbc)
- [BT_MESH_PROV_OOB_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a8553379d579a418a6453669323b18088)
- [BT_MESH_PROV_OOB_CERTIFICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a00eb3ba6b7940b02d2fe3892100f497e)
- [BT_MESH_PROV_OOB_RECORDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48aa10724108397ab8d48a3aac2817992f2)
- [BT_MESH_PROV_OOB_ON_BOX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48adbbc3c3829bb7caf1a4a5fd2066f3b4a)
- [BT_MESH_PROV_OOB_IN_BOX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48ae855a27a18bfb6ea03f0ff6165e4a291)
- [BT_MESH_PROV_OOB_ON_PAPER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a137946e3d53b996b77bebeda5fa930cb)
- [BT_MESH_PROV_OOB_IN_MANUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a4a8a7e4ab87cf360abdb167076349072)
- [BT_MESH_PROV_OOB_ON_DEV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48aa73dd9517eec86e51b48d256fc9660da)
- [bt_mesh_input_string](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga2592abf429b40ef9242bce26f5bd085e)
- [bt_mesh_input_numeric](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gabc9d68157928c2b343eddd08ef314d27)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_prov_remote_pub_key_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gae33b5b6e9650b49d46494b4a81b18674)
- [bt_mesh_auth_method_set_input](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga80be35bf7287e62cb47d8fba99d648a9)
- [bt_mesh_auth_method_set_output](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gad66ccc725a1cfdf2b79076f22f853f84)
- [bt_mesh_auth_method_set_static](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga7b6024dc32f6ec7f26cbf91545911084)
- [bt_mesh_auth_method_set_none](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gabab41ebdcae2eaa109e03cb2d8fa78c6)
- [bt_mesh_prov_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga6c8dc1b09d4cde8738be83c992b860a9)
- [bt_mesh_prov_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gac7e084e7d12a93377d49b1c3d6313399)
- [bt_mesh_provision](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga4ed6e078c1c0f197758c8dbb23db30f6)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_mesh_provision_adv](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga0bfae4ebda53052cfa027c3a7ae51ec8)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [bt_mesh_provision_gatt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga60666e0d7629caf36026974621bae664)
- [bt_mesh_provision_remote](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga9fc414e4e15d6b3ab0dae5483ed62982)
- [bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)
- [bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)
- [bt_mesh_reprovision_remote](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaa02583390f635ac251d22ed9ff953974)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_mesh_is_provisioned](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga0307e62001ba7fa303ed311ebc47f116)
- [bt_mesh_init](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga521def6f74467a9bd3f2757c6aabd405)
- [bt_mesh_comp](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md)
- [bt_mesh_reset](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga69fc65f4e07e6007388473f139e5d8d8)
- [bt_mesh_suspend](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga6c209dbad6881f1e9634d9b7d42f2c34)
- [bt_mesh_resume](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#gaa9114ce8941e641dbb23828d7c0451fd)
- [bt_mesh_iv_update_test](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga3fdc601bd036477f6bdf212667c6b0c9)
- [bt_mesh_iv_update](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#gacdf00423b03057fdf3a4207ee579eb74)
- [bt_mesh_lpn_set](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga7964f5b1abb7b12728e4ec224c95c849)
- [bt_mesh_lpn_poll](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga3fd66605950a55e299ca3a7cc697d453)
- [bt_mesh_friend_terminate](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga28b9b1d7d732e300be8d4bbffdbad391)
- [bt_mesh_rpl_pending_store](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga62f9a72c4e9dc5e4f3f42bd4df4fe452)
- [bt_mesh_va_uuid_get](../api_coap_trusted_topic_reference/P002_蓝牙网状网络（Bluetooth Mesh）.md#ga20fe74e33e6a35c452cd076c78aa4f05)

<a id="header-details"></a>

---

[上一章](P009_zephyr__dt-bindings__gpio__m2-memory-connector.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__bluetooth__classic__pbap.h_文件参考.md)
