---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-258
title: bt_hci_evt_le_frame_space_update_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__frame__space__update__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第258章\_bt\_hci\_evt\_le\_frame\_space\_update\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__frame__space__update__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 258.1\_数据成员（Data Fields）

<a id="r_a2ec660b66b28fe0ab69b9db5681a5b17"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a2ec660b66b28fe0ab69b9db5681a5b17)。

<a id="r_a8da9f4e322bd41f5870ea5cec0092584"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a8da9f4e322bd41f5870ea5cec0092584)。

<a id="r_adb081f887bc36892fc98fe78d170d93d"></a>

```c
uint8_t initiator
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[initiator](#adb081f887bc36892fc98fe78d170d93d)。

<a id="r_a1b306ba860123344436f85914455d784"></a>

```c
uint16_t frame_space
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[frame_space](#a1b306ba860123344436f85914455d784)。

<a id="r_a66d0db4fa276b0a839ce97b0c6868ae4"></a>

```c
uint8_t phys
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phys](#a66d0db4fa276b0a839ce97b0c6868ae4)。

<a id="r_af39f49f398848cfddda3edf70432a5fd"></a>

```c
uint16_t spacing_types
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[spacing_types](#af39f49f398848cfddda3edf70432a5fd)。

## 258.2\_详细说明（Detailed Documentation）

<a id="a1b306ba860123344436f85914455d784"></a>

### `frame_space`

```c
uint16_t bt_hci_evt_le_frame_space_update_complete::frame_space
```

<a id="a8da9f4e322bd41f5870ea5cec0092584"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_frame_space_update_complete::handle
```

<a id="adb081f887bc36892fc98fe78d170d93d"></a>

### `initiator`

```c
uint8_t bt_hci_evt_le_frame_space_update_complete::initiator
```

<a id="a66d0db4fa276b0a839ce97b0c6868ae4"></a>

### `phys`

```c
uint8_t bt_hci_evt_le_frame_space_update_complete::phys
```

<a id="af39f49f398848cfddda3edf70432a5fd"></a>

### `spacing_types`

```c
uint16_t bt_hci_evt_le_frame_space_update_complete::spacing_types
```

<a id="a2ec660b66b28fe0ab69b9db5681a5b17"></a>

### `status`

```c
uint8_t bt_hci_evt_le_frame_space_update_complete::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 258.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P257_bt_hci_evt_le_ext_advertising_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P259_bt_hci_evt_le_generate_dhkey_complete_结构体.md)
