---
id: learning.zephyr-docs.api-file-supplement-reference.page-51
title: zephyr__bluetooth__services__nus__inst.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/inst_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_zephyr\_\_bluetooth\_\_services\_\_nus\_\_inst.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/inst_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/gatt.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 51.1\_数据结构（Data Structures）

<a id="r_bt_5Fnus_5Finst"></a>

```c
struct bt_nus_inst
```

相关声明：[bt_nus_inst](../bluetooth_service_model_reference/P126_bt_nus_inst_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 51.2\_宏定义（Macros）

<a id="r_a3752da6f7063510a04551609672b2583"></a>

```c
#define BT_UUID_NUS_SERVICE BT_UUID_DECLARE_128(BT_UUID_NUS_SRV_VAL)
```

相关声明：[BT_UUID_NUS_SERVICE](#a3752da6f7063510a04551609672b2583)、[BT_UUID_DECLARE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadece715e13e2a529aa55c298ff760bf0)、[BT_UUID_NUS_SRV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/nus_8h.html#a8da4aaa9c77a537805c7b5bff7fc4aa6)。

<a id="r_ad652d719c4f193d433156afcb3d8fe87"></a>

```c
#define BT_UUID_NUS_TX_CHAR BT_UUID_DECLARE_128(BT_UUID_NUS_TX_CHAR_VAL)
```

相关声明：[BT_UUID_NUS_TX_CHAR](#ad652d719c4f193d433156afcb3d8fe87)、[BT_UUID_DECLARE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadece715e13e2a529aa55c298ff760bf0)、[BT_UUID_NUS_TX_CHAR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/nus_8h.html#a7636b61879884e6f6fc8e871ae09160b)。

<a id="r_aa9e0e0a89747210a3ebc36d85ce973d2"></a>

```c
#define BT_UUID_NUS_RX_CHAR BT_UUID_DECLARE_128(BT_UUID_NUS_RX_CHAR_VAL)
```

相关声明：[BT_UUID_NUS_RX_CHAR](#aa9e0e0a89747210a3ebc36d85ce973d2)、[BT_UUID_DECLARE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadece715e13e2a529aa55c298ff760bf0)、[BT_UUID_NUS_RX_CHAR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/nus_8h.html#ada90c739cf936ec52008fcc4f272e207)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 51.3\_函数（Functions）

<a id="r_a3bb5cd4e4367d402f377cee751f9b434"></a>

```c
ssize_t nus_bt_chr_write (struct bt_conn *conn, const struct bt_gatt_attr *attr, const void *buf, uint16_t len, uint16_t offset, uint8_t flags)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[nus_bt_chr_write](#a3bb5cd4e4367d402f377cee751f9b434)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

这是必需的，因为服务（Service）可能在模块（Module）之外实例化。

<a id="r_a964bdf4d6c01f257533c0a5c337f562e"></a>

```c
void nus_ccc_cfg_changed (const struct bt_gatt_attr *attr, uint16_t value)
```

相关声明：[nus_ccc_cfg_changed](#a964bdf4d6c01f257533c0a5c337f562e)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

## 51.4\_详细说明（Detailed Documentation）

<a id="aa9e0e0a89747210a3ebc36d85ce973d2"></a>

### `BT_UUID_NUS_RX_CHAR`

```c
#define BT_UUID_NUS_RX_CHAR BT_UUID_DECLARE_128(BT_UUID_NUS_RX_CHAR_VAL)
```

<a id="a3752da6f7063510a04551609672b2583"></a>

### `BT_UUID_NUS_SERVICE`

```c
#define BT_UUID_NUS_SERVICE BT_UUID_DECLARE_128(BT_UUID_NUS_SRV_VAL)
```

<a id="ad652d719c4f193d433156afcb3d8fe87"></a>

### `BT_UUID_NUS_TX_CHAR`

```c
#define BT_UUID_NUS_TX_CHAR BT_UUID_DECLARE_128(BT_UUID_NUS_TX_CHAR_VAL)
```

<a id="a3bb5cd4e4367d402f377cee751f9b434"></a>

### `nus_bt_chr_write()`

```c
ssize_t nus_bt_chr_write ( struct bt_conn * conn, const struct bt_gatt_attr * attr, const void * buf, uint16_t len, uint16_t offset, uint8_t flags )
```

这是必需的，因为服务（Service）可能在模块（Module）之外实例化。

<a id="a964bdf4d6c01f257533c0a5c337f562e"></a>

### `nus_ccc_cfg_changed()`

```c
void nus_ccc_cfg_changed ( const struct bt_gatt_attr * attr, uint16_t value )
```


## 51.5\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](../api_source_runtime_reference/P021_gatt.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P390_inst.h_源码浏览.md)
- [bt_nus_inst](../bluetooth_service_model_reference/P126_bt_nus_inst_结构体.md)
- [BT_UUID_DECLARE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadece715e13e2a529aa55c298ff760bf0)
- [BT_UUID_NUS_SRV_VAL](https://docs.zephyrproject.org/latest/doxygen/html/nus_8h.html#a8da4aaa9c77a537805c7b5bff7fc4aa6)
- [BT_UUID_NUS_TX_CHAR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/nus_8h.html#a7636b61879884e6f6fc8e871ae09160b)
- [BT_UUID_NUS_RX_CHAR_VAL](https://docs.zephyrproject.org/latest/doxygen/html/nus_8h.html#ada90c739cf936ec52008fcc4f272e207)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P050_zephyr__input__input_renesas_rx_ctsu.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P052_zephyr__dt-bindings__pinctrl__it8xxx2-pinctrl.h_文件参考.md)
