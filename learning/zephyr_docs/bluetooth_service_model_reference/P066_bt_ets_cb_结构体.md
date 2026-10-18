---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-66
title: bt_ets_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ets__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_bt\_ets\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ets__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

经过时间服务（Elapsed Time Service，ETS）的回调结构体。

```c
#include <zephyr/bluetooth/services/ets.h>
```

<a id="details"></a>

经过时间服务（Elapsed Time Service，ETS）的回调结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 66.1\_数据成员（Data Fields）

<a id="r_a82c2a9f55d6d31d1ce87df01e84b6d5f"></a>

```c
int(* read_elapsed_time )(struct bt_ets_elapsed_time *time)
```

相关声明：[read_elapsed_time](#a82c2a9f55d6d31d1ce87df01e84b6d5f)、[bt_ets_elapsed_time](P067_bt_ets_elapsed_time_结构体.md)、[time](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#a99ef1cb2c789827dd5db3886dccf9067)。

读取已逝时间回调（Read elapsed time callback），必需（MANDATORY）。

<a id="r_a48c36b23cec3f07a5e63d07ca083e276"></a>

```c
int(* read_clock_status )(uint8_t *status)
```

相关声明：[read_clock_status](#a48c36b23cec3f07a5e63d07ca083e276)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取时钟状态回调（Read clock status callback，`BT_ETS_CLOCK_STATUS`），必需（MANDATORY）。

<a id="r_a02ffefc1a0092104a56e0f8b2be70c86"></a>

```c
enum bt_ets_write_result(* write_elapsed_time )(const struct bt_ets_elapsed_time *time)
```

相关声明：[bt_ets_write_result](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga37a169057efc9b463ad531fd1f131fff)、[write_elapsed_time](#a02ffefc1a0092104a56e0f8b2be70c86)、[bt_ets_elapsed_time](P067_bt_ets_elapsed_time_结构体.md)、[time](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#a99ef1cb2c789827dd5db3886dccf9067)。

写入已逝时间回调（Write elapsed time callback），可选（OPTIONAL）。

<a id="r_a38d749d841a076ec3ff8277a78331a8b"></a>

```c
void(* indication_changed )(bool enabled)
```

相关声明：[indication_changed](#a38d749d841a076ec3ff8277a78331a8b)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

指示订阅变化回调（Indication subscription changed callback），可选（OPTIONAL）。

## 66.2\_详细说明（Detailed Documentation）

<a id="a38d749d841a076ec3ff8277a78331a8b"></a>

### `indication_changed`

```c
void(* bt_ets_cb::indication_changed) (bool enabled)
```

指示订阅变化回调（Indication subscription changed callback），可选（OPTIONAL）。

客户端为当前已逝时间特征（Current Elapsed Time characteristic）启用或禁用指示（Indications）时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `enabled` | 启用指示（Indications）时为 `true`，禁用时为 `false`。 |

<a id="a48c36b23cec3f07a5e63d07ca083e276"></a>

### `read_clock_status`

```c
int(* bt_ets_cb::read_clock_status) (uint8_t *status)
```

读取时钟状态回调（Read clock status callback，`BT_ETS_CLOCK_STATUS`），必需（MANDATORY）。

蓝牙低功耗客户端（BLE client）读取当前已逝时间特征（Current Elapsed Time characteristic）时调用。应用必须返回当前时钟状态标志（Clock status flags）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `status` | 用于存储时钟状态字节（Clock status byte）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 失败时返回负的错误编号（errno）。 |

<a id="a82c2a9f55d6d31d1ce87df01e84b6d5f"></a>

### `read_elapsed_time`

```c
int(* bt_ets_cb::read_elapsed_time) (struct bt_ets_elapsed_time *time)
```

读取已逝时间回调（Read elapsed time callback），必需（MANDATORY）。

蓝牙低功耗客户端（BLE client）读取当前已逝时间特征（Current Elapsed Time characteristic）时调用。应用必须使用当前时间信息填充已逝时间结构（Elapsed time structure）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `time` | 待填充的已逝时间结构（Elapsed time structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 失败时返回负的错误编号（errno）。 |

<a id="a02ffefc1a0092104a56e0f8b2be70c86"></a>

### `write_elapsed_time`

```c
enum bt_ets_write_result(* bt_ets_cb::write_elapsed_time) (const struct bt_ets_elapsed_time *time)
```

写入已逝时间回调（Write elapsed time callback），可选（OPTIONAL）。

蓝牙低功耗客户端（BLE client）写入当前已逝时间特征（Current Elapsed Time characteristic）时调用。应用应验证时间源质量（Time source quality）、范围及其他约束。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `time` | 客户端写入的已逝时间结构（Elapsed time structure）。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_ETS_CURRENT_ELAPSED_TIME_WRITABLE` 时可用。

**说明（Note）**：注意（Note）：根据规范，写入内容不包含时钟状态（Clock Status）和时钟能力（Clock Capabilities）。

**返回（Returns）**：返回值（Returns）：指示接受或具体拒绝原因的结果码（Result code）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/ets.h`

## 66.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/ets.h](https://docs.zephyrproject.org/latest/doxygen/html/ets_8h_source.html)
- [bt_ets_elapsed_time](P067_bt_ets_elapsed_time_结构体.md)
- [time](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#a99ef1cb2c789827dd5db3886dccf9067)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_ETS_CLOCK_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#BT_ETS_CLOCK_STATUS)
- [bt_ets_write_result](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga37a169057efc9b463ad531fd1f131fff)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [CONFIG_BT_ETS_CURRENT_ELAPSED_TIME_WRITABLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ETS_CURRENT_ELAPSED_TIME_WRITABLE)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P065_bt_cts_time_format_结构体.md) · [返回大纲](大纲.md) · [下一章](P067_bt_ets_elapsed_time_结构体.md)
