---
id: learning.zephyr-docs.api-file-clock-network-reference.page-1
title: zephyr__bluetooth__addr.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_bluetooth\_\_addr.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙设备地址（Bluetooth Device Address）的定义和工具。

<a id="details"></a>

```c
#include <stdint.h>
#include <string.h>
#include <zephyr/sys/printk.h>
```

查看此文件的源码。

蓝牙设备地址（Bluetooth Device Address）的定义和工具。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

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

## 1.2\_宏定义（Macros）

<a id="r_ga1717d2b4e61b28637be8a5f78685a3c4"></a>

```c
#define BT_ADDR_LE_PUBLIC 0x00
```

相关声明：[BT_ADDR_LE_PUBLIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga1717d2b4e61b28637be8a5f78685a3c4)。

<a id="r_ga6e81e967527b5418ee6cbc6d72c5aef9"></a>

```c
#define BT_ADDR_LE_RANDOM 0x01
```

相关声明：[BT_ADDR_LE_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga6e81e967527b5418ee6cbc6d72c5aef9)。

<a id="r_ga1fd60d5eb4c8a6d8f4df06eaba85fb96"></a>

```c
#define BT_ADDR_LE_PUBLIC_ID 0x02
```

相关声明：[BT_ADDR_LE_PUBLIC_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga1fd60d5eb4c8a6d8f4df06eaba85fb96)。

<a id="r_gafdf2572991427d95bb44d1a5ee2ad85a"></a>

```c
#define BT_ADDR_LE_RANDOM_ID 0x03
```

相关声明：[BT_ADDR_LE_RANDOM_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gafdf2572991427d95bb44d1a5ee2ad85a)。

<a id="r_gad02c40564a140300efda28ecb15674be"></a>

```c
#define BT_ADDR_LE_UNRESOLVED
```

相关声明：[BT_ADDR_LE_UNRESOLVED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gad02c40564a140300efda28ecb15674be)。

<a id="r_gab2ddd85c5972a53da0aee3974edc0258"></a>

```c
#define BT_ADDR_LE_ANONYMOUS
```

相关声明：[BT_ADDR_LE_ANONYMOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gab2ddd85c5972a53da0aee3974edc0258)。

<a id="r_ga6b6f56325b5136d2719f02eecc780d49"></a>

```c
#define BT_ADDR_SIZE 6
```

相关声明：[BT_ADDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga6b6f56325b5136d2719f02eecc780d49)。

标准蓝牙地址（Standard Bluetooth Address）的长度，单位为字节（Bytes）。

<a id="r_ga2656b9a936bf8cb9f1cc86668fca6108"></a>

```c
#define BT_ADDR_LE_SIZE 7
```

相关声明：[BT_ADDR_LE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga2656b9a936bf8cb9f1cc86668fca6108)。

蓝牙低功耗地址（LE Bluetooth Address）的字节长度。

<a id="r_ga40ddc9769e38b7537bbb4e8002de592a"></a>

```c
#define BT_ADDR_ANY (&bt_addr_any)
```

相关声明：[BT_ADDR_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga40ddc9769e38b7537bbb4e8002de592a)、[bt_addr_any](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gadd64afda1a14cbc2740f205e90169152)。

蓝牙设备的任意地址（Any Address），并非有效地址。

<a id="r_gacb24d83ded350176fc96dfc0f5dde6be"></a>

```c
#define BT_ADDR_NONE (&bt_addr_none)
```

相关声明：[BT_ADDR_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gacb24d83ded350176fc96dfc0f5dde6be)、[bt_addr_none](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga0b2f611fbd28b066d261b81303c4b93f)。

蓝牙设备的无地址值（None Address），并非有效地址。

<a id="r_ga17e9efacd50c682b2f709c217e920d48"></a>

```c
#define BT_ADDR_LE_ANY (&bt_addr_le_any)
```

相关声明：[BT_ADDR_LE_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga17e9efacd50c682b2f709c217e920d48)、[bt_addr_le_any](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga40c282f720d13b5d24a2dd62bfdceb73)。

蓝牙低功耗设备的任意地址（Any Address），并非有效地址。

<a id="r_gadfcc0281e453cba990b623631c26f80b"></a>

```c
#define BT_ADDR_LE_NONE (&bt_addr_le_none)
```

相关声明：[BT_ADDR_LE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gadfcc0281e453cba990b623631c26f80b)、[bt_addr_le_none](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gaefa17a553b6f8e9ad599e8db7538e1b8)。

蓝牙低功耗设备的无地址值（None Address），并非有效地址。

<a id="r_ga32abc1a2e827542efea5b9cb05a57fbc"></a>

```c
#define BT_ADDR_IS_RPA(a)
```

相关声明：[BT_ADDR_IS_RPA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga32abc1a2e827542efea5b9cb05a57fbc)。

