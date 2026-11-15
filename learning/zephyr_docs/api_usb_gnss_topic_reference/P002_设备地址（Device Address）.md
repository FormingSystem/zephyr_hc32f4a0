---
id: learning.zephyr-docs.api-usb-gnss-topic-reference.page-2
title: 设备地址（Device Address）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_设备地址（Device Address）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙设备地址（Bluetooth Device Address）的定义和工具。

<a id="details"></a>

蓝牙设备地址定义与辅助接口（Bluetooth Device Address Definitions and Utilities）。起始版本（Since）：1.0。接口版本（Version）：1.0.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Faddr_5Ft"></a>

```c
struct bt_addr_t
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

蓝牙（Bluetooth）设备地址。

<a id="r_bt_5Faddr_5Fle_5Ft"></a>

```c
struct bt_addr_le_t
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

蓝牙低功耗（Bluetooth LE）设备地址。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga1717d2b4e61b28637be8a5f78685a3c4"></a>

```c
#define BT_ADDR_LE_PUBLIC 0x00
```

相关声明：[BT_ADDR_LE_PUBLIC](#ga1717d2b4e61b28637be8a5f78685a3c4)。

<a id="r_ga6e81e967527b5418ee6cbc6d72c5aef9"></a>

```c
#define BT_ADDR_LE_RANDOM 0x01
```

相关声明：[BT_ADDR_LE_RANDOM](#ga6e81e967527b5418ee6cbc6d72c5aef9)。

<a id="r_ga1fd60d5eb4c8a6d8f4df06eaba85fb96"></a>

```c
#define BT_ADDR_LE_PUBLIC_ID 0x02
```

相关声明：[BT_ADDR_LE_PUBLIC_ID](#ga1fd60d5eb4c8a6d8f4df06eaba85fb96)。

<a id="r_gafdf2572991427d95bb44d1a5ee2ad85a"></a>

```c
#define BT_ADDR_LE_RANDOM_ID 0x03
```

相关声明：[BT_ADDR_LE_RANDOM_ID](#gafdf2572991427d95bb44d1a5ee2ad85a)。

<a id="r_gad02c40564a140300efda28ecb15674be"></a>

```c
#define BT_ADDR_LE_UNRESOLVED
```

相关声明：[BT_ADDR_LE_UNRESOLVED](#gad02c40564a140300efda28ecb15674be)。

<a id="r_gab2ddd85c5972a53da0aee3974edc0258"></a>

```c
#define BT_ADDR_LE_ANONYMOUS
```

相关声明：[BT_ADDR_LE_ANONYMOUS](#gab2ddd85c5972a53da0aee3974edc0258)。

<a id="r_ga6b6f56325b5136d2719f02eecc780d49"></a>

```c
#define BT_ADDR_SIZE 6
```

相关声明：[BT_ADDR_SIZE](#ga6b6f56325b5136d2719f02eecc780d49)。

标准蓝牙地址（Standard Bluetooth Address）的长度，单位为字节（Bytes）。

<a id="r_ga2656b9a936bf8cb9f1cc86668fca6108"></a>

```c
#define BT_ADDR_LE_SIZE 7
```

相关声明：[BT_ADDR_LE_SIZE](#ga2656b9a936bf8cb9f1cc86668fca6108)。

蓝牙低功耗地址（LE Bluetooth Address）的字节长度。

<a id="r_ga40ddc9769e38b7537bbb4e8002de592a"></a>

```c
#define BT_ADDR_ANY (&bt_addr_any)
```

相关声明：[BT_ADDR_ANY](#ga40ddc9769e38b7537bbb4e8002de592a)、[bt_addr_any](#gadd64afda1a14cbc2740f205e90169152)。

蓝牙设备的任意地址（Any Address），并非有效地址。

<a id="r_gacb24d83ded350176fc96dfc0f5dde6be"></a>

```c
#define BT_ADDR_NONE (&bt_addr_none)
```

相关声明：[BT_ADDR_NONE](#gacb24d83ded350176fc96dfc0f5dde6be)、[bt_addr_none](#ga0b2f611fbd28b066d261b81303c4b93f)。

蓝牙设备的无地址值（None Address），并非有效地址。

<a id="r_ga17e9efacd50c682b2f709c217e920d48"></a>

```c
#define BT_ADDR_LE_ANY (&bt_addr_le_any)
```

相关声明：[BT_ADDR_LE_ANY](#ga17e9efacd50c682b2f709c217e920d48)、[bt_addr_le_any](#ga40c282f720d13b5d24a2dd62bfdceb73)。

蓝牙低功耗设备的任意地址（Any Address），并非有效地址。

<a id="r_gadfcc0281e453cba990b623631c26f80b"></a>

```c
#define BT_ADDR_LE_NONE (&bt_addr_le_none)
```

相关声明：[BT_ADDR_LE_NONE](#gadfcc0281e453cba990b623631c26f80b)、[bt_addr_le_none](#gaefa17a553b6f8e9ad599e8db7538e1b8)。

蓝牙低功耗设备的无地址值（None Address），并非有效地址。

<a id="r_ga32abc1a2e827542efea5b9cb05a57fbc"></a>

```c
#define BT_ADDR_IS_RPA(a)
```

相关声明：[BT_ADDR_IS_RPA](#ga32abc1a2e827542efea5b9cb05a57fbc)。

检查蓝牙低功耗随机地址是否为可解析私有地址（Resolvable Private Address）。

<a id="r_gaa8745bff73c42a693cb76e42755b2bf9"></a>

```c
#define BT_ADDR_IS_NRPA(a)
```

相关声明：[BT_ADDR_IS_NRPA](#gaa8745bff73c42a693cb76e42755b2bf9)。

检查蓝牙低功耗随机地址是否为不可解析私有地址（Non-resolvable Private Address）。

<a id="r_ga0cb3aa4d48cf41d8485b570ef0e7447a"></a>

```c
#define BT_ADDR_IS_STATIC(a)
```

相关声明：[BT_ADDR_IS_STATIC](#ga0cb3aa4d48cf41d8485b570ef0e7447a)。

检查蓝牙低功耗随机地址是否为静态地址（Static Address）。

<a id="r_ga52a0bd596e726dff39b247dfbc58406d"></a>

```c
#define BT_ADDR_SET_RPA(a)
```

相关声明：[BT_ADDR_SET_RPA](#ga52a0bd596e726dff39b247dfbc58406d)。

将蓝牙低功耗随机地址设为可解析私有地址（Resolvable Private Address）。

<a id="r_ga6b23035316e9bdd071e10ecc803fcdbc"></a>

```c
#define BT_ADDR_SET_NRPA(a)
```

相关声明：[BT_ADDR_SET_NRPA](#ga6b23035316e9bdd071e10ecc803fcdbc)。

将蓝牙低功耗随机地址设为不可解析私有地址（Non-resolvable Private Address）。

<a id="r_gaa6261bf0b96099b58f0a0c3674ce5713"></a>

```c
#define BT_ADDR_SET_STATIC(a)
```

相关声明：[BT_ADDR_SET_STATIC](#gaa6261bf0b96099b58f0a0c3674ce5713)。

将蓝牙低功耗随机地址设为静态地址（Static Address）。

<a id="r_ga8097c3b80a5647b0b951d29aa30a397d"></a>

```c
#define BT_ADDR_STR_LEN 18
```

相关声明：[BT_ADDR_STR_LEN](#ga8097c3b80a5647b0b951d29aa30a397d)。

用于蓝牙地址的用户字符串缓冲区推荐长度（Recommended Length）。

<a id="r_gae0df0067c55eb4388625bb62f3d7e235"></a>

```c
#define BT_ADDR_LE_STR_LEN 20
```

相关声明：[BT_ADDR_LE_STR_LEN](#gae0df0067c55eb4388625bb62f3d7e235)。

用于蓝牙低功耗地址的用户字符串缓冲区推荐长度（Recommended Length）。

<a id="r_ga26db53edfcda476f641e50a0a89ba197"></a>

```c
#define bt_addr_str(_addr)
```

相关声明：[bt_addr_str](#ga26db53edfcda476f641e50a0a89ba197)。

将蓝牙地址（Bluetooth Address）转换为字符串。

<a id="r_gaecb794d5df4845477cf2545e8ea1b079"></a>

```c
#define bt_addr_le_str(_addr)
```

相关声明：[bt_addr_le_str](#gaecb794d5df4845477cf2545e8ea1b079)。

将蓝牙低功耗地址（Bluetooth LE Address）转换为字符串。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_ga41ff9419098728f037c3e97d29c30ba9"></a>

```c
static int bt_addr_cmp (const bt_addr_t *a, const bt_addr_t *b)
```

相关声明：[bt_addr_cmp](#ga41ff9419098728f037c3e97d29c30ba9)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

比较蓝牙设备地址（Bluetooth Device Addresses）。

<a id="r_gadecf8fe8e183a11a4ff569bc0d673ec1"></a>

```c
static bool bt_addr_eq (const bt_addr_t *a, const bt_addr_t *b)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_addr_eq](#gadecf8fe8e183a11a4ff569bc0d673ec1)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

判断两个蓝牙设备地址（Bluetooth Device Addresses）是否相等。

<a id="r_ga588d392f51372ff2951c3ff39da22f12"></a>

```c
static int bt_addr_le_cmp (const bt_addr_le_t *a, const bt_addr_le_t *b)
```

相关声明：[bt_addr_le_cmp](#ga588d392f51372ff2951c3ff39da22f12)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

比较蓝牙低功耗设备地址（Bluetooth LE Device Addresses）。

<a id="r_ga8644e77108f029088adb203e5392016b"></a>

```c
static bool bt_addr_le_eq (const bt_addr_le_t *a, const bt_addr_le_t *b)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_addr_le_eq](#ga8644e77108f029088adb203e5392016b)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

判断两个蓝牙低功耗设备地址（Bluetooth LE Device Addresses）是否相等。

<a id="r_ga5a8284cf34d0835d725dab31d710ea4c"></a>

```c
static void bt_addr_copy (bt_addr_t *dst, const bt_addr_t *src)
```

相关声明：[bt_addr_copy](#ga5a8284cf34d0835d725dab31d710ea4c)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

复制蓝牙设备地址（Bluetooth Device Address）。

<a id="r_gac6c9b20f17936efaa082fe63aedc2138"></a>

```c
static void bt_addr_le_copy (bt_addr_le_t *dst, const bt_addr_le_t *src)
```

相关声明：[bt_addr_le_copy](#gac6c9b20f17936efaa082fe63aedc2138)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

复制蓝牙低功耗设备地址（Bluetooth LE Device Address）。

<a id="r_ga756d59776902ad1ae2df1c032e91589c"></a>

```c
static void bt_addr_le_copy_addr (bt_addr_le_t *dst, const bt_addr_t *src, uint8_t src_type)
```

相关声明：[bt_addr_le_copy_addr](#ga756d59776902ad1ae2df1c032e91589c)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据蓝牙设备地址及类型，复制生成蓝牙低功耗设备地址（Bluetooth LE Device Address）。

<a id="r_gaf2d38888131c9e8bdbc820b415c14082"></a>

```c
int bt_addr_le_create_nrpa (bt_addr_le_t *addr)
```

相关声明：[bt_addr_le_create_nrpa](#gaf2d38888131c9e8bdbc820b415c14082)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

创建蓝牙低功耗随机不可解析私有地址（Random Non-resolvable Private Address）。

<a id="r_gad1b43f2f0ab58ec2c5ceaaa0d2cbc444"></a>

```c
int bt_addr_le_create_static (bt_addr_le_t *addr)
```

相关声明：[bt_addr_le_create_static](#gad1b43f2f0ab58ec2c5ceaaa0d2cbc444)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

创建蓝牙低功耗随机静态地址（Random Static Address）。

<a id="r_ga42bcee6b5aadde7ccdbe243df25043bc"></a>

```c
static bool bt_addr_le_is_rpa (const bt_addr_le_t *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_addr_le_is_rpa](#ga42bcee6b5aadde7ccdbe243df25043bc)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

检查蓝牙低功耗地址是否为随机可解析私有地址（Random Private Resolvable Address）。

<a id="r_ga7a6acc7a9267ae2645aeee38e553b8b3"></a>

```c
static bool bt_addr_le_is_identity (const bt_addr_le_t *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_addr_le_is_identity](#ga7a6acc7a9267ae2645aeee38e553b8b3)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

检查蓝牙低功耗地址是否为有效身份地址（Identity Address）。

<a id="r_ga151bdd0ada8635acfebd60f0e203cde2"></a>

```c
static int bt_addr_to_str (const bt_addr_t *addr, char *str, size_t len)
```

相关声明：[bt_addr_to_str](#ga151bdd0ada8635acfebd60f0e203cde2)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

将二进制蓝牙地址（Binary Bluetooth Address）转换为字符串。

<a id="r_ga74a644cd3de081a353a281d80b32b91e"></a>

```c
static int bt_addr_le_to_str (const bt_addr_le_t *addr, char *str, size_t len)
```

相关声明：[bt_addr_le_to_str](#ga74a644cd3de081a353a281d80b32b91e)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

将二进制蓝牙低功耗地址（Binary LE Bluetooth Address）转换为字符串。

<a id="r_gad93410d0161ca84939f4bf983da29c14"></a>

```c
int bt_addr_from_str (const char *str, bt_addr_t *addr)
```

相关声明：[bt_addr_from_str](#gad93410d0161ca84939f4bf983da29c14)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

将蓝牙地址从字符串转换为二进制形式。

<a id="r_ga24752df467449d7cb0dc25e3c4330862"></a>

```c
int bt_addr_le_from_str (const char *str, bt_addr_le_t *addr)
```

相关声明：[bt_addr_le_from_str](#ga24752df467449d7cb0dc25e3c4330862)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

将蓝牙低功耗地址从字符串转换为二进制形式。

<a id="r_ga28baaccd1e89d8939d3a73d759cded09"></a>

```c
int bt_addr_le_rpa_resolve (uint8_t id, const bt_addr_le_t *addr, bt_addr_le_t *resolved_addr)
```

相关声明：[bt_addr_le_rpa_resolve](#ga28baaccd1e89d8939d3a73d759cded09)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

将蓝牙低功耗可解析私有地址（Resolvable Private Address，RPA）解析为其身份地址（Identity Address）。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 2.4\_变量（Variables）

<a id="r_gadd64afda1a14cbc2740f205e90169152"></a>

```c
const bt_addr_t bt_addr_any
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bt_addr_any](#gadd64afda1a14cbc2740f205e90169152)。

<a id="r_ga0b2f611fbd28b066d261b81303c4b93f"></a>

```c
const bt_addr_t bt_addr_none
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bt_addr_none](#ga0b2f611fbd28b066d261b81303c4b93f)。

<a id="r_ga40c282f720d13b5d24a2dd62bfdceb73"></a>

```c
const bt_addr_le_t bt_addr_le_any
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_addr_le_any](#ga40c282f720d13b5d24a2dd62bfdceb73)。

<a id="r_gaefa17a553b6f8e9ad599e8db7538e1b8"></a>

```c
const bt_addr_le_t bt_addr_le_none
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_addr_le_none](#gaefa17a553b6f8e9ad599e8db7538e1b8)。

## 2.5\_详细说明（Detailed Documentation）

<a id="ga40ddc9769e38b7537bbb4e8002de592a"></a>

### `BT_ADDR_ANY`

```c
#define BT_ADDR_ANY (&bt_addr_any)
```

```c
#include <zephyr/bluetooth/addr.h>
```

蓝牙设备的任意地址（Any Address），并非有效地址。

<a id="gaa8745bff73c42a693cb76e42755b2bf9"></a>

### `BT_ADDR_IS_NRPA`

```c
#define BT_ADDR_IS_NRPA ( a)
```

```c
#include <zephyr/bluetooth/addr.h>
```

展开值（Value）：

```c
(((a)->val[5] & 0xc0) == 0x00)
```

检查蓝牙低功耗随机地址是否为不可解析私有地址（Non-resolvable Private Address）。

<a id="ga32abc1a2e827542efea5b9cb05a57fbc"></a>

### `BT_ADDR_IS_RPA`

```c
#define BT_ADDR_IS_RPA ( a)
```

```c
#include <zephyr/bluetooth/addr.h>
```

展开值（Value）：

```c
(((a)->val[5] & 0xc0) == 0x40)
```

检查蓝牙低功耗随机地址是否为可解析私有地址（Resolvable Private Address）。

<a id="ga0cb3aa4d48cf41d8485b570ef0e7447a"></a>

### `BT_ADDR_IS_STATIC`

```c
#define BT_ADDR_IS_STATIC ( a)
```

```c
#include <zephyr/bluetooth/addr.h>
```

展开值（Value）：

```c
(((a)->val[5] & 0xc0) == 0xc0)
```

检查蓝牙低功耗随机地址是否为静态地址（Static Address）。

<a id="gab2ddd85c5972a53da0aee3974edc0258"></a>

### `BT_ADDR_LE_ANONYMOUS`

```c
#define BT_ADDR_LE_ANONYMOUS
```

```c
#include <zephyr/bluetooth/addr.h>
```

展开值（Value）：

```c
0xFF /* No address provided
* (anonymous advertisement)
*/
```

<a id="ga17e9efacd50c682b2f709c217e920d48"></a>

### `BT_ADDR_LE_ANY`

```c
#define BT_ADDR_LE_ANY (&bt_addr_le_any)
```

```c
#include <zephyr/bluetooth/addr.h>
```

蓝牙低功耗设备的任意地址（Any Address），并非有效地址。

<a id="gadfcc0281e453cba990b623631c26f80b"></a>

### `BT_ADDR_LE_NONE`

```c
#define BT_ADDR_LE_NONE (&bt_addr_le_none)
```

```c
#include <zephyr/bluetooth/addr.h>
```

蓝牙低功耗设备的无地址值（None Address），并非有效地址。

<a id="ga1717d2b4e61b28637be8a5f78685a3c4"></a>

### `BT_ADDR_LE_PUBLIC`

```c
#define BT_ADDR_LE_PUBLIC 0x00
```

```c
#include <zephyr/bluetooth/addr.h>
```

<a id="ga1fd60d5eb4c8a6d8f4df06eaba85fb96"></a>

### `BT_ADDR_LE_PUBLIC_ID`

```c
#define BT_ADDR_LE_PUBLIC_ID 0x02
```

```c
#include <zephyr/bluetooth/addr.h>
```

<a id="ga6e81e967527b5418ee6cbc6d72c5aef9"></a>

### `BT_ADDR_LE_RANDOM`

```c
#define BT_ADDR_LE_RANDOM 0x01
```

```c
#include <zephyr/bluetooth/addr.h>
```

<a id="gafdf2572991427d95bb44d1a5ee2ad85a"></a>

### `BT_ADDR_LE_RANDOM_ID`

```c
#define BT_ADDR_LE_RANDOM_ID 0x03
```

```c
#include <zephyr/bluetooth/addr.h>
```

<a id="ga2656b9a936bf8cb9f1cc86668fca6108"></a>

### `BT_ADDR_LE_SIZE`

```c
#define BT_ADDR_LE_SIZE 7
```

```c
#include <zephyr/bluetooth/addr.h>
```

蓝牙低功耗地址（LE Bluetooth Address）的字节长度。

未采用紧凑布局（Packed），因此不能使用 `sizeof()`。

<a id="gaecb794d5df4845477cf2545e8ea1b079"></a>

### `bt_addr_le_str`

```c
#define bt_addr_le_str ( _addr)
```

```c
#include <zephyr/bluetooth/addr.h>
```

展开值（Value）：

```c
bt_addr_le_tmp_str(_addr).str
```

将蓝牙低功耗地址（Bluetooth LE Address）转换为字符串。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_addr` | 指向蓝牙低功耗地址（Bluetooth LE Address，`bt_addr_le_t`）的指针。 |

**返回（Returns）**：返回值（Returns）：字符串指针，仅在完整表达式（Full Expression）结束之前有效。实际使用中，这主要适合用作 `printk`／`printf` 或日志调用的输入参数。

<a id="gae0df0067c55eb4388625bb62f3d7e235"></a>

### `BT_ADDR_LE_STR_LEN`

```c
#define BT_ADDR_LE_STR_LEN 20
```

```c
#include <zephyr/bluetooth/addr.h>
```

用于蓝牙低功耗地址的用户字符串缓冲区推荐长度（Recommended Length）。

建议长度保证地址转换输出不会丢失所处理地址的有用信息。格式（Format）：`P:XX:XX:XX:XX:XX:XX` 或 `R:XX:XX:XX:XX:XX:XX`。

<a id="gad02c40564a140300efda28ecb15674be"></a>

### `BT_ADDR_LE_UNRESOLVED`

```c
#define BT_ADDR_LE_UNRESOLVED
```

```c
#include <zephyr/bluetooth/addr.h>
```

展开值（Value）：

```c
0xFE /* Resolvable Private Address
* (Controller unable to resolve)
*/
```

<a id="gacb24d83ded350176fc96dfc0f5dde6be"></a>

### `BT_ADDR_NONE`

```c
#define BT_ADDR_NONE (&bt_addr_none)
```

```c
#include <zephyr/bluetooth/addr.h>
```

蓝牙设备的无地址值（None Address），并非有效地址。

<a id="ga6b23035316e9bdd071e10ecc803fcdbc"></a>

### `BT_ADDR_SET_NRPA`

```c
#define BT_ADDR_SET_NRPA ( a)
```

```c
#include <zephyr/bluetooth/addr.h>
```

展开值（Value）：

```c
((a)->val[5] &= 0x3f)
```

将蓝牙低功耗随机地址设为不可解析私有地址（Non-resolvable Private Address）。

<a id="ga52a0bd596e726dff39b247dfbc58406d"></a>

### `BT_ADDR_SET_RPA`

```c
#define BT_ADDR_SET_RPA ( a)
```

```c
#include <zephyr/bluetooth/addr.h>
```

展开值（Value）：

```c
((a)->val[5] = (((a)->val[5] & 0x3f) | 0x40))
```

将蓝牙低功耗随机地址设为可解析私有地址（Resolvable Private Address）。

<a id="gaa6261bf0b96099b58f0a0c3674ce5713"></a>

### `BT_ADDR_SET_STATIC`

```c
#define BT_ADDR_SET_STATIC ( a)
```

```c
#include <zephyr/bluetooth/addr.h>
```

展开值（Value）：

```c
((a)->val[5] |= 0xc0)
```

将蓝牙低功耗随机地址设为静态地址（Static Address）。

<a id="ga6b6f56325b5136d2719f02eecc780d49"></a>

### `BT_ADDR_SIZE`

```c
#define BT_ADDR_SIZE 6
```

```c
#include <zephyr/bluetooth/addr.h>
```

标准蓝牙地址（Standard Bluetooth Address）的长度，单位为字节（Bytes）。

<a id="ga26db53edfcda476f641e50a0a89ba197"></a>

### `bt_addr_str`

```c
#define bt_addr_str ( _addr)
```

```c
#include <zephyr/bluetooth/addr.h>
```

展开值（Value）：

```c
bt_addr_tmp_str(_addr).str
```

将蓝牙地址（Bluetooth Address）转换为字符串。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_addr` | 指向蓝牙地址（Bluetooth Address，`bt_addr_t`）的指针。 |

**返回（Returns）**：返回值（Returns）：字符串指针，仅在完整表达式（Full Expression）结束之前有效。实际使用中，这主要适合用作 `printk`／`printf` 或日志调用的输入参数。

<a id="ga8097c3b80a5647b0b951d29aa30a397d"></a>

### `BT_ADDR_STR_LEN`

```c
#define BT_ADDR_STR_LEN 18
```

```c
#include <zephyr/bluetooth/addr.h>
```

用于蓝牙地址的用户字符串缓冲区推荐长度（Recommended Length）。

建议长度保证地址转换（Address Conversion）输出不会丢失所处理地址的有用信息。

<a id="ga41ff9419098728f037c3e97d29c30ba9"></a>

### `bt_addr_cmp()`

```c
int bt_addr_cmp ( const bt_addr_t * a, const bt_addr_t * b )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/addr.h>
```

比较蓝牙设备地址（Bluetooth Device Addresses）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 参与比较的第一个蓝牙设备地址（Bluetooth Device Address）。 |
| `b` | 参与比较的第二个蓝牙设备地址（Bluetooth Device Address）。 |

**返回（Returns）**：返回值（Returns）：`a < b` 时为负值，`a == b` 时为 0，否则为正值。

<a id="ga5a8284cf34d0835d725dab31d710ea4c"></a>

### `bt_addr_copy()`

```c
void bt_addr_copy ( bt_addr_t * dst, const bt_addr_t * src )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/addr.h>
```

复制蓝牙设备地址（Bluetooth Device Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dst` | 蓝牙设备地址目标缓冲区（Bluetooth Device Address Destination Buffer）。 |
| `src` | 蓝牙设备地址源缓冲区（Bluetooth Device Address Source Buffer）。 |

<a id="gadecf8fe8e183a11a4ff569bc0d673ec1"></a>

### `bt_addr_eq()`

```c
bool bt_addr_eq ( const bt_addr_t * a, const bt_addr_t * b )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/addr.h>
```

判断两个蓝牙设备地址（Bluetooth Device Addresses）是否相等。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 两个地址（Address）相等时。 |
| `false` | 其他情况。 |

<a id="gad93410d0161ca84939f4bf983da29c14"></a>

### `bt_addr_from_str()`

```c
int bt_addr_from_str ( const char * str, bt_addr_t * addr )
```

```c
#include <zephyr/bluetooth/addr.h>
```

将蓝牙地址从字符串转换为二进制形式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] str` | 蓝牙地址的字符串表示（String Representation of a Bluetooth Address）。 |
| `[out] addr` | 用于存储蓝牙地址（Bluetooth Address）的缓冲区地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。解析得到的地址（Address）存储在 `addr` 中。 |

**返回（Returns）**：返回值（Returns）：`-EINVAL` 表示地址字符串无效，`str` 不是格式正确的蓝牙地址（Bluetooth Address）。

<a id="ga588d392f51372ff2951c3ff39da22f12"></a>

### `bt_addr_le_cmp()`

```c
int bt_addr_le_cmp ( const bt_addr_le_t * a, const bt_addr_le_t * b )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/addr.h>
```

比较蓝牙低功耗设备地址（Bluetooth LE Device Addresses）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 参与比较的第一个蓝牙低功耗设备地址（Bluetooth LE Device Address）。 |
| `b` | 参与比较的第二个蓝牙低功耗设备地址（Bluetooth LE Device Address）。 |

**返回（Returns）**：返回值（Returns）：`a < b` 时为负值，`a == b` 时为 0，否则为正值。

**参阅（See Also）**：另请参见（See Also）：`bt_addr_le_eq`。

<a id="gac6c9b20f17936efaa082fe63aedc2138"></a>

### `bt_addr_le_copy()`

```c
void bt_addr_le_copy ( bt_addr_le_t * dst, const bt_addr_le_t * src )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/addr.h>
```

复制蓝牙低功耗设备地址（Bluetooth LE Device Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dst` | 蓝牙低功耗设备地址目标缓冲区（Bluetooth LE Device Address Destination Buffer）。 |
| `src` | 蓝牙低功耗设备地址源缓冲区（Bluetooth LE Device Address Source Buffer）。 |

<a id="ga756d59776902ad1ae2df1c032e91589c"></a>

### `bt_addr_le_copy_addr()`

```c
void bt_addr_le_copy_addr ( bt_addr_le_t * dst, const bt_addr_t * src, uint8_t src_type )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/addr.h>
```

根据蓝牙设备地址及类型，复制生成蓝牙低功耗设备地址（Bluetooth LE Device Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dst` | 蓝牙低功耗设备地址目标缓冲区（Bluetooth LE Device Address Destination Buffer）。 |
| `src` | 蓝牙设备地址源缓冲区（Bluetooth Device Address Source Buffer）。 |
| `src_type` | 蓝牙设备地址源类型（Bluetooth Device Address Source Type）。 |

<a id="gaf2d38888131c9e8bdbc820b415c14082"></a>

### `bt_addr_le_create_nrpa()`

```c
int bt_addr_le_create_nrpa ( bt_addr_le_t * addr)
```

```c
#include <zephyr/bluetooth/addr.h>
```

创建蓝牙低功耗随机不可解析私有地址（Random Non-resolvable Private Address）。

<a id="gad1b43f2f0ab58ec2c5ceaaa0d2cbc444"></a>

### `bt_addr_le_create_static()`

```c
int bt_addr_le_create_static ( bt_addr_le_t * addr)
```

```c
#include <zephyr/bluetooth/addr.h>
```

创建蓝牙低功耗随机静态地址（Random Static Address）。

<a id="ga8644e77108f029088adb203e5392016b"></a>

### `bt_addr_le_eq()`

```c
bool bt_addr_le_eq ( const bt_addr_le_t * a, const bt_addr_le_t * b )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/addr.h>
```

判断两个蓝牙低功耗设备地址（Bluetooth LE Device Addresses）是否相等。

仅当类型（Type）相同，且 48 位地址的数值也相同时，两个蓝牙低功耗地址（Bluetooth LE Address）才相等。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 两个地址（Address）相等时。 |
| `false` | 其他情况。 |

<a id="ga24752df467449d7cb0dc25e3c4330862"></a>

### `bt_addr_le_from_str()`

```c
int bt_addr_le_from_str ( const char * str, bt_addr_le_t * addr )
```

```c
#include <zephyr/bluetooth/addr.h>
```

将蓝牙低功耗地址从字符串转换为二进制形式。

字符串必须使用 `bt_addr_le_to_str()` 生成的格式：公开地址（Public Address）为 `P:XX:XX:XX:XX:XX:XX`，随机地址（Random Address）为 `R:XX:XX:XX:XX:XX:XX`。类型前缀和十六进制数字均不区分大小写。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] str` | 蓝牙低功耗地址（LE Bluetooth Address）的字符串表示。 |
| `[out] addr` | 用于存储蓝牙低功耗地址（LE Bluetooth Address）的缓冲区地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。解析得到的地址（Address）存储在 `addr` 中。 |
| `-EINVAL` | 地址字符串无效：`str` 的类型前缀未知，或不是格式正确的蓝牙地址（Bluetooth Address）。 |

<a id="ga7a6acc7a9267ae2645aeee38e553b8b3"></a>

### `bt_addr_le_is_identity()`

```c
bool bt_addr_le_is_identity ( const bt_addr_le_t * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/addr.h>
```

检查蓝牙低功耗地址是否为有效身份地址（Identity Address）。

有效的蓝牙低功耗身份地址（Bluetooth LE Identity Address）必须是公开地址（Public Address）或静态随机地址（Random Static Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 蓝牙低功耗设备地址（Bluetooth LE Device Address）。 |

**返回（Returns）**：返回值（Returns）：地址为有效身份地址（Identity Address）时，返回 `true`。

<a id="ga42bcee6b5aadde7ccdbe243df25043bc"></a>

### `bt_addr_le_is_rpa()`

```c
bool bt_addr_le_is_rpa ( const bt_addr_le_t * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/addr.h>
```

检查蓝牙低功耗地址是否为随机可解析私有地址（Random Private Resolvable Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 蓝牙低功耗设备地址（Bluetooth LE Device Address）。 |

**返回（Returns）**：返回值（Returns）：地址为可解析私有随机地址（Random Private Resolvable Address）时，返回 `true`。

<a id="ga28baaccd1e89d8939d3a73d759cded09"></a>

### `bt_addr_le_rpa_resolve()`

```c
int bt_addr_le_rpa_resolve ( uint8_t id, const bt_addr_le_t * addr, bt_addr_le_t * resolved_addr )
```

```c
#include <zephyr/bluetooth/addr.h>
```

将蓝牙低功耗可解析私有地址（Resolvable Private Address，RPA）解析为其身份地址（Identity Address）。

本函数使用主机的身份解析密钥数据库（Identity Resolving Key Database，IRK Database），尝试将可解析私有地址（RPA）解析为对应的身份地址（Identity Address），即公开地址或静态随机地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] id` | 使用其 IRK 数据库的本地身份（Local Identity）。必须小于 `CONFIG_BT_ID_MAX`。 |
| `[in] addr` | 要解析的可解析私有地址（RPA）。 |
| `[out] resolved_addr` | 成功时，包含解析得到的身份地址（Identity Address），即公开地址 `BT_ADDR_LE_PUBLIC` 或静态随机地址 `BT_ADDR_LE_RANDOM`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。地址已解析，`resolved_addr` 包含身份地址（Identity Address）。 |
| `-ENOENT` | `addr` 是可解析私有地址（RPA），但数据库中未找到匹配的身份解析密钥（IRK），因此无法解析该地址。 |
| `-EINVAL` | 参数无效：`addr` 或 `resolved_addr` 为 `NULL`，`id` 无效，或 `addr` 不是可解析私有地址（RPA）。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_PRIVACY` 时可用。

<a id="ga74a644cd3de081a353a281d80b32b91e"></a>

### `bt_addr_le_to_str()`

```c
int bt_addr_le_to_str ( const bt_addr_le_t * addr, char * str, size_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/addr.h>
```

将二进制蓝牙低功耗地址（Binary LE Bluetooth Address）转换为字符串。

将蓝牙低功耗地址（LE Bluetooth Address）转换为以下格式的字符串表示：

- 公开地址（Public Address）采用 `P:XX:XX:XX:XX:XX:XX`。
- 随机地址（Random Address）采用 `R:XX:XX:XX:XX:XX:XX`。

带有额外 HCI 层信息的地址类型值，例如 `BT_ADDR_LE_PUBLIC_ID` 和 `BT_ADDR_LE_RANDOM_ID`，会按其基本类型（公开地址或随机地址）格式化。表示未解析 RPA 的 HCI 哨兵值（Sentinel）`BT_ADDR_LE_UNRESOLVED` 和表示匿名广播者的 `BT_ADDR_LE_ANONYMOUS` 均按随机地址格式化。额外信息不包含在字符串中，必须由调用者单独传递。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 包含二进制蓝牙低功耗地址（Binary LE Bluetooth Address）的缓冲区地址。 |
| `str` | 用户缓冲区地址；该缓冲区须有足够空间存储由二进制低功耗地址（Binary LE Address）格式化得到的字符串。 |
| `len` | 要复制到用户字符串缓冲区的数据长度。建议取值参见 `BT_ADDR_LE_STR_LEN`。 |

**返回（Returns）**：返回值（Returns）：从二进制地址（Binary Address）成功格式化得到的字节数。

<a id="ga151bdd0ada8635acfebd60f0e203cde2"></a>

### `bt_addr_to_str()`

```c
int bt_addr_to_str ( const bt_addr_t * addr, char * str, size_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/addr.h>
```

将二进制蓝牙地址（Binary Bluetooth Address）转换为字符串。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 包含二进制蓝牙地址（Binary Bluetooth Address）的缓冲区地址。 |
| `str` | 用户缓冲区地址；该缓冲区须有足够空间存储由二进制地址（Binary Address）格式化得到的字符串。 |
| `len` | 要复制到用户字符串缓冲区的数据长度。建议取值参见 `BT_ADDR_STR_LEN`。 |

**返回（Returns）**：返回值（Returns）：从二进制地址（Binary Address）成功格式化得到的字节数。

<a id="gadd64afda1a14cbc2740f205e90169152"></a>

### `bt_addr_any`

```c
const bt_addr_t bt_addr_any
```

声明属性：`extern`。

```c
#include <zephyr/bluetooth/addr.h>
```

<a id="ga40c282f720d13b5d24a2dd62bfdceb73"></a>

### `bt_addr_le_any`

```c
const bt_addr_le_t bt_addr_le_any
```

声明属性：`extern`。

```c
#include <zephyr/bluetooth/addr.h>
```

<a id="gaefa17a553b6f8e9ad599e8db7538e1b8"></a>

### `bt_addr_le_none`

```c
const bt_addr_le_t bt_addr_le_none
```

声明属性：`extern`。

```c
#include <zephyr/bluetooth/addr.h>
```

<a id="ga0b2f611fbd28b066d261b81303c4b93f"></a>

### `bt_addr_none`

```c
const bt_addr_t bt_addr_none
```

声明属性：`extern`。

```c
#include <zephyr/bluetooth/addr.h>
```


## 2.6\_原页交叉引用（Cross References）

- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/bluetooth/addr.h](../api_file_clock_network_reference/P001_zephyr__bluetooth__addr.h_文件参考.md)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [CONFIG_BT_PRIVACY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PRIVACY)
- [CONFIG_BT_ID_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ID_MAX)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[上一章](P001_USB-C 设备 API（USB-C Device API）.md) · [返回大纲](大纲.md) · [下一章](P003_经过时间服务（Elapsed Time Service，ETS）。.md)
