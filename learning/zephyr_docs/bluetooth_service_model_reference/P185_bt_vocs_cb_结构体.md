---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-185
title: bt_vocs_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__vocs__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第185章\_bt\_vocs\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__vocs__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存音量偏移控制服务（Volume Offset Control Service）回调的结构。

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

<a id="details"></a>

保存音量偏移控制服务（Volume Offset Control Service）回调的结构体。根据角色，可通过 `bt_vocs_client_cb_register()` 或 `bt_vocs_register()` 注册这些回调供使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 185.1\_数据成员（Data Fields）

<a id="r_ae633c1f6cd8aa03d89287e783179460e"></a>

```c
bt_vocs_state_cb state
```

相关声明：[bt_vocs_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaa329fd8931add8fd4f6c59b48c91ef75)、[state](#ae633c1f6cd8aa03d89287e783179460e)。

偏移状态（offset state）已变化。

<a id="r_a50d1d429089456267b06d4450712b897"></a>

```c
bt_vocs_location_cb location
```

相关声明：[bt_vocs_location_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga84983707e04eae75f18017072b647115)、[location](#a50d1d429089456267b06d4450712b897)。

位置（location）已变化。

<a id="r_ac508b1e6dda00c607aa1cbe52423ec52"></a>

```c
bt_vocs_description_cb description
```

相关声明：[bt_vocs_description_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaa351c3ab631b16272e27cbb837d9e49c)、[description](#ac508b1e6dda00c607aa1cbe52423ec52)。

描述（Description）已变化。

<a id="r_a2ff42997b87d2a910325d4b04e67f4c5"></a>

```c
bt_vocs_discover_cb discover
```

相关声明：[bt_vocs_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gad50fd539190b5c64b5262d3830699365)、[discover](#a2ff42997b87d2a910325d4b04e67f4c5)。

发现（discovery）过程已完成。

<a id="r_a1b5a3359602ceea1a45ebe7aa79e6b3a"></a>

```c
bt_vocs_set_offset_cb set_offset
```

相关声明：[bt_vocs_set_offset_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga2630344190f12f911bb2b01c4b95ded6)、[set_offset](#a1b5a3359602ceea1a45ebe7aa79e6b3a)。

设置偏移（set offset）过程已完成。

## 185.2\_详细说明（Detailed Documentation）

<a id="ac508b1e6dda00c607aa1cbe52423ec52"></a>

### `description`

```c
bt_vocs_description_cb bt_vocs_cb::description
```

描述（Description）已变化。

<a id="a2ff42997b87d2a910325d4b04e67f4c5"></a>

### `discover`

```c
bt_vocs_discover_cb bt_vocs_cb::discover
```

发现（discovery）过程已完成。

仅客户端可设置，且需要启用 `CONFIG_BT_VOCS_CLIENT`。

<a id="a50d1d429089456267b06d4450712b897"></a>

### `location`

```c
bt_vocs_location_cb bt_vocs_cb::location
```

位置（location）已变化。

<a id="a1b5a3359602ceea1a45ebe7aa79e6b3a"></a>

### `set_offset`

```c
bt_vocs_set_offset_cb bt_vocs_cb::set_offset
```

设置偏移（set offset）过程已完成。

仅客户端可设置，且需要启用 `CONFIG_BT_VOCS_CLIENT`。

<a id="ae633c1f6cd8aa03d89287e783179460e"></a>

### `state`

```c
bt_vocs_state_cb bt_vocs_cb::state
```

偏移状态（offset state）已变化。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/vocs.h`

## 185.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/vocs.h](https://docs.zephyrproject.org/latest/doxygen/html/vocs_8h_source.html)
- [bt_vocs_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaa329fd8931add8fd4f6c59b48c91ef75)
- [bt_vocs_location_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga84983707e04eae75f18017072b647115)
- [bt_vocs_description_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaa351c3ab631b16272e27cbb837d9e49c)
- [bt_vocs_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gad50fd539190b5c64b5262d3830699365)
- [bt_vocs_set_offset_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga2630344190f12f911bb2b01c4b95ded6)
- [bt_vocs_client_cb_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaace802556eca3d634a13dd8f2bf3c544)
- [bt_vocs_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gac011ddd93bb3240148a789f1ee9ef7da)
- [CONFIG_BT_VOCS_CLIENT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_VOCS_CLIENT)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P184_bt_vocs_结构体.md) · [返回大纲](大纲.md) · [下一章](P186_bt_vocs_discover_param_结构体.md)