检查蓝牙低功耗随机地址是否为可解析私有地址（Resolvable Private Address）。

<a id="r_gaa8745bff73c42a693cb76e42755b2bf9"></a>

```c
#define BT_ADDR_IS_NRPA(a)
```

相关声明：[BT_ADDR_IS_NRPA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gaa8745bff73c42a693cb76e42755b2bf9)。

检查蓝牙低功耗随机地址是否为不可解析私有地址（Non-resolvable Private Address）。

<a id="r_ga0cb3aa4d48cf41d8485b570ef0e7447a"></a>

```c
#define BT_ADDR_IS_STATIC(a)
```

相关声明：[BT_ADDR_IS_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga0cb3aa4d48cf41d8485b570ef0e7447a)。

检查蓝牙低功耗随机地址是否为静态地址（Static Address）。

<a id="r_ga52a0bd596e726dff39b247dfbc58406d"></a>

```c
#define BT_ADDR_SET_RPA(a)
```

相关声明：[BT_ADDR_SET_RPA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga52a0bd596e726dff39b247dfbc58406d)。

将蓝牙低功耗随机地址设为可解析私有地址（Resolvable Private Address）。

<a id="r_ga6b23035316e9bdd071e10ecc803fcdbc"></a>

```c
#define BT_ADDR_SET_NRPA(a)
```

相关声明：[BT_ADDR_SET_NRPA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga6b23035316e9bdd071e10ecc803fcdbc)。

将蓝牙低功耗随机地址设为不可解析私有地址（Non-resolvable Private Address）。

<a id="r_gaa6261bf0b96099b58f0a0c3674ce5713"></a>

```c
#define BT_ADDR_SET_STATIC(a)
```

相关声明：[BT_ADDR_SET_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gaa6261bf0b96099b58f0a0c3674ce5713)。

将蓝牙低功耗随机地址设为静态地址（Static Address）。

<a id="r_ga8097c3b80a5647b0b951d29aa30a397d"></a>

```c
#define BT_ADDR_STR_LEN 18
```

相关声明：[BT_ADDR_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga8097c3b80a5647b0b951d29aa30a397d)。

用于蓝牙地址的用户字符串缓冲区推荐长度（Recommended Length）。

<a id="r_gae0df0067c55eb4388625bb62f3d7e235"></a>

```c
#define BT_ADDR_LE_STR_LEN 20
```

相关声明：[BT_ADDR_LE_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gae0df0067c55eb4388625bb62f3d7e235)。

用于蓝牙低功耗地址的用户字符串缓冲区推荐长度（Recommended Length）。

<a id="r_ga26db53edfcda476f641e50a0a89ba197"></a>

```c
#define bt_addr_str(_addr)
```

相关声明：[bt_addr_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga26db53edfcda476f641e50a0a89ba197)。

将蓝牙地址（Bluetooth Address）转换为字符串。

<a id="r_gaecb794d5df4845477cf2545e8ea1b079"></a>

```c
#define bt_addr_le_str(_addr)
```

相关声明：[bt_addr_le_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gaecb794d5df4845477cf2545e8ea1b079)。

将蓝牙低功耗地址（Bluetooth LE Address）转换为字符串。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_ga41ff9419098728f037c3e97d29c30ba9"></a>

```c
static int bt_addr_cmp (const bt_addr_t *a, const bt_addr_t *b)
```

相关声明：[bt_addr_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga41ff9419098728f037c3e97d29c30ba9)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

比较蓝牙设备地址（Bluetooth Device Addresses）。

<a id="r_gadecf8fe8e183a11a4ff569bc0d673ec1"></a>

```c
static bool bt_addr_eq (const bt_addr_t *a, const bt_addr_t *b)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_addr_eq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gadecf8fe8e183a11a4ff569bc0d673ec1)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

判断两个蓝牙设备地址（Bluetooth Device Addresses）是否相等。

<a id="r_ga588d392f51372ff2951c3ff39da22f12"></a>

```c
static int bt_addr_le_cmp (const bt_addr_le_t *a, const bt_addr_le_t *b)
```

相关声明：[bt_addr_le_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga588d392f51372ff2951c3ff39da22f12)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

比较蓝牙低功耗设备地址（Bluetooth LE Device Addresses）。

<a id="r_ga8644e77108f029088adb203e5392016b"></a>

```c
static bool bt_addr_le_eq (const bt_addr_le_t *a, const bt_addr_le_t *b)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_addr_le_eq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga8644e77108f029088adb203e5392016b)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

判断两个蓝牙低功耗设备地址（Bluetooth LE Device Addresses）是否相等。

<a id="r_ga5a8284cf34d0835d725dab31d710ea4c"></a>

```c
static void bt_addr_copy (bt_addr_t *dst, const bt_addr_t *src)
```

