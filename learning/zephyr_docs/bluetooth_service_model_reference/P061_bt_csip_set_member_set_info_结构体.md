---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-61
title: bt_csip_set_member_set_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__csip__set__member__set__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_bt\_csip\_set\_member\_set\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__csip__set__member__set__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存服务实例（Service Instance）信息的结构体。

```c
#include <zephyr/bluetooth/audio/csip.h>
```

<a id="details"></a>

保存服务实例（Service Instance）信息的结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 61.1\_数据成员（Data Fields）

<a id="r_a9ca9136177d15d68e4cabab2bce43540"></a>

```c
uint8_t sirk [16U]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sirk](#a9ca9136177d15d68e4cabab2bce43540)。

16 个八位组的集合身份解析密钥（SIRK）。

<a id="r_afcb0ae1252ca6ac09fbdaaf5c8ae8dfa"></a>

```c
uint8_t set_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[set_size](#afcb0ae1252ca6ac09fbdaaf5c8ae8dfa)。

集合大小（Set size）。

<a id="r_aa715eda78908c603ec11a48846018845"></a>

```c
uint8_t rank
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rank](#aa715eda78908c603ec11a48846018845)。

排序值（Rank）。

<a id="r_a52ba91f4e3ee911f575160355368aae5"></a>

```c
bool lockable: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[lockable](#a52ba91f4e3ee911f575160355368aae5)。

集合是否可锁定（Lockable）。

<a id="r_ae0e082aac881500f2005489d6aa88090"></a>

```c
bool locked: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[locked](#ae0e082aac881500f2005489d6aa88090)。

集合当前是否已锁定（Locked）。

<a id="r_a75ca9b78932626f167b186b203611c27"></a>

```c
bt_addr_le_t lock_client_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[lock_client_addr](#a75ca9b78932626f167b186b203611c27)。

当前持有锁的客户端地址（Client address）。

## 61.2\_详细说明（Detailed Documentation）

<a id="a75ca9b78932626f167b186b203611c27"></a>

### `lock_client_addr`

```c
bt_addr_le_t bt_csip_set_member_set_info::lock_client_addr
```

当前持有锁的客户端地址（Client address）。

服务器持有锁时为 `BT_ADDR_LE_NONE`。

<a id="a52ba91f4e3ee911f575160355368aae5"></a>

### `lockable`

```c
bool bt_csip_set_member_set_info::lockable
```

集合是否可锁定（Lockable）。

未启用 `CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT` 时，始终为 `false`。

<a id="ae0e082aac881500f2005489d6aa88090"></a>

### `locked`

```c
bool bt_csip_set_member_set_info::locked
```

集合当前是否已锁定（Locked）。

未启用 `CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT` 时，始终为 `false`。

<a id="aa715eda78908c603ec11a48846018845"></a>

### `rank`

```c
uint8_t bt_csip_set_member_set_info::rank
```

排序值（Rank）。

集合不可锁定，或未启用 `CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT` 时，始终为 `0`。

<a id="afcb0ae1252ca6ac09fbdaaf5c8ae8dfa"></a>

### `set_size`

```c
uint8_t bt_csip_set_member_set_info::set_size
```

集合大小（Set size）。

未启用 `CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT` 时，始终为 `0`。

<a id="a9ca9136177d15d68e4cabab2bce43540"></a>

### `sirk`

```c
uint8_t bt_csip_set_member_set_info::sirk[16U]
```

16 个八位组的集合身份解析密钥（SIRK）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/csip.h`

## 61.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/csip.h](https://docs.zephyrproject.org/latest/doxygen/html/csip_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [BT_ADDR_LE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gadfcc0281e453cba990b623631c26f80b)
- [CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT)
- [CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT)
- [CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P060_bt_csip_set_member_register_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P062_bt_csip_set_member_svc_inst_结构体.md)
