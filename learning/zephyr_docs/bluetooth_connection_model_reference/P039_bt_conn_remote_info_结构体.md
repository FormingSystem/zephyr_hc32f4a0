---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-39
title: bt_conn_remote_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__remote__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_bt\_conn\_remote\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__remote__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

连接的远端信息结构体。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

连接远端信息结构（Connection Remote Info Structure）。注意（Note）：仅启用 `CONFIG_BT_REMOTE_VERSION` 时，`version`、`manufacturer` 和 `subversion` 字段才包含有效数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 39.1\_数据成员（Data Fields）

<a id="r_a8bb514196bde5df561dbf76b68060729"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#a8bb514196bde5df561dbf76b68060729)。

连接类型（Connection Type）。

<a id="r_a2664f6ed3bd22f9a011126daf5d81376"></a>

```c
uint8_t version
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[version](#a2664f6ed3bd22f9a011126daf5d81376)。

远端链路层版本（Remote Link Layer version）。

<a id="r_a47cc5a4b8888a0b8faaf6880c37418b8"></a>

```c
uint16_t manufacturer
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[manufacturer](#a47cc5a4b8888a0b8faaf6880c37418b8)。

远端制造商标识符（Remote manufacturer identifier）。

<a id="r_a360979a15c958706157fc630fd55cbca"></a>

```c
uint16_t subversion
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subversion](#a360979a15c958706157fc630fd55cbca)。

制造商内部唯一的修订版本（Per-manufacturer unique revision）。

```c
union {
```

<a id="r_a81c780f45384b6f25197149e9fb003aa"></a>

```c
struct bt_conn_le_remote_info le
```

相关声明：[bt_conn_le_remote_info](P031_bt_conn_le_remote_info_结构体.md)、[le](#ae75530b09c6dea416630a4a19a1d64cc)。

低功耗连接远端信息（LE connection remote info）。

<a id="r_a8f128d4c27e38ef0d5bfbd07eeff359f"></a>

```c
struct bt_conn_br_remote_info br
```

相关声明：[bt_conn_br_remote_info](P007_bt_conn_br_remote_info_结构体.md)、[br](#ab73365f09cdb5ce870272546543bcfeb)。

基本速率／增强数据率连接远端信息（BR/EDR connection remote info）。

<a id="r_aeee3aee13425b62609529bdb5b77b8cf"></a>

```c
};
```

## 39.2\_详细说明（Detailed Documentation）

<a id="aeee3aee13425b62609529bdb5b77b8cf"></a>

### `[union]`

```c
union { ... } bt_conn_remote_info
```

<a id="ab73365f09cdb5ce870272546543bcfeb"></a>

### `br`

```c
struct bt_conn_br_remote_info bt_conn_remote_info::br
```

基本速率／增强数据率连接远端信息（BR/EDR connection remote info）。

<a id="ae75530b09c6dea416630a4a19a1d64cc"></a>

### `le`

```c
struct bt_conn_le_remote_info bt_conn_remote_info::le
```

低功耗连接远端信息（LE connection remote info）。

<a id="a47cc5a4b8888a0b8faaf6880c37418b8"></a>

### `manufacturer`

```c
uint16_t bt_conn_remote_info::manufacturer
```

远端制造商标识符（Remote manufacturer identifier）。

<a id="a360979a15c958706157fc630fd55cbca"></a>

### `subversion`

```c
uint16_t bt_conn_remote_info::subversion
```

制造商内部唯一的修订版本（Per-manufacturer unique revision）。

<a id="a8bb514196bde5df561dbf76b68060729"></a>

### `type`

```c
uint8_t bt_conn_remote_info::type
```

连接类型（Connection Type）。

<a id="a2664f6ed3bd22f9a011126daf5d81376"></a>

### `version`

```c
uint8_t bt_conn_remote_info::version
```

远端链路层版本（Remote Link Layer version）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 39.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_conn_le_remote_info](P031_bt_conn_le_remote_info_结构体.md)
- [bt_conn_br_remote_info](P007_bt_conn_br_remote_info_结构体.md)
- [CONFIG_BT_REMOTE_VERSION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_REMOTE_VERSION)
- [bt_conn_remote_info](P039_bt_conn_remote_info_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P038_bt_conn_pairing_feat_结构体.md) · [返回大纲](大纲.md) · [下一章](P040_bt_conn_sco_info_结构体.md)