相关声明：[bt_addr_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga5a8284cf34d0835d725dab31d710ea4c)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

复制蓝牙设备地址（Bluetooth Device Address）。

<a id="r_gac6c9b20f17936efaa082fe63aedc2138"></a>

```c
static void bt_addr_le_copy (bt_addr_le_t *dst, const bt_addr_le_t *src)
```

相关声明：[bt_addr_le_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gac6c9b20f17936efaa082fe63aedc2138)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

复制蓝牙低功耗设备地址（Bluetooth LE Device Address）。

<a id="r_ga756d59776902ad1ae2df1c032e91589c"></a>

```c
static void bt_addr_le_copy_addr (bt_addr_le_t *dst, const bt_addr_t *src, uint8_t src_type)
```

相关声明：[bt_addr_le_copy_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga756d59776902ad1ae2df1c032e91589c)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据蓝牙设备地址及类型，复制生成蓝牙低功耗设备地址（Bluetooth LE Device Address）。

<a id="r_gaf2d38888131c9e8bdbc820b415c14082"></a>

```c
int bt_addr_le_create_nrpa (bt_addr_le_t *addr)
```

相关声明：[bt_addr_le_create_nrpa](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gaf2d38888131c9e8bdbc820b415c14082)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

创建蓝牙低功耗随机不可解析私有地址（Random Non-resolvable Private Address）。

<a id="r_gad1b43f2f0ab58ec2c5ceaaa0d2cbc444"></a>

```c
int bt_addr_le_create_static (bt_addr_le_t *addr)
```

相关声明：[bt_addr_le_create_static](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gad1b43f2f0ab58ec2c5ceaaa0d2cbc444)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

创建蓝牙低功耗随机静态地址（Random Static Address）。

<a id="r_ga42bcee6b5aadde7ccdbe243df25043bc"></a>

```c
static bool bt_addr_le_is_rpa (const bt_addr_le_t *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_addr_le_is_rpa](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga42bcee6b5aadde7ccdbe243df25043bc)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

检查蓝牙低功耗地址是否为随机可解析私有地址（Random Private Resolvable Address）。

<a id="r_ga7a6acc7a9267ae2645aeee38e553b8b3"></a>

```c
static bool bt_addr_le_is_identity (const bt_addr_le_t *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_addr_le_is_identity](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga7a6acc7a9267ae2645aeee38e553b8b3)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

检查蓝牙低功耗地址是否为有效身份地址（Identity Address）。

<a id="r_ga151bdd0ada8635acfebd60f0e203cde2"></a>

```c
static int bt_addr_to_str (const bt_addr_t *addr, char *str, size_t len)
```

相关声明：[bt_addr_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga151bdd0ada8635acfebd60f0e203cde2)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

将二进制蓝牙地址（Binary Bluetooth Address）转换为字符串。

<a id="r_ga74a644cd3de081a353a281d80b32b91e"></a>

```c
static int bt_addr_le_to_str (const bt_addr_le_t *addr, char *str, size_t len)
```

相关声明：[bt_addr_le_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga74a644cd3de081a353a281d80b32b91e)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

将二进制蓝牙低功耗地址（Binary LE Bluetooth Address）转换为字符串。

<a id="r_gad93410d0161ca84939f4bf983da29c14"></a>

```c
int bt_addr_from_str (const char *str, bt_addr_t *addr)
```

相关声明：[bt_addr_from_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gad93410d0161ca84939f4bf983da29c14)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

将蓝牙地址从字符串转换为二进制形式。

<a id="r_ga24752df467449d7cb0dc25e3c4330862"></a>

```c
int bt_addr_le_from_str (const char *str, bt_addr_le_t *addr)
```

相关声明：[bt_addr_le_from_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga24752df467449d7cb0dc25e3c4330862)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

将蓝牙低功耗地址从字符串转换为二进制形式。

<a id="r_ga28baaccd1e89d8939d3a73d759cded09"></a>

```c
int bt_addr_le_rpa_resolve (uint8_t id, const bt_addr_le_t *addr, bt_addr_le_t *resolved_addr)
```

相关声明：[bt_addr_le_rpa_resolve](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga28baaccd1e89d8939d3a73d759cded09)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

将蓝牙低功耗可解析私有地址（Resolvable Private Address，RPA）解析为其身份地址（Identity Address）。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 1.4\_变量（Variables）

<a id="r_gadd64afda1a14cbc2740f205e90169152"></a>

```c
const bt_addr_t bt_addr_any
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bt_addr_any](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gadd64afda1a14cbc2740f205e90169152)。

<a id="r_ga0b2f611fbd28b066d261b81303c4b93f"></a>

```c
const bt_addr_t bt_addr_none
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bt_addr_none](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga0b2f611fbd28b066d261b81303c4b93f)。

<a id="r_ga40c282f720d13b5d24a2dd62bfdceb73"></a>

