---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-55
title: bt_csip_set_coordinator_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__csip__set__coordinator__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_bt\_csip\_set\_coordinator\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__csip__set__coordinator__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存协调集合标识配置文件（Coordinated Set Identification Profile，CSIP）的集合协调器（Set Coordinator）回调的结构体。

```c
#include <zephyr/bluetooth/audio/csip.h>
```

<a id="details"></a>

保存协调集合标识规范集合协调器回调（Coordinated Set Identification Profile Set Coordinator callbacks）的结构。可使用 `bt_csip_set_coordinator_register_cb()` 注册。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 55.1\_数据成员（Data Fields）

<a id="r_a724060375ef6f53fcdbabcc12032a4b0"></a>

```c
bt_csip_set_coordinator_discover_cb discover
```

相关声明：[bt_csip_set_coordinator_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaeee5f0691ba0d63a370ac5dd94cb4d5c)、[discover](#a724060375ef6f53fcdbabcc12032a4b0)。

发现完成回调（Discovery finished callback）。

<a id="r_a25474d60bcd8ee07ef3691554d9bd7ba"></a>

```c
bt_csip_set_coordinator_lock_set_cb lock_set
```

相关声明：[bt_csip_set_coordinator_lock_set_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga994431ea69920d9e84f35ca6e1e5f634)、[lock_set](#a25474d60bcd8ee07ef3691554d9bd7ba)。

集合加锁完成回调（Set locking finished callback）。

<a id="r_acc1efc493dd05f14fdc010240982e0de"></a>

```c
bt_csip_set_coordinator_lock_set_cb release_set
```

相关声明：[bt_csip_set_coordinator_lock_set_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga994431ea69920d9e84f35ca6e1e5f634)、[release_set](#acc1efc493dd05f14fdc010240982e0de)。

集合解锁完成回调（Set unlocking finished callback）。

<a id="r_adfa831556d13dbda8f06f69f69f9cac1"></a>

```c
bt_csip_set_coordinator_lock_changed_cb lock_changed
```

相关声明：[bt_csip_set_coordinator_lock_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga991ee886c814e0b72fa12ed58ef4a90b)、[lock_changed](#adfa831556d13dbda8f06f69f69f9cac1)。

集合锁定状态变化回调（Set lock state changed callback）。

<a id="r_a5bb08e8ce5759f67d2ff02459efe114d"></a>

```c
bt_csip_set_coordinator_sirk_changed_cb sirk_changed
```

相关声明：[bt_csip_set_coordinator_sirk_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gacdb98c9ae3248064e90352387df7cef2)、[sirk_changed](#a5bb08e8ce5759f67d2ff02459efe114d)。

集合身份解析密钥变化回调（SIRK changed callback）。

<a id="r_ab328cf27c2966d7762d82ffb0d334d68"></a>

```c
bt_csip_set_coordinator_size_changed_cb size_changed
```

相关声明：[bt_csip_set_coordinator_size_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaee24f364c90cdcd0b6f49c8b297a34a7)、[size_changed](#ab328cf27c2966d7762d82ffb0d334d68)。

集合大小变化回调（Set size changed callback）。

<a id="r_ae8cf52f1ace4ea1d56ec2204c59bb71c"></a>

```c
bt_csip_set_coordinator_ordered_access_cb_t ordered_access
```

相关声明：[bt_csip_set_coordinator_ordered_access_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga0f2e0b610a4db975a72c6d9a645964cb)、[ordered_access](#ae8cf52f1ace4ea1d56ec2204c59bb71c)。

有序访问过程回调（Ordered access procedure callback）。

## 55.2\_详细说明（Detailed Documentation）

<a id="a724060375ef6f53fcdbabcc12032a4b0"></a>

### `discover`

```c
bt_csip_set_coordinator_discover_cb bt_csip_set_coordinator_cb::discover
```

发现完成回调（Discovery finished callback）。

<a id="adfa831556d13dbda8f06f69f69f9cac1"></a>

### `lock_changed`

```c
bt_csip_set_coordinator_lock_changed_cb bt_csip_set_coordinator_cb::lock_changed
```

集合锁定状态变化回调（Set lock state changed callback）。

<a id="a25474d60bcd8ee07ef3691554d9bd7ba"></a>

### `lock_set`

```c
bt_csip_set_coordinator_lock_set_cb bt_csip_set_coordinator_cb::lock_set
```

集合加锁完成回调（Set locking finished callback）。

<a id="ae8cf52f1ace4ea1d56ec2204c59bb71c"></a>

### `ordered_access`

```c
bt_csip_set_coordinator_ordered_access_cb_t bt_csip_set_coordinator_cb::ordered_access
```

有序访问过程回调（Ordered access procedure callback）。

<a id="acc1efc493dd05f14fdc010240982e0de"></a>

### `release_set`

```c
bt_csip_set_coordinator_lock_set_cb bt_csip_set_coordinator_cb::release_set
```

集合解锁完成回调（Set unlocking finished callback）。

<a id="a5bb08e8ce5759f67d2ff02459efe114d"></a>

### `sirk_changed`

```c
bt_csip_set_coordinator_sirk_changed_cb bt_csip_set_coordinator_cb::sirk_changed
```

集合身份解析密钥变化回调（SIRK changed callback）。

<a id="ab328cf27c2966d7762d82ffb0d334d68"></a>

### `size_changed`

```c
bt_csip_set_coordinator_size_changed_cb bt_csip_set_coordinator_cb::size_changed
```

集合大小变化回调（Set size changed callback）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/csip.h`

## 55.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/csip.h](https://docs.zephyrproject.org/latest/doxygen/html/csip_8h_source.html)
- [bt_csip_set_coordinator_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaeee5f0691ba0d63a370ac5dd94cb4d5c)
- [bt_csip_set_coordinator_lock_set_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga994431ea69920d9e84f35ca6e1e5f634)
- [bt_csip_set_coordinator_lock_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga991ee886c814e0b72fa12ed58ef4a90b)
- [bt_csip_set_coordinator_sirk_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gacdb98c9ae3248064e90352387df7cef2)
- [bt_csip_set_coordinator_size_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaee24f364c90cdcd0b6f49c8b297a34a7)
- [bt_csip_set_coordinator_ordered_access_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga0f2e0b610a4db975a72c6d9a645964cb)
- [bt_csip_set_coordinator_register_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga08c514fda44e5a9b5cfc16be629c2b37)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P054_bt_ccp_call_control_server_bearer_结构体.md) · [返回大纲](大纲.md) · [下一章](P056_bt_csip_set_coordinator_csis_inst_结构体.md)
