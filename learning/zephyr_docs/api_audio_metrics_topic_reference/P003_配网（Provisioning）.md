---
id: learning.zephyr-docs.api-audio-metrics-topic-reference.page-3
title: 配网（Provisioning）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_配网（Provisioning）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

配网（Provisioning）

<a id="details"></a>

配网（Provisioning）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

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

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.2\_枚举（Enumerations）

<a id="r_gabe5586cff0697e137730a52728978681"></a>

```c
enum { BT_MESH_PROV_AUTH_CMAC_AES128_AES_CCM , BT_MESH_PROV_AUTH_HMAC_SHA256_AES_CCM }
```

相关声明：[BT_MESH_PROV_AUTH_CMAC_AES128_AES_CCM](#ggabe5586cff0697e137730a52728978681affa8679d8be1a12714a34ed09c3b05dd)、[BT_MESH_PROV_AUTH_HMAC_SHA256_AES_CCM](#ggabe5586cff0697e137730a52728978681a292bf2e4d29f0bd0d746bbb871f2ee5a)。

可用的认证算法（Authentication Algorithms）。

<a id="r_gabec90bd95082b9dc8fa3ca27a9d7bc66"></a>

```c
enum { BT_MESH_STATIC_OOB_AVAILABLE = (1UL << (0)) , BT_MESH_OOB_AUTH_REQUIRED = (1UL << (1)) }
```

相关声明：[BT_MESH_STATIC_OOB_AVAILABLE](#ggabec90bd95082b9dc8fa3ca27a9d7bc66a30e46fe23e508029b570e1f107b38d40)、[BT_MESH_OOB_AUTH_REQUIRED](#ggabec90bd95082b9dc8fa3ca27a9d7bc66a61f859a15fabc8d9fd278dabe5a86a37)。

带外类型字段值（OOB Type Field Values）。

<a id="r_ga5512b81ef7eeb45b0a12ef62234c8795"></a>

```c
enum bt_mesh_output_action_t { BT_MESH_NO_OUTPUT = 0 , BT_MESH_BLINK = (1UL << (0)) , BT_MESH_BEEP = (1UL << (1)) , BT_MESH_VIBRATE = (1UL << (2)) , BT_MESH_DISPLAY_NUMBER = (1UL << (3)) , BT_MESH_DISPLAY_STRING = (1UL << (4)) }
```

相关声明：[bt_mesh_output_action_t](#ga5512b81ef7eeb45b0a12ef62234c8795)、[BT_MESH_NO_OUTPUT](#gga5512b81ef7eeb45b0a12ef62234c8795ad009060fd1f501c8362a63e6c020b113)、[BT_MESH_BLINK](#gga5512b81ef7eeb45b0a12ef62234c8795ac38333011b4f76b036a04e41f1f71e83)、[BT_MESH_BEEP](#gga5512b81ef7eeb45b0a12ef62234c8795ae50031a39d19181df17ee6de1a12272c)、[BT_MESH_VIBRATE](#gga5512b81ef7eeb45b0a12ef62234c8795ab45021af96db0465f5edc6e0ea7b6079)、[BT_MESH_DISPLAY_NUMBER](#gga5512b81ef7eeb45b0a12ef62234c8795a3586ffa3e36247e0d90b83c3f075e591)、[BT_MESH_DISPLAY_STRING](#gga5512b81ef7eeb45b0a12ef62234c8795aa07d600f2afe278729bb4e35d41bf29b)。

可用的配网输出认证动作（Provisioning Output Authentication Actions）。

<a id="r_gaf71f3dbdef6b8c085e9a4f068e1f60c5"></a>

```c
enum bt_mesh_input_action_t { BT_MESH_NO_INPUT = 0 , BT_MESH_PUSH = (1UL << (0)) , BT_MESH_TWIST = (1UL << (1)) , BT_MESH_ENTER_NUMBER = (1UL << (2)) , BT_MESH_ENTER_STRING = (1UL << (3)) }
```

相关声明：[bt_mesh_input_action_t](#gaf71f3dbdef6b8c085e9a4f068e1f60c5)、[BT_MESH_NO_INPUT](#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ac721b070cad51f1cd9aa1f0b60e59056)、[BT_MESH_PUSH](#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ae4902ce51142fa49d2d5e97165d6f51c)、[BT_MESH_TWIST](#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ad6f22211d09614181cb5b0f42300a9ee)、[BT_MESH_ENTER_NUMBER](#ggaf71f3dbdef6b8c085e9a4f068e1f60c5aa0de3817e863d1f06888100de24fb4b0)、[BT_MESH_ENTER_STRING](#ggaf71f3dbdef6b8c085e9a4f068e1f60c5a5d6bd8e6110c8f53245840aead4201c2)。

可用的配网输入认证动作（Provisioning Input Authentication Actions）。

<a id="r_gaa157eb0fee30c28092a11993872b8fdd"></a>

```c
enum bt_mesh_prov_bearer_t { BT_MESH_PROV_ADV = (1UL << (0)) , BT_MESH_PROV_GATT = (1UL << (1)) , BT_MESH_PROV_REMOTE = (1UL << (2)) }
```

相关声明：[bt_mesh_prov_bearer_t](#gaa157eb0fee30c28092a11993872b8fdd)、[BT_MESH_PROV_ADV](#ggaa157eb0fee30c28092a11993872b8fdda5142f018a5426a047688c6507b3af4f8)、[BT_MESH_PROV_GATT](#ggaa157eb0fee30c28092a11993872b8fdda27c9c1278acc887214a4a30294bf52d8)、[BT_MESH_PROV_REMOTE](#ggaa157eb0fee30c28092a11993872b8fdda4222d03b09ba43b6ea772738b8987501)。

可用的配网承载（Provisioning Bearers）。

<a id="r_gaf93f7b49dada5c3f7accc54663648e48"></a>

```c
enum bt_mesh_prov_oob_info_t { BT_MESH_PROV_OOB_OTHER = (1UL << (0)) , BT_MESH_PROV_OOB_URI = (1UL << (1)) , BT_MESH_PROV_OOB_2D_CODE = (1UL << (2)) , BT_MESH_PROV_OOB_BAR_CODE = (1UL << (3)) , BT_MESH_PROV_OOB_NFC = (1UL << (4)) , BT_MESH_PROV_OOB_NUMBER = (1UL << (5)) , BT_MESH_PROV_OOB_STRING = (1UL << (6)) , BT_MESH_PROV_OOB_CERTIFICATE = (1UL << (7)) , BT_MESH_PROV_OOB_RECORDS = (1UL << (8)) , BT_MESH_PROV_OOB_ON_BOX = (1UL << (11)) , BT_MESH_PROV_OOB_IN_BOX = (1UL << (12)) , BT_MESH_PROV_OOB_ON_PAPER = (1UL << (13)) , BT_MESH_PROV_OOB_IN_MANUAL = (1UL << (14)) , BT_MESH_PROV_OOB_ON_DEV = (1UL << (15)) }
```

相关声明：[bt_mesh_prov_oob_info_t](#gaf93f7b49dada5c3f7accc54663648e48)、[BT_MESH_PROV_OOB_OTHER](#ggaf93f7b49dada5c3f7accc54663648e48a487ffb56c8c15a37b69fa1699fff301a)、[BT_MESH_PROV_OOB_URI](#ggaf93f7b49dada5c3f7accc54663648e48ad861e8de3c1fbc1658a6d0fba38785dd)、[BT_MESH_PROV_OOB_2D_CODE](#ggaf93f7b49dada5c3f7accc54663648e48a34d005022a75446a386006f7690a473e)、[BT_MESH_PROV_OOB_BAR_CODE](#ggaf93f7b49dada5c3f7accc54663648e48abe8fd10b49a7bb6c7499eb73ae3876d3)、[BT_MESH_PROV_OOB_NFC](#ggaf93f7b49dada5c3f7accc54663648e48ad9b4089a740d47950c02b4389d29df56)、[BT_MESH_PROV_OOB_NUMBER](#ggaf93f7b49dada5c3f7accc54663648e48ac5d40459453afebc841f32e1f0b33fbc)、[BT_MESH_PROV_OOB_STRING](#ggaf93f7b49dada5c3f7accc54663648e48a8553379d579a418a6453669323b18088)、[BT_MESH_PROV_OOB_CERTIFICATE](#ggaf93f7b49dada5c3f7accc54663648e48a00eb3ba6b7940b02d2fe3892100f497e)、[BT_MESH_PROV_OOB_RECORDS](#ggaf93f7b49dada5c3f7accc54663648e48aa10724108397ab8d48a3aac2817992f2)、[BT_MESH_PROV_OOB_ON_BOX](#ggaf93f7b49dada5c3f7accc54663648e48adbbc3c3829bb7caf1a4a5fd2066f3b4a)、[BT_MESH_PROV_OOB_IN_BOX](#ggaf93f7b49dada5c3f7accc54663648e48ae855a27a18bfb6ea03f0ff6165e4a291)、[BT_MESH_PROV_OOB_ON_PAPER](#ggaf93f7b49dada5c3f7accc54663648e48a137946e3d53b996b77bebeda5fa930cb)、[BT_MESH_PROV_OOB_IN_MANUAL](#ggaf93f7b49dada5c3f7accc54663648e48a4a8a7e4ab87cf360abdb167076349072)、[BT_MESH_PROV_OOB_ON_DEV](#ggaf93f7b49dada5c3f7accc54663648e48aa73dd9517eec86e51b48d256fc9660da)。

带外信息位置（Out of Band Information Location）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.3\_函数（Functions）

<a id="r_ga2592abf429b40ef9242bce26f5bd085e"></a>

```c
int bt_mesh_input_string (const char *str)
```

相关声明：[bt_mesh_input_string](#ga2592abf429b40ef9242bce26f5bd085e)。

提供配网输入带外字符串（Provisioning Input OOB String）。

<a id="r_gabc9d68157928c2b343eddd08ef314d27"></a>

```c
int bt_mesh_input_numeric (uint8_t *numeric, size_t size)
```

相关声明：[bt_mesh_input_numeric](#gabc9d68157928c2b343eddd08ef314d27)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提供配网输入带外数值（Provisioning Input OOB Numeric Value）。

<a id="r_gae33b5b6e9650b49d46494b4a81b18674"></a>

```c
int bt_mesh_prov_remote_pub_key_set (const uint8_t public_key[64])
```

相关声明：[bt_mesh_prov_remote_pub_key_set](#gae33b5b6e9650b49d46494b4a81b18674)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提供设备公钥（Device Public Key）。

<a id="r_ga80be35bf7287e62cb47d8fba99d648a9"></a>

```c
int bt_mesh_auth_method_set_input (bt_mesh_input_action_t action, uint8_t size)
```

相关声明：[bt_mesh_auth_method_set_input](#ga80be35bf7287e62cb47d8fba99d648a9)、[bt_mesh_input_action_t](#gaf71f3dbdef6b8c085e9a4f068e1f60c5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用输入带外认证（Input OOB Authentication）。

<a id="r_gad66ccc725a1cfdf2b79076f22f853f84"></a>

```c
int bt_mesh_auth_method_set_output (bt_mesh_output_action_t action, uint8_t size)
```

相关声明：[bt_mesh_auth_method_set_output](#gad66ccc725a1cfdf2b79076f22f853f84)、[bt_mesh_output_action_t](#ga5512b81ef7eeb45b0a12ef62234c8795)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用输出带外认证（Output OOB Authentication）。

<a id="r_ga7b6024dc32f6ec7f26cbf91545911084"></a>

```c
int bt_mesh_auth_method_set_static (const uint8_t *static_val, uint8_t size)
```

相关声明：[bt_mesh_auth_method_set_static](#ga7b6024dc32f6ec7f26cbf91545911084)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用静态带外认证（Static OOB Authentication）。

<a id="r_gabab41ebdcae2eaa109e03cb2d8fa78c6"></a>

```c
int bt_mesh_auth_method_set_none (void)
```

相关声明：[bt_mesh_auth_method_set_none](#gabab41ebdcae2eaa109e03cb2d8fa78c6)。

不使用带外认证（OOB Authentication）。

<a id="r_ga6c8dc1b09d4cde8738be83c992b860a9"></a>

```c
int bt_mesh_prov_enable (bt_mesh_prov_bearer_t bearers)
```

相关声明：[bt_mesh_prov_enable](#ga6c8dc1b09d4cde8738be83c992b860a9)、[bt_mesh_prov_bearer_t](#gaa157eb0fee30c28092a11993872b8fdd)。

启用指定配网承载（Provisioning Bearers）。

<a id="r_gac7e084e7d12a93377d49b1c3d6313399"></a>

```c
int bt_mesh_prov_disable (bt_mesh_prov_bearer_t bearers)
```

相关声明：[bt_mesh_prov_disable](#gac7e084e7d12a93377d49b1c3d6313399)、[bt_mesh_prov_bearer_t](#gaa157eb0fee30c28092a11993872b8fdd)。

禁用指定配网承载（Provisioning Bearers）。

<a id="r_ga4ed6e078c1c0f197758c8dbb23db30f6"></a>

```c
int bt_mesh_provision (const uint8_t net_key[16], uint16_t net_idx, uint8_t flags, uint32_t iv_index, uint16_t addr, const uint8_t dev_key[16])
```

相关声明：[bt_mesh_provision](#ga4ed6e078c1c0f197758c8dbb23db30f6)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为本地 Mesh 节点配网（Provision）。

<a id="r_ga0bfae4ebda53052cfa027c3a7ae51ec8"></a>

```c
int bt_mesh_provision_adv (const uint8_t uuid[16], uint16_t net_idx, uint16_t addr, uint8_t attention_duration)
```

相关声明：[bt_mesh_provision_adv](#ga0bfae4ebda53052cfa027c3a7ae51ec8)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用 PB-ADV 为 Mesh 节点配网（Provision）。

<a id="r_ga60666e0d7629caf36026974621bae664"></a>

```c
int bt_mesh_provision_gatt (const uint8_t uuid[16], uint16_t net_idx, uint16_t addr, uint8_t attention_duration)
```

相关声明：[bt_mesh_provision_gatt](#ga60666e0d7629caf36026974621bae664)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用 PB-GATT 为 Mesh 节点配网（Provision）。

<a id="r_ga9fc414e4e15d6b3ab0dae5483ed62982"></a>

```c
int bt_mesh_provision_remote (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, const uint8_t uuid[16], uint16_t net_idx, uint16_t addr)
```

相关声明：[bt_mesh_provision_remote](#ga9fc414e4e15d6b3ab0dae5483ed62982)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

使用 PB-Remote 为 Mesh 节点配网（Provision）。

<a id="r_gaa02583390f635ac251d22ed9ff953974"></a>

```c
int bt_mesh_reprovision_remote (struct bt_mesh_rpr_cli *cli, struct bt_mesh_rpr_node *srv, uint16_t addr, bool comp_change)
```

相关声明：[bt_mesh_reprovision_remote](#gaa02583390f635ac251d22ed9ff953974)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

使用 PB-Remote 为 Mesh 节点重新配网（Reprovision）。

<a id="r_ga0307e62001ba7fa303ed311ebc47f116"></a>

```c
bool bt_mesh_is_provisioned (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_is_provisioned](#ga0307e62001ba7fa303ed311ebc47f116)。

检查本地节点是否已配网（Provisioned）。

## 3.4\_详细说明（Detailed Documentation）

<a id="gabe5586cff0697e137730a52728978681"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

可用的认证算法（Authentication Algorithms）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_PROV_AUTH_CMAC_AES128_AES_CCM` |  |
| `BT_MESH_PROV_AUTH_HMAC_SHA256_AES_CCM` |  |

<a id="gabec90bd95082b9dc8fa3ca27a9d7bc66"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

带外类型字段值（OOB Type Field Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_STATIC_OOB_AVAILABLE` | 有可用的静态带外信息（Static Out-of-Band，Static OOB）。 |
| `BT_MESH_OOB_AUTH_REQUIRED` | 要求带外认证（OOB Authentication）。 |

<a id="gaf71f3dbdef6b8c085e9a4f068e1f60c5"></a>

### `bt_mesh_input_action_t`

```c
enum bt_mesh_input_action_t
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

可用的配网输入认证动作（Provisioning Input Authentication Actions）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_NO_INPUT` |  |
| `BT_MESH_PUSH` | 按压（Push）。 |
| `BT_MESH_TWIST` | 旋转（Twist）。 |
| `BT_MESH_ENTER_NUMBER` | 输入数字（Input Number）。 |
| `BT_MESH_ENTER_STRING` | 输入字母数字字符（Input Alphanumeric）。 |

<a id="ga5512b81ef7eeb45b0a12ef62234c8795"></a>

### `bt_mesh_output_action_t`

```c
enum bt_mesh_output_action_t
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

可用的配网输出认证动作（Provisioning Output Authentication Actions）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_NO_OUTPUT` |  |
| `BT_MESH_BLINK` | 闪烁（Blink）。 |
| `BT_MESH_BEEP` | 蜂鸣（Beep）。 |
| `BT_MESH_VIBRATE` | 振动（Vibrate）。 |
| `BT_MESH_DISPLAY_NUMBER` | 输出数字（Output Numeric）。 |
| `BT_MESH_DISPLAY_STRING` | 输出字母数字字符（Output Alphanumeric）。 |

<a id="gaa157eb0fee30c28092a11993872b8fdd"></a>

### `bt_mesh_prov_bearer_t`

```c
enum bt_mesh_prov_bearer_t
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

可用的配网承载（Provisioning Bearers）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_PROV_ADV` | 基于广播的配网承载（PB-ADV Bearer）。 |
| `BT_MESH_PROV_GATT` | 基于 GATT 的配网承载（PB-GATT Bearer）。 |
| `BT_MESH_PROV_REMOTE` | 远程配网承载（PB-Remote Bearer）。 |

<a id="gaf93f7b49dada5c3f7accc54663648e48"></a>

### `bt_mesh_prov_oob_info_t`

```c
enum bt_mesh_prov_oob_info_t
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

带外信息位置（Out of Band Information Location）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_PROV_OOB_OTHER` | 其他（Other）。 |
| `BT_MESH_PROV_OOB_URI` | 电子形式／统一资源标识符（Electronic / URI）。 |
| `BT_MESH_PROV_OOB_2D_CODE` | 二维机器可读码（2D Machine-Readable Code）。 |
| `BT_MESH_PROV_OOB_BAR_CODE` | 条形码（Bar Code）。 |
| `BT_MESH_PROV_OOB_NFC` | 近场通信（Near Field Communication，NFC）。 |
| `BT_MESH_PROV_OOB_NUMBER` | 数字（Number）。 |
| `BT_MESH_PROV_OOB_STRING` | 字符串。 |
| `BT_MESH_PROV_OOB_CERTIFICATE` | 支持基于证书的配网（Certificate-Based Provisioning）。 |
| `BT_MESH_PROV_OOB_RECORDS` | 支持配网记录（Provisioning Records）。 |
| `BT_MESH_PROV_OOB_ON_BOX` | 包装盒上（On Box）。 |
| `BT_MESH_PROV_OOB_IN_BOX` | 包装盒内（Inside Box）。 |
| `BT_MESH_PROV_OOB_ON_PAPER` | 纸张上（On Piece of Paper）。 |
| `BT_MESH_PROV_OOB_IN_MANUAL` | 手册内（Inside Manual）。 |
| `BT_MESH_PROV_OOB_ON_DEV` | 设备上（On Device）。 |

<a id="ga80be35bf7287e62cb47d8fba99d648a9"></a>

### `bt_mesh_auth_method_set_input()`

```c
int bt_mesh_auth_method_set_input ( bt_mesh_input_action_t action, uint8_t size )
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

使用输入带外认证（Input OOB Authentication）。

仅限配网器（Provisioner Only）。

指示未配网设备（Unprovisioned Device）使用指定的输入带外认证动作（Input OOB Authentication Action）。使用 `BT_MESH_PUSH`、`BT_MESH_TWIST` 或 `BT_MESH_ENTER_NUMBER` 时，将调用 `bt_mesh_prov::output_numeric` 回调并传入一个随机数，用户必须在未配网设备上输入该随机数。

使用 `BT_MESH_ENTER_STRING` 时，将调用 `bt_mesh_prov::output_string` 回调并传入一个随机字符串，用户必须在未配网设备上输入该字符串。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `action` | 未配网设备使用的认证动作（Authentication Action）。 |
| `size` | 认证大小（Authentication Size）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gabab41ebdcae2eaa109e03cb2d8fa78c6"></a>

### `bt_mesh_auth_method_set_none()`

```c
int bt_mesh_auth_method_set_none ( void )
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

不使用带外认证（OOB Authentication）。

仅限配网器（Provisioner Only）。

为新设备配网（Provisioning）时不使用任何认证。这是默认行为。

**警告（Warning）**：警告（Warning）：不使用认证会使 Mesh 网络暴露于冒充攻击（Impersonation Attacks）；攻击者可假扮未配网设备以获得网络访问权限。强烈建议使用认证。

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gad66ccc725a1cfdf2b79076f22f853f84"></a>

### `bt_mesh_auth_method_set_output()`

```c
int bt_mesh_auth_method_set_output ( bt_mesh_output_action_t action, uint8_t size )
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

使用输出带外认证（Output OOB Authentication）。

仅限配网器（Provisioner Only）。

指示未配网设备使用指定的输出带外认证动作（Output OOB Authentication Action）。将调用 `bt_mesh_prov::input` 回调。

使用 `BT_MESH_BLINK`、`BT_MESH_BEEP`、`BT_MESH_VIBRATE` 或 `BT_MESH_DISPLAY_NUMBER` 时，应用必须调用 `bt_mesh_input_numeric`，传入未配网设备所指示的随机数。

使用 `BT_MESH_DISPLAY_STRING` 时，应用必须调用 `bt_mesh_input_string`，传入未配网设备显示的随机字符串。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `action` | 未配网设备使用的认证动作（Authentication Action）。 |
| `size` | 认证大小（Authentication Size）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga7b6024dc32f6ec7f26cbf91545911084"></a>

### `bt_mesh_auth_method_set_static()`

```c
int bt_mesh_auth_method_set_static ( const uint8_t * static_val, uint8_t size )
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

使用静态带外认证（Static OOB Authentication）。

仅限配网器（Provisioner Only）。

指示未配网设备使用静态带外认证（Static OOB Authentication），并在配网时使用给定的静态认证值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `static_val` | 静态带外值（Static OOB value）。 |
| `size` | 静态带外值（Static OOB Value）的大小。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gabc9d68157928c2b343eddd08ef314d27"></a>

### `bt_mesh_input_numeric()`

```c
int bt_mesh_input_numeric ( uint8_t * numeric, size_t size )
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

提供配网输入带外数值（Provisioning Input OOB Numeric Value）。

预期在 `bt_mesh_prov::input` 回调以 `BT_MESH_ENTER_NUMBER` 作为动作被调用之后，再调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `numeric` | 指向小端序（Little-Endian）数值的指针。 |
| `size` | 数值大小，单位为字节；这不是 OOB 大小。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga2592abf429b40ef9242bce26f5bd085e"></a>

### `bt_mesh_input_string()`

```c
int bt_mesh_input_string ( const char * str)
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

提供配网输入带外字符串（Provisioning Input OOB String）。

预期在 `bt_mesh_prov::input` 回调以 `BT_MESH_ENTER_STRING` 作为动作被调用之后，再调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `str` | 字符串。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga0307e62001ba7fa303ed311ebc47f116"></a>

### `bt_mesh_is_provisioned()`

```c
bool bt_mesh_is_provisioned ( void )
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

检查本地节点是否已配网（Provisioned）。

此 API 可检查本地节点是否已配网（Provisioned）。例如，它可用于确定闪存中是否存有网络信息，即调用 `settings_load()` 后网络是否已恢复。

**返回（Returns）**：返回值（Returns）：节点已配网时为 `true`，否则为 `false`。

<a id="gac7e084e7d12a93377d49b1c3d6313399"></a>

### `bt_mesh_prov_disable()`

```c
int bt_mesh_prov_disable ( bt_mesh_prov_bearer_t bearers)
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

禁用指定配网承载（Provisioning Bearers）。

禁用一个或多个配网承载（Provisioning Bearers）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearers` | 各配网承载（Provisioning Bearers）的按位或组合。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga6c8dc1b09d4cde8738be83c992b860a9"></a>

### `bt_mesh_prov_enable()`

```c
int bt_mesh_prov_enable ( bt_mesh_prov_bearer_t bearers)
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

启用指定配网承载（Provisioning Bearers）。

启用一个或多个配网承载（Provisioning Bearers）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearers` | 各配网承载（Provisioning Bearers）的按位或组合。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gae33b5b6e9650b49d46494b4a81b18674"></a>

### `bt_mesh_prov_remote_pub_key_set()`

```c
int bt_mesh_prov_remote_pub_key_set ( const uint8_t public_key[64])
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

提供设备公钥（Device Public Key）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `public_key` | 采用大端序（Big-Endian）的设备公钥（Device Public Key）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga4ed6e078c1c0f197758c8dbb23db30f6"></a>

### `bt_mesh_provision()`

```c
int bt_mesh_provision ( const uint8_t net_key[16], uint16_t net_idx, uint8_t flags, uint32_t iv_index, uint16_t addr, const uint8_t dev_key[16] )
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

为本地 Mesh 节点配网（Provision）。

应用通常不应直接使用此 API。唯一例外是测试场景：希望在没有实际外部配网器（Provisioner）的情况下手动配网。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_key` | 网络密钥（Network Key）。 |
| `net_idx` | 网络密钥索引（Network Key Index）。 |
| `flags` | 配网标志（Provisioning Flags）。 |
| `iv_index` | IV 索引（IV Index）。 |
| `addr` | 主元素地址（Primary element address）。 |
| `dev_key` | 设备密钥（Device Key）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga0bfae4ebda53052cfa027c3a7ae51ec8"></a>

### `bt_mesh_provision_adv()`

```c
int bt_mesh_provision_adv ( const uint8_t uuid[16], uint16_t net_idx, uint16_t addr, uint8_t attention_duration )
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

使用 PB-ADV 为 Mesh 节点配网（Provision）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `uuid` | 通用唯一标识符（UUID）。 |
| `net_idx` | 网络密钥索引（Network Key Index）。 |
| `addr` | 要分配给远端设备的地址。`addr` 为 0 时，选择最低的可用地址。 |
| `attention_duration` | 要发送给远端设备的注意持续时间（Attention Duration）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga60666e0d7629caf36026974621bae664"></a>

### `bt_mesh_provision_gatt()`

```c
int bt_mesh_provision_gatt ( const uint8_t uuid[16], uint16_t net_idx, uint16_t addr, uint8_t attention_duration )
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

使用 PB-GATT 为 Mesh 节点配网（Provision）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `uuid` | 通用唯一标识符（UUID）。 |
| `net_idx` | 网络密钥索引（Network Key Index）。 |
| `addr` | 要分配给远端设备的地址。`addr` 为 0 时，选择最低的可用地址。 |
| `attention_duration` | 要发送给远端设备的注意持续时间（Attention Duration）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga9fc414e4e15d6b3ab0dae5483ed62982"></a>

### `bt_mesh_provision_remote()`

```c
int bt_mesh_provision_remote ( struct bt_mesh_rpr_cli * cli, const struct bt_mesh_rpr_node * srv, const uint8_t uuid[16], uint16_t net_idx, uint16_t addr )
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

使用 PB-Remote 为 Mesh 节点配网（Provision）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 用于执行配网的远程配网客户端模型（Remote Provisioning Client Model）。 |
| `srv` | 用于通过隧道传递配网过程的远程配网服务器（Remote Provisioning Server）。 |
| `uuid` | 未配网节点的 UUID。 |
| `net_idx` | 要提供给未配网节点的网络密钥索引（Network Key Index）。 |
| `addr` | 要分配给远端设备的地址。`addr` 为 0 时，选择最低的可用地址。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gaa02583390f635ac251d22ed9ff953974"></a>

### `bt_mesh_reprovision_remote()`

```c
int bt_mesh_reprovision_remote ( struct bt_mesh_rpr_cli * cli, struct bt_mesh_rpr_node * srv, uint16_t addr, bool comp_change )
```

```c
#include <zephyr/bluetooth/mesh/main.h>
```

使用 PB-Remote 为 Mesh 节点重新配网（Reprovision）。

重新配网（Reprovisioning）可用于更改其他设备的设备密钥（Device Key）、单播地址（Unicast Address）和组成数据（Composition Data）。重新配网使用与普通配网相同的协议，具有相同的安全级别。

重新配网（Reprovisioning）分为三个层级：

- 刷新设备密钥（Device Key）。
- 刷新设备密钥（Device Key）和节点地址（Node Address）。组成数据（Composition Data）可能变化，包括元素数量。
- 目标节点因固件更新或类似流程而改变了组成数据时，刷新设备密钥（Device Key）和组成数据（Composition Data）。

目标节点通过实例化其组成数据（Composition Data）第 128 页，表明组成数据已改变。如果元素数量发生变化，为避免地址重叠，可能还需要调整目标节点的单播地址（Unicast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 用于执行配网的远程配网客户端模型（Remote Provisioning Client Model）。 |
| `srv` | 要重新配网的远程配网服务器（Remote Provisioning Server）。 |
| `addr` | 要分配给远端设备的地址。`addr` 为 0 时，选择最低的可用地址。 |
| `comp_change` | 目标节点已表明其组成数据（Composition Data）发生变化。注意，若并非如此，目标节点将拒绝更新。 |

**说明（Note）**：注（Note）：更改目标节点的单播地址（Unicast Addresses）时，还必须修改所有直接向目标节点任一模型发布消息的节点。

**返回（Returns）**：返回值：成功时为零，否则为负错误码。


## 3.5\_原页交叉引用（Cross References）

- [bt_mesh_dev_capabilities](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md)
- [bt_mesh_prov](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)
- [bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/bluetooth/mesh/main.h](../api_file_flash_test_reference/P010_zephyr__bluetooth__mesh__main.h_文件参考.md)
- [bt_mesh_prov::output_numeric](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#ae7aec4a89f4260a99696bb46207c4338)
- [bt_mesh_prov::output_string](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a28284efee6478637446702d7839f6b8c)
- [bt_mesh_prov::input](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a31eff9c903ac721bbca7ab586dda9e80)
- [settings_load()](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga89c6d618df81f197cc5c1a2018b00648)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggabe5586cff0697e137730a52728978681affa8679d8be1a12714a34ed09c3b05dd"></a>
<a id="ggabe5586cff0697e137730a52728978681a292bf2e4d29f0bd0d746bbb871f2ee5a"></a>
<a id="ggabec90bd95082b9dc8fa3ca27a9d7bc66a30e46fe23e508029b570e1f107b38d40"></a>
<a id="ggabec90bd95082b9dc8fa3ca27a9d7bc66a61f859a15fabc8d9fd278dabe5a86a37"></a>
<a id="ggaf71f3dbdef6b8c085e9a4f068e1f60c5ac721b070cad51f1cd9aa1f0b60e59056"></a>
<a id="ggaf71f3dbdef6b8c085e9a4f068e1f60c5ae4902ce51142fa49d2d5e97165d6f51c"></a>
<a id="ggaf71f3dbdef6b8c085e9a4f068e1f60c5ad6f22211d09614181cb5b0f42300a9ee"></a>
<a id="ggaf71f3dbdef6b8c085e9a4f068e1f60c5aa0de3817e863d1f06888100de24fb4b0"></a>
<a id="ggaf71f3dbdef6b8c085e9a4f068e1f60c5a5d6bd8e6110c8f53245840aead4201c2"></a>
<a id="gga5512b81ef7eeb45b0a12ef62234c8795ad009060fd1f501c8362a63e6c020b113"></a>
<a id="gga5512b81ef7eeb45b0a12ef62234c8795ac38333011b4f76b036a04e41f1f71e83"></a>
<a id="gga5512b81ef7eeb45b0a12ef62234c8795ae50031a39d19181df17ee6de1a12272c"></a>
<a id="gga5512b81ef7eeb45b0a12ef62234c8795ab45021af96db0465f5edc6e0ea7b6079"></a>
<a id="gga5512b81ef7eeb45b0a12ef62234c8795a3586ffa3e36247e0d90b83c3f075e591"></a>
<a id="gga5512b81ef7eeb45b0a12ef62234c8795aa07d600f2afe278729bb4e35d41bf29b"></a>
<a id="ggaa157eb0fee30c28092a11993872b8fdda5142f018a5426a047688c6507b3af4f8"></a>
<a id="ggaa157eb0fee30c28092a11993872b8fdda27c9c1278acc887214a4a30294bf52d8"></a>
<a id="ggaa157eb0fee30c28092a11993872b8fdda4222d03b09ba43b6ea772738b8987501"></a>
<a id="ggaf93f7b49dada5c3f7accc54663648e48a487ffb56c8c15a37b69fa1699fff301a"></a>
<a id="ggaf93f7b49dada5c3f7accc54663648e48ad861e8de3c1fbc1658a6d0fba38785dd"></a>
<a id="ggaf93f7b49dada5c3f7accc54663648e48a34d005022a75446a386006f7690a473e"></a>
<a id="ggaf93f7b49dada5c3f7accc54663648e48abe8fd10b49a7bb6c7499eb73ae3876d3"></a>
<a id="ggaf93f7b49dada5c3f7accc54663648e48ad9b4089a740d47950c02b4389d29df56"></a>
<a id="ggaf93f7b49dada5c3f7accc54663648e48ac5d40459453afebc841f32e1f0b33fbc"></a>
<a id="ggaf93f7b49dada5c3f7accc54663648e48a8553379d579a418a6453669323b18088"></a>
<a id="ggaf93f7b49dada5c3f7accc54663648e48a00eb3ba6b7940b02d2fe3892100f497e"></a>
<a id="ggaf93f7b49dada5c3f7accc54663648e48aa10724108397ab8d48a3aac2817992f2"></a>
<a id="ggaf93f7b49dada5c3f7accc54663648e48adbbc3c3829bb7caf1a4a5fd2066f3b4a"></a>
<a id="ggaf93f7b49dada5c3f7accc54663648e48ae855a27a18bfb6ea03f0ff6165e4a291"></a>
<a id="ggaf93f7b49dada5c3f7accc54663648e48a137946e3d53b996b77bebeda5fa930cb"></a>
<a id="ggaf93f7b49dada5c3f7accc54663648e48a4a8a7e4ab87cf360abdb167076349072"></a>
<a id="ggaf93f7b49dada5c3f7accc54663648e48aa73dd9517eec86e51b48d256fc9660da"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_免提配置文件（Hands Free Profile，HFP）.md) · [返回大纲](大纲.md) · [下一章](P004_集成电路间音频总线（I2S）.md)
