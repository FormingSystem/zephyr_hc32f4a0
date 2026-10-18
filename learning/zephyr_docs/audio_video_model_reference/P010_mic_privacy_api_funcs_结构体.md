---
id: learning.zephyr-docs.audio-video-model-reference.page-10
title: mic_privacy_api_funcs_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmic__privacy__api__funcs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_mic\_privacy\_api\_funcs\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmic__privacy__api__funcs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/mic_privacy/intel/mic_privacy.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_a67548968f088126881ef11f7317e5036"></a>

```c
void(* enable_fw_managed_irq )(bool enable_irq, const void *fn)
```

相关声明：[enable_fw_managed_irq](#a67548968f088126881ef11f7317e5036)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

<a id="r_a294e4cd3bb23ccb23f7143b6a9e4dba5"></a>

```c
void(* clear_fw_managed_irq )()
```

相关声明：[clear_fw_managed_irq](#a294e4cd3bb23ccb23f7143b6a9e4dba5)。

<a id="r_afc87beb092fa02c06dcd84125ccc305a"></a>

```c
void(* enable_dmic_irq )(bool enable_irq, const void *fn)
```

相关声明：[enable_dmic_irq](#afc87beb092fa02c06dcd84125ccc305a)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

<a id="r_a8cd74fd6817c3f5bfa0fc7697765d357"></a>

```c
bool(* get_dmic_irq_status )(void)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[get_dmic_irq_status](#a8cd74fd6817c3f5bfa0fc7697765d357)。

<a id="r_ae68b97acf6ec4f5812275ee682bdf96d"></a>

```c
void(* clear_dmic_irq_status )(void)
```

相关声明：[clear_dmic_irq_status](#ae68b97acf6ec4f5812275ee682bdf96d)。

<a id="r_a558346b619a67f3f05b20cf62a7993ef"></a>

```c
enum mic_privacy_policy(* get_policy )()
```

相关声明：[mic_privacy_policy](https://docs.zephyrproject.org/latest/doxygen/html/mic__privacy_8h.html#acbabb5c150f29668a23379bcb2180931)、[get_policy](#a558346b619a67f3f05b20cf62a7993ef)。

<a id="r_ad03e41de9d08b1cdd77abd6d40f14baf"></a>

```c
uint32_t(* get_privacy_policy_register_raw_value )()
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[get_privacy_policy_register_raw_value](#ad03e41de9d08b1cdd77abd6d40f14baf)。

<a id="r_a1ee80c505a6a7d7bdf34c228acfc3b87"></a>

```c
uint32_t(* get_dma_data_zeroing_wait_time )()
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[get_dma_data_zeroing_wait_time](#a1ee80c505a6a7d7bdf34c228acfc3b87)。

<a id="r_a73ea5882b8af5f4a738913c1c16a3aaf"></a>

```c
uint32_t(* get_dma_data_zeroing_link_select )()
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[get_dma_data_zeroing_link_select](#a73ea5882b8af5f4a738913c1c16a3aaf)。

<a id="r_a3e365ecf294cf653d0439d5d6d7d6ed5"></a>

```c
uint32_t(* get_dmic_mic_disable_status )(void)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[get_dmic_mic_disable_status](#a3e365ecf294cf653d0439d5d6d7d6ed5)。

<a id="r_abedb0ba2dbb1d9ba639aab636308747f"></a>

```c
uint32_t(* get_fw_managed_mic_disable_status )()
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[get_fw_managed_mic_disable_status](#abedb0ba2dbb1d9ba639aab636308747f)。

<a id="r_a9b827a1b6b817d5e5ec19ffa94b531f0"></a>

```c
void(* set_fw_managed_mode )(bool is_fw_managed_enabled)
```

相关声明：[set_fw_managed_mode](#a9b827a1b6b817d5e5ec19ffa94b531f0)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

<a id="r_a6f21bade6b6041322cba6995f9140d6b"></a>

```c
void(* set_fw_mic_disable_status )(bool fw_mic_disable_status)
```

相关声明：[set_fw_mic_disable_status](#a6f21bade6b6041322cba6995f9140d6b)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

<a id="r_ac60beb8b72089feab7267c265d4bfe5d"></a>

```c
uint32_t(* get_fw_mic_disable_status )()
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[get_fw_mic_disable_status](#ac60beb8b72089feab7267c265d4bfe5d)。

## 10.2\_详细说明（Detailed Documentation）

<a id="ae68b97acf6ec4f5812275ee682bdf96d"></a>

### `clear_dmic_irq_status`

```c
void(* mic_privacy_api_funcs::clear_dmic_irq_status) (void)
```

<a id="a294e4cd3bb23ccb23f7143b6a9e4dba5"></a>

### `clear_fw_managed_irq`

```c
void(* mic_privacy_api_funcs::clear_fw_managed_irq) ()
```

<a id="afc87beb092fa02c06dcd84125ccc305a"></a>

### `enable_dmic_irq`

```c
void(* mic_privacy_api_funcs::enable_dmic_irq) (bool enable_irq, const void *fn)
```

<a id="a67548968f088126881ef11f7317e5036"></a>

### `enable_fw_managed_irq`

```c
void(* mic_privacy_api_funcs::enable_fw_managed_irq) (bool enable_irq, const void *fn)
```

<a id="a73ea5882b8af5f4a738913c1c16a3aaf"></a>

### `get_dma_data_zeroing_link_select`

```c
uint32_t(* mic_privacy_api_funcs::get_dma_data_zeroing_link_select) ()
```

<a id="a1ee80c505a6a7d7bdf34c228acfc3b87"></a>

### `get_dma_data_zeroing_wait_time`

```c
uint32_t(* mic_privacy_api_funcs::get_dma_data_zeroing_wait_time) ()
```

<a id="a8cd74fd6817c3f5bfa0fc7697765d357"></a>

### `get_dmic_irq_status`

```c
bool(* mic_privacy_api_funcs::get_dmic_irq_status) (void)
```

<a id="a3e365ecf294cf653d0439d5d6d7d6ed5"></a>

### `get_dmic_mic_disable_status`

```c
uint32_t(* mic_privacy_api_funcs::get_dmic_mic_disable_status) (void)
```

<a id="abedb0ba2dbb1d9ba639aab636308747f"></a>

### `get_fw_managed_mic_disable_status`

```c
uint32_t(* mic_privacy_api_funcs::get_fw_managed_mic_disable_status) ()
```

<a id="ac60beb8b72089feab7267c265d4bfe5d"></a>

### `get_fw_mic_disable_status`

```c
uint32_t(* mic_privacy_api_funcs::get_fw_mic_disable_status) ()
```

<a id="a558346b619a67f3f05b20cf62a7993ef"></a>

### `get_policy`

```c
enum mic_privacy_policy(* mic_privacy_api_funcs::get_policy) ()
```

<a id="ad03e41de9d08b1cdd77abd6d40f14baf"></a>

### `get_privacy_policy_register_raw_value`

```c
uint32_t(* mic_privacy_api_funcs::get_privacy_policy_register_raw_value) ()
```

<a id="a9b827a1b6b817d5e5ec19ffa94b531f0"></a>

### `set_fw_managed_mode`

```c
void(* mic_privacy_api_funcs::set_fw_managed_mode) (bool is_fw_managed_enabled)
```

<a id="a6f21bade6b6041322cba6995f9140d6b"></a>

### `set_fw_mic_disable_status`

```c
void(* mic_privacy_api_funcs::set_fw_mic_disable_status) (bool fw_mic_disable_status)
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/mic_privacy/intel/mic_privacy.h`

## 10.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mic_privacy/intel/mic_privacy.h](https://docs.zephyrproject.org/latest/doxygen/html/mic__privacy_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [mic_privacy_policy](https://docs.zephyrproject.org/latest/doxygen/html/mic__privacy_8h.html#acbabb5c150f29668a23379bcb2180931)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_i2s_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P011_mpipe_结构体.md)