```c
const bt_addr_le_t bt_addr_le_any
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_addr_le_any](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga40c282f720d13b5d24a2dd62bfdceb73)。

<a id="r_gaefa17a553b6f8e9ad599e8db7538e1b8"></a>

```c
const bt_addr_le_t bt_addr_le_none
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_addr_le_none](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gaefa17a553b6f8e9ad599e8db7538e1b8)。


## 1.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [string.h](../api_source_supplement_reference/P216_string.h_源码浏览.md)
- [zephyr/sys/printk.h](../api_source_runtime_reference/P051_printk.h_源码浏览.md)
- [查看此文件的源码。](../api_source_visible_fragment_reference/P001_addr.h_源码浏览.md)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [BT_ADDR_LE_PUBLIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga1717d2b4e61b28637be8a5f78685a3c4)
- [BT_ADDR_LE_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga6e81e967527b5418ee6cbc6d72c5aef9)
- [BT_ADDR_LE_PUBLIC_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga1fd60d5eb4c8a6d8f4df06eaba85fb96)
- [BT_ADDR_LE_RANDOM_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gafdf2572991427d95bb44d1a5ee2ad85a)
- [BT_ADDR_LE_UNRESOLVED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gad02c40564a140300efda28ecb15674be)
- [BT_ADDR_LE_ANONYMOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gab2ddd85c5972a53da0aee3974edc0258)
- [BT_ADDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga6b6f56325b5136d2719f02eecc780d49)
- [BT_ADDR_LE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga2656b9a936bf8cb9f1cc86668fca6108)
- [BT_ADDR_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga40ddc9769e38b7537bbb4e8002de592a)
- [bt_addr_any](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gadd64afda1a14cbc2740f205e90169152)
- [BT_ADDR_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gacb24d83ded350176fc96dfc0f5dde6be)
- [bt_addr_none](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga0b2f611fbd28b066d261b81303c4b93f)
- [BT_ADDR_LE_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga17e9efacd50c682b2f709c217e920d48)
- [bt_addr_le_any](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga40c282f720d13b5d24a2dd62bfdceb73)
- [BT_ADDR_LE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gadfcc0281e453cba990b623631c26f80b)
- [bt_addr_le_none](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gaefa17a553b6f8e9ad599e8db7538e1b8)
- [BT_ADDR_IS_RPA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga32abc1a2e827542efea5b9cb05a57fbc)
- [BT_ADDR_IS_NRPA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gaa8745bff73c42a693cb76e42755b2bf9)
- [BT_ADDR_IS_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga0cb3aa4d48cf41d8485b570ef0e7447a)
- [BT_ADDR_SET_RPA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga52a0bd596e726dff39b247dfbc58406d)
- [BT_ADDR_SET_NRPA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga6b23035316e9bdd071e10ecc803fcdbc)
- [BT_ADDR_SET_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gaa6261bf0b96099b58f0a0c3674ce5713)
- [BT_ADDR_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga8097c3b80a5647b0b951d29aa30a397d)
- [BT_ADDR_LE_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gae0df0067c55eb4388625bb62f3d7e235)
- [bt_addr_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga26db53edfcda476f641e50a0a89ba197)
- [bt_addr_le_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gaecb794d5df4845477cf2545e8ea1b079)
- [bt_addr_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga41ff9419098728f037c3e97d29c30ba9)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_addr_eq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gadecf8fe8e183a11a4ff569bc0d673ec1)
- [bt_addr_le_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga588d392f51372ff2951c3ff39da22f12)
- [bt_addr_le_eq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga8644e77108f029088adb203e5392016b)
- [bt_addr_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga5a8284cf34d0835d725dab31d710ea4c)
- [bt_addr_le_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gac6c9b20f17936efaa082fe63aedc2138)
- [bt_addr_le_copy_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga756d59776902ad1ae2df1c032e91589c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_le_create_nrpa](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gaf2d38888131c9e8bdbc820b415c14082)
- [bt_addr_le_create_static](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gad1b43f2f0ab58ec2c5ceaaa0d2cbc444)
- [bt_addr_le_is_rpa](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga42bcee6b5aadde7ccdbe243df25043bc)
- [bt_addr_le_is_identity](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga7a6acc7a9267ae2645aeee38e553b8b3)
- [bt_addr_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga151bdd0ada8635acfebd60f0e203cde2)
- [bt_addr_le_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga74a644cd3de081a353a281d80b32b91e)
- [bt_addr_from_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gad93410d0161ca84939f4bf983da29c14)
- [bt_addr_le_from_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga24752df467449d7cb0dc25e3c4330862)
- [bt_addr_le_rpa_resolve](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga28baaccd1e89d8939d3a73d759cded09)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__bluetooth__att.h_文件参考.md)
