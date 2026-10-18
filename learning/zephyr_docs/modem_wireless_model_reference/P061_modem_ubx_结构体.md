---
id: learning.zephyr-docs.modem-wireless-model-reference.page-61
title: modem_ubx_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__ubx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_modem\_ubx\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__ubx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 61.1\_数据成员（Data Fields）

<a id="r_ad98fcc4a93781ff5cd5406cb0560c849"></a>

```c
void * user_data
```

相关声明：[user_data](#ad98fcc4a93781ff5cd5406cb0560c849)。

<a id="r_a337b4afe37e031ecd563572951be9412"></a>

```c
atomic_t attached
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[attached](#a337b4afe37e031ecd563572951be9412)。

<a id="r_a0bc3ee485c2e6f63727efae5b61a64ac"></a>

```c
uint8_t * receive_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[receive_buf](#a0bc3ee485c2e6f63727efae5b61a64ac)。

<a id="r_a4add513db024eb040de858e8901bc017"></a>

```c
uint16_t receive_buf_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[receive_buf_size](#a4add513db024eb040de858e8901bc017)。

<a id="r_a639183a5a24d953015df30f64b2f1c85"></a>

```c
uint16_t receive_buf_offset
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[receive_buf_offset](#a639183a5a24d953015df30f64b2f1c85)。

<a id="r_ac9a3b4009eabeb92e2e3cff093d74d2c"></a>

```c
struct modem_ubx_script * script
```

相关声明：[modem_ubx_script](P064_modem_ubx_script_结构体.md)、[script](#ac9a3b4009eabeb92e2e3cff093d74d2c)。

<a id="r_a1b853c80109313feaebfb8cdb24b950c"></a>

```c
struct modem_pipe * pipe
```

相关声明：[pipe](#a1b853c80109313feaebfb8cdb24b950c)。

<a id="r_adfd9249b1f72aae1f2b9818cbf0de640"></a>

```c
struct k_work process_work
```

相关声明：[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)、[process_work](#adfd9249b1f72aae1f2b9818cbf0de640)。

<a id="r_ae5c5914a3c88b908e80646d71ada7bfe"></a>

```c
struct k_sem script_stopped_sem
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[script_stopped_sem](#ae5c5914a3c88b908e80646d71ada7bfe)。

<a id="r_a914c78bb7d0dcf5edf5f08273c6078df"></a>

```c
struct k_sem script_sent_sem
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[script_sent_sem](#a914c78bb7d0dcf5edf5f08273c6078df)。

表示脚本已发送的信号。

<a id="r_a0489f188b1dcdd54ba756ad821c62db5"></a>

```c
struct k_sem script_running_sem
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[script_running_sem](#a0489f188b1dcdd54ba756ad821c62db5)。

```c
struct {
```

<a id="r_a9162577fddacdf22b594b07b998a8735"></a>

```c
const struct modem_ubx_match * array
```

相关声明：[modem_ubx_match](P063_modem_ubx_match_结构体.md)、[array](#ae7182d2345bcd3585828f0f48d42321a)。

<a id="r_af033bd68f7eef66138d869dc2ed19450"></a>

```c
size_t size
```

相关声明：[size](#a98b8d6b02acbfa564b510b6f7c9908d5)。

<a id="r_aeeb735c338ed161d7eddeaa561cca5d9"></a>

```c
} unsol_matches
```

相关声明：[unsol_matches](#aeeb735c338ed161d7eddeaa561cca5d9)。

## 61.2\_详细说明（Detailed Documentation）

<a id="ae7182d2345bcd3585828f0f48d42321a"></a>

### `array`

```c
const struct modem_ubx_match* modem_ubx::array
```

<a id="a337b4afe37e031ecd563572951be9412"></a>

### `attached`

```c
atomic_t modem_ubx::attached
```

<a id="a1b853c80109313feaebfb8cdb24b950c"></a>

### `pipe`

```c
struct modem_pipe* modem_ubx::pipe
```

<a id="adfd9249b1f72aae1f2b9818cbf0de640"></a>

### `process_work`

```c
struct k_work modem_ubx::process_work
```

<a id="a0bc3ee485c2e6f63727efae5b61a64ac"></a>

### `receive_buf`

```c
uint8_t* modem_ubx::receive_buf
```

<a id="a639183a5a24d953015df30f64b2f1c85"></a>

### `receive_buf_offset`

```c
uint16_t modem_ubx::receive_buf_offset
```

<a id="a4add513db024eb040de858e8901bc017"></a>

### `receive_buf_size`

```c
uint16_t modem_ubx::receive_buf_size
```

<a id="ac9a3b4009eabeb92e2e3cff093d74d2c"></a>

### `script`

```c
struct modem_ubx_script* modem_ubx::script
```

<a id="a0489f188b1dcdd54ba756ad821c62db5"></a>

### `script_running_sem`

```c
struct k_sem modem_ubx::script_running_sem
```

<a id="a914c78bb7d0dcf5edf5f08273c6078df"></a>

### `script_sent_sem`

```c
struct k_sem modem_ubx::script_sent_sem
```

表示脚本已发送的信号。

<a id="ae5c5914a3c88b908e80646d71ada7bfe"></a>

### `script_stopped_sem`

```c
struct k_sem modem_ubx::script_stopped_sem
```

<a id="a98b8d6b02acbfa564b510b6f7c9908d5"></a>

### `size`

```c
size_t modem_ubx::size
```

<a id="aeeb735c338ed161d7eddeaa561cca5d9"></a>

### `[struct]`

```c
struct { ... } modem_ubx::unsol_matches
```

<a id="ad98fcc4a93781ff5cd5406cb0560c849"></a>

### `user_data`

```c
void* modem_ubx::user_data
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx.h`

## 61.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx.h](https://docs.zephyrproject.org/latest/doxygen/html/ubx_8h_source.html)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [modem_ubx_script](P064_modem_ubx_script_结构体.md)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [modem_ubx_match](P063_modem_ubx_match_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P060_modem_pipe_data_fragment_结构体.md) · [返回大纲](大纲.md) · [下一章](P062_modem_ubx_config_结构体.md)
